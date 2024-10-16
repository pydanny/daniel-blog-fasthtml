---
date: "2024-10-15"
published: true
slug: mermaid-charts
tags:
  - python
  - fasthtml
  - javascript 
  - nodejs 
time_to_read: 1
title: Mermaid charts!
description: My site now has mermaid charts! Many thanks to Imtiaz Khan!
---

[MermaidJS](https://mermaid.js.org/) is a JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions to create and modify diagrams dynamically. I've been a fan of tools like it (which includes [Graphviz]()) for years. 

Many thanks to [Imtiaz Khan](https://github.com/ImtiazKhanDS) for [the contribution](https://github.com/pydanny/daniel-blog-fasthtml/issues/8). 

```mermaid
flowchart LR
    A[Idea] -->|Code| B(Deploy)
    B -->|Share| C[Enjoy]
```