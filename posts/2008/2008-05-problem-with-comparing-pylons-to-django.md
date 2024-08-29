---
date: '2008-05-09T11:36:00.003-07:00'
description: ''
published: true
slug: 2008-05-problem-with-comparing-pylons-to-django
tags:
- django
- pylons
- python
- legacy-blogger
time_to_read: 5
title: The problem with comparing Pylons to Django
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/05/problem-with-comparing-pylons-to-django.html)*.

...is that my experiences with Pylons are from nearly two years ago.  My experiences with Django are ongoing.  So any comparison I do will be completely unfair.  But lets do a little anyway because there are some issues I want to raise.
<span style="font-weight: bold;">
ORM non-Issue</span>
<span style="font-weight: bold;"><span style="font-weight: bold;"></span></span>I don't have any issues here with either framework.  At the time played with Pylons I think it used SQLObject.  Now you can use SQLAlchemy.  If you want, Pylons can also handle Python's DB-API if you want a bit of pain with your SQL.  Django has its own ORM.  Personally, I'm happy with any ORM to handle all the mundane tasks, and all three ORMs have good enough documentation to make working with them a snap.  So ORM is a non-issue.

<span style="font-weight: bold;">Routing non-Issue</span>
Pylons routing of URLs to methods was easy.  Django has an easy method too.  I'm sure some folks might take issue with some of the finer points but I haven't ran into any killer issues myself.  I think both let us specify things ending with slashes, or '.php' if we have a sense of humor.  So routing is a non-issue.

<span style="font-weight: bold;">Django Templates versus Myghty/Mako
</span>The problem is my own lack of discipline.  It can be so easy to start adding in more and more logic into your views.  I would rather call python modules with python methods written in python then cook up fancy logic in a view-focused templating engine.  Yet again and again I do the stupid, and mix my content with presentation.  So I want a templating system that limits what I can do with it.

When I did Pylons the default templating system was Myghty, patterned after a Perl library called html::mason.  I did not like Myghty.  Since then, Pylons adopted Mako.  The same things that made me not like Myghty appear to be in Mako.  Too much power!  I can mix my business logic code too easily with the view stuff.

I like Django templates because it has good, hard limits on what you can do.  You aren't cooking up creative ways to do logic in views.  You are just simply writing views.  In return, it gives you a bunch of default utility methods/filters that do a bunch of repetitive work.

A common alternative with Django is Jinja templates.  I think Jinja might give application developers Myghty/Mako like power.  So I'm not very interested in Jinja.
<span style="font-weight: bold;">
Django versus Pylons Documentation
</span>I like good on-line documentation.  Its very hard to do, and Django has done a smashing job with tutorials and on-line books.  Pylons has some really good stuff, and I know that they've improved, but they are still not there with Django.

<span style="font-weight: bold;">Admin Interface
</span>So I create an application and have a table with 5 status values.  The application goes to production.  Turns out I mispelled a status title and it needs to be fixed.

In Django I log in as an admin, go to the errant record, and fix it.  To make that work I just added an internal class to the Status model.

In Pylons (and I might be wrong), I can't do this.  I either have to log into my database directly, or write a snippet of code to correct the problem, or code in an administrative module myself. 

<span style="font-weight: bold;">Summary
</span>This comparison was totally unfair.  I'm skipping a lot of wonderful things about Pylons.  Things like Pylon's unbelievable flexibility in choosing components, the rails-like webhelpers, and the collective smarts of the people who work on the project.  Or its close friendship with the latest versions of Turbogears, which probably smashes the admin interface issue right out of the ballpark.

So, in conclusion I'll play it completely safe and say that Django and Pylons are both good stuff.   I just prefer working with Django.
<span style="font-weight: bold;"></span><span style="font-weight: bold;"></span>