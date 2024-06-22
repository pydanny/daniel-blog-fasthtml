---
date: "2008-04-27T11:49:00.005-07:00"
description: ""
published: true
slug: 2008-04-feedparser-does-not-work-with-google
tags:
  - feedparser
  - python
  - GAPE
  - legacy-blogger
time_to_read: 5
title: Feedparser does not work with Google App Engine
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/04/feedparser-does-not-work-with-google.html)_.

After my laughable mistake of trying to do a `import feedparser.py`, I sat down yesterday and spent half an hour writing my rss aggregator for Google App Engine. Critical, of course, was use of the excellent `feedparser` project. It was easy to get everything working, and while not styled it looked good. Everything except for using Feedparser to parse the incoming rss and atom feeds.

Alas, Feedparser tries to use a few modules that the enterprising folks at Google restricted. I haven't done any research yet, but I wonder if it is in the arena of fetching data from URLs, since app engine has its own library. I'll poke at it tomorrow.

In any case, I was very pleased with Google App Engine. Lets go over why:

- Database is not a RDBMS. Some people might scream at this issue, but the benefits we get are wonderful. Expando seems really fun to use.
- Built-in ORM. Sure, its not SQLAlchemy or the Django system, but its not that far different in approach and implementation.
- Django Templates! If I'm not doing TAL and I'm doing XHTML/XML, then my choice is Django. Templates.
- Cleanly documented. Clear and simple sentences with good examples that are working code, not doc or CLI tests.
- Easy and intuitive. This part is critical. The framework is not in the way.

Update: Apparently Feedparser works with GAPE. Either something changed about GAPE (feedparser hasn't been updated in a while) or maybe I had a bug. Thanks to [Alex UK](https://www.blogger.com/profile/01444733525137234264) and crchemist for pointing this out.

---

## 6 comments captured from [original post](https://pydanny.blogspot.com/2008/04/feedparser-does-not-work-with-google.html) on Blogger

**reedobrien said on 2008-05-01**

"Cleanly documented. Clear and simple sentences with good examples that are working code, not doc or CLI tests."

I suppose that is another jab at zope.formlib and their doc tests on pypi.

I will note again that if you want understand what is in a zope library you should read the interfaces. That is what they are for.

And as far as the quoted text above doctests are by definition working code.

**Silas Sewell said on 2008-05-04**

Universal Feed Parser isn't supported because urllib and urllib2 aren't supported (see: https://code.google.com/p/googleappengine/issues/detail?id=61).

**Lili said on 2008-08-28**

what's the alternative to feedparser.py that would work with google appengine? anybody know?

**pydanny said on 2008-08-28**

@Lili,

My hope is that the urllib and urllib2 will be fully supported in a future GAPE release.

That or feedparser will be enhanced to work in GAPE via urlfetch. This might be a fun task.

**Alex UK said on 2008-08-31**

It may be too late but look at this article
https://www.ibm.com/developerworks/opensource/library/os-eclipse-mashup-google-pt1/
they use feedparser with GAE and it works (at least at my comp, I hope it will work on GAE server as well.

**crchemist said on 2008-09-06**

I currently use feedparser at https://tagsfetcher.appspot.com . For fetching tags from different sites for exmaple https://tagsfetcher.appspot.com/plone/python or https://tagsfetcher.appspot.com/zope%202
