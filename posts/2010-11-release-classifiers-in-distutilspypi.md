---
date: '2010-11-06T15:26:00.000-07:00'
description: ''
published: true
slug: 2010-11-release-classifiers-in-distutilspypi
tags:
- django
- plone
- python
- django packages
- zope
- legacy-blogger
time_to_read: 5
title: Release classifiers in distutils/pypi
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/11/release-classifiers-in-distutilspypi.html)*.

Thanks to [Doug Napoleone](https://dougma.com/) I'm now aware there is already a convention followed for the [python](https://python.org) and framework versions, but it appears that not enough people are aware of it. This post is pretty much a [reposting of the second comment of the post immediately preceding this one](https://www.blogger.com/comment.g?blogID=4477131926658044957&postID=7921310865600322429) and Doug gets full credit for this post. I'm just repeating his message:

The release classifiers in this post should be included in the standard distutils documentation. For the moment, you can see the full list of classifiers here:
[https://pypi.python.org/pypi?%3Aaction=list_classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers)

For the python language version the classifier is:

<blockquote>Programming Language :: Python :: x.y.z</blockquote>
With each version on it's own line. That way you can browse the repository by python version (see the bottom of the page):

[https://pypi.python.org/pypi?:action=browse&c=214](https://pypi.python.org/pypi?:action=browse&c=214)

There is also support for frameworks which you can see on that page as well. There it is done with:

<blockquote>Framework :: Django :: x.y.z</blockquote>
There is Zope, Plone, and a number of other frameworks already there.

In the example you gave the proper, and supported way of writing the metadata is:

<blockquote>Programming Language :: Python
Programming Language :: Python :: 2.4
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Framework :: Django
Framework :: Django :: 0.96
Framework :: Django :: 1.0
Framework :: Django :: 1.1
Framework :: Django :: 1.2.1
Framework :: Django :: 1.3</blockquote>
Now it becomes a matter of education and illumination. This should be in the standard distutils documentation and arguably the home page of PyPI (or easily found there). And [Django Packages](https://djangopackages.com) will be supporting this functionality in the near future.

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2010/11/release-classifiers-in-distutilspypi.html) on Blogger

**Alexis Metaireau said on 2010-11-06**

I can't see the classifiers about Django versions here: https://pypi.python.org/pypi?%3Aaction=list_classifiers.

Am I missing something ?

**pydanny said on 2010-11-06**

@Alexis - You are right, they aren't there. Can you make up your own classifications with this list or are we stuck with what classifiers are provided in the formal PyPI list?

**Doug Napoleone said on 2010-11-07**

I was going to post a followup stating that I was wrong about the framework version, but then life got in the way. then I noticed this post and realized I had better, but someone else had beaten me to it. The internets: the fastest way to make me feel like a fool ;-)

I am sure the PyPi folks will have no problems adding framework version classifiers.

**Alexis Metaireau said on 2010-11-07**

@Danny

I think the best thing is to use the existing classifiers, otherwise it will be useless, for now at least.

It's possible to ask about that on the catalog-sig mailing list, BTW (adding new classifiers), but I'm not sure it's good to support each different version os each frameworks this way, it will be hell for the classifiers maintainers.

