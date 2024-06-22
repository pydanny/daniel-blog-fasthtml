---
date: '2011-06-25T15:48:00.000-07:00'
description: ''
published: true
slug: 2011-06-do-not-upload-dev-releases-at-pypi
tags:
- django
- python
- legacy-blogger
time_to_read: 5
title: Do not upload dev releases at PyPI
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/06/do-not-upload-dev-releases-at-pypi.html)*.

In [my last blog post](https://pydanny.blogspot.com/2011/06/announcing-django-uni-form-080-beta.html) I mentioned that the plan was to release the django-uni-form 0.8.0 final in about six days. To my chagrin I was pointed at Tarek Ziade's [post about not publishing beta releases on PyPI.](https://tarekziade.wordpress.com/2011/02/15/do-not-upload-dev-releases-at-pypi/)&nbsp;So the django-uni-form team has now pushed up the 0.8.0 release of the library today, and removed the BETA from discovery via the [web](https://djangopackages.com/packages/p/django-uni-form/) or [pip](https://pypi.python.org/pypi/pip).

<b>Lesson learned</b>: Until future notice from the distutils2 effort led by Tarek, if you are running a project that has any Stable releases, don't use [PyPI](https://pypi.python.org/pypi) to publish non-final versions.