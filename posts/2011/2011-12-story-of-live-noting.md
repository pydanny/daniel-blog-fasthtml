---
date: "2011-12-04T16:46:00.000-08:00"
description: ""
published: true
slug: 2011-12-story-of-live-noting
tags:
  - pycon
  - djangocon
  - django
  - python
  - git
  - australia
  - github
  - legacy-blogger
time_to_read: 5
title: The Story of Live-Noting
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/12/story-of-live-noting.html)_.

Like a lot of people, I've got this thing I do when I attend conferences, meetups, classes, and tutorials: I take notes. My open source based ones are mostly written in [RestructuredText](https://en.wikipedia.org/wiki/ReStructuredText) and I've kept in a particular folder since at least 2006.<h3>Putting notes in a DVCS</h3>On September 13, 2009, I uploaded these notes to [Github.com](https://github.com). I did that because I wasn't pleased with the workflow I established of moving items to Dropbox for backup. I use DVCS all the time and I figured why not just put my notes where I put my code? So I added my notes as a Github repo.<h3>DVCS Notes Based Management System?</h3>For a while I tried to use the Github folder README.rst trick to make a navigations system for my notes. But Github isn't designed for making a README into a dynamic custom content navigator, and it would make a silly feature request. I would rather the Github team work on [Mercurial](https://en.wikipedia.org/wiki/Mercurial) integration or other practical things before they honored a request to turn their system into my own custom Notes Management System. Eventually I just gave up on it and moved on.<h3>Sphinx + Read The Docs!</h3>In early July of 2011 I had a wicked fun thought. What if I turned my notes into a [Sphinx](https://en.wikipedia.org/wiki/Mercurial) project and posted it on [readthedocs.org](https://readthedocs.org)? Most of my content is in RestructuredText and I've gotten really fast at rolling out Sphinx documentation. The 'hard' part would be converting the few README.rst files into index.rst files, but on the flip side I could use fancy Sphinx directives.

I'm not exactly sure when I started down this path, bit this [commit log entry](https://github.com/pydanny/pydanny-event-notes/commit/2d17305ee7e75c9972d9f3fad3b35afdc3cc4a30#Makefile) leads me to think I had it working on or around July 8th. What that would mean is that every time I pushed up a change in my notes, within minutes readthedocs.org would publish the content to the world in lovely HTML markup.

The result?<h3>[Pydanny Event Notes](https://pydanny-event-notes.readthedocs.org/)</h3>
Here's a screen shot of the front page

<div class="separator" style="clear: both; text-align: center;"><a href="https://pydanny-event-notes.readthedocs.org" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="260" src="https://1.bp.blogspot.com/-4x7yIGXZLzE/TtwS1kBMkxI/AAAAAAAAA_o/DsJOE5zxABM/s320/Screen%2BShot%2B2011-12-04%2Bat%2B4.39.23%2BPM.png" width="320" /></a></div>
<h3>PyCon Australia 2011 Test Drive</h3>For the [2011 PyCon Australia](https://pycon-au.org/2011/about/) I gave my new process a serious whirl. I found if I created the page before the talk and entered some basic data like author and title and tied it to the index then I could constantly check the quality of my output while taking my notes. It made my notes seem a bit more exciting and alive. I even tweeted about it cause I thought it was fun, and people around the world seemed to enjoy the effort I was putting into my notes. 

Because I was committing constantly in order to get updates on [readthedocs.org](https://readthedocs.org) as soon as possible, I also adopted the habit of super-short pull request messages. That's because the content I'm writing overrides the need for verbose comments. So when you see me writing "moar" it's because every minute or so I'm doing something like:


```bash
$ git commit -am "moar"
$ git push
```


<h3>Kiwi PyCon 2011</h3>I did my rapid note taking again at Kiwi PyCon and it was fun. The downside was that sometimes I get rather critical in my notes and I had a couple speakers come up to me later to clarify their positions. This makes it a bit challenging because I want to put down my thoughts, but if my thoughts impact another person, what should I do? Especially since if my negative notes on someone turn up in a search it can negatively impact the speaker way beyond a single talk. This is now always on my mind when I take notes, and I'm trying to figure out a good way to handle this going forward.

In essence, I don't want to constrain what I write but I also don't want to write something that will haunt someone else later. Even with a caveat and all that stuff, it can still be problematic. There is a difference between me ranting about something and me taking notes, and the written word is such that things are all too often taken out of context.

Food for thought indeed.<h3>DjangoCon 2011 and the invention of the term 'live-noting'</h3>At the start of [DjangoCon](https://djangocon.us/) 2011 someone tweeted that they were planning to 'live-blog' the event. Suddenly I realized that what I was doing had a name for it, and that was 'live-noting'. So I tweeted that was what I was doing and it seemed to catch on.

Not only that, but I got asked if I would accept pull requests. After a good two seconds of deep thought, I responded that I would only consider corrections and clarifications, not new material. I received not just [one](https://github.com/pydanny/pydanny-event-notes/pull/1), but [two](https://github.com/pydanny/pydanny-event-notes/pull/2) pull requests from good friends and left the conference pretty happy. 

On top of that, I managed to get featured on the front page of [https://readthedocs.org](https://readthedocs.org/)! (Thanks Eric)

[Kenneth Love](https://twitter.com/kennethlove) also took notes in a similar fashion: [readthedocs.org/docs/djangocon-2011-notes](https://readthedocs.org/docs/djangocon-2011-notes/)<h3>PyCodeConf 2011</h3>I had the excellent fortune of being an invited speaker to Github's [PyCodeConf](https://py.codeconf.com/). While I gave my talk, my lovely fiancée, [Audrey](https://twitter.com/audreyr) took notes of my talk and submitted a pull request. Her contribution was the first time I accepted content I did not write, and I'll say right now she's the only one for whom I will accept such content. On the other hand, If you take notes when I present let me know and I'll link to them from my own notes.

[Josh Bohde](https://twitter.com/#!/joshbohde) also took notes at the event in a similar fashion [readthedocs.org/projects/joshbohde-event-notes](https://readthedocs.org/projects/joshbohde-event-notes/) and even as I write this post he shares the featuring of our notes on the frontispiece of [readthedocs.org](https://readthedocs.org/):

<div class="separator" style="clear: both; text-align: center;"><a href="https://2.bp.blogspot.com/-MFII1ZIN1Y8/TtwTTKDzFvI/AAAAAAAAA_0/opbu44Ixvvc/s1600/Screen%2BShot%2B2011-12-04%2Bat%2B4.41.24%2BPM.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="186" src="https://2.bp.blogspot.com/-MFII1ZIN1Y8/TtwTTKDzFvI/AAAAAAAAA_0/opbu44Ixvvc/s320/Screen%2BShot%2B2011-12-04%2Bat%2B4.41.24%2BPM.png" width="320" /></a></div>
<h3>Closing Thoughts</h3>I often use my notes as reference, and if you follow the [commit logs](https://github.com/pydanny/pydanny-event-notes/commits/master) you may even see me comment or clean up things I wrote down years ago.

The graphs and stats of this effort is really interesting. [Fortran](https://github.com/pydanny/pydanny-event-notes/graphs/languages)? And a total of 
[Five contributors](https://github.com/pydanny/pydanny-event-notes/contributors)! 

All of this makes taking notes a lot more fun. I enjoy finding ways to enhance and improve my process, and find it exciting that others are following a similar pattern of effort. My hope is to make 2012 the Year of PyCon, where I find a way to go to a [Python](https://python.org) related conference on six continents (Antartica is too cold for my tastes) and take notes everywhere.

Going forward, should I document how I built this out? Would my steps and patterns be useful for others?

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2011/12/story-of-live-noting.html) on Blogger

**Unknown said on 2011-12-04**

Interestingly, it was your live-note efforts that made me realise the potential for BitBucket+ReadTheDocs to address my dissatisfaction with Blogger as a forum for longer form, more permanent essays:

https://readthedocs.org/docs/ncoghlan_devs-python-notes/en/latest/

**Christopher Grebs said on 2011-12-04**

You're notes are always just awesome and I love reading about all the conferences in detail and even though I cannot attend most of the time I get the important bits.

Thanks for that!

But you're notes always have a downside - they make me feel bad I've not been there :-)

**Wes Mason said on 2011-12-27**

You could always host your notes in a Github wiki (as powered by the Gollum project) then you can just commit notes in a git but have a hwst do and indexed wiki front end for the files (including .rst's).

**pydanny said on 2011-12-27**

@Wes - Github wiki is great. But I want to edit my notes in a text editor and use git as my DVCS on my notes. This makes my notes EXTREMELY portable. I can work on them whether or note I have Internet. And if I need to move them off of Github then doing so is trivial.

I've kept these notes forever because of their portability.

As soon as I go to a Wiki system I lose all that. And migration between systems becomes hard.

Of course, everyone has their own style. Use your system and live-note your next attended event! :D
