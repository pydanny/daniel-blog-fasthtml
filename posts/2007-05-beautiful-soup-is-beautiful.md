---
date: "2007-05-16T10:37:00.000-07:00"
description: ""
published: true
slug: 2007-05-beautiful-soup-is-beautiful
tags:
  - beautiful soup
  - python
  - legacy-blogger
time_to_read: 5
title: Beautiful Soup is Beautiful
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/05/beautiful-soup-is-beautiful.html)_.

I have a bunch of content stored on an old instance of [pmwiki](https://www.pmwiki.org/). I've never liked pmwiki, since it seems to only have a half-hacked state method, and just in general feels insecure. Also, I've found that wikis can be useful, but if you have short content on each page, often a FAQ style treatment will do better than a regular wiki.

So I decided to convert the pmwiki pages into a [pbwiki](https://pbwiki.com) toc construct. It would put all the content onto one page, and use the tag to provide a top level table of contents. That meant I would have to:

#. Scrape the pmwiki content index for all the meaningful links.
#. Scrape out the title and urls of each link.
#. Grab the content from each link.
#. Reformat it all to work in the pbwiki format.

I've done screen scraping before, but not in Python, and not in this scope of effort. Well, Python seems to do everything well so I opened up htmllib and started to play, thinking I would be done by brunch-time.

Immediately I'm unhappy with htmllib. The docs suck. And it just seems awkward to use once I figure it out. Doesn't feel Pythonic, although I'm sure I'm wrong in that respect somehow. Its just for me, my Python pseudo code often ends up being close to the end effort. And this was not the case.

Then a work buddy told me about [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/). Its an HTML/XML parser that is real easy to use and can work with badly formed HTML, like the sort that pmwiki sometimes generates. Its not optimized for speed, but for usability. Thats fine with me, because this is a one-time operation on maybe 150-200 entries.

The final effort worked real nice. Not super fast, but real easy to code. Beautiful Soup meant what I thought would be a quick and simple task remained so.

---

## 2 comments captured from [original post](https://pydanny.blogspot.com/2007/05/beautiful-soup-is-beautiful.html) on Blogger

**David E. Weekly said on 2007-05-16**

Hi! This seems pretty cool; we'd love to make it easy for pmwiki users to make their home with PBwiki. Would you mind sharing your importer with us? Feel free to email me at david@pbwiki.com.

**pydanny said on 2007-05-19**

Emailed you the from my HQ NASA account. Its a first draft and I'm planning to make changes to it to make it more reusable. If you do a PHP version, let me know!
