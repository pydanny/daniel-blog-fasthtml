---
date: '2011-10-09T09:00:00.000-07:00'
description: ''
published: true
slug: 2011-10-conference-talks-i-want-to-see
tags:
- pyramid
- django
- NewZealand
- python
- australia
- sql
- github
- legacy-blogger
time_to_read: 5
title: Conference Talks I want to see
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/10/conference-talks-i-want-to-see.html)*.

I'm writing this the day after [Github](https://github.com/)'s [pycodeconf](https://py.codeconf.com/) ended. That was an amazing conference, and I'll be blogging it soon (I'll also be writing about [PyCon Australia](https://pycon-au.org/), [PyCon New Zealand](https://nz.pycon.org/2011), and [DjangoCon US](https://djangocon.us/)). With all this conference experience very current in my head, things I've seen and done at them, and the&nbsp;deadline for [PyCon US](https://us.pycon.org/2012/) submissions coming up, here are some talks I really want to see happen in the next six months. If not at PyCon US, then please consider these for other forthcoming events!

Note: Couldn't do my preferred 'linkify' as well as I liked thanks to bad hotel internet. I'll clean it up later.

<b>Advanced SQL Alchemy Usage</b>

I think the uber-powerful [SQL Alchemy](https://sqlalchemy.org/) ORM needs the same sort of treatment me and [Miguel Araujo](https://tothinkornottothink.com/) gave on [Advanced Django](https://www.slideshare.net/pydanny/advanced-django-forms-usage) [Forms Usage](https://speakerdeck.com/u/pydanny/p/advanced-django-forms-usage). Not a 30 tutorial or overview or '<i>State of</i>', but tricks and patterns by someone who has used it frequently on more than one project. Multiple projects is important because the speaker should have had the chance to try multiple approaches. Start with something simple like a TimeStampModel all model classes might inherit from, then go into deeper and and more complex technical detail. Finish the talk with something crazy hard from SQL Alchemy that is hard to explain. If that causes you to open a  bug/documentation ticket, then you'll know that you've done the talk right. 

<b>Advanced Django Models Usage</b>

Following the same pattern as my SQL Alchemy idea above, start with something simple like a TimeStampModel (including South  migration of fields), then go into complex looks with Q objects, good patterns for [Managers](https://docs.djangoproject.com/en/1.3/topics/db/managers/), [Aggregation](https://docs.djangoproject.com/en/1.3/topics/db/aggregation/), [Transactions](https://docs.djangoproject.com/en/1.3/topics/db/transactions/), and then finish it with the craziest, hardest thing you can find. When putting together the closing material causes you to open tickets for broken core code/documentation, then you know you've done it right. 

<b>Python Code Obfuscation Contest</b>

This <i><b>certain-to-be-controversial talk idea</b></i> would be where the speaker would solicit Pythonistas to submit a single  arcane [Python](https://python.org/) code module that would have to display the text of "<i>Although that way may not be obvious at first unless you're Dutch.</i>" There would be a '<i>Expert</i>' category which would forbid the eval/exec functions. The "<i>Anything Goes Category</i>" would allow use of <b>eval</b>/<b>exec</b>. The conference talk would be where the speaker announces the winners and comments on the brilliant insanity of submissions.

<b>Django + Flask + Pyramid: A demonstration of useful things you can do with WSGI</b>

At pycodeconf [Armin Ronacher](https://lucumr.pocoo.org/) showed how with [WSGI](https://www.wsgi.org/), he can run [Django](https://djangoproject.com/), [Flask](https://flask.pocoo.org/), [Pyramid](https://pylonsproject.com/) all from same server from the same domain. This surprised a lot of people, including me, and I want to see more of what Armin was talking about. I don't want any theory. I don't want anything obscure. I just want meaty bits I can implement the day after I hear the talk.

<b>Zen of Python</b>

Richard Jones [gave his version of the talk at PyCon AU](https://pydanny-event-notes.readthedocs.org/en/latest/PyconAU2011/zen_of_python.html), and I want to hear other opinions about it. I'm happy to hear an expert give his view, and I would also be delighted to hear how a beginner (or relative beginner) feels about it.

<b>Websites and OO Design Concepts: A Tutorial</b>

For beginners, I would love to see a talk on a list of OO theories, and as each list item was discussed, examples designed in the context of a web site, how to do things right, plus identified anti-patterns would be presented. The web angle would be a good way to get the incoming Python web crowd to attend and identify with raised issues.