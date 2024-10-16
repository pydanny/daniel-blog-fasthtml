---
date: "2020-01-30T22:20:50.52Z"
description: Writing a Python script to generate my blog feed
published: true
slug: feed-generator
tags:
  - python
  - blog
time_to_read: 5
title: Feed Generator
type: post
---

Late last year I [changed my blog engine yet again](/moving-to-vuepress.html). I've been happy with it so far, with the exception of XML feeds. The tooling I chose doesn't have good support for feeds, certainly not with the filtering I need. Specifically, I need to have a `python` feed, a `family` feed, and so on. As much as I love my [wife](https://audrey.feldroy.com) and [daughter](/recap-2019-resolutions-2020.html#my-daughter-was-born), non-technical posts about them probably don't belong on places where this post will show up.

After trying to work within the framework of the blog engine (Vuepress), I got tired of fighting abstraction and gave up. My blog wouldn't have an XML feed.

# Solution

Last night I decided to go around the problem. In 30 minutes I coded up a solution, a Python script that bypasses the Vuepress abstraction. You can see it below:

``` python
"""
generate_feed.py

Usage:

    python generate_feed.py TAGHERE

Note:

    Works with Python 3.8, untested otherwise.
"""

from glob import glob
import sys

try:
    from feedgen.feed import FeedGenerator
    from yaml import safe_load
    from markdown2 import Markdown
except ImportError:
    print("You need to install pyyaml, feedgen, and markdown2")
    sys.exit(1)


if __name__ == "__main__":

    try:
        tag = sys.argv[1]
    except IndexError:
        print('Add a tag argument such as "python"')
        sys.exit(1)

    # TODO - convert to argument
    YEARS = [
        "2020",
    ]

    markdowner = Markdown(extras=["fenced-code-blocks", ])

    fg = FeedGenerator()
    fg.id("https://daniel.roygreenfeld.com/")
    fg.title("pydanny")
    fg.author(
        {
            "name": "Daniel Roy Greenfeld",
            "email": "daniel.roy.greenfeld@roygreenfeld.com",
        }
    )
    fg.link(href="https://daniel.roygreenfeld.com", rel="alternate")
    fg.logo("https://daniel.roygreenfeld.com/images/personalPhoto.png")
    fg.subtitle("Inside the Head of Daniel Roy Greenfeld")
    fg.link(href=f"https://daniel.roygreenfeld.com/atom.{tag}.xml", rel="self")
    fg.language("en")

    years = [f"_posts/posts{x}/*.md" for x in YEARS]
    years.sort()
    years.reverse()

    def read_post(filename):
        with open(filename) as f:
            raw = f.read()[3:]

        config = safe_load(raw[: raw.index("---")])
        content = raw[raw.index("---") + 3 :]

        return config, content

    feed = []

    for year in years:
        posts = glob(year)
        posts.sort()
        posts.reverse()
        for post in posts:
            config, content = read_post(post)
            if tag not in config["tags"]:
                continue

            # add the metadata
            print(config["title"])
            entry = fg.add_entry()
            entry.id(f'https://daniel.roygreenfeld.com/{config["slug"]}.html')
            entry.title(config["title"])
            entry.description(config["description"])
            entry.pubDate(config["date"])
            entry.updated(config["date"])

            # Add the content
            content = markdowner.convert(content)
            entry.content(content, type="html")

    print(fg.atom_str(pretty=True))
    fg.atom_file(f".vuepress/public/feeds/{tag}.atom.xml")

```

You call this on my blog for all `python` tagged content by running it thus:

``` bash
python generate_feed.py python
```

The result [validates per W3C](https://validator.w3.org/feed/#validate_by_input) and should work everywhere. Yeah! 

## Summary

This is what I've always enjoyed about Python. In a very short time I can throw together a script that makes my life better. 