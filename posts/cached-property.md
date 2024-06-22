---
date: "2014-07-01"
published: true
slug: cached-property
tags:
  - python
  - django
  - flask
  - pypi
  - pyramid
time_to_read: 4
title: "cached-property: Don't copy/paste code"
---

In Python, the `@cached_property` decorator is a really nice piece of
code. What it does is it caches the result of a
[property](https://docs.python.org/2/library/functions.html#property)
call. The cached result will persist as long as the instance does, so if
the instance is passed around and the function subsequently invoked, the
cached result will be returned.

If that doesn't make much sense, below is a snippet of code that shows
the code and demonstrates it in action. As always, I'm using
[pytest](/pytest-no-boilerplate-testing.html) to
validate my code:

```python
from datetime import datetime, timedelta
import time

class cached_property(object):
    """ A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property.

        Source: https://github.com/bottlepy/bottle/commit/fa7733e075da0d790d809aa3d2f53071897e6f76
        """

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value

class SlowClass1(object):

    @cached_property
    def very_slow(self):
        """Represents a performance heavy property."""
        time.sleep(1)  # Wait a WHOLE second!
        return "I am slooooow"

def test_slow_class1():
    # Instantiate the slow class
    slow_class = SlowClass1()

    # Start the clock!
    start = datetime.now()

    # Call the property. This time it's really slow...
    assert slow_class.very_slow == "I am slooooow"

    # Check that it took at least a second to run
    assert timedelta(milliseconds=1000) >= start - datetime.now()

    # Call the property a second time. This time it runs fast.
    assert slow_class.very_slow == "I am slooooow"

    # Second time running, should take a TINY amount of time.
    # Should take just a microsecond, but we'll play a test for and test
    #   for a maximim of at least 100 milliseconds.
    assert timedelta(milliseconds=1100) > start - datetime.now()
```

This is great for encapsulating slow database queries, fetching results
from third-party REST APIs, performing slow algorithms, and anything
else where you would want to catch the results. Pretty neat, yeah!

While originally implemented for web frameworks such as Django, Flask,
Pyramid, and Bottle, I've copy/pasted the `cached_property` property
from non-web project to project as a quick way to give my code a little
boost. I got tired of doing this, and on May 17th, 2014 I decided to
release it as a package called cached-property on
[PyPI](https://pypi.python.org/pypi/cached-property). Using it is easy:

```python
# assuming you've already done "pip install cached-property"
from cached_property import cached_property

class SlowClass2(object):

    @cached_property
    def very_slow(self):
        """Represents a performance heavy property."""
        time.sleep(1)  # Wait a WHOLE second!
        return "I am slooooow"

def test_slow_class2():
    # Instantiate the slow class
    slow_class = SlowClass2()

    # Start the clock!
    start = datetime.now()

    # Call the property. This time it's really slow...
    assert slow_class.very_slow == "I am slooooow"

    # Check that it took at least a second to run
    assert timedelta(milliseconds=1000) >= start - datetime.now()

    # Call the property a second time. This time it runs fast.
    assert slow_class.very_slow == "I am slooooow"

    # Second time running, should take a TINY amount of time.
    # Should take just a microsecond, but we'll play a test for and test
    #   for a maximim of at least 100 milliseconds.
    assert timedelta(milliseconds=1100) > start - datetime.now()
```

Hooray! No more copy/pasting for me! I was very pleased with myself.

Little did I know how fortunate I was for having released this package.

# Don't Copy/Paste Code

The very next day after I released the cached-property package, [Tin
Tvrtković](https://github.com/Tinche) opened an issue asking for [better
multithreaded
support](https://github.com/pydanny/cached-property/issues/6). To my
shock and embarressment, my copy/pasted code could have been disastrous
if brought into the wrong project. I had blindly been assuming that the
code I hadn't bothered to try and understand worked under any
situation, when in reality it had been designed for working within the
context of a web framework.

Ultimately, Tin [submitted a pull
request](https://github.com/pydanny/cached-property/pull/9), and now the
`cached-property` package also includes a `@threaded_cached_property`
decorator. Thank you Tin!

However, the lessons of the experience had been burned into my brain.

# Lessons Learned

1.  Don't copy/paste code blindly from project to project.
2.  If you are repeatedly moving code from project to project, take the
    time to understand what the code is actually doing.
3.  Instead of copy/pasting code from project to project, make a package
    and ask for input from others. If making a package feels like too
    much work,
    [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
    makes creating new packages really easy.

# Going forward

One exciting development has been the [discussion to include a
cached_property decorator in core
Python](https://github.com/pydanny/cached-property/issues/2). Even if my
contribution to the effort has been merely the encapsulation of the
code, it's nice to know I may have some small part in the development
of the language.

![image](/images/directions_med.png)
