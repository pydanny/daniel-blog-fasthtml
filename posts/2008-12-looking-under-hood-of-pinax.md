---
date: '2008-12-16T16:26:00.002-08:00'
description: ''
published: true
slug: 2008-12-looking-under-hood-of-pinax
tags:
- django
- python
- pinax
- legacy-blogger
time_to_read: 5
title: Looking under the hood of Pinax
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/12/looking-under-hood-of-pinax.html)*.

I've started to look around because one of the requirements I'll have to follow is to change the '<span style="font-style: italic;">Tribes</span>' section to be called something else like '<span style="font-style: italic;">Groups</span>' or '<span style="font-style: italic;">Crews</span>'. Of course I compared it to some of the other frameworks I've played with, and here are some thoughts. I went from module to module of Pinax, and found some nice commonalities that made me happy:


- There is a minimum of boilerplate. Everything is doing something meaningful. 
- Django models are easy to read.
- Relating your Django model to the User is easy.

- Django forms are straightforward.
- No interfaces!

More to come as I play.