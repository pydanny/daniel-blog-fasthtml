---
date: '2024-09-03T08:33:14.926680'
description: My list of tmux commands with minimal flavor text.
published: true
tags:
 - cheatsheet
 - howto
title: tmux cheatsheet
image: /public/images/tmux-logo-medium.png
twitter_image: /public/images/tmux-logo-medium.png
---

_My list of tmux commands with minimal flavor text._

The tmux terminal utility allows for splitting terminal into multiple window panes. The splits can be vertical or horizontal. Installation instructions are [here](https://github.com/tmux/tmux/wiki/Installing).

## Creating a new tmux session

```bash
tmux new -s SessionName
```

## Creating new panes

Horizontal panes


`Ctrl+B "` 


Vertical panes


`Ctrl+B %`


## Scrolling

`Ctrl+B [`

Then use arrow keys or pageup and pagedown. Press `q` to quit.


## Moving between panes


`Ctrl+B` plus arrow keys

## Closing the current pane

`Ctrl+b+x`

## Killing the current session

Sometimes you want to end the current session.

`Ctrl+b`

`:kill-session`

## Not yet finished

More to come!

![](/public/images/tmux-logo-medium.png)
