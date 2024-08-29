---
date: '2008-11-14T09:52:00.003-08:00'
description: ''
published: true
slug: 2008-11-subscribers-zope-3-style
tags:
- zope
- legacy-blogger
time_to_read: 5
title: Subscribers Zope 3 style
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/11/subscribers-zope-3-style.html)*.

Vernon Chapman shared this with me.  Very elegant.

`configure.zcml`

```xml
<subscriber
    for="Products.CMFCore.interfaces.IActionSucceededEvent"
    handler=".handlers.vernstuff_content_thing" />
```
    
handlers module

```python
def vernstuff_content_thing(event):
    """This will do all the work"""
    action_as_string = event.action
    content = event.object
    # Do whatever you like here
```