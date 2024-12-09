---
date: '2024-12-09T11:10:39.032418'
description: "What I use to improve my experience using the terminal"
published: true
tags:
- terminal
- tools
title: Favorite Terminal Tools
---

Links in the headers!

# [atuin](https://atuin.sh/)

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

# [tokei](https://github.com/XAMPPRocky/tokei)

Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language. 