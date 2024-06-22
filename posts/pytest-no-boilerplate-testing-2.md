---
date: '2014-01-16'
published: true
slug: pytest-no-boilerplate-testing-2
tags:
- python
- django
- testing
time_to_read: 3
title: 'pytest: no-boilerplate testing (part 2)'
---

In my previous [blog
post](/pytest-no-boilerplate-testing.html) I covered
test discovery and writing basic tests using
[pytest](https://pytest.org/). Today I'm going to cover a few more
features that I really enjoy: `raises` and `fixtures`.

The Intuitively Named `raises` **context manager**
==================================================

When using **pytest**, you can assert whether or not an exception
occurred via the following:

``` python
# test_exceptions.py
from pytest import raises

def test_an_exception():
    with raises(IndexError):
        # Indexing the 30th item in a 3 item list
        [5, 10, 15][30]

class CustomException(Exception):
    pass

def test_my_exception():
    with raises(CustomException):
        raise CustomException
```

This is similar to, but just a bit easier to remember than the
implementation in
[unittest](https://docs.python.org/2/library/unittest.html).

What I like about it is that even if I step away from code and tests for
enough time to go on vacation and [get
married](/i-married-audrey-roy.html), when I come
back I always remember the precise name of the **context manager** used
to raise exceptions.

Fixtures as Function Arguments
==============================

When writing tests, it's not uncommon to need common objects used
between tests. However, if you have a complicated process to generate
these common objects, then you have to write tests for your tests. When
using Python's venerable **unittest** framework, this always causes a
spaghetti-code headache. However, via the virtue of simplicity,
**pytest** helps keep our test code cleaner and more maintainable.

Rather than try and explain that further, I'll write some code to get
my point across:

``` python
# test_fixtures.py
from pytest import fixture

@fixture  # Registering this function as a fixture.
def complex_data():
    # Creating test data entirely in this function to isolate it
    #   from the rest of this module.
    class DataTypes(object):
        string = str
        list = list
    return DataTypes()

def test_types(complex_data): # fixture is passed as an argument
    assert isinstance("Elephant", complex_data.string)
    assert isinstance([5, 10, 15], complex_data.list)
```

Nice and simple, which is how I think test harnesses should operate.

Writing Tests for Fixtures
--------------------------

Let's pretend that the `complex_data()` is a terribly sophisticated
function in it's own right. It's so sophisticated that I can't
determine what it's actually doing, and I start to get worried.
Fortunately, because the `complex_data()` argument itself is written as
a function, I can easily write a test for it.

``` python
# test_fixtures.py
# note: this version of test_fixtures.py is built off the previous example

def test_complex_data(complex_data):
    assert isinstance(complex_data, object)
    assert complex_data.string == str
    assert complex_data.list == list
```

Now that I can easily write tests for my fixtures, that means I can
refactor them! I can replace difficult-to-use libraries with easier
ones, break up giant functions into little ones, and generally simplify
the unnecessarily complex.

If you've ever been in that weird place where a **unittest** `setUp()`
method is indecipherable, you know just how useful this can be.

Scoping Fixtures
----------------

What if I want a fixture that shares it's scope across several test
functions?

``` python
# test_fixtures_with_scope.py
from pytest import fixture

@fixture(scope="module")  # Registering fixture with module-level scope
def scope_data():
    return {"count": 0}

def test_first(scope_data):
    assert scope_data["count"] == 0
    scope_data["count"] += 1

def test_second(scope_data):
    assert scope_data["count"] == 1
```

Executing Teardown Code
-----------------------

I can tear down data structures in them. This is useful for any sort of
data binding, including file management.

``` python
# test_fixtures_with_teardown.py
from pytest import fixture

@fixture
def file_data(request): # The fixture MUST have a 'request' argument
    text = open("data.txt", "w")

    @request.addfinalizer
    def teardown():
        text.close()
    return text

def test_data_type(file_data):
    assert isinstance(file_data, file)
```

What's really nice about this teardown feature is that when combined
with the fixture decorator's `scope` argument, I can exactly control
when fixtures are taken down. This is an amazing piece of control. While
I can and have duplicated this behavior using **unittest**, with
**pytest** I can do it with more obvious code.

More **pytext** Fixture Features
--------------------------------

Want to know more things you can do with **pytest** fixtures? Please
read the [pytest fixtures
documentation](https://pytest.org/latest/fixture.html)

More to Come
============

In my [next blog
post](/pytest-no-boilerplate-testing-3.html) I
describe usage of the following **pytest** features:

-   Changing behavior of **pytest** with `pytest.ini` and plug-ins.
-   Integration with **Django** and other frameworks.
-   Integration with `setup.py`
