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

## Zoom!

To zoom into a window:

`ctrl+b z`

To zoom out just run it again:

`ctrl+b `

## How to reload Tmux

To reload a tmux session, you can use the following command within tmux:

`:source-file ~/.tmux.conf`

Alternatively, with the configuration provided earlier, you can simply press Ctrl-a followed by r to reload the configuration, thanks to this line:

`bind r source-file ~/.tmux.conf \; display "Reloaded!"`

This shortcut reloads the configuration and displays a confirmation message.

## Simple conf improvements that are awesome

In your `~/.tmux.conf` add these line:

```
# Makes the panes mouse clickable
set -g mouse on

# More attractive terminals
set -g default-terminal "screen-256color"
```

Note: Too much config can make your tmux alien to others, making it hard for you to work in other devices. 

## Not yet finished

More to come!

![](/public/images/tmux-logo-medium.png)
