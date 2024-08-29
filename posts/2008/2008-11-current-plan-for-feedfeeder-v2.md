---
date: '2008-11-24T10:56:00.006-08:00'
description: ''
published: true
slug: 2008-11-current-plan-for-feedfeeder-v2
tags:
- feedfeeder
- plone
- legacy-blogger
time_to_read: 5
title: Current plan for FeedFeeder v2
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/11/current-plan-for-feedfeeder-v2.html)*.

Somehow this blog post stayed in draft mode forever.  But it details the plans I have for FeedFeeder v2, plans that seem to be pretty solid.

The problem with my [previous FeedFeeder v2 architecture](https://pydanny.blogspot.com/2008/10/morning-brainstorm-about-feedfeeder-v2.html) is that it tampered with something that was not broken; the basic FeedFeeder architecture.  Why do code cartwheels when the use of Collections can do all the work for you?

The new idea is to have each <span style="font-weight: bold;">FeedFolder</span> be responsible<a href="https://1.bp.blogspot.com/_KEFU5_uGRyw/SSsBQRjK4KI/AAAAAAAAAdU/8ebFi3s8KNo/s1600-h/Picture+1.png"><img alt="" border="0" id="BLOGGER_PHOTO_ID_5272309167867748514" src="https://1.bp.blogspot.com/_KEFU5_uGRyw/SSsBQRjK4KI/AAAAAAAAAdU/8ebFi3s8KNo/s320/Picture+1.png" style="margin: 0pt 0pt 10px 10px; float: right; cursor: pointer; width: 320px; height: 156px;" /></a> for a single feed.  Attributes to handle special cases (generally broken feeds your customer demands you handle) will be hung off the <span style="font-weight: bold;">FeedFolder </span>in which<span style="font-weight: bold;"> FeedItems</span> will be generated and reside.  If you need to combine multiple feeds then you just use a Collection.  No need for a special <span style="font-weight: bold;">FeedDefinition</span> content type, keeping the architecture simple and ensuring that the code remains straightforward.

The quick-and-dirty UML above is nearly identical to the way FeedFeeder v1 is built.  I've just added a '<span style="font-weight: bold;">rules</span>' lines attribute.  It could be more accurately be called '<span style="font-weight: bold;">feedParserEdgeCases'</span>, and will let you correct some of the funny cases you get when your customer says, "I need to have our site recieve feed from Joe Schmoe's bad feed and it has to happen next week!"  In the case below, JoeSchmoe has decided to change the Title attribute in his Atom feed to JoeSchmoeTitle.
<blockquote style="color: rgb(0, 0, 153);">'JoeSchmoeTitle => Title'</blockquote>Basically the idea will be that through a simple dialogue like the one below, you'll tell FeedFeeder to take the value of JoeSchmoe's custom title and put it into the correct FeedItem attribute.  And you'll be able to do it without any custom/hard coding!

The credit for this goes to the Van Rees brothers.  They looked at my crazy thoughts, forced me to defend them, and tossed in great ideas when they grokked the rantings of my insanity.  ;)