---
date: '2024-11-21T15:12:54.669148'
description: How to get the last element in a shell command.
image: /public/logos/til-1.png
published: true
tags:
- TIL
title: 'TIL: Last Token in Shell'
twitter_image: /public/logos/til-1.png
---

To get the last element in a shell command, do this:

```sh
> !$
```

To demonstrate usage, let's do a directory list on this website's posts directory:

```sh
> ls -l posts
```

I can get the last token, which is `posts`, by typing:

```sh
> !$
posts
zsh: command not found: posts
```

The shell will try to run that token, which as you can see often fails. What's awesome about that is it is now in the shell history, meaning I can easily compose new commands by using the shell history. As I use the rocket-powered [Atuin](https://atuin.sh/) shell history tool, this means I now have that token easily found at my command line forever. Here's atuin in action - on the line with GLOBAL I've typed in the word 'posts':

```sh
 │ 4 3ms    6d ago mv posts/til-*.md posts/til/
 │ 3 18ms   2d ago git add posts/                                                                                  │
 │ 2 6ms   10m ago ls -l posts                                                                                     │
 │ 1 2ms   10m ago posts                                                                                           │
 │ > 2ms    9m ago ls -asl posts                                                                                   │
 │─────────────────────────────────────────────────────────────────────────────────────────────────────────────────│
 │[    GLOBAL    ] posts 
 ```

Using Atuin, I can fetch the last token to my shell without running it, which is a superpower. I can now compose all kinds of stuff off the saved token. Yeah!

Attribution for this command goes to Jeremy Howard.