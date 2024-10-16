---
date: "2021-03-01T23:45:00.00Z"
published: true
description: My list of simple and complex git commands and operations.
slug: git-cheatsheet
tags:
  - git
  - cheatsheet
  - howto
time_to_read: 5
title: Git Cheatsheet
type: post
---

I use a mix of both command-line and [GitHub Desktop](https://desktop.github.com/), keeping both fresh in my mind. I don't want to go entirely desktop because there are times (ssh-ing for example) when I have to use the command-line.

Note: Anything with an asterisk (`*`) can be done with [GitHub Desktop](https://desktop.github.com/).

# Creating a new branch\*

Work in the smallest, most atomic feature branches possible. It's easier for people to review smaller things, meaning you will move faster.

```bash
git checkout -b my-new-branch
```

# Committing all my changes\*

Note: Don't end commit messages with punctuation. Many projects reject it. Not sure why, it is just a thing.

Note 2: GitHub desktop makes adding long commits easy.

```bash
git commit -am "I am committing everything"
```

# Pushing my branch up\*

```bash
git push origin my-new-branch
```

# Deleting a local branch

```bash
git branch -d my-new-branch
```

# Deleting a remote branch (on GitHub, Gitlab, etc)

```bash
git branch -D my-new-branch
```

# Squashing all commits into a new one

Rebase is fundamental to working with Git. Yet unless I really think hard I screw them up. Therefore, I tend to just squash everything down to one commit and look good in the process. Until now, no one has known I frequently copy/pasta this series for all my PRs. Here is how I do it:

```bash
git checkout my-new-branch
git reset $(git merge-base master my-new-branch)
git add -A
git commit -m "OMG done in just one commit!"
git push --force
```

# Rebase from main

You've done some coding on your branch and now you want to bring in the latest changes from main. This is a common scenario. Here is how you do it:

```bash
git checkout main
git pull
git checkout my-updated-branch
git rebase main my-updated-branch
git push --force
```

# Updating an older commit

You've done some coding on your branch and now you want to update an older commit. [This article](https://tech.serhatteker.com/post/2020-09/changing-old-git-commit-messages/) covers the process.

The only change I make is to NOT specify the branch in the ` git push --force`.

# Delete all local merged branches

Will delete all your local branches that have been merged. Before you do that, verify what will be deleted first.

```bash
git branch --merged | egrep -v \
  "(^\*|master|main|dev)" | xargs git branch -d
```
