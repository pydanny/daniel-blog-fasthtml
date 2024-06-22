---
date: '2011-04-01T00:01:00.000-07:00'
description: ''
published: true
slug: 2011-03-announcing-garbaginator
tags:
- pycon
- pyramid
- django
- foss
- plone
- python
- xml
- zope
- GAPE
- legacy-blogger
time_to_read: 5
title: Announcing Garbaginator!
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/03/announcing-garbaginator.html)*.

While working on [Packaginator](https://github.com/cartwheelweb/packaginator) at the PyCon 2011 sprints we discovered some serious issues in the way that Django handles garbage collection. After a huge amount of work, we managed to isolate and fix the problem. This 'fix', as it were, was only possible by doing a very sophisticated 'hack' of critical internal components of the Django Web Application framework. We also discovered that similar issues occurred in other existing Python application frameworks such as Pyramid, Flask, Web.py, Web2Py, Grok, Twisted, Tornado, Google App Engine, and Rails.

Since then the Packaginator community has been fiercely debating what we should do with our newly created set of hacks. After a lot of arguments going both ways we've decided to come up with our own application framework and release it to the world under the GPL license.

This brand new application framework ignores the lessons learned from all the other Python frameworks and embraces the cutting edge concept of Not-Invented-Here. It focuses less on features and enhancements over existing systems and much, much more on the critical concept of formal Garbage handling.

Some of the critical modules include:


- RubberGloves (for handling dirty objects)
- Django-Garbaginator
- Flask-Recycling
- Pyramid-Garbaginator
- Web.2.py Garbaginator Bridgerator ('cause people always get Web2Py and web.py confused with each other so we bridged them together)
- BlueBream

<div>Check out the home page at: [https://garbaginator.cartwheelweb.com](https://garbaginator.cartwheelweb.com/)</div>Fork Garbaginator on GitHub: [https://github.com/cartwheelweb/garbaginator](https://github.com/cartwheelweb/garbaginator)

<b>Note:</b> This was an April Fool's Day Joke
<ul></ul>

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2011/03/announcing-garbaginator.html) on Blogger

**Paolo Corti said on 2011-04-01**

1th of April :)

