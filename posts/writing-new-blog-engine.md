---
date: "2018-03-29"
description: Where I describe why and how I wrote a new blog engine
slug: writing-new-blog-engine
tags:
  - python
  - django
  - flask
  - blog
time_to_read: 4
published: true
title: Writing A New Blog Engine
---

![Everest from Kalar Patar](/images/EverestfromKalarPatarcrop.JPG)

Since around February of 2012, I've been publishing this blog as a static HTML site using [Pelican](https://blog.getpelican.com/). The experience was pretty good, but over time I ran into a few problems with the fact that I never upgraded the site to match current versions of Pelican. Which meant the following:

- My RSS feed didn't follow the modern W3C RSS/Atom specifications. So I haven't been published in [Planet Python](https://https://planetpython.org/) in years.
- As time went by, upgrading to modern Pelican became harder and harder. And trying to get it to work wasn't much fun either.

So I started looking at other options. My requirements:

- All my old page links needed to work. I didn't want to have to cook up some kind of redirect system.
- I wanted to be able to make customizations without fighting through a complex extension system.
- Theming needed to be easy.
- Markdown needed to be supported. While I like RestructuredText, the honest truth is that I can pour out my thoughts faster with Markdown.

With those requirements in mind, I got started reviewing other tools. I tried a bunch of options (Hugo, Lektor, Pelican again, etc) but none of them met my requirements to the degree I wanted.

## Climbing the Moutain

Eventually, I decided the best course of action was to write my own blog engine with [Flask](https://palletsprojects.com/p/flask/) and host it on AWS Lambda via [Zappa](https://github.com/miserlou/zappa) with a JSON and Markdown backend. Using Flask and Zappa seemed like a good fit for me.

The reason is that while our core engine at work is always Django, we use Flask on AWS Lambda to power many microservices. For persistence we have DynamoDB/Redis or Django-powered APIs.

So one day this month I wrote up a blog engine that suited my requirements. I flung a theme on it and deployed it to AWS Lambda.

Hooray! Mission accomplished!

## Falling Off the Mountain

With pleasure, I asked friends to take a look at my new blog system. Immediately these friends started to tell me it was running slow.

You see, it turns out if you load a **huge JSON** file for each page load AND render markdown on the server side, your site is going to be slow. Even after numerous optimizations the pages still loaded in seconds.

## Climbing a Frozen Mountain

I thought about writing something to convert the JSON to native python objects. Or using an S3-located SQLite3 backend. But that felt like a lot of work to me and I wanted to get to writing.

That's when my awesome wife suggested I render the blog out as static HTML and just put that on S3. She said if I needed custom elements, that's what I could host those on AWS Lambda via Zappa and load them with Javascript.

Inspired by her idea, I installed [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) and a few minutes later I had a static version of my blog. I removed the pagination and was done.

## Inside the Mountain

My new blog is built and deployed with the following backend components:

- Python
- Flask
- Boto3
- Markdown2
- feedgen
- Django (because it has the best `truncatewords_html` tools)

The markdown files that make up the content have metadata stored as JSON. That makes it easy to read and parse, but I have considered switching to [TOML](https://en.m.wikipedia.org/wiki/TOML).

Looking out the window a few days ago I came up with a name for my blog engine: "Mountain".

## Why Flask? Why Not Django?

Because Flask is better at doing work that doesn't involve SQL. And I don't want a SQL-powered blog. I want something that lets me write in markdown using my text editor. Mountain lets me do precisely that.

## What's Next?

Here are some things I plan to do:

- Switch from Disqus-powered comments to GitHub issue powered ones.
- Take a look at switching the metadata from JSON to TOML.
- Write an AWS Lambda-powered search backend for the blog.

## Summary

The end result of this is you'll probably see me writing more blog entries in the days to come. Mountain works exactly how I want it. It has removed some of the hindrances that slowed me down.

In fact, this is my first blog post written in Markdown on the new blog. How cool is that?
