---
date: "2008-02-14T05:49:00.003-08:00"
description: ""
published: true
slug: 2008-02-ditching-funkload
tags:
  - plone
  - legacy-blogger
time_to_read: 5
title: Ditching Funkload
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/ditching-funkload.html)_.

After some thought, I've decided to ditch Funkload as a stress/load testing tool. Its fun to play with, but Funkload has a couple issues that makes it hard to justify

- The lack of charting. Yes, writing charting software is fun, but my current work deadline (end of month) doesn't give me the ability to do my other work and do that charting and still meake the deadlines.
- I've noticed that funkload has some good properties like pointing out slowest objects, it doesn't well define what all of its metrics really mean. What is P90 anyway and why do I care? Why aren't metrics defined like the rest of the package.

So I'm looking into other tools including Zope/Plone specific ones like ZopeProfiler and the TAL checker..
