---
date: "2014-09-15"
published: true
slug: adding-django-form-instance-attributes
tags:
  - python
  - django
  - howto
  - class-based-views
  - forms
time_to_read: 2
title: Adding Django form instance attributes
description: "Sometimes in the `clean()`, `clean_FOO` or `save()` methods of a Django
form, you need to have additional form instance attributes available.  A
sample case for this is having `user_id` available. This is a simple
example of how to do it in Class-Based Views."
---

Sometimes in the `clean()`, `clean_FOO` or `save()` methods of a Django
form, you need to have additional form instance attributes available. A
sample case for this is having `user_id` available. This is a simple
example of how to do it in Class-Based Views.

Assuming this form:

```python
from django import forms

from .models import MyModel


class MyForm(forms.ModelForm):

    class Meta:
        model = MyModel

    def __init__(self, user_id, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)

        # set the user_id as an attribute of the form
        self.user_id = user_id
```

Now that the form is defined, the view needs to inject the form with the
user id:

```python
from django.views.generic import UpdateView

# this assumes that django-braces is installed
from braces.views import LoginRequiredMixin

from .forms import MyForm
from .models import MyModel


class MyUpdateView(LoginRequiredMixin, UpdateView):
    model = MyModel
    form_class = MyForm
    success_url = "/someplace/"

    def get_form_kwargs(self):
        """This method is what injects forms with their keyword
            arguments."""
        # grab the current set of form #kwargs
        kwargs = super(MyUpdateView, self).get_form_kwargs()
        # Update the kwargs with the user_id
        kwargs['user_id'] = self.request.user.pk
        return kwargs
```

# Additional Notes

You can use this technique with:

- `forms.Form`
- `forms.ModelForm`
- `CreateView`
- `FormView`
- `UpdateView`

As always, <https://ccbv.co.uk> is a great resource for deliving into
Django forms.

While this technique is used by `django-braces` through the
`UserFormKwargsMixin` and `UserKwargModelFormMixin` mixins, it's useful
to know how to do it outside that very useful tool. The reason being
that attaching the `user` object or `user_id` is just one option out of
many.

# django-vanilla-views

This should also work with
[django-vanilla-views](https://django-vanilla-views.org), but I haven't
tested it yet.

[![image](/images/form-attributes.png)](audrey.feldroy.com)

# See you at BarCamp Django SF!

On October 4th and 5th I'll be at [BarCamp Django
SF](/barcamp-django-sf.html) if you want to talk
about Django, Python, or have me teach you how to do cartwheels.
