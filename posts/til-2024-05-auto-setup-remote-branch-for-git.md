---
date: '2024-05-21T09:38:05.180325'
description: 'For getting rid of the "fatal: The current branch new-awesome-feature has no upstream branch" error.'
published: true
tags:
- TIL
- git
- howto
title: 'TIL: Auto setup remote branch for git'
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

*For getting rid of the "fatal: The current branch new-awesome-feature has no upstream branch" error.*

Whenever I create a new branch and try to push the new commit then I start seeing this error:

```
git push --force
fatal: The current branch new-awesome-feature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin new-awesome-feature

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

To fix it so git just auto creates the branch, just enter this magic command:

```bash
git config --global --add --bool push.autoSetupRemote true
```

