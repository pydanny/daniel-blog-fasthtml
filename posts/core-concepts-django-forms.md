---
blogbook: 'True'
date: 2013-3-29
published: true
slug: core-concepts-django-forms
tags:
- python
- django
- forms
- class-based-views
time_to_read: 3
title: Core Concepts of Django Forms
description: "The concepts behind Django's non-model forms can be
listed in just three items."
---

In my opinion, the concepts behind Django's non-model forms can be
listed in just three (3) bullets:

- Forms render HTML.
- Forms are "just" Python constructs.
- Forms validate dictionaries (Python's Key/Value structure).

Let's dig in!

# Forms render HTML.

If I construct a Django form:

```python
# myapp/forms.py
from django import forms

class MyForm(forms.Form):

    title = forms.CharField(required=True)
```

I can render it in a template, or for better clarity in this post, the
Python REPL:

```python
>>> from myapp.forms import MyForm
>>> f = MyForm()
>>> f
<__main__.MyForm object at 0x1016c6990>
>>> print(f)
<tr><th><label for="id_title">Title:</label></th>
<td><input id="id_title" name="title" type="text" /></td></tr>
```

You can even see this done with initial values in the Django docs:
<https://docs.djangoproject.com/en/1.5/ref/forms/api/#django.forms.Form.initial>

# Forms are "just" Python constructs.

I believe it was [Alex](https://twitter.com/alex_gaynor)
[Gaynor](https://alexgaynor.net/) who said back in 2008 that Django forms
were "just" Python constructs. He's right:

```python
>>> from myapp.forms import MyForm
>>> # class
>>> MyForm
<class 'myapp.forms.MyForm'>
>>> # object
>>> form = MyForm()
>>> form
<myapp.forms.MyForm object at 0x1023f1450>
>>> # iterable
>>> [x for x in form]
[<django.forms.forms.BoundField object at 0x102495990>]
>>> [x for x in form.fields]
['title']
>>> # dictionary-like
>>> form.fields['title']
<django.forms.fields.CharField object at 0x1024a17d0>
```

Understanding the structure of Django forms is really useful. This
structure is what allows the modification mechanism that I described in
my [previous post](/overloading-form-fields.html).

We don't have to stop in just the `forms.py` module. You can also
modify forms in views (either the classic `views.py` module or in
whatever API library you might be using):

```python
from django import forms
from django.shortcuts import redirect
from django.views.generic import FormView

class MyFormView(FormView):

    form_class = MyForm

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.fields['favorite_icecream'] = forms.ChoiceField(
            label="What is your favorite flavor from this list?",
            choices=((0, "Chocolate"), (1, "Vanilla"), (2, "Berry")),
            widget=forms.RadioSelect,
            required=True
        )
        return form

    def form_valid(self, form):
        # Get user's favorite ice cream.
        # You can do anything you want with it
        favorite_icecream = form.cleaned_data['favorite_icecream']

        # return the anticipated redirect
        return redirect("home")
```

As you can see, with an understanding of basic Python types and some
experience with Django forms you can become very creative in
applications of forms. Please keep in mind that the devil is in the
details, and overly creative use of forms (or anything) is a road you
should carefully tread. It's always good to remember that simplicity is
best and that the goal isn't to just write code, but to write
maintainable code.

# Forms validate dictionaries.

One of the primary functions of any HTTP-friendly form libraries is
validating dictionary-like data objects. HTTP query strings are
key/value structures and in order to avoid corruption in the persistence
layer of any project, regardless of framework or language, validation
needs to occur.

During it's request/response cycle Django converts `HTTP POST` (and
`HTTP GET`) objects into something called a `QueryDict`, which is an
merely an extended Django dictionary. See the comments in the code
example below for proof:

```python
import logging

from django.http import HttpResponse
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict

logger = logging.getLogger(__main__)

def my_form_view(request):

    logging.debug(
        # logs True because request.POST is an instance of QueryDict
        isinstance(request.POST, QueryDict)
    )
    logging.debug(
        # logs True because QueryDict is a dictionary
        issubclass(QueryDict, dict)
    )

    return HttpResponse()
```

This is all fine and good, but what does it mean for developers trying
to solve problems? Well, it means that Django forms serve quite handily
as a means for validation of dictionaries:

```python
>>> from myapp.forms import MyForm
>>> good_form = MyForm({"title": "Two Scoops of Django"})
>>> good_form.is_valid()
True
>>> good_form.errors
{}
>>> bad_form = MyForm({})
>>> bad_form.is_valid()
False
>>> bad_form.errors
{'title': [u'This field is required.']}
```

The power of this can't be understated. In fact, I'll be exploring
this particular facet of Django forms more in at least one upcoming blog
post.

# Epilogue

ModelForms adds at least three more bullets...

- ModelForms render Model fields as HTML
- ModelForms automatically choose validators based off of Model field
  definitions.
- ModelForms save dictionaries to SQL tables.

... and I touch on them in [my post on
ModelForms](/core-concepts-django-modelforms.html).
