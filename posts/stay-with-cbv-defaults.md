---
date: '2012-11-27'
published: true
slug: stay-with-cbv-defaults
tags:
- python
- rant
- django
- python
- howto
- class-based-views
time_to_read: 3
title: Stay with the Django CBV defaults!
---

One virtue of Django Class Based Views (CBVs) is that they come with
pretty good default settings. The virtue of this is you can really pare
your code down in size and complexity.

For example, here is an implementation of CBVs based on a
straight-forward Django model , `stuffage.models.Stuff`, that has a
`get_absolute_url` method:

**stuffage/views.py**:

``` python
from django.views import generic

from stuffage.models import Stuff

class StuffDetailView(generic.DetailView):
    model = Stuff

class StuffListView(generic.ListView):
    model = Stuff

class StuffCreateView(generic.CreateView):
    model = Stuff

class StuffUpdateView(generic.UpdateView):
    model = Stuff
```

**stuffage/urls.py**:

``` python
from django.conf.urls.defaults import patterns, url, include

from stuffage import views

urlpatterns = patterns("",

    url(
        regex=r"^create/$",
        view=views.StuffCreateView.as_view(),
        name="stuff_create",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=views.StuffUpdateView.as_view(),
        name="stuff_update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.StuffDetailView.as_view(),
        name="stuff_detail",
    ),
    url(
        regex=r"^$",
        view=views.StuffListView.as_view(),
        name="stuff_list",
    ),
)
```

These four CBVs will default to the following three templates without
any action on my part:

    stuffage/stuff_detail.html (StuffDetailView)
    stuffage/stuff_form.html (StuffCreateView, StuffUpdateView)
    stuffage/stuff_list.html (StuffListView)

So easy I use a simple script to render all this code!

What about doing this all in the urls.py?
=========================================

Yes, I could do this all in the urls.py, but real Django code involves
doing some logic in views, no matter how skinny you try to make said
views. While I'm a huge proponent of logic in fat models, invariably
I'm adding to the view context, or doing something else that requires
tweaking of CBV settings.

The problem
===========

One trait of developers is we like to **tinker**.

Unfortunately, I keep seeing developers tinkering on the settings for
Django CBVs without any reason besides tinkeringWhich means you get
things like:

**unfortunately tinkered stuffage/views.py**

``` python
# 1. Using template_name means extra code and extra developer lookup time.
# 2. Changing the context_object_name means extra code  and extra developer     
#       lookup time.
class StuffDetailView(generic.DetailView):
    model = Stuff
    template_name = "stuffage/stuffs.html"
    context_object_name = 'stuff'
```

**unfortunately tinkered stuffage/urls.py**

``` python
# 1. Logic into your URLConf should be kept to a minimum
# 2. Unless you are using the same view more than once, specifying the
#       template_name here is a waste of code. And makes it harder to
#       understand the view.
url(
    regex=r"^$",
    view=views.StuffListView.as_view(template_name="stuffage/stuffs.html"),
    name="stuff_list",
),

# No matter how fat your models get, you always end up extending all views,
#   so this will have to be moved into the formal views.py at some point. So
#   why not start with it in the views.py in the first place.
url(
    regex=r"^$",
    view=ListView.as_view(
        model=Stuff,
        template_name="stuffage/stuffs.html"),
    name="stuff_list",
),
```

Don't forget you can also tinker/tweak formats and slug/pk identifier
defaults, and a ton of other things that are part of Django CBVs. While
this gives you great power, if misused that power can cause grief in
terms of code obfuscation and the need for additional testing.

My opinion is that these defaults were meant as a standard for the CBV
to operate, upon which developers familiar with the Django CBV API could
extend and expand their code for minimal effort. Yes, you can tweak them
to match your preferred patterns, but that's extra work. Work you
shouldn't be doing if you can avoid it.

My Advice
=========

Stick with the defaults and only modify behavior that actually needs to
be modified. For example, if you want to show multiple versions of a
ListView you might do something like:

**stuffage/urls.py with a pydanny approved use of template_name**

``` python
url(
    regex=r"^$",
    view=views.StuffListView.as_view(),
    name="stuff_list",
),

# Same view but with a template designed to show larger list items.
url(
    regex=r"^large/$",
    view=views.StuffListView.as_view(template_name="stuffage/stuff_list_large.html"),
    name="stuff_list_large",
),
```

Summary
=======

This is the pattern I follow when I build projects. I stick to the
framework standard as much as possible. Since many systems rely on
convention over configuration, this makes it easier and faster to
develop projects, be it Django, Twisted, or some other tool.

It's the work you can see in my [recent](https://petcheatsheets.com)
[public](https://movehero.io) [projects](https://lacurrents.com), and what
I want to port to long existing sites like [Django
Packages](https://djangopackages.com).
