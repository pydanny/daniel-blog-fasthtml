---
date: "2021-05-23"
tags:
  - blog
  - nextjs
  - react
  - vercel
  - TIL
published: true
title: Blog Revamp 2021
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

Today my wife Audrey and I dug in and learned some of the tools chosen by the [Octopus Energy](https://octopusenergy.com) frontend team. One of our efforts turned into redoing this blog.

## Tools

Here's my quick review of the tools we learned

### React

React has really, really improved in the past six years. When it first launched I tried it out and disliked it. Eventually I embraced VueJS. The tooling and docs for React have really improved, the need for tribal knowledge is gone (a similar problem existed for Django until we wrote Two Scoops of Django).

### Next.js

[Next.js](https://nextjs.org/) is lovely. I’m 100% sold now. Before I just planned to go along with the flow, but now I’m a total Next JS convert. Everything about is elegant, doing just enough to be useful but not so much that it gets in the way.

### Vercel

[Vercel](https://vercel.com/) is decent, certainly a lot better than pushing to S3 then bouncing cloudfront! For what it's worth, I’ve used Netlify since near it's launch and can make it do amazing tricks. Plus the [Netlify's new collaborative deploy previews](https://www.netlify.com/blog/2021/05/19/next-generation-deploy-previews-plus-netlify-acquires-featurepeek/) are out of this world. However, the challenge with Netlify is that its documentation of critical components such as `netlify.toml` and environment variable precedence could use improvement. In comparison, [Vercel’s documentation is really good](https://vercel.com/docs). While I can’t do everything in Vercel that I can do with Netlify (yet) , the docs alone justify using it.

### Summary of Tools

It was so much fun to learn these tools, especially NextJS. They were relatively easy for us (my wife Audrey paired with me). They abstract away the nasty stuff (routing, webpack, deployment) yet give us low level access to the things we need. That makes them pleasant to use, and in my opinion enjoyment of tools is a critical feature.

## FAQ

### What about tags?

A number of my books and articles link to content tags. I'll have them up later this week.

### What about comments?

I've had Disqus on this blog for about 9 years. It's been the biggest slowdown for years, making dozens or hundreds of external calls. Also, I never liked that I didn't own the text on my own system.

Besides, I already get pinged enough in social media and email. I don't need another distraction.

### What about pydanny.com?

Yeah, you might be forwarded here from that domain. The thing is, much as I love coding in Python, I've learned to enjoy other languages. Golang, modern JS, Kotlin, even C# in Unity are things I've really gotten into. By moving off the old domain I feel more free to do other things.
