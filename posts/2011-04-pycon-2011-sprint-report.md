---
date: '2011-04-05T10:23:00.000-07:00'
description: ''
published: true
slug: 2011-04-pycon-2011-sprint-report
tags:
- opencomparison
- pycon
- pyramid
- django
- python
- google
- django packages
- legacy-blogger
time_to_read: 5
title: PyCon 2011 Sprint Report
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/04/pycon-2011-sprint-report.html)*.

I love sprints. I've yet to participate in a sprint where I didn't learn something that made a difference in my programming career. Off the top of my head some of the things I've learned include [distributed version control](https://en.wikipedia.org/wiki/Distributed_Version_Control_System), picking the right [Python](https://python.org/) tool, [JQuery](https://jquery.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Bazaar](https://en.wikipedia.org/wiki/Bazaar_(software)), [Git](https://en.wikipedia.org/wiki/Git_(software)), [Mercurial](https://en.wikipedia.org/wiki/Mercurial_(software)), the true importance of [unittests](https://docs.python.org/library/unittest.html), and Python's [built-in zip function](https://docs.python.org/library/functions.html#zip). And the [PyCon 2011 sprints](https://us.pycon.org/2011/sprints/projects/) were no different.

[PyCon 2011](https://us.pycon.org/2011/) was different in that this time I was going to co-lead a project, specifically [Django Packages](https://djangopackages.com/) and the hopeful launch of Python Packages.

<b>Note</b>: The goal of Python Packages is not to replace [PyPI](https://pypi.python.org/), but rather serve as a resource to find, evaluate, and compare packages used in the every day life of a Python. In my opinion, PyPI should be dedicated to listing and serving packages - anything else (comments, ratings, documentation, etc) just adds complexity to the project and diffuses the focus of their team.

It all started with us being the second-to-last in line at the PyCon sprint announcements. At the microphone I forgot to mention a few things so I was worried that our attendance would suck. I tried to take it in good humor, but doubt worried at my gut. My co-lead, [Audrey Roy](https://twitter.com/audreyr), was confident that if no one showed, then we would have fun with just the two of us hacking away.

To our delight and surprise, turnout was good with about ten (10) people showing up. And thanks to [lessons learned at DjangoCon 2010](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#djangocon-2010)&nbsp;and our tricks to [getting more sprinters](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#getting-sprinters)&nbsp;and helping&nbsp;[sprinters](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#assigning-work) [deliver](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#be-conservative) [code](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#helping-people-get-stuff-done), the number of participants kept growing. In the end we had twenty-four (24) new contributors to the project, which was simply amazing.

Test coverage had been mediocre on [Django Packages](https://github.com/djangopackages/djangopackages), but after a show stopping bug got into production (someone changed a commonly used function to a property), we did a huge amount of work to not only increase [test coverage](https://www.djangopackages.com/packages/p/django-coverage/) but also refactor tests to be simpler and actually test rather than just increase coverage numbers. The improved quality and quantity of test coverage gave contributors the confidence to refactor and simplify some of the 'brilliant code' that I had written during the first month of the project.

We also got a [bit draconian about accepting pull requests](https://readthedocs.org/docs/packaginator/en/latest/lessons_learned.html#pull-requests)&nbsp;but&nbsp;[documented how to get pull requests accepted](https://readthedocs.org/docs/packaginator/en/latest/contributing.html#how-to-get-your-pull-request-accepted). That might sound mean but if stopping one person's bug allowed ten (10) other people to maintain productivity then everyone is happier. Also, it allowed us to coach some of the new Python developers coming from other languages on their work. Which was awesome because we saw people's work evolve in a day from rank beginner material to competent Pythonista submissions. To think we had some part in helping people improve is one of the best things we got out of the sprint.

And the results?

The biggest thing, which we got into place on the second evening of the sprint, is that Django Packages is now an instance of [Packaginator](https://github.com/cartwheelweb/packaginator). Packaginator is a framework for launching package comparison sites for Python based tools. After a bit more work to happen this coming Sunday (4/10/2011), we'll be able to trivially deploy Python Packages, Pyramid Packages, Plone Packages, and Flask Packages - all of them able to support patches from Packaginator without causing the maintainers of those sites to hate our guts. We should also will have the hooks to support things like Vim Packages, Ubuntu Packages, Fedora Packages and more quite shortly.

Packaginator handles repos much better and now supports&nbsp;[Bitbucket](https://bitbucket.org/), [Github](https://github.com/), and [Launchpad](https://launchpad.net/) out of the box. [SourceForge](https://sourceforge.net/) may happen very soon. [Google Project Hosting](https://code.google.com/hosting/), when Google implements [Project Hosting API ](https://code.google.com/p/support/issues/detail?id=5088)(cause we refuse to screen scrape pages for MetaData) will be handled shortly thereafter. Thanks to the work of the 'repo men' adding a new repo is now much easier, and we hope people submit new ones to handle things like Trac and other repo systems.

Our [documentation](https://readthedocs.org/docs/packaginator/en/latest/index.html) went from passable to incredible, and our [installation story is awesome](https://readthedocs.org/docs/packaginator/en/latest/install.html). You want people to participate in your project? Then learn you some [RestructuredText](https://en.wikipedia.org/wiki/Restructured_Text) and [Sphinx](https://sphinx.pocoo.org/) and host your documentation on [Read the Docs](https://readthedocs.org/). Read the Docs is awesome and I need to blog about why all Python docs should move there.

There was a huge amount of template cleanup - and the grid X-Y access can be rotated. We haven't turned on that feature yet, but you'll see it shortly.

<b>Conclusion</b>

The sprints were awesome. I learned a lot about running projects and managed to get into some new coding tricks (zip() comes to mind) into my brain. That this project is helping the open source world made it even better. And the best thing of all is I got to make over twenty new friends - all of whom worked with us towards a single common goal.

<b>PyCon 2011 Contributors</b>



- Aaron Kavlie
- Adam Saegebarth
- Alex Robbins
- Andrii Kurinny
- Audrey Roy
- Brian Ball
- Bryan Weingarten
- Chris Adams
- Daniel Greenfeld
- Eric Spunagle
- Evgeny Fadeev
- Flaviu Simihaian
- Gisle Aas (Repo Man)
- Jacob Burch
- James Pacileo
- Jeff Schenck
- Jim Allman
- John M. Camara
- Jonas Obrist
- jrothenbuhler
- Nate Aune
- Nolan Brubaker
- Preston Holmes
- Stuart Powers
- Szilveszter Farkas (Repo Man)
- Tom Brander
- Vasja Volin

