---
date: '2025-02-07T01:00:20.254354'
description: A more elegant way to display default help.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Typer commands defaulting to help'
twitter_image: /public/logos/til-1.png
---

If you save this code to `cli.py`: 

```python
import typer

app = typer.Typer()

@app.command()
def create():
    """Creates a user"""
    typer.echoint("Creating user")

@app.command()
def delete():
    """Deletes a user"""
    typer.echo("Deleting user")

if __name__ == "__main__":
    app()
```

and run it you get:

```plaintext
$ python cli.py
Usage: cli.py [OPTIONS] COMMAND [ARGS]...
Try 'cli.py --help' for help.
╭─ Error ────────────╮
│ Missing command.   │
╰────────────────────╯
```

That's not bad, but it forces you to request help before doing anything. Here's how it can be made so much better through the `@app.callback` command. See below:


```python
import typer

app = typer.Typer()

# Setup the helper default
@app.callback(invoke_without_command=True)
def helper(ctx: typer.Context):
    """
    Awesome CLI app
    """
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())

@app.command()
def create():
    """Creates a user"""
    typer.echoint("Creating user")

@app.command()
def delete():
    """Deletes a user"""
    typer.echo("Deleting user")

if __name__ == "__main__":
    app()
```

Now we get something as a default that really shows off the charm of `typer`:

```plaintext
 $ python cli.py

 Usage: cli.py [OPTIONS] COMMAND [ARGS]...

 Awesome CLI app

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                       │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.│
│ --help                        Show this message and exit.                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────╮
│ create   Creates a user │
│ delete   Deletes a user │
╰─────────────────────────╯
```