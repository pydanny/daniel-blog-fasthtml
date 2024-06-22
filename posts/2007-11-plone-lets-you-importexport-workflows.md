---
date: "2007-11-07T07:13:00.000-08:00"
description: ""
published: true
slug: 2007-11-plone-lets-you-importexport-workflows
tags:
  - plone
  - legacy-blogger
time_to_read: 5
title: Plone lets you import/export workflows!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/plone-lets-you-importexport-workflows.html)_.

This is for an application that I'm hoping we'll be able to replace after this month. When I put it together it was my place to learn new stuff and make some critical mistakes. In the future workflows will be defined via code, but for now, I'm going to do it in the ZMI.

The problem was doing it in production. We are simply not allowed to touch production boxes or the ZMI there without getting into trouble. And our sys admins know nothing about Plone and Zope (and arguably \*nix). So I have to automate the process.

My first thought is Selenium since hopefully the sys admins know how to use that fun tool. But using Selenium for configuration is problematic at best. The ZMI often uses dynamic form field ids per page load, or per Zope instances. This has bit me before.

I looked up doing it programmatically. I could write a script, but instructing a sys admin to run the script might be painful too. I've run into problems with this too.

Then I remembered that much of the ZMI lets you do imports/exports. A quick check and yes, we can do it with workflows.

Now the downside is that it is a slippery slope. Once we start doing things through the ZMI you can't go back. But again, this project will probably be migrated to something much better next year.
