---
date: "2007-11-05T10:18:00.000-08:00"
description: ""
published: true
slug: 2007-11-head-meets-desk
tags:
  - zope
  - legacy-blogger
time_to_read: 5
title: Head meets desk
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/head-meets-desk.html)_.

I need to add a `DateTime` field to my primary content object. Unfortunately, in Zope 3, they named it `Datetime` in `zope.schema`. Now, before you say I should notice the coding standards, please note that the single textline object is `zope.schema.TextLine`.

Figuring out this one took me way too long for comfort.

This is the first time I've seen this sort of mistake in Zope 3. Until now I've been delighted with Zope 3's consistency and elegance.

I'm hoping it will be a while before I find the same sort of thing again.
