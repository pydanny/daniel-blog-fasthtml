---
date: "2023-12-04T15:30:00.00Z"
published: true
slug: til-2023-12-forcing-pip-to-use-virtualenv
tags:
  - howto
  - python
  - TIL
time_to_read: 1
title: "TIL: Forcing pip to use virtualenv"
description: Necessary because installing things into your base python causes false positives, true negatives, and other head bangers.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

Necessary because installing things into your base python causes false positives, true negatives, and other head bangers.

Set this environment variable, preferably in your rc file:

``` bash
# ~/.zshrc 
export PIP_REQUIRE_VIRTUALENV=true
```

Now if I try to use pip outside a virtualenv:

``` bash
dj-notebook on  main [$] is 📦 v0.6.1 via 🐍 v3.10.6 
❯ pip install ruff 
ERROR: Could not find an activated virtualenv (required).
```

This TIL is thanks to David Winterbottom.