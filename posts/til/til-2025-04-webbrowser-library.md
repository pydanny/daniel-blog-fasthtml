---
date: '2025-04-15T12:30:43.170061'
description: Python's built-in library for controlling browsers from Python
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: webbrowser library'
twitter_image: /public/logos/til-1.png
---

Python comes with [webbrowser](https://docs.python.org/3/library/webbrowser.html), a library for opening webbrowsers to specific pages such as this one. 

```python
>>> import webbrowser
>>> url = 'https://daniel.feldroy.com/'
>>> webbrowser.open(url)
```