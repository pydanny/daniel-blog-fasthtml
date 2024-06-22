---
date: '2011-01-15T08:13:00.000-08:00'
description: ''
published: true
slug: 2011-01-january-mongo-la-conference
tags:
- django
- mongodb
- legacy-blogger
time_to_read: 5
title: January Mongo LA conference
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/01/january-mongo-la-conference.html)*.

Back in the mid-1990s my professional software development career started in [relational databases](https://en.wikipedia.org/wiki/Relational_database). Periodically though I interacted with [NoSQL](https://en.wikipedia.org/wiki/NoSQL) databases. In 1999 I heard about [ObjectStore](https://en.wikipedia.org/wiki/ObjectStore). In 2003 I played with a few [XML databases](https://en.wikipedia.org/wiki/XML_database). With XML databases of the time, I found all you got out of them was a lot of complexity bolted onto a SQL based system. In 2006 I was introduced to [ZODB](https://en.wikipedia.org/wiki/ZODB), the [Zope](https://en.wikipedia.org/wiki/Zope) stack's object oriented database. ZODB has some fascinating traits, but the hard schemas used by [Plone](https://plone.org/) and Zope made it as rigid/stable as SQL systems but without as many useful tools. In 2008 I played a bit with Google's [BigTable](https://en.wikipedia.org/wiki/BigTable) via appengine, where my impression was that of a relational database without indexes.

Since then, a lot of new NoSQL solutions that have embraced the idea of schema-less architectures have presented themselves. I've glanced at them but until recently nothing on my plate really justified their use and taking the time to learn how to use them. Recently I've come across a project that justifies the whole [document store](https://en.wikipedia.org/wiki/Nosql#Document_store) approach used in systems like [MongoDB](https://en.wikipedia.org/wiki/MongoDB), [CouchDB](https://en.wikipedia.org/wiki/CouchDB), and others. However, because users of NoSQL tend to be such heavy [kool-aid](https://en.wikipedia.org/wiki/Drinking_the_Kool-Aid) drinkers, I've been a bit shy.

Well, last night [Media Temple](https://mediatemple.net/) laid out an awesome spread for [Mongo Los Angeles](https://www.10gen.com/conferences/mongola2011). The agenda was clearly a kool-aid fountain of information, but at least they weren't trying to sell me a timeshare, right? Plus, it gave me a chance to hang with awesome [python](https://python.org/) folk like [Audrey Roy](https://www.audreymroy.com/) and [Brian Luft](https://twitter.com/unbracketed). 

Most of the talks were will implemented, I've picked out two presentations out for being just plain well done:

<b>Building your first MongoDB Application</b>
Antoine Girbal delivered a talk that was a great, elegant introduction to MongoDB. In thirty minutes he gave a solid introduction to why Mongo was created, how the data is structured, how to call data, how to index it, and more. And yet it didn't feel like a firehose of information. This is how it should be done for any introduction to any open source project. 

<b>Beyond Logging: Using MongoDB to Power a Private Social Network</b>
This was the pièce de résistance of the evening, a presentation on mating MongoDB with an existing relational database design. It was incredibly informative and demonstrated that with a bit of moderation and discipline you can make the very difficult rather easy. Plus the presenter, Justin Jenkins educates via [learnmongo.com](https://learnmongo.com/).

<b>Have I drunk the kool-aid?</b>
So what did I get out of these introductory talks? Well, it appears that MongoDB is exactly what I need for an upcoming [Django](https://djangoproject.com/) project. The downside is that if I use MongoDB for all the persistence for this Django project then I lose the chief advantage of working with Django. I'm not talking about the admin and ORM themselves cause I know django-nonrel and mongoengine exists, I'm talking about the [multitude of efforts](https://www.djangopackages.com/) that support the relational database roots of Django.

Also, this project involves quite a bit of information best stored in a relational database. Not everything is a document! And I know from a lot of experience that trying to fit a spiffy square peg into a round hole is dangerous.&nbsp;So what I'll probably do is use PostGreSQL for the accounting information and user management. The documents will be stored in MongoDB, with one of the indexes for said documents being on the username attribute of each document.

Simplicity itself, right?