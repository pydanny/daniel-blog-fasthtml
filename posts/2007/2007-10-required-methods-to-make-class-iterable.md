---
date: '2007-10-09T03:54:00.000-07:00'
description: ''
published: true
slug: 2007-10-required-methods-to-make-class-iterable
tags:
- legacy-blogger
time_to_read: 5
title: Required methods to make a class iterable
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/10/required-methods-to-make-class-iterable.html)*.

Really useful:

```python
#required iterable elements
class MyIterator(object):

    def iter(self):
        return self.data.iter()

    def len(self):
        return len(self.data)

    def contains(self, v):
        return v in self.data

    def getitem(self, v):
        return self.data[v]
```