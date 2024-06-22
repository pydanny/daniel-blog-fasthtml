---
date: "2023-12-18T15:30:00.00Z"
published: true
slug: til-2023-12-change-older-git-commit
tags:
  - howto
  - git
  - TIL
time_to_read: 1
title: "TIL: Change older git commit"
description: How to change an older git commit rather than the most recent one.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

Typically I try to avoid changing older commits in a pull request.  My reasoning has a tiny bit to do with preserving history and lots to do with being resistant to trying new things. Finally I got around to looking this up today, it is easy to do.

WARNING: Do this on branches of main, not on the main branch itself. More on that at the end.

# Find the commit

In our example the change we want to amend is 3 commits back, do this to find it:

```bash
git rebase -i HEAD~3
```

That will bring up a screen that looks like this in your text editor:

```bash
pick ec0fb5e0333c Configure omnitron galactic retroverter
pick 6e7f323681f1 Activate the anvil generator
pick 0001757cea8f Wind up clockwork battery
pick 849f7c453458 Solidify the electricity

# Rebase dd341c1572..64c2cbbd76 onto dd34dc1572 (4 commands)
```

On the third line, change the word, `pick` to `edit`. It should now look like this:

```bash
pick ec0fb5e0333c Configure omnitron galactic retroverter
pick 6e7f323681f1 Activate the anvil generator
edit 0001757cea8f Wind up clockwork battery # <-- changed line
pick 849f7c453458 Solidify the electricity

# Rebase dd341c1572..64c2cbbd76 onto dd34dc1572 (4 commands)
```

Save and close the file. 

# Make changes

Now make changes to code files and save them. 

# Commit and rebase

Run these commands to have git recognize the changes:

```bash
git commit --all --amend --no-edit
git rebase --continue
```

If you have a remote repo (aka github or gitlab) you will need to run `git push --force` .

# About the warning

Before you do this understand this rewrites the SHA-1s from the point of change forward. Any old SHA-1 representatives of those commits are gone. Hence this should happen on a branch away from master, preferably in a pull request.

# References

- [stackoverflow.com/a/1186549](https://stackoverflow.com/a/1186549) - If for nothing else the instructions on how the tilde (~) works is really nice to know.