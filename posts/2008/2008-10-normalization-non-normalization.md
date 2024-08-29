---
date: '2008-10-20T09:39:00.005-07:00'
description: ''
published: true
slug: 2008-10-normalization-non-normalization
tags:
- technology
- rant
- legacy-blogger
time_to_read: 5
title: Normalization, Non-Normalization, Denormalization
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/10/normalization-non-normalization.html)*.

I don't do much SQL anymore, thanks to tools like SQL Alchemy and the rather proprietary and object oriented ZODB.  However, when I do interact with SQL databases I always go for the 5th normal form because this just seems right.  I've dealt with more than enough non-normalized databases in my time to feel completely justified in this response to bad design.

The worst cases of non-normalized data in my experience have been with financial transactions or user data.  Once I dealt with a financial databases that tracked the amounts in a pool of money in the same table as the historical transactions against that pool.  Sound confusing?  You bet, especially since determining what money was real and what was historic was done in an amazing piece of undocumented spaghetti code.

I've admittedly created two monsters of this sort of design.  One was my first database design in a professional environment, and as the project went on I realized my mistakes and tried to fix them.  The other was a database design where I took an application running by itself and tried to create an environment for it where multiple people could have instances of this application.  It worked, but it was really hacked.  I didn't know about source control back then so going back to doing it right was impossible.

So now you understand why I like normalized databases.  Of course, once I get something working in 5th normal form then I start considering breaking the rules.  And I do so in a systematic approach.  This is called denormalization. The art of denormalization is knowing when to break the rules of normalization to improve performance and make life easier for anyone touching the project.  The key is that when you do this that your breakage is clearly identified in developer documentation.

Some places I've found are good for denormalization include financial transactions, report helpers, and tables that track the history of another record.

Its shocking though how often I've run into people who equate non-normalized databases with denormalized databases.  Sometimes you get a few newbies who like the sound of 'denormalization' as a word, but normally in my experience it is due to some 'senior developer' who hasn't read a coding book since 1997.  You know who I am talking about.