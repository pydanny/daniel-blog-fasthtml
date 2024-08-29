---
date: "2008-01-24T05:36:00.000-08:00"
description: ""
published: true
slug: 2008-01-svn-versionator
tags:
  - python
  - legacy-blogger
time_to_read: 5
title: SVN versionator!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/01/svn-versionator.html)_.

I'm the one who has been cutting tags for our big project at work. The problem is that its kind of a pain with a number of steps, and while I've yet to make a mistake, the chances are there. So last night I decided I ought to build a tag creator in Python.

This won't be some generic tool to release on the world. We've got some application and environment specific things going on that I can't share.

That said, I could probably do it in a way to make it generic. Basically you would create a config file for your location, a SVN externals file, and then when you would run Versionator it would create the tag with just the system version as your only parameter. And I could probably do it in a way so it would support SVN or Bizare. Maybe Mercury or Git in the distant future.

Hmmmm....

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2008/01/svn-versionator.html) on Blogger

**Reinout van Rees said on 2008-01-24**

I made a simple python script to help me with tagging releases just two weeks ago. Every colleague that I gave it to is now happily using it.

It just searches the version.txt, figures out the right tags directory in svn, looks if there's a tag for the version already and applies it if you want it.

Afterwards it offers to make a .tgz or a private .egg out of it and copies it optionally to our private download area.

Just automating the tagging takes so much pain out of the release process already!
