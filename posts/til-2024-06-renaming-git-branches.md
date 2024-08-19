---
date: '2024-06-04T09:55:47.055467'
description: Sometimes branches evolve into things that don't match their names.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- howto
- git
title: 'TIL: Renaming git branches'
twitter_image: /public/logos/til-1.png
---


*Sometimes branches evolve into things that don't match their names.*

To rename the current branch:

```
git branch -m NEWNAME
```

To rename a branch while pointed to any branch:

```
git branch -m OLDNAME NEWNAME
```

To push the local branch and reset the upstream branch:

```
git push origin -u NEWNAME
```

To cleanup the old branch:

```
git push origin --delete OLDNAME
```

---

Note: The source of this is this [Stack Overflow post](https://stackoverflow.com/questions/6591213/how-can-i-rename-a-local-git-branch). I wrote this TIL because I look this up about once a week, so decided to add it to the "bookmark" system that is my blog. Also, the use of `<brackets>` there for `REPLACE_THIS` content is unfortunate as it doesn't work well with the options keys.