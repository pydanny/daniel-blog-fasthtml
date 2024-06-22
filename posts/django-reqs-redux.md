---
date: '2012-08-15'
published: true
slug: django-reqs-redux
tags:
- python
- django
- setup
time_to_read: 3
title: Django Requirements 2012-08-15
---

A little over three months ago [I blogged about my preferred
requirements](/django-requirements-for-a-project.html)
list. It's now nearly the eve of [Django Dash](https://djangodash.com),
and I feel it's time to update the list. I'm going to bump the
versions on some of the existing packages and add some new ones to the
list.

New Packages
============

[django-braces==0.1.3](https://pypi.python.org/pypi/django-braces/)
------------------------------------------------------------------

Want to use Django Class Based Views but unhappy with the missing
components like `LoginRequiredMixin`, `SelectRelatedMixin`, and even
`StaffuserRequiredMixin`? Not to worry, as this library will make Django
CBVs **134% easier to use**.

[django-secure==0.1.2](https://pypi.python.org/pypi/django-secure/)
------------------------------------------------------------------

Django is rather secure, but there is a checklist of things that the
security experts want you to do. Save yourself forgetting something and
use this library to do all those little things.

[django-profiletools==0.1.3](https://pypi.python.org/pypi/django-profiletools/)
------------------------------------------------------------------------------

Have you ever used the django-debug-toolbar and noticed that you did
that same `request.user.get_profile()` call a dozen times? Ever want to
just call that once? This library, by yours truly, resolves the issue.
It loads the user's profile object once, and then passes it down the
request chain.

------------------------------------------------------------------------

Existing Packages
=================

[Django==1.4.1](https://pypi.python.org/pypi/Django/1.4.1)
---------------------------------------------------------

If you need sessions, forms, templates, and relational database models,
then I can argue you've got the ideal
[Django](https://djangoproject.com) project. Make certain you are running
the latest Django version (1.4.1). If you have any reason to stick to
the Django 1.3 series, I advise bumping it up to Django 1.3.2.

[psycopg2==2.4.5](https://pypi.python.org/pypi/psycopg2)
-------------------------------------------------------

This is the database connector to PostgreSQL, which is what you should
be using. Django is known for playing 'nicer' with PostgreSQL than
say... MySQL.

[django-debug-toolbar==0.9.4](https://pypi.python.org/pypi/django-debug-toolbar)
-------------------------------------------------------------------------------

Because not using this tool is insane.

[django-extensions==0.8](https://pypi.python.org/pypi/django-extensions)
-----------------------------------------------------------------------

Because amongst other things this library gives you, I never want to
write my own `TimeStampedModel` ever again. :-)

[South==0.7.6](https://pypi.python.org/pypi/South)
-------------------------------------------------

Django gives you the freedom to migrate data in the way you want. The
way I want to do it is via South.

[django-registration==0.8.0](https://pypi.python.org/pypi/django-registration)
-----------------------------------------------------------------------------

The common go-to tool for non-Social registration.

This is a very solid tool, but you do have to make your own templates or
find someone's fork that has a copy of templates that match.

django-social-auth== 0.7.4
--------------------------

Want to authenticate via Twitter, Facebook, or GitHub? Then use this
very useful package.

[django-floppyforms==1.0](https://pypi.python.org/pypi/django-floppyforms)
-------------------------------------------------------------------------

An excellent tool for making your forms HTML5-ish out of the box. It
allows full control of form rendering in the templates.

[django-crispy-forms==1.1.4](https://pypi.python.org/pypi/django-crispy-forms)
-----------------------------------------------------------------------------

The child of my own django-uni-forms, this will let me create forms
using div-based controls super fast, and do layout customizations if I
need them.

[django-heroku-postgresify==0.2](https://pypi.python.org/pypi/django-heroku-postgresify)
---------------------------------------------------------------------------------------

This tool makes getting the PostGreSQL settings out of Heroku trivial.

[django-heroku-memcacheify==0.3](https://pypi.python.org/pypi/django-heroku-memcacheify)
---------------------------------------------------------------------------------------

This tool makes getting the memcache settings for Heroku trivial.

[gunicorn==0.14.6](https://pypi.python.org/pypi/gunicorn)
--------------------------------------------------------

All the cool kids who play in devops swear by Gunicorn.

------------------------------------------------------------------------

Installing the above packages
=============================

Never copy/paste these libraries directly into your projects. Do it the
right way: **use proper Python dependency management**.

Create a `requirements.txt` file and install them as proper
dependencies. The file should contain the following text:

    Django==1.4.1
    South==0.7.5   
    django-braces==0.1.3    
    django-crispy-forms==1.1.4
    django-debug-toolbar==0.9.4
    django-extensions==0.8
    django-floppyforms==1.0
    django-social-auth==0.7.4
    django-heroku-memcacheify==0.3
    django-heroku-postgresify==0.2
    django-profiletools==0.1.3
    django-registration==0.8.0   
    django-secure==0.1.2
    gunicorn==0.14.2
    psycopg2==2.4.5

Once you have that, you install them thus in your
[virtualenv](https://pypi.python.org/pypi/virtualenv):

    pip install -r requirements.txt

Now that I have all this, it's time to code!
