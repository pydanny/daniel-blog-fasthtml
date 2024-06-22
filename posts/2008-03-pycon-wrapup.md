---
date: "2008-03-24T00:11:00.012-07:00"
description: ""
published: true
slug: 2008-03-pycon-wrapup
tags:
  - turbogears
  - pycon
  - python
  - wsgi
  - legacy-blogger
time_to_read: 5
title: Pycon Wrapup
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/03/pycon-wrapup.html)_.

I meant to write this sooner, but I came back to my 10th wedding anniversary. So whatever makes up my audience has had to wait. Waiting is over so here we go:

## Bring more business cards

I ran out of my own business cards the first day. Next time I go to a conference, I'll bring a hundred of them.

## Tutorials were worth every penny

Don't go to these conferences and miss out on the tutorials. Much of the rest of the conference is hallway conferences, short presentations, and sprints. The tutorials are hours of focused training given by really smart people. You hurt yourself if you don't make time and money for these things. On the other hand, 16 hours of training on multiple topics after traveling to get there is not super ideal. I was sad to have missed out on the middle slot, but on the other hand I was really focused for all the training I did get. I think two days of tutorials is better than one really long day.

Mt first tutorial was Numpy, which exposed me to the crunchy fun of the real grinding power of manipulating giant data sets at speed. The multi-dimensional arrays are really powerful, and I suspect that if used correctly 2-d arrays could make standard SQL database number munching look anemic when it comes to doing calculations. It might be interesting to create some tests comparing MySQL to Numpy for doing sums and the like. Another thought is fetching out data and using other Python science tools to generate charts and graphs. I've got a page full of ideas and I can't wait to try them out.

Second was Agile Testing and the experience was great. I've been a big fan of this since my Java days, and loved DocTests for Python. Up until my current big project, I did tons of testing in everything I did, and used Selenium for things where I wasn't happy with the system's test suite (that was with Plone until October 2007). Anyway, we were walked through Stupidity Driven Development (write code and write tests for things that break), Nosetests (a global test suite that just plain makes writing tests easy), Twill (simple dialogue for writing HTTP tests), and a number of other useful tools. While there I met [Remco Wendt ](https://www.remcowendt.com/)for the first as well plus the noted Larry Hastings of Facebook.

## Keynote Talks

I liked all the keynote talks. Sure, Guido might be giving the same one on Python 3 each year, but besides Youtube I've never seen it before.

Unlike some people, I didn't mind the presence of White Oak's Chris Hagner giving a speech on why Python rocks in their corporate world. He gave a good speech and showed how WOTI uses their knowledge of open source to increase the worth of US tax dollars spent. This is important to me because I see so much waste living as I do in the Washington, DC area. I've seen mediocre developers leave their positions to become Enterprise Architects for projects that really just needed a CMS like Plone or a number crunching application best served by Django. Money wasted on these tools could be invested into Open Source efforts, the same way that Apache has benefited by patronage from IBM and other large firms. Remember kids, with some good leadership on the OS side, you get this equation:

```
patronage != control of open source project
```

Van Johnson's speech on Intellectual Property was really good. I take a Lawrence Lessig approach to the whole thing so listening to him as sort of like being in a church and nodding to the pastor. Sure, I had my differences, but its good to see an Open Source lawyer explain the real world to the masses. I don't want to get in trouble for not paying attention to the particulars, so this was good for me. I've heard/read much of it before, but the refresher was important to me since its so easy to forget the particulars and get yourself into trouble.

## Session Talks

I went to a lot of these, and rather than repeat my notes I'm just going to review highlights and the odd lowlight.

An early favorite was [Chris McDonough's talk on repoze](https://us.pycon.org/2008/conference/schedule/event/7/). I had seen it before in November at [ZPUG](https://zpug.org/) but this time he demonstrated something stunning. This time he got [Trac](https://trac.edgewall.org/) to work inside of [Plone](https://plone.org/). How cool is that?

I had hoped for more on the [Stackless Python ](https://us.pycon.org/2008/conference/schedule/event/15/)talk. However, that was not meant to be. The original presenter cancelled out and he was replaced by someone who was not good at oration. Also, the slides were the same as a presentation 2 years ago. Lastly, the speaker couldn't properly answer any questions so basically was just clicking slides.

The [SQLAlchemy](https://us.pycon.org/2008/conference/schedule/event/44/) talk was great. The package has really come a long way. A lot of features probably aren't needed for most efforts, but having them there means you have to dip less and less into SQL and database specific items. I like how you can do Sqlite purely in memory for testing, which means for development on the [genwriter project](https://code.google.com/p/genwriter/) its perfect.

I've been a fan of Alex Martelli since I first opened the Python Cookbook. His talk on [callback patterns](https://us.pycon.org/2008/conference/schedule/event/52/) was like a firehose of really useful knowledge and lessons learned right into my brain. People left early and I guess I pity them. Sure, some of the stuff he talked about was advanced, but it wasn't that bad.

Also of good note was the [Pyglet](https://us.pycon.org/2008/conference/schedule/event/56/) talk. Pyglet is a cross-platform multimedia library that lets you code in graphics and audio for anything you want. Unlike Pygame it uses the OS standard bits to do its media actions which means technically its core cpython. I downloaded one demo that is a fractal terrain generator and didn't download the 3-D shooter. Yes, someone made a half-decent 3-D shooter using a high level language. Wow.

I went to the [Iterators](https://us.pycon.org/2008/conference/schedule/event/75/) talk which taught me about namedcollection.tuples. This is good stuff because you can stick complex data into a list-like object and then do fun stuff like easy sorting and other interesting things.

In retrospect I wish I had gone to the talk on [python containers](https://us.pycon.org/2008/conference/schedule/event/78/) but the one on [Nose](https://us.pycon.org/2008/conference/schedule/event/79/) testing was not bad. The speaker, also the creator, was not good at speaking. But his philosophy and tool are great. Very simply, Nose is a script you call that runs all the tests inside what you point it at. It runs anything that looks like a test. Sure, it doesn't have as much finesse as other tools, but its easy to use. And in my opinion, when testing is hard to do, it means you tend not to do it as much as you should.

Finally I was impressed by Mark Ramm of TurboGears. His [talk](https://us.pycon.org/2008/conference/schedule/event/82/) was not so much on his framework but on that with WSGI all frameworks just become glue bits for bigger and better things. He wants people to play together and adhere to standards so if you want something else to use, you can do so without breaking your tools.

## Lightning Talks

I wasn't that much impressed by them. There were, as [Bruce Eckel pointed out](https://groups.google.com/group/comp.lang.python/browse_thread/thread/2b6cb0e7245347be), too many commercial based talks which generally were hiring spiels. I've got nothing against recruiters, but lightning talks are supposed to be technical, with maybe a _...and we're hiring'_ at the end. So what happened is I didn't pay attention to a number of them, and they blurred together. there were some awesome things presented there, like Larry Hastings of Facebook or Zed Shaw's great humor, but most of it was rather bleah. So sad that makes me.

## Summary of Pycon

I'm not done yet! Lots more happened like a BOF or two, touching OLPCs, shaking Guido's hand, eating the odd good meal, and the sprints. That will come in a later post.
