---
date: '2025-01-31T18:18:35.368709'
description: Obvious now that I think about it!
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python

title: 'TIL: Every Jupyter notebook cell runs in an async loop'
twitter_image: /public/logos/til-1.png
---

Since June of last year I've done a decent amount of async/await programming inside of Jupyter notebooks. And I never thought about the fact that I didn't have to run an async loop. Sure, I knew that the Jupyter server is async, but until I did a direct export to Python module from a notebook this distinction hadn't mattered.

A fun little nuance, and it makes me think that one of the better places to accelerate async/await programming skills is in a notebook. 