---
date: "2012-05-10"
published: true
slug: choosing-api-framework-for-django
tags:
  - python
  - django
  - api
  - review
time_to_read: 3
title: Choosing an API framework for Django
---

First off, out of the box, [Django](https://djangoproject.com) lets you
construct API responses with a little work. All you need to do is
something like this:

```python
# Copied from https://docs.djangoproject.com/en/1.4/topics/class-based-views/#more-than-just-html
from django import http
from django.utils import simplejson as json

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)
```

Once you get that mixin, use it in your views like so:

```python
# modified from djangoproject.com sample code
from django.utils import simplejson as json

class JSONDetailView(JSONResponseMixin, MyCustomUserView):
    def convert_context_to_json(self, context):

        context['objects'] = User.objects.values('first_name','last_name','is_active')
        return json.dumps(context)
```

This works pretty well in a number of simple cases, but doing things
like pagination, posting of data, metadata, API discovery, and other
important things ends up being a bit more work. This is where the
resource oriented API frameworks come in.

# What makes a decent API Framework?

These features:

- pagination
- posting of data with validation
- Publishing of metadata along with querysets
- API discovery
- proper HTTP response handling
- caching
- serialization
- throttling
- permissions
- authentication

Proper API frameworks also need:

- Really good test coverage of their code
- Decent performance
- Documentation
- An active community to advance and support the framework

If you take these factors, at this time there are only two API
frameworks worth using, [django-tastypie](#django-tastypie) and
[django-rest-framework](#django-rest-framework).

# Which one is better? django-tastypie or django-rest-framework?

I say they are equal.

You simply can't go wrong with either one. The authors and communities
behind both of them are active, the code is solid and tested. And here
are my specific thoughts about both of them:

# django-tastypie

Using django-tastypie is like playing with pure Python while using the
Django ORM. I find it very comfortable. Seems really fast too. The
documentation is incredible, and I rarely have any problems figuring
anything out. It also supports OAuth 1.0a out of the box, which is
mighty awesome these days.

In fact, I wrote a custom OAuth2 handler for django-tastypie for
consumer.io that I'm working to extract for
publication.

# django-rest-framework

As it's based off Django 1.3 style Class Based Views (CBVs), it has a
very familiar pattern. Actually, because of the quality of the
documentation, I really prefer using django-rest-framework CBVs more
than using Django's actual CBVs.

Maybe I should make an HTML renderer for django-rest-framework? :-)

# But what about django-piston?

**Don't use django-piston**.

I don't want to say anything negative, but let's face it:
**django-piston is dead**. Besides a critical security release last
year, nothing has been done for it in about 3 years. The documentation
is weak, the code mostly untested, and the original author left. He has
gone on to do some amazing things. Django-piston was amazing in its
time, but its time has passed and so should you.

The only reason for using django-piston for years has been that it
supported OAuth, but django-tastypie now addresses that use case. I've
used django-tastypie's basic OAuth class and rolled custom
Authentication modules to support some extra OAuth flavors and found it
wonderful.

Use django-tastypie or django-rest-framework instead. You'll be much,
much happier for it.

---

[Discuss this on Hacker
News](https://news.ycombinator.com/item?id=3954314)
