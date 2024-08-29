---
date: '2011-07-12T15:41:00.000-07:00'
description: ''
published: true
slug: 2011-07-normalization-noitazilamron
tags:
- mongodb
- sql
- legacy-blogger
- foxpro
time_to_read: 5
title: Normalization noitazilamroN
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/07/normalization-noitazilamron.html)*.

Since pretty much the start of my career as a developer back in the 1990s one skill I've carried from job-to-job has been an understanding of relational databases. Over the years I've worked with [Foxpro](https://en.wikipedia.org/wiki/Foxpro), [Access](https://en.wikipedia.org/wiki/Microsoft_Access), [Oracle](https://en.wikipedia.org/wiki/Oracle_Database), [SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), [MySQL](https://en.wikipedia.org/wiki/MySQL), [Sqlite](https://en.wikipedia.org/wiki/Sqlite), and now&nbsp;[PostGreSQL](https://en.wikipedia.org/wiki/Postgresql).

Interestingly enough,&nbsp;[database normalization](https://en.wikipedia.org/wiki/Database_Normalization) comes&nbsp;instinctively&nbsp;to me. I knew about complex SQL joins and unions and subqueries before I read anything about normalization. As I read up on normalization, it was rather exciting to discover that my natural instinct during database design was to hit the fourth or fifth normal form without thinking about it. &nbsp;And since for most of my pre-[Python](https://python.org/) career the number of records I dealt with was measured in the tens of thousands, normalization was a great tool. I was aware that my record sets were smallish, and good database design kept my stuff running fast.

<b>Relational Databases are not a panacea that lets you overcome bad code</b>.

It surprises me how many developers I've encountered over the years who complained about the performance issues of normalized data but didn't understand normalization. Instead, they refused to follow any sort of standard and every table seemed to duplicate data and every query requires complex joins for trivial data calls. And usually with sets of records in the count of tens of thousands, not millions or billions. The end result are projects that were/are unmaintainable and slow, with or without normalization.

<b>NoSQL is not a panacea that lets you overcome bad code</b>.

Which brings me to the current state of things. NoSQL is a big thing, with advantages of NoSQL being touted in the arenas of speed, reliability, flexible architecture, avoidance of <a href="https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch">Object relational&nbsp;impedance&nbsp;mismatch</a>, and just plain ease of development. I've spent a year spinning an [XML](https://en.wikipedia.org/wiki/XML) database stapled on top of MS SQL Server, years using [ZODB](https://en.wikipedia.org/wiki/ZODB), and about a woefully short time working on [MongoDB](https://en.wikipedia.org/wiki/MongoDB) projects. Like relational databases, the sad truth about XML, ZODB, and MongoDB is that there are problems. And just as with relational databases, the worst of it stemmed not from any issues with data systems, but developers and engineers.&nbsp;Like any other tool you can make terrible mistakes that lead to unmaintainable projects.

So for now, like most of the developers I know, what I like to do is as follows:


1. Create a well-normalized database preferably using PostGreSQL.
- Cache predicted slowdown areas in [Redis](https://en.wikipedia.org/wiki/Redis_(data_store)).&nbsp;
- Use data analysis to spot database bottlenecks and [break normalization](https://en.wikipedia.org/wiki/Denormalization) via specific non-normalized tables.
- Use a queue system like [Celery](https://celeryproject.org/) or even chronjobs to populate the&nbsp;non-normalized&nbsp;table so the user never sees anything slow.
- Cache the results of queries against the specific&nbsp;non-normalized&nbsp;tables in Redis.

<div>The end result is something with the rigidity of a relational database but with the delivery speed of a key/value database.&nbsp; Since I work a lot in [Django](https://djangoproject.com/) this means I get the advantage of most of the [Django Packages ecosystem](https://djangopackages.com/) (at this time you lose much of the ecosphere if you go pure NoSQL). You can do the same in [Pyramid](https://pylonsproject.org/projects/pyramid/about), [Rails](https://en.wikipedia.org/wiki/Ruby_on_Rails), or whatever. Maybe its a bit conservative, but it works just fine.</div>