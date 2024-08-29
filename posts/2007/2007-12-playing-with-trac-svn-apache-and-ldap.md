---
date: "2007-12-13T07:08:00.000-08:00"
description: ""
published: true
slug: 2007-12-playing-with-trac-svn-apache-and-ldap
tags:
  - python
  - legacy-blogger
time_to_read: 5
title: Playing with Trac, SVN, Apache, and LDAP
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/12/playing-with-trac-svn-apache-and-ldap.html)_.

For work I have a task of creating a script utility that lets system administrators create Projects in a mix of Trac, SVN, Apache, and LDAP. Its a bunch of work, and lets me lay with pure Python yet again. Much as I like Plone/Zope, sometimes its nice to just do this sort of thing.

Anyway, Trac already comes with a command line interface. I extend it and use it quite a bit. The problem, alas, is that the Trac CLI mixes logic with presentation. So you can't extend all of it. Also, I have lots more stuff that my system is doing.

So today I'm creating views for my script. The views are the individual methods called by the user of the script, and they exist as functions within a single class. No business logic. It means at some point we can put a website around the core functionality of the script.

Anyway, I needed to write documentation for this script. I figured I would stick it in the doc strings of the individual view methods and call it with the `__doc__` method. Well, I did so, and it works like a charm. So again, in Python, the code documents itself.

Again, more reason to love Python.

:)
