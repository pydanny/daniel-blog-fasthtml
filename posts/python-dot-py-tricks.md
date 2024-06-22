---
date: "2014-12-19"
published: true
slug: python-dot-py-tricks
tags:
  - python
time_to_read: 4
title: setup.py tricks
---

![Setup.py tricks](/images/setup.png)

Seasons greetings!

Before I begin, I want to make very clear that most of what I'm about
to explain are **'tricks'**. They aren't "best practices", and in
at least one case, is possibly inadvisable.

Speaking of inadvisable practices, at some point I'll write a
**'setup.py traps'** blog post, which are things I believe you should
never, ever do in a **setup.py** module.

## Tricks

These are tricks I have to make package management in
[python](https://python.org) a tiny bit easier. Before you attempt to
implement them, I recommend you have at least basic experience with
creating new packages. Two ways to learn about python packaging are the
[New Library
Sprint](https://audreyr.gitbooks.io/new-library-sprint/content/)
(beginner friendly) and the [Python Packaging User
Guide](https://python-packaging-user-guide.readthedocs.org) (more
advanced).

### 'python setup.py publish'

This is where it all started. One day I was looking at some of [Tom
Christie's code](https://github.com/tomchristie) and discovered the
[python setup.py
publish](https://github.com/tomchristie/django-rest-framework/blob/971578ca345c3d3bae7fd93b87c41d43483b6f05/setup.py#L61-L67)
command inside the **setup.py** module of **Django Rest Framework**. It
goes something like this:

```python
# setup.py
import os
import sys

# I'll discuss version tricks in a future blog post.
version = "42.0.0"

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

# Below this point is the rest of the setup() function
```

What's awesome about this is that using this technique I don't have to
look up the somewhat cryptic **python setup.py sdist upload** command,
or the actually cryptic **python setup.py bdist_wheel upload**.
Instead, when it's time to push one of my packages to
[PyPI](https://pypi.python.org/pypi), I just type:

```bash
$ python setup.py publish
```

Much easier to remember!

### 'python setup.py tag'

The problem with Tom Christie's **python setup.py publish** command is
that it forces me to type out the **git tag** command. Okay, let's be
honest, it forces me to copy/paste the output of my screen. Therefore,
all on my very own, I 'invented' the **python setup.py tag** command:

```python
# setup.py

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()
```

Pretty nifty, eh? Now I don't have to remember so many cryptic git
commands. And I get to shorten the python setup.py publish command:

```python
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()
```

When I need to do a version release, I commit my code then type:

```bash
$ python setup.py publish
$ python setup.py tag
```

Why don't I combine the commands? Well, you aren't supposed to put
things like 'RC1' or '-alpha' in your PyPI version names. By
seperating the commands I have finer grained control over my package
releases. I'm encouraged to place alpha, beta, and release candidates
in git tags, rather than formal PyPI releases.

### 'python setup.py test'

I'm fairly certain some of my readers are going to have a seriously
problem with this trick. In fact, depending on the the response of those
who manage Python's packaging infrastructure, it might be moved to my
forthcoming 'traps' blog post.

Alrighty then...

I like [py.test](https://pytest.org). I've [blogged about the use of
py.test](/pytest-no-boilerplate-testing.html). I
try to use it everywhere. Yet, I'm really not a fan of how we're
supposed tie it into **python setup.py test**. The precise moment I get
uncomfortable with **py.test** is when it makes me add special classes
into **setup.py**.

Fortunately, there is another way:

```python
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'flake8',
        'coverage'
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirments." % err_msg
        raise ImportError(msg)
    os.system('py.test')
    sys.exit()
```

Which means I get to use **py.test** and **python setup.py test** with a
trivial addition of code:

```bash
$ python setup.py test
```

In theory, one could run **pip install** on the missing requirements, or
call them from a requirements file. However, since these are 'tricks',
I like to keep things short and sweet. If I get enough positive results
for this one I'll update this example to include calling of **pip** for
missing requirements.

**note**: This doesn't mean I'm not using
[tox](https://pypi.python.org/pypi/tox). In fact, I use tox to call my
version of **python setup.py test**.

## What about subprocess?

There are those who will ask, "Why aren't you using the
[subprocess](https://docs.python.org/2/library/subprocess.html) library
for these shell commands?"

My answer to that question is, "Because if I need a nuclear weapon to
kill a rabbit maybe I'm overdoing things." For these simple tricks,
the **os.system()** function is good enough.

## Why not just use a Makefile?

While I code primarily on Mac OSX and Linux, most of my open source
packages are used Windows. Thanks to [AppVeyor](https://appveyor.com),
I'm testing more and more of them in that environment. In fact, I'll
probably be modifying these "tricks" to work better for Windows users.

## Updates

- 2014/12/21 - Added a note about using tox.
- 2014/12/21 - Added a note about Makefile and Windows
