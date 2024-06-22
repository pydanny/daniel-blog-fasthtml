---
date: '2010-11-06T12:34:00.000-07:00'
description: ''
published: true
slug: 2010-11-request-for-new-pypi-classifiers
tags:
- django
- plone
- python
- django packages
- zope
- legacy-blogger
time_to_read: 5
title: A request for new pypi classifiers
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/11/request-for-new-pypi-classifiers.html)*.

This request is to help enhance [Django Packages](https://djangopackages.com/), [PyPM Index](https://code.activestate.com/pypm/), and other projects. This would also help the Python community at large.

Would it be possible that a standard be established for listing in [PyPI](https://pypi.python.org/pypi) [classifiers](https://docs.python.org/distutils/setupscript.html#additional-meta-data) which versions of a package is known to operate? Using [James Bennett](https://b-list.org/)'s django-registration at [https://pypi.python.org/pypi/django-registration](https://pypi.python.org/pypi/django-registration) as an example (see my bolded, last two lines to understand what I'm trying to demonstrate):
<blockquote>Development Status :: 5 - Production/Stable
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Utilities
<b>Python Versions :: 2.4, 2.5, 2.6, 2.7
Django Versions :: 0.96, 1.0, 1.1, 1.2.1, 1.3</b></blockquote>The metadata system I'm writing about in this blog post is [specified on the distutils documentation page](https://docs.python.org/distutils/setupscript.html#additional-meta-data).

I picked a Django package but this could be for Zope, Pyramid, PyQT, or anything.

If we had something like this in place then people could quickly identify on PyPI and other resources if a tool can be of use to&nbsp;them or if it needs to be updated to the latest code base. If this already exists, then can someone point me at the existing specification so I can promote it?

<b>Edit: </b>[Noah Kantrowitz](https://coderanger.net/) suggested I take a look at the 'requires' keyword which is part of the distutils spec. However, this does not show up in the PyPI API ([https://wiki.python.org/moin/PyPiXmlRpc](https://wiki.python.org/moin/PyPiXmlRpc)) and so doesn't fit our needs.

---

## 7 comments captured from [original post](https://pydanny.blogspot.com/2010/11/request-for-new-pypi-classifiers.html) on Blogger

**Richard Jones said on 2010-11-06**

It's quite easy to enhance the XML-RPC interface.

**Doug Napoleone said on 2010-11-06**

I am very glad you brought up this topic. There is already a convention followed for the python and framework versions, but it appears that not enough people are aware of it. It should be included in the standard distutils documentation.

You can see the full list of classifiers here:
https://pypi.python.org/pypi?%3Aaction=list_classifiers


For the python language version the classifier is:

Programming Language :: Python :: 

With each version on it's own line. That way you can browse the repository by python version (see the bottom of the page):

https://pypi.python.org/pypi?:action=browse&amp;c=214

There is also support for frameworks which you can see on that page as well. There it is done with:

Framework :: Django :: 

There is Zope, Plone, and a number of other frameworks already there.

In the example you gave the proper, and supported way of writing the metadata is:

Programming Language :: Python
Programming Language :: Python :: 2.4
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Framework :: Django
Framework :: Django :: 0.96
Framework :: Django :: 1.0
Framework :: Django :: 1.1
Framework :: Django :: 1.2.1
Framework :: Django :: 1.3


People should already be following this convention, and it should be advertised more.

**pydanny said on 2010-11-06**

@Richard, I would love to see the XML-RPC interface for PyPI enhanced! However, as @Doug pointed out, the information is there already in the classifiers.

The question then becomes does it make sense to have PyPI slurp information out of the classifiers that are already returned by the XML-RPC API? If so, I'm happy to tes the results via Django Packages and another project I'm on.

Another issue to be raised is educating the Python audience at large about classifiers.

**Richard Jones said on 2010-11-06**

Generally speaking if there's a need for something in PyPI it can be done. We (Martin von Löwis and myself) just need to be aware of it. Which we usually aren't, for some reason. And people write HTML scapers instead.

**Alexis Metaireau said on 2010-11-06**

Hi, 

The classifiers already exists for python versions:

Programming Language :: Python :: 2
Programming Language :: Python :: 2.3
Programming Language :: Python :: 2.4
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.0
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2

BTW, I'm not sure the right way to define that a project is dependent on which or which version of a framework is to use the classifiers.

We already can do that using the requires fields, and it will be easy to deal with them with the upcoming distutils2 release, because the setup.py thing will disappear, going to be replaced by a static setup.cfg file.

**pydanny said on 2010-11-06**

@Richard - Maybe a bigger typeface or more precedence to to the bug tracker and help links?

**Doug Napoleone said on 2010-11-07**

*sigh* oops! I was wrong about the framework version classifiers. They are not part of the list. I should double check my facts first. Sorry... Richard and others should be able to add that feature though.

We should put out a request for feedback on which versions need official listing for which frameworks. I would not expect the PyPi folks to track down all the versions themselves. Nor should al the potential versions be included IMHO. For example Django 0.92 is just out.

