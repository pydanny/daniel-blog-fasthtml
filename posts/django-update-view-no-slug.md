---
date: "2012-07-28"
published: true
slug: django-update-view-no-slug
tags:
  - python
  - django
  - howto
  - class-based-views
time_to_read: 2
title: Django Update View Without Slug in the URL
---

Today I wanted to use the Django Class Based View (CBV) UpdateView but
without a slug identifier in the URL. For example, instead of
`/profiles/pydanny/` I would go to `/my-crazy-profile/`. Also, I needed
to force authentication.

I've done this with Django functional views a few times times, but
today I did it in Django. This is what I did:

## 1. Added django-braces to my project

[Kenneth Love](https://twitter.com/kennethlove) and [Chris
Jones](https://twitter.com/tehjones)' awesome
[django-braces](https://github.com/brack3t/django-braces/) package has
some very handy mixins for working with Django CBVs. Kenneth and Chris
really understand CBVs, specifically on how to extend them, and have
provided a bunch of really useful utility methods in the django-braces
library. Yeah, I could figure this stuff out on my own, but since those
guys already did the hard work I might as well just lean on them.

```bash
pip install django-braces==0.1.3
```

```python
# settings.py
INSTALLED_APPS = (
...
'braces',
...
)
```

## 2. Wrote the view

Assuming a very simple profile Model and Form (which they weren't - but
that's not what this post is about), this is how I implemented the
view:

```python
# profiles/views.py
from django.views.generic import UpdateView

from braces.views import LoginRequiredMixin  # handles authentication

from profiles.forms import ProfileForm
from profiles.models import Profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProfileForm
    success_url = "/my-crazy-profile/"  # You should be using reverse here

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
```

## 3. Wrote the URLconf

The URL pretty much wrote itself:

```python
from django.conf.urls.defaults import patterns, url

from profiles import views

urlpatterns = patterns("",
    url(regex=r'^my-crazy-profile/$',
        view=views.ProfileUpdateView.as_view(),
        name='profile_update'),
)
```

## Closing Thoughts

For a while, I've used django-braces for anything that involves CBVs. I
can't imagine working on projects using CBVs without them. In fact,
some of the mixins such as `LoginRequiredMixin` are things that I could
argue ought to be in core Django.

This pattern really nails the sweet spot of Django CBVs. Thanks to the
use of mixins and model forms, I get an amazing amount of stuff done in
a 5 line CBV.
