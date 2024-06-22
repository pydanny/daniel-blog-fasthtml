---
date: "2008-02-17T17:58:00.002-08:00"
description: ""
published: true
slug: 2008-02-plone-3-drives-me-to-drink
tags:
  - plone
  - legacy-blogger
time_to_read: 5
title: Plone 3 drives me to drink!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/plone-3-drives-me-to-drink.html)_.

I've done lots with Plone 2.5.x. I've written captcha apps in both Zope 3 and Grok. Now its time to play with Plone 3 thanks to [aclark.net](https://aclark.net).

The first task is mostly CSS, which reveals a couple weaknesses I have, the primary of which is that I simply suck at visual design. No, lets change that, I'm terrible. Really bad. I can recognize good designs but doing it myself is nearly impossible. It takes me forever and the end results look like monkey poo. In fact, being so bad at visual art is something I've really tried to fix my whole life to absolutely no avail. Today I spent lots more time I'm mostly not billing for because I just did things real slowly.

Maybe I should just spend my time mastering Generic Setup?

The second task is to do some work with portlets. We can get by with some static HTML in our portlets, but wouldn't it be nice to have a simple portlet tool that lets you upload an image, enter a link, and then you've got a pretty portlet linker! A great little handy tool for Plone 3, and something to wet my teeth on. So after the css misery, I jumped eagerly into this task. I already had a simple portlet package ready, and I cleaned it up to be able to have the right fields (the image item is actually a TextLine for now to make early testing simple), and to also be a valid Plone 3 package. I restarted Plone and presto - the package was there! Time elapsed: 30 minutes! Yay Plone 3!

While committing to SVN I got distracted and made a mistake. Then I reinstalled the project to make sure I hadn't broken anything else. All looked good. That ate up another 30 minutes but it was a good thing to check.

So then I decided to test it out. And you know what? I can't get the addForm or editForm to work - you know the bits powered by `zope.formlib`. Instead I get a 404 error when I try and add my portlet.link portlet. I've banged my head a bit, since doing this in Zope 3 was a snap. Yet this Plone 3 portlet has been annoying. This looks to be so simple and I know I'll curse myself later for how obvious it must really, actually be.
