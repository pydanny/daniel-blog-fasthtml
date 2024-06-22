---
date: '2009-11-11T18:15:00.002-08:00'
description: ''
published: true
slug: 2009-11-picking-django-powered-cms
tags:
- november
- django
- review
- blog
- legacy-blogger
time_to_read: 5
title: Picking a Django powered CMS
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/11/picking-django-powered-cms.html)*.

<h3>Note as of October 2011</h3>
The CMS options have changed greatly since I wrote this blog post in 2009. I might write a more current post. In the meantime, instead of FeinCMS, use [Django CMS](https://django-cms.org/), [Mezzanine](https://mezzanine.jupo.org/), or use the [CMS grid on Django Packages](https://djangopackages.com/grids/g/cms/) to make your own decision.

<h3>Back to the old blog post...</h3>
A few months ago I asked the community to help us ([NASA SMD](https://nasascience.nasa.gov/)) [pick a Django powered CMS](https://pydanny.blogspot.com/2009/09/show-me-your-open-source-django-cms.html).

The response of the community was awesome. We were provided a decent sized list of CMS candidates to evaluate. We got a lot of responses, both in comments on my blog, twitter messages, and even direct emails. We compiled the list and got to work.

Now it was time for evaluation. As much as I wanted to do it myself, this was given to the capable hands of my co-worker, [Chris Adams](https://improbable.org/chris/). I was a bit jealous because I like to explore, but that's how it worked out.

First Chris used a process of elimination to weed out the ones that were unusable based on my published requirements:


-  Was it actually open source?

-  Was it 508 compliant or easy to make so?
-  Runs on PostGreSQL and MySQL?
-  Is there an active community?

That narrowed things down a bit. Now Chris added some more filters:


-  Could you show pages nested inside of pages? In order words, could you rely on Tree Traversal for display of content?
-  Was there documentation? In English?

That reduced things to an even smaller list. Chris took the revised list of candidates, downloaded the code, and started them up. During this process he removed candidates that required patching to get working at the most basic level. He also looked at the code and made a few judgments there as well.

Day by day it was a sad to see the list get smaller and smaller. Each project was the labor of many hours by talented people who cared about their work. Yet Chris had a job to do, and while he didn't drop candidates easily, he did drop them.

Chris now added our sample content to each surviving candidate and invited the rest of the team to look at the code and the results. It was now up to our subjective evaluation. Two finalists stood out as winners, [FeinCMS](https://spinlock.ch/pub/feincms/html/) and [Django CMS 2](https://www.django-cms.org/en/). They were so close that one might consider the results to be a tie. Both met all our needs, their code bases smelled pretty nice, documentation felt complete, code had test coverage, and the community active. They even shared a lot of the same dependencies!

The call was very close but in the end we picked FeinCMS.

Django CMS 2 was a very, very close second. I cannot say that enough.

In a few months we'll announce the front facing site we are building. We'll contribute the work we can to the open source community, which will either be work done on FeinCMS or stand alone applications.

Finally, I want to make clear the amount of effort and clarity of work Chris Adams put into these evaluations. He did the hard work and he did it well.

20 more posts to go!

---

## 15 comments captured from [original post](https://pydanny.blogspot.com/2009/11/picking-django-powered-cms.html) on Blogger

**david said on 2009-11-11**

Can you or Chris go into more details about why FeinCMS was chosen over others?

**Unknown said on 2009-11-11**

So ... what was the tiebreaker?! A coin toss?

**Davide Callegari said on 2009-11-12**

I choose FeinCMS too for my last project. Good choice!

**Unknown said on 2009-11-12**

Yes, I'd love to hear your reasons as well. I have been using django-cms for the last 6 months and would love to know if there is a better option out there.

**pydanny said on 2009-11-12**

@david, @bengdell:

FeinCms and Django-CMS were prime choices because they...

 * Was actually open source
 * Was 508 compliant and easy-to-fix
 * Ran on all databases we wanted
 * Had active communities
 * Demonstrated use of Tree Traversal, actually both using Django-MPTT
 * Had competently written English documentation
 * Worked out of the box
 * Code smelled nice
 * Had good test coverage

You do realize that is in the blog entry, right?

As for FeinCMS vs Django CMS, it pretty much came down to just having to pick a winner. The weaknesses either had were encapsulated in tickets and were being actively worked on.

**Unknown said on 2009-11-12**

Hi Danny, I could see how you ended up with django-cms and feincms, what i thought would be useful to know was what feincms did (or impressed you with) that django-cms did not. 

As mentioned, I use django-cms and so am interested to hear any reasons why I should give feincms a chance, OVER django-cms.

excellent blog post though.

**Unknown said on 2009-11-15**

Hi,

Have you evaluated :

https://code.google.com/p/django-page-cms/

If yes? What was the issue with it?

**Chris Adams said on 2009-11-15**

@faden: One issue was our desire to mix different types of content - the reorderable blocks model solves a number of problems which we need to address.

@david, @bengdell: The main thing I ran into were a few cases where it seemed harder to work with django-cms than FeinCMS - not intractable but it felt more natural for my needs. I think django-cms 2.0 is moving in the right direction and I certainly wouldn't say you're wrong to use it - I think the big thing about CMSes is avoiding the one-size-fits-all mindset that field is infected with. I like the FeinCMS goal of being a framework rather than a massively configurable application but there are plenty of cases where the reverse is preferable.

**Touareg said on 2009-12-27**

I gave Django CMS a chance like three times.

The first one ended up in a bug report. After a while I tried it for the second time and making it to work wasn't a trivial task so eventually I gave up again (south migrations didn't work, had to turn them off, mysterious exceptions, etc).

The last time was a few days ago - again, weird exceptions using python 2.6 (if I remember correctly, when I tried Django CMS for the first it, I had an opposite issue - incompatibility with python 2.4).

Django CMS is developing fast, but it's too unstable and I can't wait any longer, so I choose FeinCMS.

**loon said on 2010-03-31**

Both CMS are good ones. 
Both have issues with multiple menus.
Django-CMS is more easy to use as a developer.
FeinCMS is like said before more a CMS-Framework than configurable app. It makes use of the well known register methods to hook the parts of the framework together.
Django-CMS is configurable und extensible through plugins.
FeinCMS is a set of &quot;extensions&quot; wich has to be glued together by you (register functions). Therefore it is much more extensive but has a little steeper learning curve.
I choosed FineCMS.

**Baylink said on 2010-09-29**

So, a year later, how did it work out, and what the site?  I'm doing this d-tree myself now, and the extra input would be useful...

**pydanny said on 2010-09-29**

@baylink,

The site launched and is doing well: https://science.nasa.gov/

As for comparing CMS, I do that now via https://www.djangopackages.com/grids/g/cms/

**Baylink said on 2010-09-30**

And so far, that is the *only* NASA site I've used that doesn't come apart when I Ctrl-+ the text up 5 notches, as is my wont.  *Very* nice.  Compliments to your CSS jockey, or the CMS, or both.

Thanks for the followup, and I'll check the matrix.  WebGUI has just grown beyond all reason...

One question: why no &quot;Powered By&quot; anywhere; NASA prohibit this?  That would seem to fall in Bob Jacobs' lap, and he seems like a reasonable guy...

**Baylink said on 2010-09-30**

I don't, though, see any way to get from 

https://www.djangopackages.com/packages/p/django-cms/

to the package's home page; is that a bug, a feech, or am I blind?

**pydanny said on 2010-09-30**

@Baylink - AFAIK, the decision to not have 'Powered By' was made at a higher level than us mere implementers.

As for packages, it was a conscious decision that they don't list home pages for projects, just links to their repo and pypi pages. It helps keep the closed source stuff out of Django Packages.

