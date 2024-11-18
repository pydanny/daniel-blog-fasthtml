---
date: '2024-11-18T18:27:21.938091'
description: How to keep order of records without having to update all the records
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
- javascript
- nodejs
title: 'TIL: Fractional Indexing'
twitter_image: /public/logos/til-1.png
---

In the past when I've done this for web pages and various other interfaces it has been a mess. I've built ungainly sort order in numeric or alphanumeric batches. Inevitably there is a conflict, often sooner rather than later. So sorting a list of things often means updating all the elements to preserve the order in the datastore. I've learned to mark each element with a big value, but it's ugly and ungainly

Fortunately for me, going forward, I now know about Fractional Indexing. 

References:

- https://www.figma.com/blog/realtime-editing-of-ordered-sequences/
- https://observablehq.com/@dgreensp/implementing-fractional-indexing
- https://github.com/httpie/fractional-indexing-python