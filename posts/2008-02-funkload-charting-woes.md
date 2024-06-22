---
date: "2008-02-08T09:17:00.000-08:00"
description: ""
published: true
slug: 2008-02-funkload-charting-woes
tags:
  - plone
  - python
  - legacy-blogger
time_to_read: 5
title: Funkload Charting woes
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/funkload-charting-woes.html)_.

So for our big Plone project I started to look at some tools to do some load testing. I wanted a Python tool, and stumbled across [Funkload](https://pypi.org/project/funkload/) by the folks at Nuxeo. It was easy to install, write tests, and generate reports. You could even stick a monitor on the hosting server and it would combine reports into one big handy report. However, not everything was perfect, and the big gotcha was the charting library.

Funkload uses python-gdchart (version 1.6 - 1.8) to generate images of chart data. Its an optional install but I think that visual charts allow us to easily spot major issues and deal with them. There was no `easy_installing` python-gdchart, so I followed the Funkload install script and went to [Francois Meehan's page](https://moinmoin.wikiwikiweb.de/FrancoisMeehan) on the issue. That directed me to [https://www.nullcube.com](Nullcube.com's software page). From there I delved and found my way to the now obsolete pygdchart 2.0 and no sign of the earlier versions.

Not good. 1.8 to 2.0 often means API changes, which means funkload probably wouldn't work. And neither would Francois Meehan's installation instructions. In fact, I can't get pygdchart 2.0 working at all.

I spent about 30 minutes dickering around with pygdchart 2.0. That also included time spent googling and seeing if anyone had a solution. No one seems to in my albeit brief investigation.

Now the question is this, do I

I stopped at that point. Even if I got pygdchart 2.0 working, I had no guarantee Funkload would be able to use it. So unless I find a copy of pygdchart 1.8 or so, its not worth the time.

Another thought is this: Funkload generates pretty easily understood XML. I could use Mathplotlib to generate the charts pretty easily. It would be a bit of work, but not a murderous amount.

So I guess I have three tasks:

- Look for a copy of pygdchart 1.8
- Write a script using Mathplotlib to turn Funkload report XML into pretty charts.
- Consider using another tool like Jmeter.

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2008/02/funkload-charting-woes.html) on Blogger

**Олег said on 2008-06-04**

Hi.

Is there some tutorial for funkload.

Find it hard to start with it

Please help

(please contact me on email: oltarasenko@gmail.com)
