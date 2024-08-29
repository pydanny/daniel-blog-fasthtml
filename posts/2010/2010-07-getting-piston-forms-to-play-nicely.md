---
date: "2010-07-16T15:14:00.000-07:00"
description: ""
published: true
slug: 2010-07-getting-piston-forms-to-play-nicely
tags:
  - django
  - forms
  - json
  - python
  - xml
  - legacy-blogger
time_to_read: 5
title: Getting piston forms to play nicely with JSON
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/07/getting-piston-forms-to-play-nicely.html)_.

<blockquote><b>Critical Update 2012/05/10!!!</b> 
<b>Critical Update 2012/05/10!!!</b> 
<b>Critical Update 2012/05/10!!!</b> 

Except for a critical security patch,&nbsp;[django-piston](htts://bitbucket.org/jespern/django-piston/wiki/Home) has been unsupported for over 10 years. That is an eternity, and the number of forks to address multiple issues is cause for alarm. Also, the original author has left the project. Because of that, in it's place at this time I recommend [django-tastypie](https://pypi.python.org/pypi/django-tastypie). It is [up-to-date](https://github.com/toastdriven/django-tastypie/commits/master), has [very good documentation](https://django-tastypie.readthedocs.org/), [supports OAUTH](https://django-tastypie.readthedocs.org/en/latest/authentication_authorization.html#oauthauthentication), and scored second place in the Django Packages thunderdome (it got nearly 3x as many points!). Another tool to consider is [Django Rest Framework](https://django-rest-framework.readthedocs.org/), which is as good as django-tastypie but lacks the OAUTH support.</blockquote>
<b>Back to the existing blog post...</b>

A commonly used tool by [Djangonauts](https://djangopeople.com/) is [django-piston](https://bitbucket.org/jespern/django-piston/wiki/Home), which is designed to make building a [REST](https://en.wikipedia.org/wiki/REST) API easier. It even works with [Django](https://djangoproject.com/) forms to provide easily written PUT/POST validation, which should be pretty darn nice. Unfortunately,&nbsp;if you go with django-piston forms validation it doesn't accomodate the JSON (or XML or YAML) requests and if validation fails it responds in HTML. Even more unfortunate, making validation accept and return JSON with&nbsp;PUT/POST requests is not documented.

<i>While one could argue that it is documented in the django-piston docstrings, in my opinion that is not sufficient.</i>

Fortunately while working on a project for [Revolution Systems](https://www.revsys.com/) we worked out a solution:



```python
"""
myapi/resource.py

    author: Daniel Greenfeld
    license: BSD

This assumes your API accepts JSON only.
"""

import json

from piston.decorator import decorator
from piston.resource import Resource
from piston.utils import rc, FormValidationError

def validate(v_form, operation='POST'):
    """ This fetches the submitted data for the form
        from request.data because we always expect JSON data
        It is otherwise a copy of piston.util.validate.
    """

    @decorator
    def wrap(f, self, request, *a, **kwa):

        # Assume that the JSON response is in request.data
        # Probably want to do a getattr(request, data, None)
        #   and raise an exception if data is not found
        form = v_form(request.data)

        if form.is_valid():
            setattr(request, 'form', form)
            return f(self, request, *a, **kwa)
        else:
            raise FormValidationError(form)
    return wrap

class Resource(Resource):

    def form_validation_response(self, e):
        """
        Turns the error object into a serializable construct.
        All credit for this method goes to Jacob Kaplan-Moss
        """

        # Create a 400 status_code response
        resp = rc.BAD_REQUEST

        # Serialize the error.form.errors object
        json_errors = json.dumps(
            dict(
                (k, map(unicode, v))
                for (k,v) in e.form.errors.iteritems()
            )
        )
        resp.write(json_errors)
        return resp
```

Usage in handlers.py:

```python
from django import forms

from piston.handler import BaseHandler

from myapp.models import Article

# We use our custom validate rather than piston's default
from myapi.resource import validate

class ArticleForm(forms.Form):
    """ This is best stored in forms.py but we put
        here for sake of clarity"""

    author      = forms.CharField(required=True)
    title       = forms.CharField(required=True)
    content     = forms.CharField(required=True)

class ArticleHandler(BaseHandler):

    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE', )
    model = Article

    @validate(ArticleForm)
    def create(self, request):
        # Create/POST code goes here.

    @validate(ArticleForm)
    def update(self, request, id):
        # Update/PUT code goes here.

```

Usage in urls.py:

```python
from django.conf.urls.defaults import *

from piston.authentication import HttpBasicAuthentication as auth

# Import our ArticleHandler
from myapi.handlers import ArticleHandler
# Use our custom Resource class instead of piston's default
from myapi.resource import Resource

article_handler = Resource(ArticleHandler, authentication=auth)

urlpatterns = patterns('',
   url(
        r'^articles/(?P(\d+))$',
        article_handler,
        { 'emitter_format': 'json' },
        name='api_article'

```

Of course, this assumes you are mapping Create/Read/Update/Delete ([CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)) actions to your API.

I'm interested to see other solutions people have used to handle this in django-piston, and what suggestions people have that could improve on the examples I'm supplying here.

---

## 5 comments captured from [original post](https://pydanny.blogspot.com/2010/07/getting-piston-forms-to-play-nicely.html) on Blogger

**Tom said on 2010-07-17**

Nice. I created an XML mimer for piston so that it could receive XML in the same format that it emits XML which worked well for what I wanted. It's @ https://bitbucket.org/cootetom/xml-mimer/overview

**pydanny said on 2010-07-17**

@Tom,

Do you have the non-patch version of the code?

**Ryan Blunden said on 2011-02-08**

This is absolutely brilliant work. I've had a few challenges getting Django Piston to work and this blog post was immensely useful. Thanks heaps!

**Unknown said on 2012-10-06**

hey, thanks to for setting clear that piston is not developed anymore, that really makes me considering to try another framework... unfortunaly i have to say that the documentation of tastypie is awful especially if you try wo work with non-rel datatsources

**pydanny said on 2012-10-06**

Marty,

If you have problems with the tastypie documentation, might I suggest you do one of the following:

1. Submit a ticket to github.com/toastdriven/django-tastypie/issues and specify where you feel there are specific areas of weakness.

2. If you figure it out, submit it as a pull request to django-tastypie.

Also, there is a MongoEngine wrapper someone wrote for tastypie that you can find at https://www.djangopackages.com/packages/p/django-tastypie-mongoengine/. If MongoDB isn't your nonrel database, then at least you can use that as a baseline for your own implementation.

```

```
