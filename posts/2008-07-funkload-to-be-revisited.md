---
date: "2008-07-30T19:15:00.003-07:00"
description: ""
published: true
slug: 2008-07-funkload-to-be-revisited
tags:
  - funkload
  - Linux
  - python
  - MacOS
  - legacy-blogger
time_to_read: 5
title: Funkload to be revisited!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/07/funkload-to-be-revisited.html)_.

Benoit Delbosc (I assume its him because the Blogger sign was 'Ben') last week responded to these two posts I made in February:


- [Funkload Charting Woes](/posts/2008-02-funkload-charting-woes)
- [Ditching Funkload](/posts/2008-02-ditching-funkload.html)

Benoit is the author of [Funkload](https://github.com/nuxeo/FunkLoad), a promising python based functional and web load tester I explored earlier in the year. Its biggest shortcoming was the problem with getting graphical charting to work because the graphing library it was using was impossible (for me) to find. Sure, numbers are important, but a picture says a thousand words.

Especially to managers.

Well, Benoit told me that the latest Funkload calls for python-gdchart2, for which linux packages (at least Debian and Ubuntu) can be had. So installation across the many machines I touch will be trivial. I don't always use linux, but now I'll make sure to use it when I need Funkload to do what I need. It might also work with Mac OS X, something I plan to investigate tomorrow.

This makes me very happy. I really enjoyed playing with Funkload, and plan to do more of it in the near future. 

And, just to make Benoit happy, even though it wasn't official, for the past 6 months or so I've used it in many unofficial load/functional tests for [https://nasascience.nasa.gov](https://nasascience.nasa.gov/) as well as other internal efforts. :)
