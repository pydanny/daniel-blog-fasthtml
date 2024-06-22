---
date: '2012-10-16'
published: true
slug: get-or-create-view
tags:
- python
- django
- howto
- class-based-views
time_to_read: 2
title: Django GetOrCreateView
description: Probably the first article outside the official docs on how to use the Django CBV form_valid method. Written in 2012 and still accurate in 2023!
---

Today I decided to use the Django class based view (CBV) CreateView, but
I wanted to avoid duplications and submit to the view from the front
page of a site. The reason was I needed a simple newsletter signup form.
This is what I cooked up and should work for Django 1.3, 1.4, and the
forthcoming 1.5 release. Here is what I did:

# 1. Installed dependencies

This version requires the following package to be pip installed into
your virtualenv.

-   [django-extensions](https://github.com/django-extensions/django-extensions)
    so we can have easy timestamps on models.

This also needs to be added to your list of `INSTALLED_APPS`:

``` python
INSTALLED_APPS += (
    'django_extensions',
)
```

# 2. Defined the model

The model is really simple, and inherits from TimeStampedModel so we
know when people signed up:

``` python
from django.db import models

from django_extensions.db.models import TimeStampedModel


class NewsLetterSignup(TimeStampedModel):

    email = models.EmailField("Email")

    def __unicode__(self):
        return self.email
```

# 3. Wrote the view

Here's the somewhat challenging part that forced me to dive into
Django's source code. Even with the documentation work we've done over
the past few months, it's clear we've got a long way to go.

Because of that source code diving, for this blog post I really did my
best to document why I did things in the
`NewsLetterSignupView.form_valid()` method.

``` python
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .models import NewsLetterSignup


class NewsLetterSignupView(CreateView):
    """ Signs up users to a newsletter """

    model = NewsLetterSignup
    success_url = '/newsletter-signed-up/'  # replace with reverse

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
            (django.views.generic.edit.ModelFormMixin)
        If the form is valid, redirect to the supplied URL.
            (django.views.generic.edit.FormMixin)
        """

        # Get the email from the form.cleaned_data dictionary
        email = form.cleaned_data.get("email", "")

        # Get or create the signup. We don't need to do anything with the
        #   model instance or created boolean so we don't set them.
        NewsLetterSignup.objects.get_or_create(email=email)  

        # Don't use super() to inherit as it will do a form.save()
        # You could call the FormMixin's form_valid() method but I think    
        #   using a HttpResponseRedirect() much more explicit.
        return HttpResponseRedirect(self.success_url)  
```

# 4. Wired it together

In urls.py:

``` python
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import NewsLetterSignupView

urlpatterns = patterns('',
    url(regex=r'^newsletter-signed-up/$',
        view=TemplateView.as_view(
            template_name="pages/newsletter_signed_up.html"
        ),
        name='newsletter_signedup',
    ),
    url(regex=r'^newsletter-signup/$',
        view=NewsLetterSignupView.as_view(),
        name='news_letter_signup',
    ),
)
```

# Closing thoughts

First off, you'll notice I didn't include the
`pages/newsletter_signed_up.html` because for this case it's too
trivial.

Second, this is one of those very clear cases where a functional view
would have been so much easier compared to the effort I spent writing
this as a class based view. The line count would have been about the
same, but the mental bandwidth involved in figuring this would have been
a fraction of the effort I spent.

**Note from August 2023**: At the time I wrote this in 2012 figuring this out took a lot of work. Django CBVs were very new and the docs were in a raw state. What's shocking to me is how well this has aged. I just re-read this and it's still accurate (although lacking in good use of Django defaults). 

Speaking of Django defaults, within a month of writing this article I would [advocate using Django CBV defaults](/posts/stay-with-cbv-defaults) for consistent code written with less effort.
