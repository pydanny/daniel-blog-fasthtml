---
blogbook: 'True'
date: 2013-7-11
published: true
slug: experiences-with-django-python3
tags:
- python
- django
- python3
time_to_read: 5
title: My experiences with Django and Python 3
---

The following are my notes, observations, and resources on the subject
of working with Python 3 (with or without Django).

Recently I've become involved in a couple of Django efforts that used
Python 3.3. The quick summary of what I learned is pretty much what I
expected: Out of the box Django 1.5 (and the pending 1.6 release) works
fine with Python 3.3.2.

Use Python 3.3.2!
=================

Myself and others have encountered problems with using Django 1.5+ and
earlier versions of Python 3. The issues can be tricky; for example
`syncdb` fails in curious ways on Python 3.3.0.

The answer, for me, is to use Python 3.3.2 and don't look back.

Checking for Python 3 Compatibility
===================================

The steps I use are below. They are in rough order:

-   Look up the package on [PyPI](https://pypi.python.org/pypi/) and see
    if any of it's trove classifiers mention Python 3 status.
-   See if a pull request for Python 3 support is outstanding.
-   Run the test suite using Python 3.3
-   Use [2to3](https://docs.python.org/2/library/2to3.html) to scan the
    code for issues.
-   If a Django project, check the models for `__str__()` methods. If it
    has them, it's a pretty good indicator it's Python 3.3 friendly.
-   Make a judgement call.

Important Packages that work with Python 3
==========================================

In this section I'm listing a few of the Python and Django packages
I'm using that worked without me having to do anything sort of
modification or pull request:

-   Django 1.5 and 1.6 beta
-   Pillow (drop-in replacement for PIL)
-   South
-   django-bootstrap-registration (templates for django-registration)
-   django-braces
-   django-crispy-forms
-   requests

Conversion process
==================

How I convert Python 2 code to Python 3:

-   Use 2to3 until you get used to not using it.
-   Fix any problems you find in the code. Try to keep solutions as
    simple as possible.
-   Submit the pull request.
-   Politely poke the package owner to accept the pull request.
-   Once the owner accepts the pull request, gently poke the package
    owner to push the update to PyPI.

Packages that needed conversion
===============================

Here are four packages worth noting that had to be converted:

-   unicode-slugify
-   django-registration
-   django-stripe-payments (in progress)
-   django-nose

Let's get into some detail for each package:

[unicode-slugify](https://pypi.python.org/pypi/unicode-slugify)
---------------------------------------------------------------

This is a handy, more unicode friendly replacement for Django's
django.utils.text.slugify function. It failed on Django 1.6 beta, so I
forked it, submitted a successful pull request after testing it on
Python 2.6, 2.7, and Python 3.3.2. The Mozilla team pushed it to PyPI
and even gave me
[badges](https://badges.mozilla.org/en-US/profiles/profile/pydanny) for
my efforts!

In the future I would like to see this little package work without the
dependency of Django itself, and I've had a couple replacement
dependencies suggested.

django-registration
-------------------

With the 1.0 release, it's been updated for Django 1.5, *unless* you
use customized User models or Python 3. I really needed this on PyPI,
but the maintainer is very busy. Therefore, I forked the project,
renamed it to [django-reg](https://pypi.python.org/pypi/django-reg)
while referencing the original, and pushed it to PyPI. Not ideal, but
sometimes you have to do what you have to do.

Lesson learned: In the future skip these issues and just use
[django-allauth](https://pypi.python.org/pypi/django-allauth).

**Update 08/08/2013**: All my Python 3 work is now on django-allauth.
This way I don't have to do the work of maintaining a compatibility
branch.

[django-stripe-payments](https://pypi.python.org/pypi/django-stripe-payments) (in progress)
-------------------------------------------------------------------------------------------

While django-zebra is better known for handling stripe payments, I
prefer to use Eldarion's excellent, well-maintained and tested
django-stripe-payments. It was delayed because django-nose wasn't
Python 3 compatible, but that's been fixed as of at least 7/28/2013.
Unfortunately, it's Travis-CI tests fail with the Django 1.5 era custom
user model because of what might be a linter misconfiguration. In
theory, the just released version of pylint (1.0) should work without
any problems.

Of course, I informed the maintainers of my efforts and problems.

**Update 07/30/2013**: Updated the text to reflect the current status of
the linter problems I'm having.

**Update 08/08/2013**: While django-stripe-payments is useful, it
doesn't do everything that I need. I tried extending it's logic into a
third app, but that was proving unweildy. Therefore, I forked the
project to [dj-stripe](https://pypi.python.org/pypi/dj-stripe), which
has the features and compatibility that I need.

[django-nose](https://pypi.python.org/pypi/django-nose)
-------------------------------------------------------

Today, I asked the maintainer to visit an outstanding pull request that
adds Python 3 compatibility. It's a good idea to do this since they
might already be working on it, or may have observations they want to
share.

**Update 7/28/2013**: Jeff Balogh pushed a Python 3.3.2+ compatible
version up to PyPI a few days ago. Makes everything so much better!

Dealing with Slow Maintainers
=============================

For what it's worth, from experience ranting to or about slow-moving
maintainers is absolutely counter-productive. People have lives and jobs
that sometimes get in the way of open source. It's more productive to
be patient, be polite, and if necessary do an absolutely minimal fork or
find a working alternative.

Handy Resources
===============

The following are two useful resources on converting Python 2 to Python
3. I don't follow their methods exactly, I just use them as rough
guidelines for my own workflow.

-   [Porting Django apps to Python 3](https://youtu.be/cJMGvAYYUyY) video
    by Jacob Kaplan-Moss
-   [Porting to Python 3](https://python3porting.com/) book (free HTML or
    paid PDF, Kindle, ePub) by Lennart Regebro

For various Python 3 recipes, I keep my kindle reader open to this
priceless gem:

-   [Python Cookbook, 3rd
    Edition](https://www.amazon.com/Python-Cookbook-ebook/dp/B00DQV4GGY/?tag=ihpydanny)
    book by David Beazley and Brian K. JOnes.

Closing Thoughts
================

This blog post makes it seems like I've put in a lot of work getting
things to Python 3, but that isn't the case at all. In fact, for the
most part the transition has been trivial. There are a few minor
hiccups, but nothing that's killing a whole day or destroying a
deadline.

**Benefit of using Python 3?** I get to call myself a **Python 3
Hipster**.

**Downside of using Python 3?** A little bit of extra homework on each
project. However, each time I fix something it's done and I've made
the world a better place.
