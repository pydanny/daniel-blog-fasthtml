---
date: "2012-03-05"
published: true
slug: sorry-state-python-oauth-providers
tags:
  - python
  - django
  - OAuth
  - api
  - Consumer-Notebook
  - rant
time_to_read: 5
title: The sorry state of Python OAuth providers
---

This is one of those challenging posts to write. The people whose
projects I'm going to describe have put in a lot of dedicated, hard
work to overcome a challenging subject. Writing an OAuth consumer is a
hard problem and writing an OAuth provider is an even harder problem.
The efforts put in by the authors of these projects has been nothing
short of incredible. The problem, however, is that the existing projects
are not usable as-is, and need the support of the community in order to
improve.

The terrible thing is that this is a solved problem within our
community. Python based projects are successfully implementing OAuth
providers, and often using internally hacked versions of the efforts
I'm about to describe. However, they aren't giving this back to the
community. It might be that they want to protect their competitive edge,
but I'm going to be nice and say that it's because their too busy to
find time to send pull requests back.

In any case, let me present our use case. For [Consumer
Notebook](https://consumernotebook.com) we want an
[API](https://api.consumernotebook.com). We want to be able to track
usernames, passwords, and the application using our
[API](https://api.consumernotebook.com) - which is the OAuth use case.
Much as BasicAuth or DigestAuth is the easier way to go in terms of
implementation, OAuth was designed for our use case: allowing
third-party developers to build apps using our API without having to
store credentials. In fact, it's a critical security issue: Twitter
dealt with malicious "Twitter apps" stealing usernames and passwords
before they switched to OAuth. As an API provider, being an OAuth
provider might be more challenging, but it's the responsible thing to
do.

# Existing OAuth Providers

Time to get into the meat of the issue. Let's look at the current
implementations of OAuth providing within the Python community. Again, I
wish I didn't have to be negative, but I'm up against the wall:

## OAuth2app (Django)

<https://github.com/hiidef/OAuth2app>

OAuth version: 2.0

- Strange URL construction that might be a security hole.
- Bitwise operators in the logic making it harder to debug. Security
  is hard. Don't complicate your security code because your mistakes
  will cost.
- Uncommented code. Security is hard. Comment your code.
- Documentation outdated and insufficient.
- Doesn't work without serious hacking and adding of undocumented
  parameters. Which means I have to worry if I'm breaking anything.
- We managed to get it working with GET requests. Then we realized
  that we were using GET requests, which seems like a bad idea.

## django-piston (Django)

<https://bitbucket.org/jespern/django-piston>

OAuth version: 1.0

- Stalled project.
- Documentation insufficient.

## django-oauth-plus (Django)

<https://code.larlet.fr/django-oauth-plus>

OAuth version: 1.0a

- Tutorial doesn't work.
- Documentation insufficient.
- Doesn't work without serious hacking. Which means I have to worry
  if I'm breaking anything.
- We could not get it to work.

## lastuser (Flask)

<https://github.com/hasgeek/lastuser>

OAuth version: 2.0

- No documentation
- No tests to serve as documentation
- Lack of documentation means I'm not sure if it is actually a OAuth
  provider.

## python-oauth2 (Python)

<https://github.com/dgouldin/python-OAuth2> (best example)

OAuth version: 1.0

- Called 'OAuth2' but only works with OAuth 1? Really? **WTF?** This
  needs to fixed.
- Documentation insufficient.
- Provides only a skeleton of a provider. Not a turnkey solution.
- Doesn't work as a provider without serious hacking. Which means I
  have to worry if I'm breaking anything.
- Many, many forks of the project, with various blog posts advising
  people to use various particular forks rather than the main one.

# How about a solution?

Alright, I've ranted and laid out out a bunch of bullets identifying a
problem. Time to try and fix the problem.

For starters, a production-usable OAuth provider should meet certain
standards:

- Near turnkey solution
- Working code (duplicates above bullet but I'm making a point)
- Working tutorials
- Documentation
- Commented code
- Linted code
- Test coverage > 80%

This is my specification. If your project for any Python framework
matches it, I'll list it on a forthcoming website that also covers
Python based OAuth consumers.

For what it's worth, Idan Gazit has been working on something to help
address the problem, specifically <https://github.com/idan/oauthlib>. It
also is intended to cover the Python OAuth consumption issue I didn't
cover in this article. It and related efforts need a lot of work, so...

The PyCon US 2012 sprints start on March 12. I think as a community, we
Pythonistas should band together and make things right. I think we'll
have the brainpower and enough eyes on the problem to make serious
headway on the issue, either by fixing existing solutions or creating
new ones. Right now I've got interest from people to join in and help,
including Idan Gazit, Audrey Roy, George Hickman, and others.

We're willing to put in the time to make OAuth in Python better, how
about you?

Join us at the PyCon US sprints either in person or on-line. [Details of
the sprint are near the bottom of this PyCon Sprint
page](https://us.pycon.org/2012/community/sprints/projects/).

[![OAuth Logo](/images/6803475636_f34fb400eb_m.jpg)](https://oauth.net/)

---

## Updates

- 03/05/2012 - Removed Velruse from the list of providers as it's
  lead, Michael Merickel, clarified that it is not a provider.
- 03/06/2012 - Added a link to the PyCon OAuth sprints.
- 6/24/2013 - This article has been translated by Anja Skrba to
  Serbo-Croatian:
  <https://science.webhostinggeeks.com/lose-stanje-python>
- 07/07/2013 - Please consider
  <https://github.com/evonove/django-oauth-toolkit> for use as a
  Django-powered OAuth provider. The team behind it is doing it right!
- 01/16/2014 - Please consider
  <https://github.com/lepture/flask-oauthlib> for use as a
  Flask-powered OAuth provider.

---

[Discuss this post on Hacker
News](https://news.ycombinator.com/item?id=3666853)
