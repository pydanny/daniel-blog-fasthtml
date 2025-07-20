---
date: '2024-11-13T15:00:14.753658'
description: "Once I've isolated a test failure to a very small set of failures I use this instead of running pytest directly. What it does on exception is start the IPython pdb interface."
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
- testing
title: "TIL: Making pytest use Ipython's PDB"
twitter_image: /public/logos/til-1.png
---

```sh
alias pdb='pytest --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb'
```

Usage:

```sh
pdb tests/test_things::test_broken_thing
```