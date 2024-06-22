---
date: '2014-04-24'
published: true
slug: python-partials-are-fun
tags:
- python
time_to_read: 4
title: Python Partials are Fun!
---

Writing reusable code is a good thing, right? The trick is to do so in a
way that makes your life and those of others easier, but to do so in a
very clear and maintainable way. Recently I've been playing around with
Python's
[functools.partial](https://docs.python.org/2.7/library/functools.html#functools.partial)
function, which I've found can help facilitate writing reusable code.

[![image](/images/partials.png)](/python-partials-are-fun.html)

While the documentation has a nice explanation and demonstration of
`functools.partial`, it's very serious. I've got my own internal
version of things which I think is a little more fun.

My Explanation of `functools.partial`
=====================================

What `functools.partial` does is:

-   Makes a new version of a function with one or more arguments already
    filled in.
-   New version of a function documents itself.

Rather than dive into paragraphs of explanation, I'll use code examples
to explain how this works.

My Demonstration of `functools.partial`
=======================================

First, let's say we want to create a function that explicitly performs
[exponentiation](https://en.wikipedia.org/wiki/Exponentiation). This way
we can get the
[squares](https://en.wikipedia.org/wiki/Square_(algebra)),
[cubes](https://en.wikipedia.org/wiki/Cube_(algebra)), and other power
operations on any number. This duplicates Python's built-in `pow()`
function, but our version has the very nice addition of keyword
arguments.

``` python
def power(base, exponent):
    return base ** exponent
```

Now what if we want to have dedicated square and cube functions that
leverage the `power()` function? Of course, we can do it thus:

``` python
def square(base):
    return power(base, 2)

def cube(base):
    return power(base, 3)
```

This works, but what if we want to create 15 or 20 variations of our
`power()` function? What about 1000 of them? Writing that much
repetitive code is, needless to say, annoying. This is where partials
come into play. Let's rewrite our square and cube functions using
partials, and test it for success using
[py.test](/pytest-no-boilerplate-testing.html):

``` python
from functools import partial

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

def test_partials():
    assert square(2) == 4
    assert cube(2) == 8
```

Whoa! That's awesome. You know what adds to that awesome? Functions
created with partial document themselves (to a degree). I'll
demonstrate with more tests:

``` python
def test_partial_docs():
    assert square.keywords == {"exponent": 2}
    assert square.func == power

    assert cube.keywords == {"exponent": 3}
    assert cube.func == power
```

Using a loop, let's build and test ten (10) custom `power()` functions,
which I'll call 'power partials' (ahem... I find 'power partials'
sounds rather amusing.):

``` python
def test_power_partials():

    # List to store the partials
    power_partials = []
    for x in range(1, 11):

        # create the partial
        f = partial(power, exponent=x)

        # Add the partial to the list
        power_partials.append(f)

    # We could just use list comprehension instead of the loop
    # [partial(power, exponent=x) for x in range(1, 11)]


    # Test the first power
    assert power_partials[0](2) == 2

    # Test the fifth power
    assert power_partials[4](2) == 32

    # Test the tenth power
    assert power_partials[9](2) == 1024        
```

A Way to Organize Partials
==========================

Lists are great, but sometimes it's nice to have a more legible way of
interacting with functions. There are an infinite ways to make this
happen, but I like the dot notation of classes. So here is a 'partial
structure' class which follows a pattern I think is pretty handy:

``` python
# Since I like my article code to work in both Python 2.7 and 3,
#   I'll import the excellent six library to manage the
#   differences between Python versions. Six is available on PyPI
#   at https://pypi.python.org/pypi/six.
from six import add_metaclass

class PowerMeta(type):
    def __init__(cls, name, bases, dct):

        # generate 50 partial power functions:
        for x in range(1, 51):

            # Set the partials to the class
            setattr(
                # cls represents the class
                cls,

                # name the partial
                "p{}".format(x),

                # partials created here
                partial(power, exponent=x)
            )
        super(PowerMeta, cls).__init__(name, bases, dct)

@add_metaclass(PowerMeta)
class PowerStructure(object):
    pass
```

Okay, let's test our PowerStructure class as an instantiated
PowerStructure:

``` python
def test_power_structure_object():
    p = PowerStructure()

    # 10 squared
    assert p.p2(10) == 100

    # 2 to the 5th power
    assert p.p5(2) == 32

    # 2 to the 50th power
    assert p.p50(2) == 1125899906842624
```

Looks good, right? But wait, there's more!

Thanks to the power of metaclasses, we don't need to instantiate the
PowerStructure class!

``` python
def test_power_structure_class():
    # Thanks to the power of metaclasses, we don't need to instantiate!

    # 10 squared
    assert PowerStructure.p2(10) == 100

    # 2 to the 5th power
    assert PowerStructure.p5(2) == 32

    # 2 to the 50th power
    assert PowerStructure.p50(2) == 1125899906842624
```

[Source Code](https://gist.github.com/pydanny/11295815)

Summary
=======

I've provided some simple examples of how to use `functools.partials`.
I find them really useful for certain tasks, mostly in avoiding
repeating myself. Like any coding tool, complex usage can cloak the
meaning of code, so be careful and use `functools.partials` judiciously.

Update: [Nick Coghlan](https://twitter.com/ncoghlan_dev) reminded me to
mention that Python has a `pow()` built-in.

Update 04/30/2014: [Samuel John](https://twitter.com/samueljohn_de)
corrected me on Nick Coghlan's name.
