---
date: '2010-08-17T07:30:00.000-07:00'
description: ''
published: true
slug: 2010-08-announcing-django-packages
tags:
- django
- djangodash
- django packages
- sprint
- legacy-blogger
time_to_read: 5
title: Announcing Django Packages!
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/08/announcing-django-packages.html)*.

I'm part of a [two person team](https://djangodash.com/teams/scared-of-rabbits/) that just launched that BETA site for [https://djangopackages.com](https://djangopackages.com/), a site that is designed to list all the [Django](https://djangoproject.com/) Applications, Frameworks, and Packages created by the Django community. While there are already a few places to look for these things, it is quite easy to argue that they are challenging to navigate, don't give any hard metrics, or are woefully incomplete/unstable/closed. Our goal was to provide an attractive, easy-to-navigate, easy-to-add-data, stable site and share it with the world.

Also, this was our entry into [Django Dash 2010](https://djangodash.com/), and was the culmination of a few days of brainstorming over paper, a lot of research, and two days of feverish coding/designing. The project was feature complete to our specifications at 5pm the second day, and the rest of the time was spent adding in UI tweaks, usability enhancements, and trying to deploy our creation.

Since then, we've cleaned up a the UI, improved the design, and got the site stable. The [code is open source and on github,](https://github.com/opencomparison/opencomparison) so fork and contribute!

<b>Design Consideration: No 'Like' button or 'Rate my app' rating systems</b>

We wanted hard metrics. So the package numbers are pulled from the repo sites such as [Github](https://github.com/), [Bitbucket](https://bitbucket.com/), and [Google Code](https://code.google.com/hosting/). Otherwise things get weighted funny. Sure, this system can be monkeyed with, but its a good metric for now. We've had suggestions from Django core developers of coming up with a quality check system, things like [pypants](https://pypants.org/)&nbsp;and/or a formalized approval system.

<b>Design Consideration: Grids</b>

Early on we wanted to duplicate and improve upon the [Django CMS Comparison](https://code.djangoproject.com/wiki/CMSAppsComparison)&nbsp;page. There is also a version for [Forums](https://code.djangoproject.com/wiki/ForumAppsComparison), but it would be nice to have a [current one for blogs](https://pydanny.blogspot.com/2009/04/show-me-your-open-source-django-blog.html)! In addition,&nbsp;recently I heard that 't<i>ag clouds are the mullets of web 2.0</i>'. This really struck a chord in my soul. Since we had metrics on packages, why not compare those metrics, and use those comparisons, which we call 'grids', instead of tags? In fact, we extended our idea and instead of traditional tabs we use grids in the top navigation area as seen below:

<div class="separator" style="clear: both; text-align: center;"><a href="https://1.bp.blogspot.com/_KEFU5_uGRyw/TGok9P6U5BI/AAAAAAAAAw4/KOlaapAL6ZE/s1600/Screen+shot+2010-08-17+at+12.57.44+AM.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="92" src="https://1.bp.blogspot.com/_KEFU5_uGRyw/TGok9P6U5BI/AAAAAAAAAw4/KOlaapAL6ZE/s320/Screen+shot+2010-08-17+at+12.57.44+AM.png" width="320" /></a></div>
<b>Design Consideration: Categories</b>

The site groups packages into three categories, '<b>Apps</b>' which are individual django applications. '<b>Frameworks</b>' which are aggregates of apps and python modules. And '<b>Projects</b>' which are implementations of Apps and Frameworks. We've thought about adding '<b>Tools</b>' but weren't sure if there was anything that fit that concept, and we are leery about allowing regular [Python](https://python.org/) efforts into the fold.

<b>Design Consideration: Regex vs XML</b>

Slurping data out of Github was easy, especially since I used [python-github2](https://github.com/pydanny/python-github2). Bitbucket has a RESTful API as well that serves out JSON. I think Google Code does as well. [PyPI](https://pypi.python.org/) does not and DOAP on PyPI seems to give little that is useful, so I was forced to do screen scrapes of version numbers and downloads. I'm much faster with Regex and string methods than XML juggling, and speed was of the issue this weekend. I'm not sure what benefit there is to redoing it in HTML5lib or lxml, since what I have works and appears to be stable.

<b>Design Consideration: Leave caching and optimization for later</b>

Besides a tiny bit of memory based template caching on the home page, there is/was no optimization. In time I plan to cache many things using a proper key/value store like [redis](https://code.google.com/p/redis/) or [memcached](https://memcached.org/). Perhaps not before more design and usability work is done.

<b>Why scared of rabbits?</b>

You wouldn't understand unless you live on the Kansas prairie.

<b>Note</b>: if you have any suggestions, issues, problems with Django Packages please use our [issue tracker](https://github.com/opencomparison/opencomparison/issues)!

---

## 14 comments captured from [original post](https://pydanny.blogspot.com/2010/08/announcing-django-packages.html) on Blogger

**Mathieu Leduc-Hamel said on 2010-08-17**

Very cool initiative !

Do you think you'll implement a way to use your site with a kind of &quot;find-link&quot; mechanism ?

I would love to be able to use your website in my buildout confs ! ;0

**pydanny said on 2010-08-17**

@arrakis - Open up a ticket and we'll consider it! github.com/pydanny/scaredofrabbits/issues

**peterbe said on 2010-08-17**

I've got some django packages that I'd like to see included. 

Perhaps that should be a top-priority design consideration: How to add more packages.

**pydanny said on 2010-08-17**

@peterbe - Just go to https://djangopackages.com/packages/add/ and do it yourself.

We are trying to figure out how to make the links to that page more obvious. :P

**akaihola said on 2010-08-17**

You've created the missing piece! With all the great reusable apps and tools, the problem – especially for new Django developers – has been how to find and evaluate them.

My thought with the CMS and forum app wiki pages always was that they really should evolve into a central app database, and it should be super easy  for app developers and the whole community to contribute data. Such existing sites just weren't good enough. Django Packages already seems to be.

It's great that the code for your site is open as well. But let's not stop there: public dumps of the database and a comprehensive public API could inspire cool tools from the community.

Thanks, Daniel and Audrey!

**peterbe said on 2010-08-18**

@pyDanny

You know how the &quot;Add package&quot; and &quot;Add grid&quot; appears only once you're logged in, I would make it always appear and then if you're not logged in it diverts you to sign up/log in. 

Major feature request: Maturity and last update date on the packages is often key to decide sometimes which one to choose.

**michuk said on 2010-08-18**

Great initiative. I can see it grow big.

In projects tab (https://djangopackages.com/categories/projects/) you can add Filmaster, the open source film recommendation engine &amp; community website powered by django. 
Bitbucket: https://bitbucket.org/filmaster/filmaster-test/
Developer's website: https://filmaster.org
The actual website: https://filmaster.com

**Bill Mill said on 2010-08-18**

You should add an option &quot;mercurial&quot; in the &quot;Repo&quot; field of the &quot;add an app&quot; form.

Byteflow has their own hg repo at https://hg.piranha.org.ua/byteflow/ , but I can't add the package without lying about where the code is hosted.

Plus it should be relatively easy to drag some information out of any hg repository? I'm guessing because hg is in python, not because I've ever actually done so.

**Bill Mill said on 2010-08-18**

Also, for some reason I can't submit https://github.com/f4nt/django-yaba/ , I get a server error when I try. I'm trying to make a grid of all reasonable blog engines, since I've been making a list. Strangely enough, I've been doing it for NASA as well as you have :)

**pydanny said on 2010-08-18**

@michuk - Filmaster looks awesome! As for adding it to the projects, we are relying on the community such as yourself. Go ahead and create an account (https://djangopackages.com/signup) and add Filmaster as a Package under the category of 'Project'.

**pydanny said on 2010-08-18**

@akaihola - We're so honored you like our efforts, since your work inspired a lot of the details of the grid. We had in mind public dumps of data and a good API down the road.

**pydanny said on 2010-08-18**

@bill mill - Yeah, we've seen people adding in custom URLs for packages. Its an existing issue. :P

**ptone said on 2010-08-21**

Would be neat to see a link between this and another dash project : readthedocs

**pydanny said on 2010-08-22**

@ptone - Check out [add Read the Docs link](https://github.com/pydanny/scaredofrabbits/issues#issue/29)!

