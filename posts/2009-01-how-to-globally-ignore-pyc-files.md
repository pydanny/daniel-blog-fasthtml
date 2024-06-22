---
date: "2009-01-05T08:52:00.004-08:00"
description: ""
published: true
slug: 2009-01-how-to-globally-ignore-pyc-files
tags:
  - python
  - legacy-blogger
time_to_read: 5
title: How to globally ignore .pyc files
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/01/how-to-globally-ignore-pyc-files.html)_.

This has been driving me nuts. Sure, I run svn propset on directories and do so recursively, but I've hated having to remember to do it. Well, I just did it globally! How? I found my subversion config file!

```
emacs ~/.subversion/config
global-ignores = *.pyc
ctrl-x-s
ctrl-x-z
```

Yeah! No more annoying .pyc!

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2009/01/how-to-globally-ignore-pyc-files.html) on Blogger

**Zenos said on 2009-08-21**

Awesome, I keep forgetting how to do this every time I setup a new machine and have to look for the solution again. Thanks for posting it up!
