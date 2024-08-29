---
date: "2008-05-19T13:22:00.003-07:00"
description: ""
published: true
slug: 2008-05-i-love-graphing
tags:
  - python
  - graphviz
  - legacy-blogger
time_to_read: 5
title: I love graphing
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/05/i-love-graphing.html)_.

I don't mean charting (pie, bar, line, etc). I mean drawing edges and nodes and showing relations between objects of all sorts. That means between data objects, code objects, people, companies, and so much more. Its lots of fun and writing clean, extensible code to do it is a blast for me.

Mostly I work in [graphviz](https://graphviz.org/) using Python. I played with [PyDot](https://code.google.com/p/pydot/) for a while but wasn't happy with it so I tend to write some base code to handle things in a way that ended up being duplicated by the [GvGen](https://software.inl.fr/trac/wiki/GvGen) project. Which is very nicely done.

However, there are limits to graphviz. Graphviz doesn't do animation or make 3-d images are two big items. However, its nice and light as a renderer which is very important especially for generating content for the web on the fly. Nevertheless I've done wonderful things like mapping out relations between 150 applications or reverse engineering ZODB content into UML.

So imagine my delight when I found Ubigraph (defunct in 2022) this morning. It does 3-d graphs and animates things. I don't think it will replace Graphviz because it does different things. I haven't played with it yet but I will.
