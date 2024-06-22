---
date: '2011-12-16T11:57:00.000-08:00'
description: ''
published: true
slug: 2011-12-announcing-consumer-notebook
tags:
- opencomparison
- consumernotebook
- django
- djangodash
- python
- legacy-blogger
time_to_read: 5
title: Announcing Consumer Notebook!
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/12/announcing-consumer-notebook.html)*.

Need a [Python programming language](https://python.org/) book? Want to see a comparison of the ones I own and use? Check out my [Must-Have Python Programming Books ](https://consumernotebook.com/grids/pydanny/must-have-python-programming-books/) comparison grid. 

<div class="separator" style="clear: both; text-align: center;"><a href="https://consumernotebook.com/grids/pydanny/must-have-python-programming-books/"><img border="0" height="123" src="https://1.bp.blogspot.com/-opvIYk7fbOc/TuuX4ohbUCI/AAAAAAAABBU/z52xqc4zSrQ/s200/Screen+shot+2011-12-16+at+11.09.28+AM.png" width="200" /></a></div>
Let's drill down and take a closer look at one of the items on the page, in this case [Doug Hellmann](https://www.doughellmann.com/)'s amazing [The Python Standard Library by Example](https://consumernotebook.com/the-python-standard-library-by-example-developers-library/4f03f0db73c4e2000b00008f/). The product detail pages include the ability to add pros and cons and attach said products to comparison grids and specialized lists like 'my wishlist' and 'my possessions'.

Speaking of wishlists, [check out my own](https://consumernotebook.com/lists/pydanny/wishlist/):

<div class="separator" style="clear: both; text-align: center;"><a href="https://consumernotebook.com/lists/pydanny/wishlist/"><img border="0" height="211" src="https://4.bp.blogspot.com/-N4Y6vZPX85s/TuuX-Y34NjI/AAAAAAAABBc/AgqXee08HSM/s320/Screen+shot+2011-12-16+at+11.10.18+AM.png" width="320" /></a></div>
In order to add items, like&nbsp;[footy pajamas](https://consumernotebook.com/pajamacity-ninja-monkey-polar-fleece-feetie-pajamas-for-teens-and-adults-size-6-58-to-59/4f03f0f673c4e2000a00009d/),&nbsp;&nbsp;I click on the 'add' button and paste the Amazon (or BestBuy) URL into the form:

<div class="separator" style="clear: both; text-align: center;"><a href="https://1.bp.blogspot.com/-_5gFPrlJNbA/TuuY_hnZElI/AAAAAAAABB0/UgKbJoFjLD8/s1600/Screen+shot+2011-12-16+at+11.14.18+AM.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="185" src="https://1.bp.blogspot.com/-_5gFPrlJNbA/TuuY_hnZElI/AAAAAAAABB0/UgKbJoFjLD8/s200/Screen+shot+2011-12-16+at+11.14.18+AM.png" width="200" /></a></div><div class="separator" style="clear: both; text-align: center;"><a href="https://1.bp.blogspot.com/-J72QEuoMOVg/TuuY8RBLiiI/AAAAAAAABBs/YSW3ds8OD-o/s1600/Screen+shot+2011-12-16+at+11.14.50+AM.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="146" src="https://1.bp.blogspot.com/-J72QEuoMOVg/TuuY8RBLiiI/AAAAAAAABBs/YSW3ds8OD-o/s200/Screen+shot+2011-12-16+at+11.14.50+AM.png" width="200" /></a></div>

At this time we just handle Amazon USA and BestBuy USA. In the future we plan on adding more affiliate providers, including non-USA providers to support our non-USA friends.

<h3>There's a lot more than that...</h3>In addition to [weekly infographics](https://consumernotebook.com/blog/2011/dec/we-love-infographics/), comparison grids, lists, and products, Consumer Notebook also awards points, coins,  badges, and a growing privilege set to participating users. We even implemented an energy bar which regenerates over time, designed to match the pace of human users and serve as one of the brakes on scripts and bots. 

<div class="separator" style="clear: both; text-align: center;"><a href="https://consumernotebook.com/profiles/pydanny/"><img border="0" height="200" src="https://1.bp.blogspot.com/-Bj2ykQAhb3c/TuuZfjoCWzI/AAAAAAAABB8/diG3lEqUTwk/s200/Screen+shot+2011-12-16+at+11.18.00+AM.png" width="156" /></a></div>
<h3>Technology</h3>I built this with [Audrey Roy](https://twitter.com/audreyr) using Python, [Django](https://djangoproject.com/), [JQuery](https://jquery.com/), [PostGreSQL](https://www.postgresql.org/), [Memcached](https://www.memcached.org/), and [RabbitMQ](https://www.rabbitmq.com/). I'll be blogging in depth about the technical side in an upcoming post.

<h3>Genesis</h3>
It was the summer of 2010 and we were brainstorming ideas for a coding contest called Django Dash. The one we settled on was a listing and comparison site for Django called [Django Packages](https://djangopackages.com/). The result has been a very useful tool for the Django community. Eventually, with the help of several dozen people, we turned the code into the [Open Comparison](https://opencomparison.org/) framework and launched [Pyramid](https://pyramid.opencomparison.org/) and [Plone](https://plone.opencomparison.org/) implementations. Time permitting this year, we plan to do Python, Flask, Twisted, Node, JQuery, and other implementations.

Since then we've wanted to do something similar, but in the context of products. And we wanted to do it right - elegant design combined with an ad-free space. So we cooked up Consumer Notebook, launching today!

We'll be adding features and enhancements in the months to come. We've acquired a [community manager](https://twitter.com/toastythedog), and even have a [blog](https://consumernotebook.com/blog/). We would love for you to [check out the site](https://consumernotebook.com/), share it with your friends and family, and send us your commentary, suggestions, and advice.

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2011/12/announcing-consumer-notebook.html) on Blogger

**pydanny said on 2011-12-19**

Hi Jenny,

We plan to support Google and other OAUTH providers in the future. OAUTH makes it so we aren't having to store peoples hashed passwords. 

As for implementing our own user/password system, that's something we'll consider in the future.

