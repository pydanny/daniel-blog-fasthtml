---
date: "2008-04-24T09:07:00.004-07:00"
description: ""
published: true
slug: 2008-04-what-i-want-in-feed-aggregator
tags:
  - django
  - beautiful soup
  - feedparser
  - grok
  - GAPE
  - rss
  - wxpython
  - legacy-blogger
time_to_read: 5
title: What I want in a feed aggregator
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/04/what-i-want-in-feed-aggregator.html)_.

The list is simple:

1. One page that displays all the content. Maybe do some pagination, or hide descriptions and just show titles. Otherwise have tags, author, description, and link to original post.
2. One page with a text area that accepts one feed per line.
3. Include some sort of authentication.

## Ways to get this done

Google App Engine handles #3 for me nicely and gives me free hosting. But feedparser doesn't play well with it and I'm not about to do that kind of debugging. Maybe I ought to try BeautifulSoup?

I'm tempted to try a pure Django system, since that could handle all three, but then I would have to pay for hosting. The same would go for Grok as well. I don't want to pay for hosting yet. Or maybe I ought to just pony up a few bucks a month anyhow...

Of course, I can always write my own simple wxPython client.

What to do... what to do...

**Update:** Never code on two hours sleep. I'm going with Google app Engine because I realized that when you import of feedparser you can't do this:

```
import feedparser.py
```
