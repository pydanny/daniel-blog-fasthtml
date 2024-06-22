---
date: '2012-09-04'
published: true
slug: installing-pycairo-on-mac-osx
tags:
- python
- tools
- howto
- setup
time_to_read: 2
title: Installing Pycairo on Mountain Lion
---

[Pycairo](https://cairographics.org/pycairo/) is the binding for the
[cairo graphics library](https://cairographics.org/). It's also not
something you can get running with a simple `pip install py2cairo`.
After many hours of working the search engines and dancing to the
configure/make/make install melody, I figured out an answer that worked
for me.

Step 1 - Install GCC
====================

If you don't have it yet, go get
<https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.7-v2.pkg>
and install it. It's 200 MB so make sure you have a fast connection
and/or a good place to wait.

Step 2 - Install Homebrew
=========================

I use Homebrew instead of Macports. If you don't have it yet, paste
this in a terminal prompt:

``` bash
ruby <(curl -fsSkL raw.github.com/mxcl/homebrew/go)
```

Step 3 - Install Cairo
======================

In your terminal prompt, type the following:

``` bash
$ brew install cairo --use-clang
```

You'll get some messages about LDFLAGS and CPPFLAGS in build variables,
but that's only important if you skip Homebrew and build your own
software later that interacts with **cairo**.

Step 4 - Install Pycairo itself
===============================

The nasty little trick to this is to remember that **Pycairo** is
packaged on it's site and other places as **py2cairo**. When they get
around to releasing version 3 of Pycairo, I'm going to beg and plead
that they follow an obvious naming system for their bundles. I know this
is done in other communities, but it's frustrating and a real barrier
for getting into a project.

In case, in your terminal prompt, type the following:

``` bash
$ brew install py2cairo
```

If you are using a non-Homebrew installed Python like I do, you have to
set the PYTHONPATH to find pycairo. Set your PYTHONPATH in your
.bashrc/.profile/.whatever to the following:

``` bash
PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH.
```

Yes, it's the system Python, but for now I'm okay with it. If someone
has an easy recipe for alternative Python installations, I would love to
link to it.
