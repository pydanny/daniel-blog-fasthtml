---
date: '2024-08-06T12:00:00.192810'
description: How to convert inconsistent datetime strings into datetime objects.
image: /logos/til-1.png
published: true
tags:
- TIL
- howto
- python
- FastHTML
title: 'TIL: Parsing messy datetimes strings'
twitter_image: /logos/til-1.png
---

*How to convert inconsistent datetime strings into datetime objects.*

Recently I've been working on yet another rewrite of my blog, this time to [FastHTML](https://about.fastht.ml/). Thanks to the power and ease of that framework, that took about 45 minutes to replicate all the web pages of my blog. Wahoo!

Alas, the atom/rss feeds took quite a bit longer. 

For the atom/rss feeds I chose to use the venerable [Feedgen](https://pypi.org/project/feedgen/) library. The challenge there is that Feedgen is rightfully particular about the datetime objects it accepts. And over the years as this site has had 650 posts added the timestamps have become rather inconsistent in their format. On that issue I fully blame the author, who unfortunately is me.

In any case, I wrote a little Python function that handles it in a timezone aware way using the `dateutils.parser()` functon that I learned.

```python
# Python stdlib
from datetime import datetime
from dateutils import parser

# You'll need to install the pytz dependency
import pytz

def convert_dtstr_to_dt(date_str: str) -> datetime:
    """
    Convert a naive or non-naive date/datetime string
    to a datetime object. Naive datetime strings are
    assumed to be in GMT (UTC) timezone.
    """
    try:
        dt = parser.parse(date_str)
        if dt.tzinfo is None:
            # If the datetime object is naive, set it to GMT (UTC)
            dt = dt.replace(tzinfo=pytz.UTC)
        return dt
    except (ValueError, TypeError) as e:
        Raise Exception(f"Error parsing date string: {e}")
```

Original source code [here](https://github.com/pydanny/daniel-blog-fasthtml/blob/da9500d0c4af9876c267fdd447f4656796516163/components.py#L12-L31).

_Note: As of publishing, this article is still on my old blog. The DNS switchover to the [FastHTML version of my blog](https://danielfeldroycom-production.up.railway.app/) happens later this week._