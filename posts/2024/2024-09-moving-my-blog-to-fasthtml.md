---
date: '2024-10-01T10:38:23.690964'
published: false
tags:
- FastHTML
- python
- blog    
title: Moving my blog to FastHTML
description: All the details of moving my blog from Next.js to FastHTML.
---

## Notes

This is my interpretation of feedback

- Alexis: Show the magnitude of what is happening
- Alexis: Be a bit more clear in the LOC 

- Jeremy: Needs more of a background section to explain what's going on and just more words in general to tie things together -- what are you talking about, and how does it fit in? 



## Blog post from here on

Recently I've been using and contributing to [FastHTML](https://fastht.ml/). I've enjoyed the clarity and speed of the framework, finding its design intuitive yet concise. In fact, my first test project with FastHTML was this blog - I had about 80% of the functionality of the site done in 45 minutes. 

## What stayed the same

### Performance

FastHTML is a compact ASGI framework leveraging Starlette that runs fast. It eschews templates and JSON for lean Python functions, reducing render time. I also use an in-memory cache for the content. The result is my FastHTML blog on a minimal Railway instance runs about as fast as my old Next.js blog on Vercel.

### Content

All my articles were brought over, as well as the Atom feeds. And the design. From a user's perspective, there is no difference between the old and new site.

## Changes 

### Python instead of Node

React and Next.js were okay, but the pure Python style (no templates!) of FastHTML is more enjoyable to me. Also, the stampede of the Node.js community to TypeScript turned me off to React. TypeScript has all the things I don't like about Python type hints and almost none of the things I enjoy.

_My love/hate for Python type hints is something I may write about in the future._

### Pretty HTML Source

FastHTML doesn't minimize or uglify HTML source code. This makes debugging layout problems a bit easier due to reduced friction.

### Adds Search

Before I added [search](https://daniel.feldroy.com/search) to my site to find old articles I wrote, I had to rely on Google or go to the [really big articles list](https://daniel.feldroy.com/posts). Yes, that list of articles is every blog entry I've made, currently up to 661 articles. I found it quite useful for looking up content by title/description, and the load time was fast.

While I could have implemented this search in Node.js, it wasn't added until right after this FastHTML version of my site.

### Brings in HTMX

The search feature uses [HTMX](https://htmx.org/) to improve the experience. Yes, I am an HTMX hipster.

### Uses CDN for non-custom CSS and JS

The old site stored and served all the CSS and JS. I've gone back to using CDNs. Yes, I know there are ways to do injection attacks, but this is a READ-only site serving blog content.

### 61% less code

The new site is only 532 lines of Python wheras the old site clocked in at 1,364 lines of code (1309 Javascript, 55 Python). Compared to Next.js, FastHTML is a very concise framework. 

## Summary

While any blog rewrite I've done has been fun, this iteration was especially enjoyable. It provided the means to practice on a new tool (FastHTML) and methodology (writing HTML in Python rather than templates). Keeping the same performance is rather nice, as is the 61% reduction in lines of code.