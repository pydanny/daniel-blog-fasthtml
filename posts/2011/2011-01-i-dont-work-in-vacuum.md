---
date: '2011-01-06T11:17:00.000-08:00'
description: ''
published: true
slug: 2011-01-i-dont-work-in-vacuum
tags:
- blog
- legacy-blogger
time_to_read: 5
title: I don't work in a vacuum
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/01/i-dont-work-in-vacuum.html)*.

Not too long ago I wrote a blog rant called '[Stupid Template Languages](https://pydanny.blogspot.com/2010/12/stupid-template-languages.html)'. I suspected I was setting off a firestorm, but I have to admit I didn't quite expect to have the singular honor of having both [Armin Ronacher](https://lucumr.pocoo.org/2010/12/5/not-so-stupid-template-languages/) and [Mike Bayer](https://techspot.zzzeek.org/2010/12/04/in-response-to-stupid-template-languages/) respond to me in their own blogs. As one might say, "Danny, you really stepped into it."

My initial response to their entries was to start writing another post that would refute what they said point-by-point. However, while the tone in my original post was somewhat confrontational, the problem is that I didn't want to turn the debate into a sordid affair with drawn sides. You see, I've long respected both Mike and Armin as developers and people. Even if I didn't care about them, all it would do is stir up angry retaliations and steer people away from good tools. So I [linked to their responses](https://pydanny.blogspot.com/2010/12/reactions-to-stupid-template-languages.html),&nbsp;let it go, and I hope we can drink over the issue this year at [Pycon](https://us.pycon.org/2011/home/).

However, if we step away from the tools, the real problem I was addressing in my post was this:

<b>I don't work in a vacuum</b>

Any tool has the potential for misuse. As [Alex Gaynor](https://alexgaynor.net/) pointed out in [Django Dose](https://djangodose.com/podcasts/community-catchup/episode/32/), he is familiar with the poorly crafted system which was part of the reason why I wrote 'Stupid Template Languages'. Heck, anyone reading this blog has probably run into one of those nightmarish system created by others that we have to maintain, and many of us will sheepishly admit to having been the author of such systems.

When you create a system like that you are making things harder for others to contribute and enhance. Trivial tasks become monumental and the desire to post your sad story to [The Daily WTF](https://thedailywtf.com/) becomes very strong.

<b>Don't work in a vacuum</b>

There are the well-documented methods called 'best practices' that us programmers ought to follow in order to make our work more maintainable. &nbsp;In the general programming world, patterns like [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC) is a common way to break up pieces of a project into predictable components. In the [Python](https://python.org/) world, we generally follow a set of standards called '[pep-8](https://www.python.org/dev/peps/pep-0008/)' for writing our code. Various groups and organizations often have additional standards for naming, tests, and documentation styles.

Standards can be created without wisdom or consideration for real-world issues. Too many tests and documentation can eat up time on a project and cause interminable delays; there are horror stories about developers writing pages of non-technical material in order to produce a single line of working code.

Following these methods and doing so with wisdom is like striving for a [platonic ideal](https://en.wikipedia.org/wiki/Theory_of_forms). It is both gratifying and time consuming to reach for perfection - and this perfection is fleeting because of the shifting requirements of clients, operating systems, and tool changes. To attempt to reach for this helps a person be considered a good developer, but doesn't guarantee that they are actually good.

<b>Breaking the rules</b>

Sometimes you have to abandon best practices. Sometimes the tool at hand makes it hard to perform a task without breaking the rules. In the python world a good example is&nbsp;[monkey-patching](https://en.wikipedia.org/wiki/Monkey-patching), which we do with trepidation. In the relational database world, people with a deep understanding of&nbsp;[normalization](https://en.wikipedia.org/wiki/Database_normalization)&nbsp;will sometimes indulge in&nbsp;[de-normalization](https://en.wikipedia.org/wiki/Denormalization)&nbsp;in order to boost performance.

Unlike best practices, there is no platonic ideal that clearly states when breaking the rules is a good thing. Ever seen a database created by a developer without any knowledge of normalization who smugly says their database is better because it started off de-normalized? How many of us have seen views where control and persistence is integrally embedded? Or where views are embedded in control code?

In regards to the debate that triggered this post, I've read the following phrase a few times as an argument against my rant: "We're all consenting adults here".

Does that mean we can do what we want? That we can write spaghetti code?

Certainly most people reading this post will know that statement generally refers to variable handling in Python, not the right to sunder the rules of good coding practices. Yet I've seen people use that as a mantra to ignore any sense of good coding practices for python related projects. Which meant that the level of effort to maintain and expand those projects increased at the same rapid rate that the bus factor decreased.

<b>Conclusion</b>

I'll just throw out some well known platitudes:


- Code like you aren't in a vacuum.&nbsp;
- Break the rules only when you have a concrete reason.&nbsp;
- Learn to take criticism well.

