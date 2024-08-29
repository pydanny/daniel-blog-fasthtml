---
date: "2011-06-24T14:04:00.000-07:00"
description: ""
published: true
slug: 2011-06-announcing-django-uni-form-080-beta
tags:
  - djangocon
  - django
  - forms
  - legacy-blogger
time_to_read: 5
title: Announcing django-uni-form 0.8.0 beta!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/06/announcing-django-uni-form-080-beta.html)_.

This has been a long time coming, but I am pleased to announce the release of the[ django-uni-form 0.8.0 beta](https://pypi.python.org/pypi/django-uni-form/0.8.0-beta). We plan to release the 0.8.0 final next Friday around the start of July 2011.

This is an enormous jump forward in the project, and I think you'll like what has been done and who contributed.

<b>Some notable changes</b>


1. As of this release, there is now a [formal django-uni-form](https://pypi.python.org/pypi/django-uni-form/0.8.0-beta) release on [PyPI](https://pypi.python.org/pypi) that fully supports [Django](https://djangoproject.com/) [CSRF](https://docs.djangoproject.com/en/1.3/ref/contrib/csrf/) tokens.
- Better error messages to help you debug. No more annoying Null messages on bad helpers!
- The [Python](https://python.org/) code has been carefully cleaned and optimized. Much easier to read, debug, and it plain [runs faster on form heavy sites](https://django-uni-form.readthedocs.org/en/latest/faq.html#how-fast-is-django-uni-form).
- Various improvements to the templates to better match the parent [Uni-Form](https://sprawsm.com/uni-form/) library.
- Only compatible with Django 1.2 or higher and Python 2.6 or higher. If you need something to work with other earlier versions of Django/Python, then I suggest using [django-uni-form 0.7.0](https://pypi.python.org/pypi/django-uni-form/0.7.0). Or better yet, upgrade your site!
- [Much improved documentation](https://django-uni-form.readthedocs.org/en/latest) on the awesome [readthedocs.org](https://readthedocs.org/) site.
- [Tons of other things](https://django-uni-form.readthedocs.org/en/latest/changelog.html#id1)!
- Upcoming faster release cycles. More on that in the next section...

<b>Leadership change for django-uni-form</b>

Let's face it, over a year between releases&nbsp;is too long for any active open source project. I haven't done the incredible (and patient) [django-uni-form community](https://github.com/pydanny/django-uni-form/watchers) justice in supporting their issues and pull requests. This project has needed a much more active lead for some time. Fortunately, I found a new project in the way of [Miguel Araujo](https://tothinkornottothink.com/aboutme/).

[Miguel Araujo](https://twitter.com/maraujop) shares my passion for good form generation and has a very deep understanding of Python, Django, and HTML. Also, his decisions on everything about this project either matches my own thoughts or he's been able to easily convince me why his concepts are sound. He is responsive to pull requests and issues, and his work is of high quality. So we should be seeing lots of releases and a better evolution of the system to match other advancements in the Django community.

So going forward Miguel will be the project lead for django-uni-form, and I'll be '<i>former&nbsp;project lead' </i>and<i>&nbsp;'documentation donkey</i>'.

<b>The future of django-uni-form in the face of the forms refactor</b>

Some people are wondering what place django-uni-form has in the face of th[None](https://www.blogger.com/) by Greg Mullegger. Is the need for django-uni-form going away?

First of all, I actually have been pushing for a forms refactor in Django for some time. At the [djangocon.us](https://djangocon.us/)&nbsp;2010 sprints [Russel Keith-McGee](https://cecinestpasun.com/), Django core developer and DSF president,&nbsp;asked my opinion on the design of a forms refactor. For the GSOC effort, I was delighted that the GSOC forms project followed the opinion that I preferred in how to &nbsp;doing things, and so I put in my non-binding vote for Gregor's approach. I'm rooting for you Gregor!

Second, while I think that while this library may change a bit to accomodate the eventual integration of Gregor's work, the need to be able to do&nbsp;guaranteed&nbsp;working [Section 508](https://django-uni-form.readthedocs.org/en/latest/concepts.html#section-508) compliant layouts easily and more importantly make fancy layout changes in Python will keep this library alive and useful for a long time coming.

<b>Whither goes the source code?</b>

Finally, we'll be keeping the repo at[ https://github.com/pydanny/django-uni-form](https://github.com/pydanny/django-uni-form) for the 0.8.x series so we have time to properly warn the community. When the forms refactor hits Django (prompting the necessary release of the 0.9.x series) we may be moving the library to its own [github](https://github.com/) account.

<b>Conclusion</b>

I want to thank all the contributors, users, and anyone who gave me guidance or suggestions for this project. All the credit for this goes to you.&nbsp;I'm honored to have started something used by so many great people in so many wonderful ways.

This evolved from a Django beginner's shortcut filter to a rather sizable project with a great community. Due to my support of this project I learned [git-scm](https://git-scm.com/), setuptools, [JQuery](https://jquery.com/), [Sphinx](https://sphinx.pocoo.org/), [custom Django filters and templatetags](https://docs.djangoproject.com/en/1.3/howto/custom-template-tags/), and more. I look forward to where it will go in the future with Miguel as lead.
