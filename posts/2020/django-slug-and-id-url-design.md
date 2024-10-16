---
date: "2020-05-20T08:00:00.00Z"
description: How to combine slugs and IDs to make a a human readable unique URL design.
published: true
slug: django-slug-and-id-url-design
tags:
  - python
  - django
  - forms
time_to_read: 8
title: Django Slug + ID URL Design
type: post
---

One of the things I like about [dev.to](https://dev.to/) is their URL design. It combines a slug with a hashed value representing an internal representative of some kind of index value to ensure uniqueness. You can see an example of it in my post "Autodocumenting Makefiles" featured in the URL "[https://dev.to/feldroy/autodocumenting-makefiles-175b](dev.to/feldroy/autodocumenting-makefiles-175b)".

Let's break apart that URL:

1. `feldroy` is my company name.
2. `autodocumenting-makefiles` is the slug and it's based off the article title.
3. `175b` is a hashed value that is either stored in an indexed character field or broken down by the router into a numeric primary key.

Here is another way of looking at their URL design:

```
/<org-or-username>/<slugified-title>/<hashed-id>
```

Let's see how we can implement a simplified version of this technique using Django.

# Our Version of the URL

We're going with a simpler version of the **Dev.to** implementation. Our implmentation will the database primary key to ensure uniqueness instead of the hashed value relied on by **Dev.to**. I think **Dev.to** uses an identifier because it's more easily remembered and/or they feel it makes for a more attractive URL.

What **Dev.to** doesn't do is rely on it for security, as they know short hashes like this are easily broken.

```
/<username>/<slugified-title>/<primary-key>/
```

Okay, now that we've determined our URL design, let's build it!

## The Model

Store the data!

```python
# articles/models.py
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    slug = models.CharField(_("Slug"),
        max_length=100,
        db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    # More fields...
```

## The Form

Collect and validate the data!

```python
# articles/forms.py
from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', ) # more fields
```

## The Views

Now that we have the model and form, let's build the views:

```python
# articles/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import slugify
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import ArticleForm
from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        # Save the data to an article object -
        #   this hasn't yet saved to the database.
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = self.request.user
        # Save again - this time to the database
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm

    def get_object(self):
        # We could return a 403 forbidden, but for content
        #   sites like dev.to or github the pattern is to return
        #   a 404.
        return get_object_or_404(Article,
            slug=self.kwargs['slug'],
            id=self.kwargs['pk'],
            author__username=self.kwargs['username'],
            author=self.request.user
        )

    def form_valid(self, form):
        # Update the slug if the title has changed.
        # If you allow this you might
        #     want to set up a redirect system
        # If you don't want to figure that rediect,
        #    just delete this method.
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.save()
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        return get_object_or_404(Article,
            slug=self.kwargs['slug'],
            id=self.kwargs['pk'],
            author__username=self.kwargs['username']
        )
```

## The URLs

Let's route this into our urls:

```python
# articles/urls.py
from django.urls import path

from articles import views

urlpatterns = [
    path(route='/new/',
        view=views.ArticleCreateView.as_view(),
        name='create',
    ),
    path(route='/<slug:username>/<slug:slug>-<int:pk>/edit/',
        view=views.ArticleUpdateView.as_view(),
        name='update',
    ),
    path(route='/<slug:username>/<slug:slug>-<int:pk>/',
        view=views.ArticleDetailView.as_view(),
        name='create',
    ),
]
```

And in the project's root config, we add in this:

```python
# config/urls.py or wherever you stick the project's root urls.py
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin, change this URL
    path('two-scops-of-django-is-awesome', admin.site.urls),
    # Articles management
    path('', include('articles.urls', namespace='article')),
    # More URLS here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# There's certainly more URLs down here
```

Add templates and there it is, a site that follows our implementation of the **Dev.to** URL design!

## Two Scoops of Django 3.x is out!

We just released the alpha version of the first edition of our book, [Two Scoops of Django 3.x](https://www.feldroy.com/products/two-scoops-of-django-3-x). This updates the book to Django 3.0, 3.1, and when it's close to release, Django 3.2. All the code works in Python 3.8 and 3.9. You can see the new cover featured below along with myself and my wife/co-author, [Audrey](https://audrey.feldroy.com).

[![Image of Daniel and Audrey holding Two Scoops of Django 3.x](https://daniel.feldroy.com/images/tsd3.x-audrey-daniel.jpg)](https://www.feldroy.com/products/two-scoops-of-django-3-x)
