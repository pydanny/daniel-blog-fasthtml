---
date: "2008-06-02T08:28:00.004-07:00"
description: ""
published: true
slug: 2008-06-how-not-to-build-view
tags:
  - plone
  - python
  - zope
  - five
  - legacy-blogger
time_to_read: 5
title: How not to build a view
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/06/how-not-to-build-view.html)_.

I like simple, sweet, and easy to use. Which means sometimes Zope 3 style things are awesome, and other times it sucks. What's worse is implementations you have to maintain where someone took something very simple and made it very complex.

In our case study, lets see what a predecessor to me did using Plone and a lot of Five:

1. Extended the ATEvent type.
2. Created a <span style="font-weight: bold;">view</span> using portal_catalog. This creates an <span style="font-weight: bold;">object</span> which calls another <span style="font-weight: bold;">object</span> which calls a specific <span style="font-weight: bold;">function</span> to grab relevant data from each brain object and place that data in a dictionary.
3. Made the view, 2 objects and functions <span style="font-weight: bold;">bolded</span> above not as extensions as other bits that existed elsewhere but coded them individually.
4. Tied it together with zcml.

The end result was a results object containing brains and a counter. Um... okay. I understand this was done so that the Plone template serving this would have the batch features and all, but this is over engineering.

I think a better solution would have been this:

1. Extend the ATEvent type.
2. Create a utility package with code to be reused in creating batches later.
3. Make the view call the utility package so you don't have to code much.
4. Tie it together with zcml.

I like this method. The better developers I work with and the gurus I admire will tell you any time you write the same section of code more than once you should look at code reuse techniques. Either wrap your code in functions, use inheritence, or play with polymorphism. All that good stuff.

Sigh.

At least I get paid to maintain this code. Finally it isn't in the NASA effort.
