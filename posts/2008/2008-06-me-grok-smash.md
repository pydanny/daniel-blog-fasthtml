---
date: '2008-06-30T13:52:00.003-07:00'
description: ''
published: true
slug: 2008-06-me-grok-smash
tags:
- grok
- review
- graphviz
- zope
- legacy-blogger
time_to_read: 5
title: Me Grok Smash!
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/06/me-grok-smash.html)*.

So as I started on yet another graphviz application for the web, I decided to go with a new framework.  I would use [Grok](https://grok.zope.org/)!

Grok comes out of the Zope community, and has its foundation in the rather mature components of that application server.  The difference is that tying bits of Grok together does not rely on seemingly arcane xml files.  You just code in Python and a bit of [TAL](https://wiki.zope.org/ZPT/TALSpecification14) for the views.  If you want you can leverage in more bits from the Zope world, such as zope.formlib and other interesting bits.
[
It is a matter of public record that I have a like/hate relationship with zope.formlib.](https://pydanny.blogspot.com/2008/04/issues-with-zopeformlib.html)

There are some really nice things I discovered about Grok:


- Intuitive.
- Only one magic bit, in that class defined as views look for their lowercase template automatically, and you can override this if you like.
- The framework is out of the way.
- Inheriting models is a cinch.
- Lets you play with either the ZODB or SQL ORMs.
- Easy use of TAL.

Some negatives:


- A possible gotcha when you instantiate an object inside another object requires you to do a super(MyObject, self).__init__() inside the object's __init__.  Not sure why I should have to write this out and it might be I did something wrong.
- Um... still trying to find faults.

I'm rather pleased.  Grok has grown up lots since I really looked at it in late autumn of 2007.  I look forward to working with it more.