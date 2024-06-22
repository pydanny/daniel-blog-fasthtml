---
date: '2014-01-15'
published: true
slug: pytest-no-boilerplate-testing
tags:
- python
- django
- testing
time_to_read: 3
title: 'pytest: no-boilerplate testing'
---

When I first encountered Holger Krekel's [pytest](https://pytest.org/)
this summer on [Jeff Knupp's
blog](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
I felt like I had been living under a rock for years. I've been using
Python's [unittest](https://docs.python.org/2/library/unittest.html)
framework since 2006 and [nose](https://pypi.python.org/pypi/nose) to
find tests since 2008, but here was another test framework that actually
predates **nose**! **pytest** is a very mature testing tool for testing
Python. My favorite features:

-   It can run **unittest**, **doctest**, and **nose**, style tests
    suites, making it ideal for new and legacy projects.
-   It includes an intuitively named `raises` **context manager** for
    testing exceptions.
-   You can define fixture arguments to generate baseline data. This is
    very, very different from Django-style fixtures.
-   Via `pytest.ini` you can change the behavior of pytest.
-   Integrates nicely with `setup.py`.

Alright, lets dive into usage.

Test Discovery
==============

The first thing that **pytest** provides is test discovery. Like
**nose**, starting from the directory where it is run, it will find any
Python module prefixed with `test_` and will attempt to run any defined
**unittest** or function prefixed with `test_`. **pytest** explores
properly defined Python packages, searching recursively through
directories that include `__init__.py` modules. Since an image is
probably easier to read, here's a sample directory structure annotated
with which files are checked for tests:

``` bash
address/
    __init__.py
    envelope.py 
    geo.py 
    test_envelope.py # checked for tests
    test_geo.py # checked for tests
records/
    # pytest WON'T look here because it lacks __init__.py
    records.csv
    records.py
    test_records.py # skipped because records/ lacks __init__.py
__init__.py
main.py
test_main.py  # checked for tests
```

Now that I've explained which files are checked for tests, here is how
**pytest** determines what in each Python module is run as a test.

1.  **pytest** *just runs* **doctests** and **unittests**.
2.  **pytest** runs any function prefixed with `test_` as a test.
3.  **pytest** does [its
    best](https://pytest.org/latest/nose.html#unsupported-idioms-known-issues)
    to run tests written for **nose**.

Yes, **pytest** behaves similarly to **nose** in test discovery. Next is
another feature that it shares with **nose** that I really enjoy.

Writing Tests as Functions
==========================

Python's **unittest** framework works, but it's always felt like too
much boilerplate. I admit I like to write tests, but working with the
**unittest** framework always dimmed that fun. I suppose this is why the
assert keyword is useful, because it changes this:

``` python
import unittest

class TestMyStuff(unittest.TestCase):

    def test_the_obvious(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
```

to this:

``` python
>>> assert True == True
```

The former is nine lines of code (seven if you are using **pytest** to
find this test) to do what the assert statement does in one. However,
the nine lines of **unittest** code has a couple major advantages:

1.  Not automatically run when stumbled on by the Python interpreter.
2.  Produces a more illuminating response than an uninformative
    AssertionError.

Fortunately, tools like **pytest** (and **nose**) provide the ability to
write tests as functions. This means we can combine the advantages of
both `unittest` and `assert` thus:

``` python
def test_the_obvious():
    assert True == True
```

Now we are down to just two lines of code! That could be increased to
five if we called **pytest** the same as we did in the **unittest**
example:

``` python
import pytest

def test_the_obvious():
    assert True == True

if __name__ == '__main__':
    pytest.main()
```

The next part is wonderful. If an `assert` statement fails, then
**pytest** provides a very informative response. Let's check it out by
running the following code:

``` python
import pytest

def test_gonna_fail():
    assert True == False  # Going to fail here on line 4

if __name__ == '__main__':
    pytest.main()
```

When I run this code, I get the following response:

``` bash
==================== FAILURES =====================
----------------- test_gonna_fail -----------------

    def test_gonna_fail():
>       assert True == False
E       assert True == False

samples.py:4: AssertionError
======== 1 failed, 0 passed in 0.1 seconds ========
```

As you can see, pytest identified where the `assert` statement failed on
line 4 and displays exactly caused the failure (`True` did not equal
`False`). Very nice indeed.

What's Next?
=============

In my next [blog
post](/pytest-no-boilerplate-testing-2.html) I
describe the following features of writing tests with **pytest**.

-   The `raises` **context manager**
-   Fixtures
-   Fixture Teardown
