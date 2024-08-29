---
date: '2008-09-15T09:17:00.008-07:00'
description: ''
published: true
slug: 2008-09-plone-os-projects-take-two-radius
tags:
- geek celebrities
- feedfeeder
- feedparser
- plone
- atom
- legacy-blogger
time_to_read: 5
title: 'Plone OS projects take two: Radius package and FeedFeeder package'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/09/plone-os-projects-take-two-radius.html)*.

I still haven't made up my mind.  Lets go over my options, since working on either can be lots of fun.  Do keep in mind my target Plone version is 3.x.

<span style="font-weight: bold;">Plone Radius Package</span>
This would be really useful for my job.  A Plone package that allows authentication via Radius/RSA would likely mean lots more Plone work for NASA HQ.  Once I got a functional prototype I'm sure I could get some funding for more work.  Since Wichert Akkerman's [pyrad](https://www.wiggy.net/code/pyrad/) python module is supposedly pure Python this makes integration really easy.  I like easy integration.

One thing I like about this potential project is that it should be a pretty quick effort.  Actually, the hard part will probably be finding a server to test against.

<span style="font-weight: bold;">FeedFeeder Package</span>
<span class="highlightedSearchTerm">[Reinout](https://vanrees.org/)</span>[None](https://vanrees.org/) invited me in a [response](https://www.blogger.com/comment.g?blogID=4477131926658044957&postID=2983369878163019663) to this [post](https://pydanny.blogspot.com/2008/09/some-ideas-for-open-source-plone.html) to take a crack at FeedFeeder when I brought up this issue.   The issue?

Feedfeeder assumes the best out of its sources, and assumes that FeedParser is going to return something nice.  What if we could make FeedFeeder either assume the worst of its sources, or give FeedFeeder administrators more flexibility in how to handle feeds?
<span class="highlightedSearchTerm"></span>
Alas, the problem with RSS (and even Atom) is that people consider the specification (if they actually look at the specification) as mere loose guidelines.  I'm not going to point any fingers at anyone because I like my job, but I will say that the ability of Web Browsers to look at anything remotely like RSS and then display the contents like a feed makes life for us Plone developers a pain in the butt.

Periodically, I got people saying, "<span style="font-style: italic;">Include this as a feed!</span>" until I trained them to realize that most RSS feeds are junk.  Which is nevertheless embarrassing when the so-called feed that displays as an RSS feed in Firefox or Safari is completely screwy when it comes the XML.  In fact, at my job we've pretty much forked FeedFeeder in order to support customer requests, with each RSS feed item being a custom script.  The results work and yet are not very pretty.

So my big idea is this that FeedFeeder would be enhanced in one of two ways:



1. <span style="font-weight: bold;">Custom Scripts</span> - FeedFeeder administrator can do TTW scripts (portable via Generic Setup) to control how FeedFeeder parses the incoming feed.  The scripting would be restricted Python.  This way the same feed that can be seen via the browser can now be interpreted by FeedFeeder as well.  The problem is the normal sort of issues you get with TTW programming, especially when it comes time to validate the script, or port it around (Even with Generic Setup).

- <span style="font-weight: bold;">Custom Plugins</span> - How about a plugin system of some sort?  Basically, you would follow a standard API and put your plugins in a particular folder.  FeedFeeder would pick up the plugin and run the appropriate plugin (we would have a selector tool) against the appropriate feed.  This way we could grow the functionality and robustness of the tool as more RSS and Atom feeds are added, and could also support new protocols as they become popular

Idea #1 seems quick to do, yet iffy and chock full of potential surprises, but Idea #2 seems like a solid way to do this effort.

<span class="highlightedSearchTerm">BTW,  [Reinout](https://vanrees.org/)</span>[None](https://vanrees.org/) has responded to all my posts on the subject of FeedFeeder. He commented on my first post, which was me whining about not reading the code, to the second which was deliberating on making a RSS package that was like FeedFeeder, but could handle problematic RSS better.

So hopefully Reinout is going to read this post too and share an opinion. ;)