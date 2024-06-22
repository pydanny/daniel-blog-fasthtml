---
date: "2023-10-02T15:45:00.00Z"
published: true
slug: til-2023-10-rich-console-status-for-slow-processes
tags:
  - python
  - TIL
time_to_read: 1
title: "TIL: Rich.console.status for slow processes"
description: From the command-line a trick to inform users know the system hasn't died and they should wait until it is done.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

For building CLI, there's so much that [rich](https://pypi.org/project/rich/) provides that I can't imagine not using it. Here's adding a moving bar that updates:


```python 
from time import sleep
from rich.console import Console

console = Console()

with console.status(
    "[bold red]Starting...[/bold red]", spinner="bouncingBar"
) as status:
    console.log("Process started")
    sleep(3)
    # If you want to be lazy, not closing the tags doesn't seem to have side effects
    status.update("[bold yellow]still going...")
    console.log("Process still going")
    sleep(2)
    status.update("[bold green]almost there...")
    console.log("Process getting close", style="bold")
    sleep(1)
    console.log("Finish!", style="bold green")
```

Rich comes with a lot of spinners to show the system processing. This script displays most of them in action:

```python
from rich import console, spinner

from time import sleep

console = console.Console()

with console.status("Here we go...") as status:
    sleep(2)
    for key in spinner.SPINNERS.keys():
        # Skipping the 15 dot variations
        if key.startswith("dots"):
            continue
        status.update(key, spinner=key)
        sleep(2)
```