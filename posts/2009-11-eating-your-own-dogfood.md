---
date: '2009-11-08T08:54:00.006-08:00'
description: ''
published: true
slug: 2009-11-eating-your-own-dogfood
tags:
- november
- django
- blog
- legacy-blogger
time_to_read: 5
title: Eating your own dogfood
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/11/eating-your-own-dogfood.html)*.

Since way back in 2007 when I blogged about [JSON and Python](https://pydanny.blogspot.com/2007/05/json-and-python.html) I've used blogspot as my blog engine. I've never been completely happy with it because it didn't easily support code coloration. Still, it worked, had great up time, and I got used to it.

Recently though on [twitter](https://twitter.com/pydanny) I've been getting a few dings about using python to host my blog. And since I've now captured [pydanny.com](https://pydanny.com/) and [pydanny.net](https://pydanny.net/) it makes even more sense. I toyed a few times with writing my own blog engine but while I've done it for my job, I never wanted to do it for myself.

So I've been shopping around for what I consider the best blog engine for me. I had a lot of great options thanks to a [blog engine query asked in April](https://pydanny.blogspot.com/2009/04/show-me-your-open-source-django-blog.html). In the end we just extended the [Pinax](https://pinaxproject.com) blog engine with a few widgets and that was good enough. Anyway, recently I started to look at those again as viable options.

However, one more option presented itself. [Kevin Fricovsky](https://blog.montylounge.com/)'s [Mingus](https://github.com/montylounge/django-mingus/tree). It has everything I want in a blog, and also seems to closely follow what I would like to think I would have done in my blog. That is, to say, he fetched bits and pieces from all over the [Django](https://djangoproject.com/) ecosphere and assembled them into one universal whole. Yup, I like it a lot.

So my plan is over the next week or so is to set it up on a [Webfaction](https://www.webfaction.com/) account and start blogging from there.

24 more posts to go! (I'm behind on days but plan to make it up with posts)

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2009/11/eating-your-own-dogfood.html) on Blogger

**Unknown said on 2009-11-09**

Are you planning on documenting the steps you followed to set up django-mingus on webfaction?  I tried a while back, and ran into some issues, so I'd be interested in seeing some better step by step instructions..

**pydanny said on 2009-11-09**

@Mikkel, I'll check out your work since I like Atom a lot.

@mwarkentin, I'll definitely blog about my efforts! :)

**Unknown said on 2009-11-09**

I am using App Engine (so... free hosting!) and using Micolog: https://code.google.com/p/micolog/

My Blog is at:  https://www.livingubuntu.com

It is easy, free, and works with your new domain!

**kevin said on 2009-11-09**

Great to hear! I have a few requests to pull additions into Mingus core, but I've been swamped with moving my home. I should be able to get some in this week. But the 0.8.3 version is well and good enough as is without these pull requests being merged.

@Mikkel - I'll ping you about your customizations. Maybe if I give you the commit access to Mingus you can work on getting these features in?

