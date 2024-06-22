---
date: "2008-02-10T19:08:00.000-08:00"
description: ""
published: true
slug: 2008-02-funkload-matplotlib-charts
tags:
  - python
  - legacy-blogger
time_to_read: 5
title: Funkload + Matplotlib = charts!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/funkload-matplotlib-charts.html)_.

First I tried to use the Funkload bench xml data. Alas, the xml had values that assuredly went into reports, but figuring out what went where was a royal pain. So then I switched to the HTML report. That turned out to be easier, but it was still a pain. The HTML was vaid XHTML, but the lack of labeling meant it was like old time screen scraping. On a whim I looked at the RST, and realized that it would be very easy to pull data from it.

So I wrote a simple script to grab table data from the RST file. Then I started to make a few charts. Presto! Lots of fun. Its not done yet, but it will be soon. I'll put it on my Google code site and share once I've got it working nicely.
