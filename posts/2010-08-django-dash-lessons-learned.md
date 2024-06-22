---
date: '2010-08-21T09:22:00.000-07:00'
description: ''
published: true
slug: 2010-08-django-dash-lessons-learned
tags:
- django
- djangodash
- django packages
- sprint
- legacy-blogger
time_to_read: 5
title: Django Dash Lessons Learned
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/08/django-dash-lessons-learned.html)*.

Our experience with [Django Dash 2010](https://djangodash.com/) was that it was an wonderful exercise in classic [Django](https://djangoproject.com/) development, [cowboy/cowgirl coding](https://en.wikipedia.org/wiki/Cowboy_coding), and drinking copious amounts of [caffeinated](https://en.wikipedia.org/wiki/Caffeine) beverages. The result, [Django Packages](https://djangopackages.com/), is something we are happy with, are&nbsp;continuing&nbsp;to improve, and hope will improve the community.

<b>Lesson: Fixtures are a must</b>

Django gives you this amazing [Admin control panel](https://docs.djangoproject.com/en/dev/ref/contrib/admin/). As soon as you get your models in place and are entering test data, start creating fixtures. For the dash we named them initial_data.json and loaded them into the individual app directories. This meant that every time we blew away the database we got a reload with records in place. Sometimes this means you have to hand-edit [JSON](https://en.wikipedia.org/wiki/JSON) (or [YAML](https://en.wikipedia.org/wiki/YAML) if you swing that way), but the alternative is to waste time re-entering the same data again and again. Don't forget to change the names of your test fixtures before you launch!

From the command-line how to save a fixture pydanny-style:

<pre class="prettyprint lang-bsh">./manage.py dumpdata package &gt; apps/packages/fixtures/initial_data.json</pre>
One nice thing about fixtures is that when you do have the time/need, you can use them to help you write tests. And it makes development easier for contributors.

<b>Lesson: Research ahead of time</b>

In the days before the contest, we researched to see if our target repos ([Github](https://github.com/), ;[BitBucket](https://bitbucket.org/), and&nbsp;[Google Project Hosting](https://code.google.com/)) each had an API and a python library to speak to that API. Github has both an API and python library, Bitbucket has an API but no library. And as far as we can tell, Google Project Hosting lacks both API and library (<i>someone please tell me I'm wrong about Google Project Hosting lacking an API</i>).

This meant that when we commenced coding we knew which code base to work with - we weren't trying to look up this or that random package.

We did the same thing for rendering charts.

<b>Lesson: Get it working then optimize</b>

Looking at some of the code makes us wince a bit.&nbsp;<i>But we got it working.</i>&nbsp;Now we can go back and do some code cleanup, maybe use an&nbsp;[XML parser instead of regex](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)&nbsp;to try to scrape content from PyPI, and generally feel better about ourselves.

<b>Lesson: Plan out system architecture in advance</b>

In retrospect it was really amusing, but the night of launch the site was serving via the Django runserver command. We were so dead tired and neither of us are crack system administrators that we did what we had to do to score the contest launch point. The next day [Audrey](https://audreyr.posterous.com//) got the site running under[Apache](https://httpd.apache.org/), and next week we'll be giving someone else system access to increase reliability. Next year for the contest we'll probably use&nbsp;[something like this](https://djangopackages.com/grids/g/webserver/)&nbsp;or get&nbsp;[continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)&nbsp;running in the first hour.

<b>Lesson: Don't be afraid to chat with others after the contest starts</b>

Share your ideas, selected packages and frameworks with your competitors. The break from coding helps clear the mind and they might counter with a better idea/package/framework you can use.

---

## 3 comments captured from [original post](https://pydanny.blogspot.com/2010/08/django-dash-lessons-learned.html) on Blogger

**dartdog said on 2010-08-21**

Very nice post with some good detail. I need to get comfy with Fixtures asap, for upgrading my Mingus site... so many little pieces to track,, 
<b> </b>
Great project! congratulations to both of you.

**Alex said on 2010-08-21**

Lesson: Get it working then optimize


Lesson: Plan out system architecture in advance


Bit of a contradiction, don't you think ;)

**pydanny said on 2010-08-22**

@Alex - A little bit. But if we had thought the system work through we might have had a system that didn't go down every 20-30 minutes.

