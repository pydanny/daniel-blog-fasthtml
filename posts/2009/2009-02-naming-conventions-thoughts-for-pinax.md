---
date: '2009-02-19T15:48:00.002-08:00'
description: ''
published: true
slug: 2009-02-naming-conventions-thoughts-for-pinax
tags:
- django
- plone
- pinax
- spacebook
- legacy-blogger
time_to_read: 5
title: Naming conventions thoughts for Pinax and Django
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/02/naming-conventions-thoughts-for-pinax.html)*.

I really like Pinax. As the core framework behind our NASA HQ open source social networking application Spacebook, it has been a literal godsend. Out of the box it met most of our requirements, and the Pinax team has graciously added many of our needs to the feature set of Pinax going forward (div based forms, for example). My opinion is that Pinax is a great demonstration of what you can do using Python, Django, and an open source community. We'll be using it for Spacebook and other projects moving forward.

However, if there is one thing I could improve in Pinax (and Django), would be its adherence to a model naming standard. Yes, it does follow the Django convention of naming models, but it doesn't have any internal conventions beyond the Django convention.

Whatever do I mean?

Well, lets say I want a single report to display all the bookmarks and blogs I've added in the last 2 hours, and include the name and description of each item. In theory, via the ORM, I can simply query both via user as a related field, write a django template to display the data, plug in a url, and then I'm done.

That is the theory. 

However, the problem is that the Bookmark model has description and note fields, and the Blog model has title and tease fields. To make this more clear, let me demonstrate what I get:

 1. BOOKMARK: description/note
 2. BLOG: title/tease
 
So now either my template or my view has to account for different naming conventions per type. Yes, I know that django templates will not display absent variables, but what if I need to add a third model that follows yet a different convention? Or a fifth? Or a sixth? What if I want to write some awesome introspection engine to creatively fetch and list titles and descriptions of the records? Oops - now I have to carefully catalog each type or queryset I'm going to receive. Testing will have to account for lots of use cases. My code is now more complex. Heavier. Slower.

I'm having to configure, rather than follow convention.

<span style="font-weight: bold;">A proposed solution</span>

Its all about convention over configuration.

Years ago in the dark ages of the late 1990s or early 2000s, a bunch of librarians got together and established the Dublin Core for content. Everything had a title and description field, not to mention optional body, author and other useful fields that could with every bit of content.

I propose this solution for Pinax (and Django) as a standard for items that represent text based editable content. So maybe not for financial/sports numbers, but instead for blogs, bookmarks, wiki pages, projects, groups, tribes, articles, and all that other bit of stuff that we like to read.

So if I do a query that returns Bookmarks and Blogs, all I need to care about is the convention of using titles and descriptions, not checking the model to see if my understanding of its configuration (name, tease, note, rant, description, intro, etc) is correct.

Pretty neat!

And yes, those of you from the Plone/Zope communities will find this very familiar.

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2009/02/naming-conventions-thoughts-for-pinax.html) on Blogger

**Александр said on 2010-03-29**

That's not convention, that's invention. Inventing &quot;special words&quot; besides a little well-known core of language-wide reserved words means hard approach for novices, for those who want something simple, obvious, unobstructed and light. Each language special word should be introduced with great care as they produce naming conflicts.

