---
date: '2024-12-09T11:10:39.032418'
description: "A few incredible tools for making the terminal more useful and fun."
published: true
tags:
- terminal
- tools
title: Top Terminal Tools
---

Links in the headers!

# [Atuin](https://atuin.sh/)

The site explains perfectly what it does:

> "Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. With this context, Atuin gives you faster and better search of your shell history.
>
> Additionally, Atuin (optionally) syncs your shell history between all of your machines. Fully end-to-end encrypted, of course.
>
> You may use either the server I host, or host your own! Or just don’t use sync at all. As all history sync is encrypted, the host can't read your shell history."

Even for OSX users, I recommend installing [following these instructions](https://docs.atuin.sh/#quickstart).

# [bat](https://github.com/sharkdp/bat)

`bat` is a `cat` clone that supports syntax highlighting for a large number of programming and markup languages. Super handy for quickly reviewing a file. 

# [tmux](https://github.com/tmux/tmux)

tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.

For OSX users, ignore the site's instructions to use `port` and install it like this:

```sh
brew install tmux
```

## [Shell Sage](https://github.com/answerDotAI/shell_sage)

> "ShellSage saves sysadmins' sanity by solving shell script snafus super swiftly"
>
> -- Isaac Flath

Once you get past the tongue twister of an introduction you can enjoy this TMUX-powered AI tool. To help answer your questions Shell Sage uses your shell's context based on your current terminal state. For me this is really nice because I can't remember all the esoteric flags and quirks of the CLI world and for RSI reasons don't like to take my hands away from the keyboard.

The [Answer.AI blog entry](https://www.answer.ai/posts/2024-12-05-introducing-shell-sage.html) introducing Shell Sage is a nice dive into the history, philosophy, and usage of the tool.

# [tokei](https://github.com/XAMPPRocky/tokei)

Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language. 