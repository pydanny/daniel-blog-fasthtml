---
date: '2008-06-23T07:01:00.002-07:00'
description: ''
published: true
slug: 2008-06-ruby-security-problems
tags:
- ruby
- python
- legacy-blogger
time_to_read: 5
title: Ruby Security Problems
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/06/ruby-security-problems.html)*.

On the surface:

[https://www.ruby-lang.org/en/news/2008/06/20/arbitrary-code-execution-vulnerabilities/](https://www.ruby-lang.org/en/news/2008/06/20/arbitrary-code-execution-vulnerabilities/)

Digging deep:

[https://www.zedshaw.com/rants/the_big_ruby_vulnerabilities.html](https://www.zedshaw.com/rants/the_big_ruby_vulnerabilities.html)

In my world, Ruby is the dark side.  Tantalizing and yet there is a rock of stability about Python that I really enjoy, even if I can't define what I mean.  Maybe its the security to know that the language is deep as it is broad?

Anyway, at least for today I'm grateful I've stuck with Python.

---

## 6 comments captured from [original post](https://pydanny.blogspot.com/2008/06/ruby-security-problems.html) on Blogger

**Michael said on 2008-06-23**

I have taken a year-long detour into Ruby because of a company-wide decision to use Ruby-on-Rails after using Python for 2 years previously.  Some of Ruby is good most of it doesn't impress me.  I have continued my core work in Python and am getting excited for 2.6 and some of the changes.  For example, I just found out about the multiprocessing support today in https://jessenoller.com/2008/06/19/python-26-and-30-beta-1-released/.

Replacing threading with multiprocessing could be a big win for some of my apps.

**Michael said on 2008-06-23**

BTW, I can barely read any of Zed Shaw's writings because of his (over)use of profanity.  I just start reading it and ask myself, why does he need to be swearing here...and here...and here...and everywhere.  All that profanity is distracting and childish.

**pydanny said on 2008-06-23**

@michael: Could you post on your blog what you like and don't like about Ruby?

As for Zed Shaw, I have found in person that he doesn't get so obscene.  I agree that he loses readers with how he writes.

**Michael said on 2008-06-23**

@danny: Here's an old piece I wrote about how Ruby imports versus how Python imports:
https://backyardbamboo.blogspot.com/2007/12/rubys-require-is-lacking.html

The bottom line is that Ruby doesn't handle its namespaces nearly as elegantly as Python does, IMHO.

Also, I'm glad to hear that Zed represents better in real life because his online persona is out of control!  :-o

**Michael said on 2008-06-23**

@danny: sorry to clog up the comment area but I don't want to actually put this on my blog but I do like the way that Ruby handles blocks.  In Ruby, blocks are simply anonymous functions.  Methods can accept blocks by default.  It all gets pretty cool without being overly complicated.

On the downside, I don't like Ruby's syntax.  It reminds me of the bad old days of Perl with sigils everywhere.  Python is 100% cleaner to read and write.

**pydanny said on 2008-06-23**

@michael: Clog away.  It's on google's dime.

Python namespaces are nice. I think after reading your post I wonder how spoiled I am by what you can do via namespaces in Python and how I would react to the Ruby way.

I'm not sure about the block issue.  I've heard other Ruby folks talk about it, but I just don't grok it yet.

The Ruby syntax does turn me off.  I did Perl for 6 months in 1999 and loved regular expressions and hated the rest.

As for Zed, I met this great, pleasant guy at Pycon and talked to him for 30 minutes before we traded names.  Then I realized who I was talking to, and found it all just pretty funny.  Normally I don't like obscenity but after meeting him I'll give him a pass.

