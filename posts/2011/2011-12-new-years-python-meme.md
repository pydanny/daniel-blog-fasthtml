---
date: '2011-12-22T16:46:00.000-08:00'
description: ''
published: true
slug: 2011-12-new-years-python-meme
tags:
- opencomparison
- courses
- pyramid
- django
- plone
- python
- classes
- django packages
- legacy-blogger
time_to_read: 5
title: "New Year\u2019s Python Meme"
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/12/new-years-python-meme.html)*.

I love these blog memes, so I give you my version of [Tarek Ziade's New Year's Python Meme](https://tarekziade.wordpress.com/2011/12/20/new-years-python-meme-2/).

<h3>1. What’s the coolest Python application, framework or library you have discovered in 2011?</h3>
For [python](https://python.org) libraries, that would have to be [Kenneth Reitz](https://twitter.com/kennethreitz)' [python-requests](https://docs.python-requests.org/) library. I've used it for an amazing amount of stuff and [blogged](https://pydanny.blogspot.com/2011/05/python-http-requests-for-humans.html) about it. It took the grunge out of doing HTTP actions with Python. The API is clean and elegant, getting out of your way. It embodies the State of the art for API design, which closely matches the Zen of Python.

For applications, [djangolint.com](https://djangolint.com) is awesome. It has helped me out so much on several projects. I would love to see something like this implemented and maintained for modern Python.

All the Python friendly PaaS efforts that have emerged are changing the landscape for those of us who want to launch projects but don't want to become full time system administrators in the process. [Heroku](https://heroku.com), [DjangoZoom](https://djangozoom.com), [DotCloud](https://www.dotcloud.com/), [ep.io](https://ep.io), [gondor.io](https://gondor.io), and others are making it possible for developers to focus on development not server tooling. Google App Engine paved the way and it is wonderful to see the rest of the universe catch up with material that more closely follow core.

<h3>2. What new programming technique did you learn in 2011?</h3>
Event based programming! I've touched on it for years, but this year I really got a lot more more into it thanks to [Aurynn Shaw](https://twitter.com/aurynn) kickstarting me and [Audrey Roy](https://twitter.com/audreyr) expanding my knowledge ever since.

<h3>3. What’s the name of the open source project you contributed the most in 2011? What did you do?</h3>
I participated mostly as co-lead in the [Open Comparison](https://opencomparison.org) project, which amongst other things involved running the largest sprint at PyCon 2011. We maintained [Django Packages](https://djangopackages.com) and launched [Pyramid](https://pyramid.opencomparison.org) and [Plone](https://plone.opencomparison.org) versions of the project. We hope to launch a Python implementation in 2012.

I took a lot of notes this year at [pydanny-event-notes](https://pydanny-event-notes.rtfd.org) - enough to make a book.

<h3>4. What was the Python blog or website you read the most in 2011?</h3>
Like [Nick Coghlan](https://www.boredomandlaziness.org/2011/12/new-year-python-meme-december-2011.html), that would be [https://planet.python.org](https://planet.python.org).

<h3>5. What are the three top things you want to learn in 2012?</h3>


1. How to use whatever consistently maintained project that replaces PIL that works in Python 2.7.x and Python 3.x.
- Really advanced Python as taught by Raymond Hettiger.
- [backbone.js](https://documentcloud.github.com/backbone/)


<h3>6. What are the top software, app or lib you wish someone would write in 2012?</h3>
A tool python-requests, but for shell access. Something like [Unipath](https://pypi.python.org/pypi/Unipath), but kept up-to-date and with nicely written documentation on [Read the Docs](https://rtfd.org).

A PIL replacement that is maintained, works for all modern Pythons, and is close enough to the PIL API to not cause too much confusion.

Something like [Django Lint](https://djangolint.com) but for Python 2.7.x/3.x.

An open source project that tracks test coverages across PyPI and publishes reports of the results via an API.

<h3>Want to do your own list? here’s how:</h3>

- copy-paste the questions and answer to them in your blog
- tweet it with the #2012pythonmeme hashtag



---

## 6 comments captured from [original post](https://pydanny.blogspot.com/2011/12/new-years-python-meme.html) on Blogger

**Rok Garbas said on 2011-12-23**

hey,

would Pillow (fork by Alex Clark and its largely used in among plonistas) be the solution for PIL you're looking for? or at least would be a place where we can get PIL working for python 2.7 and 3.x.

or you are looking completely new library?

https://pypi.python.org/pypi/Pillow
https://github.org/collective/Pillow

**pydanny said on 2011-12-23**

@Rok,

Let's face the truth, PIL is effectively unmaintained. Pillow is Alex Clark's way of getting it to be a reliable package installation.

Also, according to the Image experts I know (I'm engaged to one who has written a commercial Image processing library but she isn't the only one), PIL's processing capabilities are limited compared to other tools. For example, Image rotation causes a huge amount of lossy compared to tools used by other languages.

PIL that works in all places suffices for now, but in the long run the Python world needs a real replacement.

**Unknown said on 2011-12-23**

The limited built-in shell support annoys me too, but I'm not sure an OO-path object is the answer.

My own contributions to making shell programming in Python less painful are WalkDir and Shell Command:

https://walkdir.readthedocs.org/
https://shell-command.readthedocs.org/

(They each have some issues at the moment - I plan to release new versions of both of them in early January)

You may also want to talk to Antoine Pitrou about releasing his pathlib work as a PyPI package:
https://hg.python.org/features/pathlib/file/tip/Lib/pathlib.py

**Jons Obrist said on 2011-12-27**

&quot;A PIL replacement that is maintained, works for all modern Pythons, and is close enough to the PIL API to not cause too much confusion.&quot;

I could not agree more. And while we're at it, it would be amazing if this could be done in pure Python.

**PA Parent said on 2011-12-30**

Hi!

I really like this idea :

&quot;An open source project that tracks test coverages across PyPI and publishes reports of the results via an API.&quot;

I might participate if someone starts that :)

**Ken Swift said on 2012-01-04**

&quot;How to use whatever consistently maintained project that replaces PIL that works in Python 2.7.x and Python 3.x.&quot;

you can try Pystacia: https://liquibits.bitbucket.org/index.html

and please spread the word!

