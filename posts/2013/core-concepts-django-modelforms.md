---
blogbook: "True"
date: 2013-6-13
published: true
slug: core-concepts-django-modelforms
tags:
  - python
  - django
  - forms
time_to_read: 8
title: Core Concepts of Django ModelForms
description: "The concepts behind Django's model forms can be boiled down to six items."
---

In my opinion, the concepts behind Django's model forms can be listed
in just six (6) bullets. The bullets I've marked in **bold** at the top
are the topic of this blog post, while the two of these that were
[covered in a previous blog post on Django
forms](/core-concepts-django-forms.html) are at
bottom of my list.

- **ModelForms render Model fields as HTML.**
- **ModelForms select validators based off of Model field
  definitions.**
- **ModelForms don't have to display/change all available fields.**
- **ModelForms save dictionaries to SQL tables.**
- Forms are "just" Python constructs. (covered previous)
- Forms validate Python dictionaries. (covered previous)

# ModelForms render Model fields as HTML.

If I create a Django model:

```python
# myapp/models.py
from django.db import models

class MyModel(models.Model):

    title = models.CharField(max_length=100)
```

Then attach it to a ModelForm:

```python
# myapp/forms.py
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    class Meta:

        model = MyModel
```

I can render it in a template, or for better clarity in this post, the
Python REPL:

```python
>>> from myapp.forms import MyModelForm
>>> mf = MyModelForm()
>>> mf
<__main__.MyForm object at 0x1023c8bd0>
>>> print(mf)
<tr><th><label for="id_title">Title:</label></th>
<td><input id="id_title" name="title" maxlength="100" type="text" /></td></tr>
```

# ModelForms select validators based off of Model field definitions.

One of the nice things about Django is that its forms library protects
your models. It does this by assigning one or more of Django's many
built-in validators to the form fields it generates, and using them to
check incoming data. Let's dive in:

```python
>>> from myapp.forms import MyModelForm
>>> mf = MyModelForm()
>>> mf
<__main__.MyForm object at 0x1023c8bd0>
>>> mf.fields
{'title': <django.forms.fields.CharField object at 0x102474bd0>}
>>> field = mf.fields['title']
>>> field.max_length
100
>>> field.validators
[<django.core.validators.MaxLengthValidator object at 0x102403b10>]
```

Each individual field contains a list of validators (in this case, just
one validator) supplied by Django and any ModelForm customizations that
might have been done.

If you want to add more validators to a ModelForm (perhaps we want our
title field to require at least 20 characters) one way to do it is by
overriding the field definition in the ModelForm class's `__init__`
method. That's a mouthful, so I'll just demonstrate in code:

```python
# myapp/forms.py
from django import forms
from django.core.validators import MinLengthValidator

from .models import MyModel

class MyModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].min_length = 20
        self.fields["title"].validators.append(MinLengthValidator)

    class Meta:

        model = MyModel
```

If we stop/start the shell, we now see some new elements added to the
form object:

```python
>>> # Don't forget to stop/start the Django shell!
>>> from myapp.forms import MyModelForm
>>> mf = MyModelForm()
>>> mf
<__main__.MyForm object at 0x1023c8bd0>
>>> mf.fields
{'title': <django.forms.fields.CharField object at 0x1023ee810>}
>>> field = mf.fields['title']
>>> field.max_length
100
>>> field.min_length
20
>>> field.validators
[<django.core.validators.MaxLengthValidator object at 0x10240c7d0>, <django.core.validators.MinLengthValidator object at 0x1023eef90>]
```

Now we have two validators for the field!

There are other ways to override the title field validators. The easiest
but not necessarily the best way is to replicate the ModelForm
definition of the field in the form like so:

```python
# myapp/forms.py
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    title = forms.CharField(max_length=100, min_length=20)

    class Meta:

        model = MyModel
```

I don't like this technique. This makes it so we are defining the title
field in two places, once in the model and once in the form. I go into
more of the details and problems of this approach in my previous blog
post at [Overloading Django Form
Fields](/overloading-form-fields.html).

# ModelForms don't have to display/change all available fields.

Before we dive into this section, let's increase our model to have two
fields as shown below:

```python
# myapp/models.py
from django.db import models

class MyModel(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
```

Let's say that we don't want to allow users the ability to change
slugs on existing content, otherwise URLs will be broken. In this case,
we rely on the `fields` attribute of `ModelForm.Meta` to make it so we
only display what we want to display:

```python
# myapp/forms.py
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    class Meta:

        model = MyModel
        fields = ('title', )
```

Easy!

## But what about ModelForm.Meta.excludes?

We advocate strongly against using `ModelForm.Meta.excludes`.

In fact, when we were writing [Two Scoops of
Django](https://feldroy.com/products/two-scoops-of-django-1-5) the majority of our technical
reviewers as well as our security reviewer fervently insisted that we
advocate against use of `ModelForm.Meta.excludes`. We provide numerous
warnings about it's usage, and go in-depth as to why in _section
21.12_. For reference, Django's own documentation is now including a
rather mild warning (no warning box) on the subject at [selecting the
fields to
use](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelforms-selecting-fields).
I might try and get that addressed in the next few days...

In any case, the problem with `ModelForm.Meta.excludes` is similar to
but worse than duplicating field functionality. It means that changes to
models (new fields for example) will display in associated forms
**unless** you remember to modify the associated forms. Since a single
model can have multiple forms, and we developers forget or leave
projects, you can understanding what sort of security nightmare this can
cause.

Do yourself a favor and stay away from `ModelForm.Meta.excludes`.

# ModelForms save dictionaries to SQL tables

In my [previous post of Django
forms](/core-concepts-django-forms.html) I covered
_forms validate dictionaries_. Well, ModelForms do the same thing AND
give us the power to save that validated dictionary to SQL tables. We
don't even need to involve web pages!

This is really useful because it means that we can take data from any
source, be it user input from the web, JSON data fetched from an API,
and even CSVs generated from Excel reports and transform that into data
that resides in SQL.

Let's go over using our ModelForm with title/slug fields used with all
those methods. In our samples (web page, json, csv), we'll use
generating a timestamp to demonstrate how we can modify the model data
before it's saved, and we'll base all three examples off the model and
ModelForm combination listed below.

```python
# myapp/models.py
from django.db import models


class MyModel(models.Model):

    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
```

```python
# myapp/forms.py
from django import Forms

from .models import MyModel


class MyModel(forms.ModelForm):

    class Meta:

        model = MyModel
        fields = ('title', )
```

And now to our three examples!

## Example #1 Web Page

This should look pretty familiar to many Django developers. it's the
traditional Django view pattern of processing simple model forms.

```python
# myapp/views.py
from django.core.shortcuts import render, redirect
from django import forms
from django.utils import timezone

from .forms import MyModelForm


def add_model(request):

    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('victory')
    else:
        form = MyModelForm()

    return render(request, "my_template.html", {'form': form})
```

## Example #2 API/JSON

In this example, we're validating the output of a RESTful API before
letting it touch our database. It's critical that such APIs are not
allowed to touch our systems without proper validation - don't make my
mistakes! Also, even internally within a project it's really important
to validate all data coming from different databases. And Django makes
it easy!

```python
# myapp/api/reitz.py
from django.utils import timezone

import requests  # You are using requests-python, right?

from .forms import MyModelForm


class ReitzApiException(Exception):
    pass


def fetch_reitz_data(target_url):
    response = requests.get(target_url)
    if response.status_code == 200:

        # generate the form from the response
        form = MyModelForm(response.json())
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return model_instance

        # Simplistic exception handling
        raise ReitzApiException(form.errors)

    # Simplistic exception handling
    raise ReitzApiException(response.status_code)
```

## Example #3 CSV Import

I'll admit my mistake again: I've written my own validation tools to
handle data coming from CSVs and Excel documents into Django projects.
My validation scripts always seem fragile, and they are. What I'm doing
going forward is I'm leaning on form libraries to do the hard work of
validating data and saving it to models.

```python
import csv

from django.utils import timezone

from .forms import MyModelForm


def import_csv(filename):
    rows = open(filename)
    records_added = 0
    errors = []
    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):

        # Bind the row data to the MyModelForm
        form = MyModelForm(row)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            records_added += 1
        else:
            errors.append(form.errors)

    return records_added, errors
```

# Closing Thoughts

I can think of three things:

**Forget the HTML**: For nearly every sort of occasion where new data is
coming into your system, form libraries save you from doing extra work
and cover your behind. While my experience is with Django forms, there
are many form libraries out there. The patterns explored in this post
are certainly available in other web frameworks (see
<https://flask.pocoo.org/snippets/category/forms/> for proof).

**HTML Rendering Issues**: No form library is going to do everything,
and because of evolving standards, decent HTML rendering is a pain for
form library authors. For example, Django's default form HTML rendering
remains stuck in 2005 because if they had kept up with modern trends of
HTML form layout we would have many different flavors of forms in Django
core (a testing nightmare). Which means, as a developer, it's important
when using a new form library to learn how to override the default form
HTML rendering.

**What about AJAX?**: Whoops! Does this mean I have to write another
blog post? Not at all. In Django, AJAX is just another view, either
function- or class-based. The secret is to validate the incoming data
the same way as you would any other view request by using forms.
