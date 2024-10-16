---
date: "2012-05-11"
published: true
slug: css-hacking
tags:
  - python
  - django
  - blog 
time_to_read: 1
title: CSS Hacking to make my code samples legible
---

I've been very happy with [Pelican](https://pelican.readthedocs.org/) as
a blog engine so far, and haven't even moved off the sample theme.
There's just been one problem: Myself and others have had a lot of
trouble reading the code snippets.

I didn't have time to cook up a full Pelican theme, so instead I just
hacked the local CSS files. The problem with this hack is that every
time I regenerate the blog I have to copy the right CSS files into
place. So next week when I have time I'll do a proper Pelican theme.

In the meantime, enjoy!

```python
from random import shuffle

class Meal(object):
    def __init__(self):
        self.food_type = ['Beef', 'Fish', 'Vegetarian', 'Chicken']
        shuffle(self.food_type)
```
