---
date: '2011-02-17T11:21:00.000-08:00'
description: ''
published: true
slug: 2011-02-my-django-tutorial-at-pycon
tags:
- pycon
- geek celebrities
- django
- python
- legacy-blogger
time_to_read: 5
title: My Django tutorial at PyCon
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/02/my-django-tutorial-at-pycon.html)*.

Working on my tutorial slides for my [PyCon](https://us.pycon.org/2011) [class/tutoria](https://us.pycon.org/2011/schedule/presentations/111/)l/[workshop](https://pydanny.blogspot.com/2011/02/my-pinax-solutions-class-at-pycon-2011.html) last night I suddenly came to a stark realization.

<b>Out of dozens of slides, only 5 of them are Pinax specific.</b>

<span class="Apple-style-span" style="font-size: x-large;">o.O</span>

I think this is because the slides are a condensed version of what the best and brightest in the [Django](https://djangoproject.com/) and [Python](https://python.org/) community think are good practices and tools. What do I mean?


- [Jacob Kaplan-Moss](https://jacobian.org/) on matching best practices with incredible documentation and tests.
- [James Bennett](https://b-list.org/)&nbsp;on using small apps rather than monolithic ones.
- [James Tauber](https://jtauber.com/) and [Brian Rosner](https://brianrosner.com/)'s code in [Pinax](https://pinaxproject.com/) which taught me and so many others incredible Django tricks.
- [PEP-8](https://www.python.org/dev/peps/pep-0008/)
- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Mark Ramm](https://compoundthinking.com/blog/index.php/about/)&nbsp;on well, nearly everything but especially his critical commentaries on Django.

So what does this mean?

Well, I've been rethinking the mantra "Pinax is Django". &nbsp;It is hard to say that when users of [django-cms ](https://django-cms.org/)and [satchmoproject](https://satchmoproject.com/) and other frameworks can't use core Pinax components. That said, users of those tools tend to rely on same foundation: Python, Django, [virtualenv](https://virtualenv.openplans.org/), and [pip](https://pip.openplans.org/) and growing ecosphere of [Django Packages](https://djangopackages.com/).

Which leads me to realize that with just 5 slides pertaining to Pinax material in the tutorial, the Pinax Solutions class could be renamed "<b>Django Solutions class with a bit of Pinax</b>".

And this makes a lot of sense. Some of the bits that made Pinax special such as static media handling are now part of Django as of the [forthcoming 1.3 release](https://docs.djangoproject.com/en/dev/releases/1.3/#extended-static-files-handling). Lessons learned from [Django Uni-Form](https://github.com/pydanny/django-uni-form) which grew out of supporting div-based forms in Pinax are helping determine the path of forms work in Django 1.4. Which means that if you are using django-cms or other [CMS](https://www.djangopackages.com/grids/g/cms/), [django-shop](https://django-shop.org/) or other [e-commerce](https://www.djangopackages.com/grids/g/ecommerce/) tools, then you are benefitting from what Pinax has done for the community.

All of this leads to my closing statements about the class/workshop: The class is about Django with a little bit of Pinax tossed in. Having in the past worked with [multiple](https://storymarket.com/) [non-Pinax](https://science.nasa.gov/) [projects](https://cartwheelweb.com/), I can assure you that the solutions presented and the workshop itself will be of use to you regardless of if your project is using that framework.