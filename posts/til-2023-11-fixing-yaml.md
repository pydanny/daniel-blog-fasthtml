---
date: "2023-11-08T14:30:00.00Z"
published: true
slug: til-2023-11-fixing-yaml
tags:
  - howto
  - python
  - TIL
time_to_read: 1
title: "TIL: Fixing YAML"
description: Here's how to prettify YAML across your projects.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

I got tired of manually correcting and prettifying YAML only to run into periodic instances where my cleanup broke configurations. Alas, `yamllint` tells you what's wrong but doesn't fix problems. I would rather have an easy-to-use CLI tool that does all the work for me. 

Thanks to David Winterbottom for the suggestion.

Step 1: Install `yamlfix`

```bash
pip install yamlfix
```

Step 2: Recursively clean up all the YAML

```bash
yamlfix .
```