---
date: '2011-02-14T09:38:00.000-08:00'
description: ''
published: true
slug: 2011-02-my-pinax-solutions-class-at-pycon-2011
tags:
- pycon
- django
- python
- pinax
- legacy-blogger
time_to_read: 5
title: My Pinax Solutions class at Pycon 2011
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/02/my-pinax-solutions-class-at-pycon-2011.html)*.

Heavily inspired by [Zed Shaw's Learn Python the Hard Way](https://sheddingbikes.com/posts/1295120282.html) class I'm changing the lecture style format of the [Pinax Solutions class](https://us.pycon.org/2011/schedule/presentations/111/) at&nbsp;[PyCon 2011](https://us.pycon.org/2011) to a more workshop-oriented format.

Which means that the first half of the class we (myself and the [peerless](https://us.pycon.org/2011/speaker/profile/143/) [Brian](https://brianrosner.com/) [Rosner](https://github.com/brosner)) will spend on material critical for people new to [Pinax](https://pinaxproject.com/)&nbsp;or old hands who want to see what 0.9 offers. That means setting things up via virtualenv and pip, Pinax specific settings, media handling, template layout, extending core Pinax apps, use of [idios to change profiles](https://github.com/eldarion/idios), openid/openauth, [Django Packages](https://djangopackages.com/) to find Pinax approved stuff and more. That will be the foundation and our slides/handouts will be useful as cheat sheets for these critical parts in any [Django](https://djangoproject.com/) application.

The second half of the&nbsp;class&nbsp;will be a workshop. We'll spend the next half helping people with their personal projects, and will even have a few stock projects we can toss at people that either already are open source or could be released as open source.&nbsp;We won't write your project for you, but we will provide advice, guidance, and some elbow grease in getting things to work.&nbsp;If someone asks for something that we think the rest of the class could benefit from, we'll show them how to do it on the projector and then everyone benefits.

After the class, I'm free the rest of the day so I'll continue helping people even after the tutorial is officially over. Thursday (March 10th, 2011) after lunch I'll be also available to provide aid and support. &nbsp;Anyone else can join but those who attended the Pinax Solutions tutorial will get precedence.

During the [main body of the conference](https://us.pycon.org/2011/schedule/lists/talks/) I'll be attending talks and giving a [couple](https://us.pycon.org/2011/schedule/presentations/56/) [myself](https://us.pycon.org/2011/schedule/presentations/72/)&nbsp;so my time to provide aid will likely be completely curtailed.

I will be there at the [sprints](https://us.pycon.org/2011/sprints/) working on various [Pinax](https://github.com/djangopackages/djangopackages) [and](https://github.com/pydanny/django-uni-form) [Django](https://github.com/pydanny/django-la-facebook) [projects](https://github.com/pydanny/django-tagging-ext).

If time permits we'll go over deployment, but I recommend [Jacob Kaplan-Moss' Python/Django Deployment Workshop](https://us.pycon.org/2011/schedule/presentations/173/) if you want a full treatment of the subject.

Note I: If you've already signed up for the Pinax Solutions tutorial, you should be getting an email from the PyCon tutorial staff shortly.

Note II: If you are new to [Python](https://python.org/), I recommend that you take any of the [basic](https://us.pycon.org/2011/schedule/presentations/108/) [Python](https://us.pycon.org/2011/schedule/presentations/99/) [tutorials](https://us.pycon.org/2011/schedule/presentations/117/) at PyCon instead of this class.

---

## 6 comments captured from [original post](https://pydanny.blogspot.com/2011/02/my-pinax-solutions-class-at-pycon-2011.html) on Blogger

**Aza said on 2011-02-15**

Thanks very much guys for providing us with something like Pinax. 
On the UI side Pinax seems to focus more on jQuery than Dojo (even though we have dojango - which is a great start). 

Is there a particular reason for this? 
I prefer Dojo, mainly because of it's syntax and structure.

Thanks

**pydanny said on 2011-02-15**

@Aza,

We choose JQuery in the heady days of Pinax 0.5a because it was a requirement for Django Uni-Form - which was necessary for the 508ification of Pinax. Also, JQuery is more ubiquitous than Dojo so we could count on easier adoption. In fact, in the 2 years since we choose JQuery you are only the second person I'm aware to wonder why we choose JQuery in particular. ;)

**Aza said on 2011-02-16**

Wow :-) I'm really suprised by that stat. Guess jQuery is doing much better than I thought. 

I'll just swallow the bitter pill and roll with jQuery then. 
But for me (w.r.t. syntax and structure):
web2py &lt;--&gt; jQuery
Django &lt;--&gt; Dojo
So I thought, for the same reason we prefer Django over web2py, we would prefer Dojo over jQuery.
Do you at least see my line of thinking though?

**pydanny said on 2011-02-16**

@aza - what a unique statement about JQuery vs Dojo. Can you clarify your position?

**PD said on 2011-02-18**

Hi Danny,

I've signed up for this tutorial, but I am new to Python and Django. I've signed up for the &quot;Learn Python the hard way' tutorial as well... but I believe this tutorial will be before that one! 
We're using Pinax on our website, and that is why I signed up for  this. I'm planning to try and get as much as I can out of the online tutorials... but I'm slightly worried now- do you think I will be able to cope with this tutorial?

Thanks,
Pradnya

**pydanny said on 2011-02-18**

Hi Pradnya,

If you go through the entire Django tutorial then you should be good for taking the Pinax Solutions class. 

Take lots of notes on the things you don't understand. After you take Zed's class a lot of things will make more sense.

See you in a few weeks!

