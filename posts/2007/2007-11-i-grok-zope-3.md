---
date: "2007-11-01T16:14:00.000-07:00"
description: ""
published: true
slug: 2007-11-i-grok-zope-3
tags:
  - grok
  - zope
  - legacy-blogger
time_to_read: 5
title: I grok Zope 3!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/i-grok-zope-3.html)_.

I've struggled with Zope 3 for a bit. I read books, perused documentation, and took a class in Italy. And yet, it felt confusing. Well, this week I had to finish up a Zope 3 solution in record time. So I really hit the books and squinted my eyes real hard. It was frustrating because I got the individual bits, but putting them together was painful and a matter of trial and error rather than an understanding of how to meld components together.

The long and the short is that I used a mix of using Grok and writing Zope 3 tests to figure out problems I was having in my efforts. And then after about two days of struggling and banging my head against the wall, something clicked.

I get Zope 3.

I made something not working work in minutes.

I'm no expert. I've got a long way to go. I've got to work more with Adapters. But tying pieces together is no longer something scary. It makes sense now.

So, here are my lessons learned for anyone who wants to do Zope 3 and is a newbie..

1. Start with Grok. It removes a lot of the overhead and tells you the core bits of how Zope 3 components and interfaces work.

2. Write Zope 3 unit (doc) tests. I can't understate this issue. Don't worry about functional tests. The nice thing is that they insure that before you go to trying to put pieces together, that your component level bugs are mostly gone, so you don't think that zcml is a monster when really its a bug you didn't spot.
