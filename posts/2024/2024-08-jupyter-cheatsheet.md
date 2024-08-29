---
date: '2024-08-26T16:59:13.639858'
description: A list of tips and tricks for working with Jupyter Notebooks.
published: false
tags:
  - cheatsheet
  - howto
  - python
  - jupyter
title: Jupyter Cheatsheet
---

_A list of tips and tricks for working with Jupyter Notebooks._

## Debug with the %debug magic command

If you have an error that's challenging to debug, activate debugger in post-mortem mode. In the cell underneath the error, create a new cell with this error

 with this simple  You can activate this mode simply running %debug without any argument. If an exception has just occurred, this lets you inspect its stack frames interactively. Note that this will always work only on the last traceback that occurred, so you must call this quickly after an exception that you wish to inspect has fired, because if another one occurs, it clobbers the previous one.