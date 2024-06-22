---
date: "2023-11-12T10:30:00.00Z"
published: true
slug: til-2023-11-autoloading-on-filechange-using-watchdog
tags:
  - howto
  - python
  - TIL
time_to_read: 1
title: "TIL: Autoloading on Filechange using Watchdog"
description: Using Watchdog to monitor changes to a directory so we can alter what we serve out as HTTP.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

Using Watchdog to monitor changes to a directory so we can alter what we serve out as HTTP. Each segment is the evolution towards getting it to work.

## Serving HTTP from a directory

I've done this for ages:

```sh
python -m http.server 8000 -d /path/to/files
```

## Using `http.server` in a function

The Python docs aren't very clear on this, and rather than think hard about it I did this fun hack:

```python
# cli.py
from pathlib import Path
from subprocess import check_call

def server(site: Path) -> None:
    check_call(['python', '-m', 'http.server', '8000', '-d', site])
```

## Autoreloading on filechanges

A bit more involved, and can certainly be improved. Here goes:

```python
# server.py
import functools
import http.server
import os
import socketserver
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def build_handler(directory: Path):
    """Specify the directory of SimpleHTTPRequestHandler"""
    return functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)


class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type in ["created", "modified"]:
            print(f"Reloading server due to file change: {event.src_path}")
            os._exit(0)


def run_server(directory: Path, port: int = 8000):
    with socketserver.TCPServer(("", port), build_handler(directory)) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()


def server(directory: Path, port: int = 8000):
    """Serve files in the watched directory"""
    # Watch the directory
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, site, recursive=True)
    observer.start()

    try:
        # Run the HTTP server
        run_server(directory=directory, port=port)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
```

Usage:

```python
# cli.py
from .server import server

def serve(site: Path, port: int = 8000):
    server(site="/path/to/directory/of/html", port=7500)
```