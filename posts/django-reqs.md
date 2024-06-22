---
date: "2012-05-09"
published: true
slug: django-reqs
tags:
  - python
  - django
  - setup
time_to_read: 2
title: Django Requirements for a project
---

Today I'm starting a new project. I'm working as fast as I can and
hope to launch on Friday. What are my package dependencies?

# [Django==1.4](https://pypi.python.org/pypi/Django/1.4)

Unlike my last quick project which was [Flask](https://flask.pocoo.org/),
this effort really falls into [Django](https://djangoproject.com)'s
sweet spot. I need sessions, forms, templates, and models to do things
in an ideal Django pattern.

# [psycopg2==2.4.5](https://pypi.python.org/pypi/psycopg2)

I need transactions and hard-type validation in the database, which
means PostgreSQL. If I didn't need transactions or the hard-type
validation I would consider MongoDB instead.

# [django-debug-toolbar==0.9.4](https://pypi.python.org/pypi/django-debug-toolbar)

Because not using this tool is insane.

# [django-extensions==0.8](https://pypi.python.org/pypi/django-extensions)

Because amongst other things this library gives you, I never want to
write my own `TimeStampedModel` ever again. :-)

# [South==0.7.5](https://pypi.python.org/pypi/South)

Django gives you the freedom to migrate data in the way you want. The
way I want to do it is via South.

# [django-registration==0.8.0](https://pypi.python.org/pypi/django-registration)

Normally
[django-social-auth](https://pypi.python.org/pypi/django-social-auth) is
my go-to tool for registration, but in this case I need simple
username/password registration. This is a very solid tool, but you do
have to make your own templates or find someone's fork that has a copy
of templates that match.

**Update 2013/12/17**: django-registration is no longer maintained and
doesn't entirely work with modern Django's new user model system. Use
[django-allauth](https://github.com/pennersr/django-allauth) instead.

# [django-floppyforms==0.4.7](https://pypi.python.org/pypi/django-floppyforms)

An excellent tool for making your forms HTML5-ish out of the box.

# [django-crispy-forms==1.1.3](https://pypi.python.org/pypi/django-crispy-forms)

The child of my own django-uni-forms, this will let me create forms
using div-based controls super fast, and do layout customizations if I
need them.

# [django-heroku-postgresify==0.2](https://pypi.python.org/pypi/django-heroku-postgresify)

This tool makes getting the PostGreSQL settings out of Heroku trivial.

# [django-heroku-memcacheify==0.1](https://pypi.python.org/pypi/django-heroku-memcacheify)

This tool makes getting the memcache settings for Heroku trivial.

# [gunicorn==0.14.2](https://pypi.python.org/pypi/gunicorn)

All the cool kids who play in devops swear by Gunicorn. I use it because
Heroku seems to recommend it for Django deployments.

---

# Installing the above packages

Never copy/paste these libraries directly into your projects. If you do
that, you'll end up hating yourself later as your local instances
become unmaintained forks of the real project. Also, unless you are
really careful in your copy/pasting, you'll be in violation of various
open source licenses. Odds are the FOSS police aren't going to find
you, but I can assure you that when you bring in one of the authors of
these packages to help you fix a problem he/she is going to be mighty
annoyed at the lack of attribution.

Do it the right way: do proper Python dependency management.

Create a `requirements.txt` file and install them as proper
dependencies. The file should contain the following text:

    Django==1.4
    South==0.7.5
    django-crispy-forms==1.1.3
    django-debug-toolbar==0.9.4
    django-extensions==0.8
    django-floppyforms==0.4.7
    django-heroku-memcacheify==0.1
    django-heroku-postgresify==0.2
    django-registration==0.8.0
    gunicorn==0.14.2
    psycopg2==2.4.5

Once you have that, you install them thus in your
[virtualenv](https://pypi.python.org/pypi/virtualenv):

    pip install -r requirements.txt

Now that I have all this, it's time to code!

---

[![2010 Snowstorm!](/images/4358842735_38991c0944.jpg)](https://www.flickr.com/photos/pydanny/4358842735/)
