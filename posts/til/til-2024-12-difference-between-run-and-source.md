---
date: '2024-12-23T17:05:43.817074'
description: Different ways to run bash commands that explains part of my frustration
  with bash over the years.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Difference between run and source'
twitter_image: /public/logos/til-1.png
---

- `Run` launches a child process in a new bash within bash, so variables last only the lifetime of the command. This is why launching Python environments doesn't use `run`.

- `source` is the current basj, so variables last beyond the running of a script. This is why launching Python environments use `source`.