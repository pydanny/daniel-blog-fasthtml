---
date: "2009-11-09T19:01:00.002-08:00"
description: ""
published: true
slug: 2009-11-code-ill-reuse
tags:
  - november
  - django
  - Linux
  - plone
  - python
  - blog
  - legacy-blogger
time_to_read: 5
title: Code I'll reuse
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/11/code-ill-reuse.html)_.

When I'm evaluating a package to use in my work or play I tend to look at five things. I think many of my on-line colleagues look at a similar list. If its missing too many of these things then odds are I'll go somewhere else for my needs or roll my own.

<span style="font-weight: bold;">Documentation</span>
Did the author bother with a README file? How about some sphinx documentation? How complete it it? Does it get me started and give a few basic examples?

I'm okay with typos and mistakes. These happen. But I want to see

<span style="font-weight: bold;">Licensing</span>
Everyone has their own idea of what they like for licenses. I like the MIT/BSD thing. I can understand the attraction to LGPL and GPL although they aren't for me. What I can't stand and won't use are monstrosities like GPL/Commercial used by such libraries as ExtJs.

Want to make money off your software? Easy... let anyone use it and charge for support. Worked damn well for communities and companies like [Python](https://python.org/), [Django](https://djangoproject.com/), [Plone](https://plone.org/), various [Linux](https://www.linux.org/) distributions (Redhat anyone?), etc...

<span style="font-weight: bold;">Eggification</span>
Is your software constructed so that it can be installed via easy_install or pip? And yes, this is a bit of mild embarrassment for me, so I'm happy enough to eggify other people's work.

<span style="font-weight: bold;">Tests</span>
Do you have tests? Even a nearly empty tests file or folder? How about a test application? If you have no tests then your package is suspect. How do I know it will work independently of your personal computer?

<span style="font-weight: bold;">Code Quality</span>
Does the code smell bad? Can it be easily extended? If its innovative but the code needs work is it on a DVCS so more people can easily contribute?

22 more posts to go!
