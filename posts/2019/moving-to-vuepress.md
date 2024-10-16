---
date: "2019-10-14"
description: Why and how I'm moving my blog to vuepress.
published: true
slug: moving-to-vuepress
tags:
  - javascript
  - blog
  - Vue.js
time_to_read: 5
title: Moving to Vuepress
type: post
---

[In 2018 I wrote my own blog engine](/writing-new-blog-engine) and it's time to move off.

# Tooling is fun until it isn't

I like writing code and thought this was going to be a fun, easy project. How hard is it to write a blog engine anyway?

The truth is I would rather be writing or coding new things then building and maintaining something that's been done thousands of times by other people. Yes, the foundation of a blog isn't hard, but the challenge is in the details. Here are some bits of grief I encountered:

- [Falling off the mountain](/writing-new-blog-engine.html#falling-off-the-mountain)
- [Climbing a frozen mountain](/writing-new-blog-engine.html#climbing-a-frozen-mountain)

Yes, [Frozen-flask](https://pythonhosted.org/Frozen-Flask/) allowed me to turn my site into a static site. However, **the compilation time took over 5 minutes**. While I ran my site locally on localhost, testing out additional features to see how they rendered in the final build took too long. For example, my plans to optimize page/image loads and add search came to a screeching halt.

The end result was that for all my fun in writing the Mountain blog engine for myself, I felt uncomfortable with the results. Every time I visited my blog to write I would see the problems in the current system, try to fix them, then step away.

It's been time to migrate my blog for a while.

## Choosing a new blog engine

A few months ago I wrote up these requirements:

- Must be a static site because [Jamstack](https://jamstack.org/) rocks.
- If not using .html extension, must easily redirect from .html to as not to annoy old readers. [Netlify's redirects](https://www.netlify.com/docs/redirects/) are perfect for this kind of thing.
- Search needs to be a thing.
- Powered by [VueJS](https://vuejs.org/) because it's my favorite frontend framework.

So when I saw that my coworker, [Amanda Quint](https://www.amandaquint.com) had started a Vuepress blog I decided to give it a try. Setup was easy, but as always the challenge was in the details.

## Migration challenges

My current blog is over 7 years old and has over 130 articles. I ran into a number of problems with converting from a forgiving blog engine I wrote to something designed to prevent you from having missing content. There was also coming up with a theme.

Fortunately for me, my co-worker and friend [Ahmad Mostafa](https://www.ahmadmostafa.com/) helped me out. Together we converted my blog over. He did a ton of work on my blog conversion and for that I am very thankful. I look forward to collaborating with him in the future.

## Moving back to GitHub

Yes, I'm hosting my blog repo on [GitHub](https://github.com/pydanny/pydanny-v2/) again. While I've been a user of GitLab for many years, and vastly prefer it for private projects, GitHub is where most the open source communities I'm involved in lives. Time to come back.

## Going forward

We'll be making changes in the days to come. Some things we'll be doing:

1. Add page transitions like what [Amanda](https://www.amandaquint.com) has on her blog.
2. Increase the accessibility of the design.
3. Change the front page hero panel in some way.
4. Write more articles!
