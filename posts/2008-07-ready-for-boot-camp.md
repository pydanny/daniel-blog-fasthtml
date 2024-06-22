---
date: '2008-07-11T07:07:00.003-07:00'
description: ''
published: true
slug: 2008-07-ready-for-boot-camp
tags:
- plone bootcamp 2008
- plone
- laptop
- buildout
- legacy-blogger
time_to_read: 5
title: Ready for boot camp!
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/07/ready-for-boot-camp.html)*.

Next week I'll be in [Plone 3.x Boot Camp](https://plonebootcamps.com) at American University.  I've worked with Plone 3.x for months, but haven't had time to get really spot on with its features.  So I'm looking towards this second experience with Joel Burton with a lot of excitement.

Anyway, after spending some time with [elephantangelchild](https://elephantangelchild.blogspot.com/)'s laptop yesterday getting [Python](https://python.org) 2.4.4 installed, then [PIL](https://www.pythonware.com/products/pil/), then [Plone](https://plone.org) 3.1.3, then taking it back down to 3.1.2, then installing in the boot camp modules, I decided to do the same for myself last night.

I decided to take a shortcut.  I modified the buildout.cfg so from the start it did everything in one go, installing Plone 3.1.2 and the boot camp modules.  That way I could just do one build and be happy.

Alas, buildout wouldn't work.  I had to do my buildout for Plone 3.1.2 and then run it again with the boot camp modules.  How silly is that?  Oh well, its done and with ArgoUML I'm ready to go!