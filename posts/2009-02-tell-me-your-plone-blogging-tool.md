---
date: '2009-02-02T12:29:00.006-08:00'
description: ''
published: true
slug: 2009-02-tell-me-your-plone-blogging-tool
tags:
- plone
- legacy-blogger
time_to_read: 5
title: Tell me your Plone blogging tool preferences
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/02/tell-me-your-plone-blogging-tool.html)*.

I have a new internal facing Plone project here at NASA. One of my requirements is to have a blog system. So this is your chance to suggest to me your favorite blogging tool. Want to see some requirements? Sure!


- Must work in Plone 3.1.x+.
- Groups will have blogs.
- Users will be in possibly multiple groups.

- Any user in a group can post a blog entry.
- Output must be Section 508 compliant.

What do I want to see in a blogging tool as a developer?


- Easy to implement.
- Clean code base so it will be easy to migrate to future versions of Plone.

<span style="font-weight: bold;">Update</span>: Thanks to the comments, for now I am going with Scrawl. It meets my formal requirements handily, and also meets my personal preferences. If the scope of the blog grows I will explore other options.

---

## 5 comments captured from [original post](https://pydanny.blogspot.com/2009/02/tell-me-your-plone-blogging-tool.html) on Blogger

**Jon Stahl said on 2009-02-02**

Scrawl (we wrote it at ONE/Northwest) or QuillsEnabled.  Basically you want something that uses existing content types, which is more future proof. 

Scrawl is very minimalist, QuillsEnabled is a bit more feature-rich, but also a bit more "work-in-progress."

**Unknown said on 2009-02-02**

I agree with Jon's point of view. I also use Scrawl in my Plone site.

**Unknown said on 2009-02-02**

I'm a big fan of using the right tool for the right job. You can make Plone do blogging, but it pales to what other blog-focused systems like WordPress can do.

Consider wrapping WP and Plone behind Deliverance. That's what OpenPlans.org is.

**ajung said on 2009-02-02**

Using the standard NewsItem for my blog. Blog items get a special subject 'BlogItem'. A collection is used for aggregating and syndication...no further pain with your next Plone migration

**pydanny said on 2009-02-03**

@Jon Stahl, @shigeo, @limi, @Alex - I'm giving scrawl a test run now. 

@ajung - I will try that as well.

@Jon Stahl, @duffyd - QuillsEnabled goes way beyond my list requirements. If I ever need its capabilities, I should be able to cook up a migration system.

@Gerry, @Alex - The idea of using deliverance to fetch the precise and exactly right tool is an interesting one. The extra complexity doesn't fit the budget/timeline I have for this project, but I'll keep it in mind for future efforts.

