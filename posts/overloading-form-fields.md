---
blogbook: "True"
date: 2013-3-27
published: true
slug: overloading-form-fields
tags:
  - python
  - django
  - forms
time_to_read: 3
title: Overloading Django Form Fields
description: "How to overload Django form fields in an extensible way."
---

One of the patterns we get positive feedback for mentioning in our
[book](https://www.feldroy.com/books/two-scoops-of-django-3-x) is **overloading form fields**.

The problem this pattern handles is the use case of when we have a model
with a field(s) that allows for blank values, how do we force users to
enter values?

For example, assuming the following model:

```python
# myapp/models.py
from django.db import models

class MyModel(models.Model):

    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
```

How do we make all those fields (name, age, profession, bio) required
without modifying the database?

This is the way I used to do it:

```python
# myapp/forms.py
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    profession = forms.CharField(required=True)
    bio = forms.TextField(required=True)

    class Meta:
        model = MyModel
```

See the problems with this approach?

`MyModelForm` is nearly a copy of `MyModel`, and was in fact created by
copy/pasting model and then modifying it. In software engineering
parlance, it violates the principal of Don't Repeat Yourself
([DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)) and is
fertile ground for introducing bugs.

# `MyModelForm` has a bug!

Can you spot the bug?

The code example below illuminates where I purposefully/gleefully placed
an error:

```python
class MyModel(models.Model):

    # 50 character database field
    name = models.CharField(max_length=50, blank=True)

class MyModelForm(forms.ModelForm):

    # Most people don't write tests to check for field length.
    # 100 character form field - probably not spotted until deployed.
    # Easy error to make when violating DRY since the model can change
    #   and leave the form definition behind.
    name = forms.CharField(max_length=100, required=True)
```

Bugs like this happen either because developers are human and make
mistakes, or because the model evolves over time and the forms are left
behind. This is a serious maintenance issue, and one that will bite you
or the developers who end up maintaining code you've written.

Can you spot the second bug? ;-)

How do we fix this?

# A Better Way

In instantiated Django forms, fields are kept in a dict-like object.
Which means, instead of writing forms in a way that duplicates the
model, a better way is to explicitly modify only what we want to modify:

```python
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['name'].required = True
        self.fields['age'].required = True
        self.fields['bio'].required = True
        self.fields['profession'].required = True

    class Meta:
        model = MyModel
```

## Other field attributes

This isn't just limited to the `required` attribute. It can also be
applied to `help_text`, `label`, `choices`, `widgets`, or any other form
field attribute:

```python
from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        # snip the other fields for the sake of brevity
        # Adding content to the form
        self.fields['profession'].help_text = "Job title here"

    class Meta:
        model = MyModel
```

## Try it with Inheritance!

We can even do this with inheritance:

```python
from django import forms

class BaseEmailForm(forms.Form):
    email = forms.EmailField("Email")
    email2 = forms.EmailField("Email 2")

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']
        if email != email2:
            raise forms.ValidationError("Emails don't match")
        return self.cleaned_data

class ContactForm(BaseEmailForm):
    message = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs):
        self.fields['email2'].label = "Confirm your email"
        self.fields['email2'].help_text = "We want to be sure!"
```

# Summary

From the perspective of general software development, it's always a
good thing to avoid repeating yourself. This might seem like as much or
in some cases even more typing, but it's a lot better than making an
embarrassing/costly mistake.

From the perspective of a Python developer our approach more closely
matches the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).
This is because we only modify the field properties that need to be
modified, the approach specified is more explicit.

Today's reading is Matt Harrison's [Guide to Learning Iteration and
Generators in
Python](https://www.amazon.com/Guide-Learning-Iteration-Generators-ebook/dp/B007JR4FCQ/?ie=UTF8&qid=1364400929&sr=1-5&tag=ihpydanny-20)
