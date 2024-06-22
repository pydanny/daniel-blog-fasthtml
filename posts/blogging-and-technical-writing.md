---
date: "2021-09-15"
published: true
slug: blogging-and-technical-writing
tags:
- blog
time_to_read: 4
title: Blogging and Technical Writing
description: Answers to questions I was asked recently about technical blog writing.
---

Here are answers to questions I was asked about technical blog writing.

# How do I set up my blog?

This site is built with React and Next.js. In May of this year (2021) I needed to learn these tools real fast so took the basic Next.js tutorial. I built enough foundations with those skills to build this site and the foundations of [Octopus Energy USA](https://octopusenergy.com) and [MHF's help-a-family site](https://helpafamily.margaritahumanitarian.org/). 

Individual articles are written in Markdown, are rendered into HTML, and then served out on a static site. 

From 2008-ish to 2012 I wrote on blogger using HTML in a WYSIWYG editor - unpleasant for a coder like myself. From 2012-2018 my site was in RestructuredText (on Pelican). After that, I've been in Markdown on three engines now. You can read a loose history of my blogging efforts [here](/tags/blog).

# What are the pros and cons of my blog?

Pros:

- Markdown is liberating as an author. For blogging, I just don't need all the features of RestructuredText. And WYSIWYG doesn't always work so well for code
- The clean design and high contrast is music to my eyes
- Creating my own platform gives me a place to hone my React and Next.js 
- Next.js feels like early Django. Everything works just right and nothing is too complicated. The ease of rendering some things in advance can't be understated - anyone who complains about heavyweight SPA sites is interacting with older SPA tech
- React's giant and stable ecosystem makes up for the fact that I rolled my blog engine 


Cons:

- My theme isn't based on a framework and I am not good at CSS. I may convert to a tailwind framework to make tuning the design easier
- Some of the code in the project is copy/pasta, serious DRF failures on my part. I should fix that one of these days

# How do I approach my writing?

These days I write notes to myself and to people I know. Sometimes it is to make a public point. Sometimes it is both.

For posts to myself, I write them because I need to be able to find the content again. The fastest way for me to find a note and avoid losing is to post it on my blog. This is about 80% of my blog.

For making public points, I am trying to convince the world of my arguments and beliefs. Here are several points I share often or other individuals share on my behalf:

- [The Thirty Minute Rule](/posts/thirty-minute-rule)
- [When to Use MongoDB with Django](/posts/when-to-use-mongodb-with-django)
- [Code, Code, Code](/posts/code-code-code)

My workflow is that I like to write it all out in one go. Working for days or weeks on a blog post just isn't my style. Those take a lot of work and in my experience typically have meager payoff in terms of benefit to myself or others compared to the work involved. That means my posts aren't too long.

My writing style is concise sentences and short paragraphs. Being an author has taught me the very useful habit of removing extraneous words. 

# Any tips?

- Use whatever platform makes it easiest for you to write
- Just because you write a lot about Python, JavaScript, Go, etc doesn't mean your blog has to be on Python, JavaScript, Go, etc. Stick with the platform that makes you happiest as a writer
- If you aren't confident of your writing ability, ask friends to review drafts
- Grammar and spelling are critical, especially for people building their careers or online presence. Use software to catch problems before (or even after) you publish