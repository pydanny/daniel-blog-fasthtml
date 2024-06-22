---
date: '2007-11-13T11:51:00.000-08:00'
description: ''
published: true
slug: 2007-11-adding-new-user-at-root-of-plonezope-2
tags:
- plone
- zope
- legacy-blogger
time_to_read: 5
title: Adding a new user at the root of Plone/Zope 2 programmatically
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/adding-new-user-at-root-of-plonezope-2.html)*.

Sometimes you just need to do this sort of thing.
<pre class="prettyprint-py">>>> app.portal._addRole('MyRole')</pre>