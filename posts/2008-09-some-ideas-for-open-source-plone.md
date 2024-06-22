---
date: '2008-09-12T13:44:00.002-07:00'
description: ''
published: true
slug: 2008-09-some-ideas-for-open-source-plone
tags:
- plone
- legacy-blogger
time_to_read: 5
title: Some ideas for open source Plone Products
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/09/some-ideas-for-open-source-plone.html)*.



- <span style="font-weight: bold;">RSA Authentication Plugin </span>(I know they have them for Zope, but perhaps making them Plone 3 friendly if that is needed?)



- <span style="font-weight: bold;">Robust RSS/Atom consumer</span> (I've worked with FeedFeeder.  It is pretty good but has trouble handling ugly RSS feeds.  Maybe I should just contribute to FeedFeeder?)




---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2008/09/some-ideas-for-open-source-plone.html) on Blogger

**Reinout van Rees said on 2008-09-14**

You're welcome to take a shot at feedfeeder. It uses feedparser for consuming feeds, so RSS ought to be parsed just fine. Or at least as fine as you're going to get them parsed. Any problems are probably assumptions that feedfeeder makes about converting a blog post to something ploneish.

And of course the biggest assumption is that feedfeeder actually creates items in your plone site. Reason: it was originally meant to grab items from an otherwise company-internal feed and publish them on another website.

Reinout van Rees

