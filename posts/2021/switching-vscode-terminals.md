---
date: "2021-04-09T23:45:00.00Z"
published: true
description: By default VSCode doesn't include this keybinding. Here's how you add it.
slug: git-cheatsheet
tags:
  - VS Code
  - howto
time_to_read: 1
title: Switching between VS Code terminals using hotkeys
type: post
---

When I code I prefer to keep my hands on the keyboard as much as possible. For me, this keeps me more focused on the task at hand. Switching to the mouse is something try to I reserve for interacting with browsers.

By default [VSCode](https://code.visualstudio.com/) doesn't include the keybinding necessary to switch terminals via the keyboard. You are forced to use the mouse, which disrupts my flow.

Here's how you add terminal switching keybindings in VSCode:

# Step 1

Use `ctrl+p` (`cmd+p` on the Mac) and type `keybindings.json`. Select the file from the drop downlist. This will open a file that looks like this:

```json
// Place your key bindings in this file to
// override the defaults
[]
```

# Step 2

Replace the contents of `keybindings.json` with this for Windows or Linux:

```json
// Place your key bindings in this file to
// override the defaults
[
  {
    "key": "ctrl+down",
    "command": "workbench.action.terminal.focusNext",
    "when": "terminalFocus"
  },
  {
    "key": "ctrl+up",
    "command": "workbench.action.terminal.focusPrevious",
    "when": "terminalFocus"
  }
]
```

Or this when using the Mac:

```json
// Place your key bindings in this file to
// override the defaults
[
  {
    "key": "cmd+down",
    "command": "workbench.action.terminal.focusNext",
    "when": "terminalFocus"
  },
  {
    "key": "cmd+up",
    "command": "workbench.action.terminal.focusPrevious",
    "when": "terminalFocus"
  }
]
```

Now you can use the keyboard commands of Apple+UpArrow and Apple+DownArrow to switch terminals in VS Code.
