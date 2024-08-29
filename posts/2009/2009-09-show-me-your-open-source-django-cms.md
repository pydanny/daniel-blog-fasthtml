---
date: '2009-09-16T08:29:00.006-07:00'
description: ''
published: true
slug: 2009-09-show-me-your-open-source-django-cms
tags:
- django
- python
- legacy-blogger
time_to_read: 5
title: Show me your open source Django CMS
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/09/show-me-your-open-source-django-cms.html)*.

Want your open source CMS to be tried out by [NASA](https://www.nasa.gov/) [SMD](https://nasascience.nasa.gov/)?

Django comes from the CMS world, and rolling your own isn't that hard. Nevertheless, we don't want to reinvent the wheel, so this is a solicitation for open source Django CMS efforts with active communities.

Our requirements:


- Must be powered by Django.
- Most be open source.

- Follows Django/Python best practices.
- Must be extensible.

- Elegant user interface.

- Renders humanely in FF, Safari, and IE 7, and 8. IE6 is a definite plus.
- Section 508 compliant or at least pretty close.

- No patching of Django to make things work.
- Must be able to run with PostgreSQL and MySQL.
- Must have an active community. Which means that commits to the CMS need to have happened within the last two months.</li><li style="font-weight: bold;">You must provide a featured sites list to be even considered as an option.


Make your entries in the comments to this blog. If we pick your tool we'll give you full credit for your hard work.

---

## 11 comments captured from [original post](https://pydanny.blogspot.com/2009/09/show-me-your-open-source-django-cms.html) on Blogger

**Unknown said on 2009-09-16**

https://github.com/digi604/django-cms-2.0/ but you probably knew about this one already

**Eric Florenzano said on 2009-09-16**

I've heard a lot of really good things about feincms:

https://spinlock.ch/pub/feincms/

**Unknown said on 2009-09-16**

Well, probably not exactly all best practice, but it is work in progress (and my first site:))
https://www.kiind.nl (dutch)
code: lp:babyweb (launchpad)

--
Yoram

**pydanny said on 2009-09-16**

Eric and BartTC, We can't even begin to consider feincms until someone points us at a list of feincms powered sites.

**akaihola said on 2009-09-17**

A few months ago I created [a CMS apps comparison wiki page](https://code.djangoproject.com/wiki/CMSAppsComparison) in the Django wiki for gathering information about solutions out there.

The page might not be up-to-date since I haven't followed the development of most of the projects mentioned there. Help appreciated :)

**Unknown said on 2009-09-17**

As part of News21, a Carnegie and Knight funded project, we created django-newsroom: https://code.google.com/p/django-newsroom/source/checkout 

https://code.google.com/p/django-newsroom/source/browse/branches/pinax/INSTALL

* We have an elegant user interface and an interesting visual editor / page layout system.

* We've had great support along the way from the folks at LincolnLoop who have contributed to the best programming practices employed in the site.

* this is currently in use at https://news21.com

* we have started a user group here:

https://groups.google.com/group/django-newsroom

There still is some roughing out along the edges that need to happen (for instance, it currently requires PostgreSQL) but my colleagues and I will be willing to work to make this compliant.

**pydanny said on 2009-09-18**

I contacted messagecms.com for when they plan to open source their code and also a list of sample sites.

**Unknown said on 2009-10-27**

Django page CMS: https://code.google.com/p/django-page-cms/

It's a well tested CMS (85% test coverage)

**Arek said on 2009-11-08**

So, which CMS system did you end up using ? I am curious as we are in the same step of our project planning . 

Cheers,

**pydanny said on 2009-11-09**

@Arek - Thanks for the prompt! I'll aobut it in detail this week.

**pydanny said on 2010-02-10**

We picked Fein CMS based off of https://pydanny.blogspot.com/2009/11/picking-django-powered-cms.html.

