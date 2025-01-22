---
date: '2025-01-22T10:00:33.783460'
description: "How I install L\xD6VE, a 2d gamework written in C++ that uses Lua as its\
  \ scripting language. Nothing against GODOT or Unity, but I want a tool where I\
  \ don't need a specialized IDE to build games for my little girl."
published: true
tags:
- lua
- love2d
- howto
- MacOS
title: "Installing L\xD6VE on Mac"
---

The line instructions in this post are for Mac. If you aren't on Mac, instructions for getting started can be found [here](https://love2d.org/wiki/Getting_Started).

## Using homebrew to install the binary

```sh
brew install --cask love
```

Confirm that it runs

```sh
love --version
```

Depending on your Mac configuration you might get a popup saying that `love` is from an unverified developer. If this happens:

1. Go to `System Settings`, then click `Privacy & Security`
2. Scroll down to '"love" was block from use because it is not from an identified developer' and click the `Open Anyway` button
3. Follow the dialogues, which probably includes a password check

## Hello, World

Create a directory and in it add a `main.lua` file with the following code:

```lua
function love.draw()
    love.graphics.print("Hello, World", 400, 300)
end
```

Open a terminal and type:

```sh
cd /path/to/directory
love .
```
