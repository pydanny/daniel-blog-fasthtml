---
date: '2009-04-22T09:04:00.004-07:00'
description: ''
published: true
slug: 2009-04-sweet-spots-of-plone
tags:
- django
- plone
- python
- pinax
- legacy-blogger
time_to_read: 5
title: Sweet spots of Plone
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/04/sweet-spots-of-plone.html)*.

Yes, I am posting this with [Django](https://djangoproject.com/) and [Pinax](https://pinaxproject.com/) tags because I think my Django and Pinax friends can learn from the lessons of [Plone](https://plone.org/).

I'm admittedly more interested in doing Django these days yet I keep myself firmly aware of the things for which I think Plone (and its components and relatives) is unsurpassed in the Python framework world. Arguing these things to Djangonauts is interesting, because so many times they just reject things out of hand (just like certain Zope zealots I know). And I think that is to their loss. When you hit Plone's sweet spot, things get interesting.

<span style="font-weight: bold;">Standards</span>
[I've ranted about this before](https://pydanny.blogspot.com/2009/02/naming-conventions-thoughts-for-pinax.html). In essence Plone follows a subset of the Dublin core. Any database object in Plone has certain fields you can rely on in searches, views, and business logic. You don't have to introspect the objects to find these stock fields. Until I went back to entirely developer defined models with Django, I forgot just how much I had taken this for granted.

<span style="font-weight: bold;">Workflow</span>
Years ago some madman integrated DCWorkFlow into Plone. You can build custom workflows either in script or via the UI. The scripts and interface to use it has been unpleasant until recently, but then name a workflow engine capable of handling complicated workflows that is fun/easy to use? Thanks to Martin Aspelli his product called collective.wtf, Plone workflow management has become much, much easier. As far as I know, nothing in Django (or TurboGears or Rails) compares except maybe GoFlow, and I don't speak French.

<span style="font-weight: bold;">Object Oriented Database</span>
I like the Django ORM. I like SqlAlchemy. Until I run into the edges of the fact that they are modeling table records as objects. [Object Relational Impedance Mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch) anyone? Ouch the pain! I do recognize that relational databases are very useful and powerful, but sometimes I wish things were different. One day, when I'm indepedantly wealthy and own my own private tropical island I plan to get the Django ORM running with the ZODB.

<span style="font-weight: bold;">ACLs</span>
Groups and Users permissions in Plone are implemented really well. Object oriented databases handle hierarchies and references very well, so the whole parent-child ownership thing is done easily. This is critical in CMS work - ownership and control. Other frameworks have this built-in, but it is not automatically attached to each content object that you create. You get very used to it being magically done for you in Plone.

---

## 2 comments captured from [original post](https://pydanny.blogspot.com/2009/04/sweet-spots-of-plone.html) on Blogger

**pydanny said on 2009-04-23**

@tunix, Ever hear the phrase, "Those who do not understand their history are doomed to repeat it."

Or watch Mark Ramm's presention of what Django can learn from Zope?

If you don't like it, block my blog.

**pydanny said on 2009-04-23**

@tunix, point taken. Next time I will write things differently.

