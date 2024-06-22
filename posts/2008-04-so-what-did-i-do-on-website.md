---
date: "2008-04-11T04:20:00.000-07:00"
description: ""
published: true
slug: 2008-04-so-what-did-i-do-on-website
tags:
  - work
  - NASA science
  - plone
  - python
  - NASA
  - legacy-dannygreenfeld
time_to_read: 5
title: So what did I do on the website?
---

_This was originally posted on blogger [here](https://dannygreenfeld.blogspot.com/2008/04/so-what-did-i-do-on-website.html)_.

I've gotten a lot of emails asking for specifics on what I did with [https://nasascience.nasa.gov](https://nasascience.nasa.gov/). I'll try and address this on several different levels. First details about the project and effort:

The project had about 20 people on it, with three of us being full time developer/engineers. The rest were system administrators, graphic designers, content editors, and the odd rotating management. The project took over a year.

The project was created using mostly open source tools. Comparable purchasable tools would have cost $200k-$250K to get started, required as much per year in licensing costs, and would have required just as much work. Several large firms and agencies use the same toolset that we do for this precise reason, with examples being Novell, Lufthansa, and the CIA (yes, the CIA can't afford overpriced tools).

<span style="font-weight: bold;">My Role
</span>Though the project officially started in Spring 2007, my effort started in Fall 2006. That was when I did a product comparison (with presentation) between a number of purchasable (COTS) and open source (OS) remedies to the issue of content management. I had been an advocate of OS efforts for some time. Apparently I did a good job so for the NASA Science project, they choose one of my OS suggestions.

A quick list of things I did once the project began includes:

- Created over a hundred Plone views from the data. If you know how to view the source HTML, you can see thats my work. The CSS/Javascript/images were done by others. Because of code reuse techniques the amount of code generated is actually quite small.

- Added and modified lots of different content types and their relations with other content types. Content types include things like [Missions](https://nasascience.nasa.gov/missions), [Programs](https://nasascience.nasa.gov/programs), [Big Questions](https://nasascience.nasa.gov/big-questions), and areas of the site you can't see yet. ;)

- Wrote a script to map out the [Zope 2](https://en.wikipedia.org/wiki/Zope) database architecture when our tool to handle that broke down. The database architecture is complex, arguably too complex and now that we are done with launch, we will be simplifying it (we hope).

- Modified an existing third party [Plone ](https://en.wikipedia.org/wiki/Plone_%28software%29)package to support handling of incoming RSS feeds that followed no standard but their own.
- Created most of the [Zope 3](https://en.wikipedia.org/wiki/Zope_3) feedback forms and their handlers on the site. I have to admit I really don't like the form api we used as the results are ugly and the library itself is annoying. You can read my thoughts on that subject [here](https://pydanny.blogspot.com/2008/04/issues-with-zopeformlib.html) (warning - rather technical).

- Added and modified existing relationships between content areas.

- Created a Zope 3 [captcha ](https://en.wikipedia.org/wiki/Captcha)engine that eventually got shelved.

- Ensured that HTML rendered is section 508 compliant and meets international usability requirements. Which means the visually disabled can use it without issue. I wasn't the 508 overseer, and the one we had sucked. But I certainly adhered to the protocols.

There is much other stuff that I did that I'll try to address in future blog posts. If you want the technicalese, this site is full of that kinf of stuff.

Some of the open source tools we used include:

- [Python Programming Language
  ](https://python.org/)
- [Apache Http Server](https://httpd.apache.org/)

- [Plone Content Management System
  ](https://plone.org/)
- [Zope 2 Application Server
  ](https://wiki.zope.org/zope2/Zope2Wiki)
- [Linux Operating System](https://www.linux.org/)

Note the lack of Microsoft, Sun, Oracle, and Java? Thats because we believe in true open source and choosing the best tools.
