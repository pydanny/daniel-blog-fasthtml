---
date: "2008-04-10T11:39:00.002-07:00"
description: ""
published: true
slug: 2008-04-history-of-my-most-used-shell-commands
tags:
  - MacOS
  - legacy-blogger
time_to_read: 5
title: History of my most used shell commands
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/04/history-of-my-most-used-shell-commands.html)_.

Courtesy of [me -> flub](https://bruynooghe.blogspot.com/2008/04/shell-history.html):

```
history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn |head -n 20
107 svn
101 cd
101 ./bin/instance
58 ls
37 python
26 mate
16 grep
11 rm
8 ssh
4 ipython
4 easy_install
3 sqlite3
2 sudo
2 pwd
2 mkdir
2 history
2 django-admin.py
2 django-admin
2 ./bin/instance1
1 wget
```
