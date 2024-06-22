---
date: "2023-09-27T15:45:00.00Z"
published: true
slug: til-2023-09-finding-and-ignoring-with-glob
tags:
  - TIL
time_to_read: 1
title: "TIL: Finding and ignoring files with Glob"
description: How to find and ignore files and directories when using glob
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

[Glob](https://en.wikipedia.org/wiki/Glob_(programming)) is a really handy tool for finding filepaths. It resembles regular expressions but the syntax is different. Finding matches is easy:

```bash
# finds python files in the current working directory
*.py
# finds all the nested python files.
**/*.py
```

What I didn't know until today is how to exclude files. That's done through the use of the `!` operator. So the inverse of the above is:

```bash
# finds anything but python files in the current working directory
*.[!py]*
# finds anything but python files in the nested directory 
- **/*.[!py]*
```