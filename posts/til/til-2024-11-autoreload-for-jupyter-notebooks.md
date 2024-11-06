---
date: '2024-11-06T18:00:00.928751'
description: How to skip having to restart your notebook on code changes.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
- jupyter
- howto
title: 'TIL: Autoreload for Jupyter notebooks'
twitter_image: /public/logos/til-1.png
---

Add these commands to the top of a notebook within a Python cell. Thanks to Jeremy Howard for the tip.

```python
%load_ext autoreload
%autoreload 2
```