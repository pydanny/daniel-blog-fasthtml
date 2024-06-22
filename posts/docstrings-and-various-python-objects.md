---
date: "2014-03-05"
published: true
slug: docstrings-and-various-python-objects
tags:
  - python
time_to_read: 4
title: Docstrings and Various Python Objects
---

Early in my journeys with Python I struggled with understanding the
purpose and use of **lambda** functions. When I finally understood them
I was disappointed by their lack of **docstrings**. For that reason, and
various other shortcomings, [I went back to standard
functions](https://pydanny.blogspot.com/2007/07/lambdas-no-more.html).
Also, for what it's worth, I've even spoken about how [you shouldn't
use
lambdas](https://www.slideshare.net/pydanny/python-worst-practices/41).

Recently I was thinking about how everything in Python is an object.
This includes lambdas. Since all Python objects have the `__doc__`
special (aka 'magic') attribute, can we add custom docstrings to
everything?

Using [pytest](/pytest-no-boilerplate-testing.html),
Python 2.7.x, and lambdas, let's find out!

```python
# test_docstrings.py
import pytest

def test_lambdas():
    # Create a lambda and test it
    doubler = lambda x: " ".join([x, x])
    assert doubler("fun") == "fun fun"

    # Add a docstring to the lambda
    doubler.__doc__ = "Doubles strings"

    # Test that calling __doc__ works
    assert doubler.__doc__ == "Doubles strings"
```

Hey! It worked! If I try it in the shell, I can even see that the
`help()` function works:

```python
>>> # Welcome to the REPL!
>>> doubler = lambda x: " ".join([x, x])
>>> doubler.__doc__ = "Doubles strings"
>>> help(doubler)
Help on function <lambda> in module __main__:

<lambda> lambda x
    Doubles strings
```

Contrary to what I thought in 2007, Python lambdas _can_ be documented.
Modifying their docstring functions with both the direct `__doc___`
special attribute and the `help()` built-in works just fine.

## Should We Use Lambdas?

As demonstrated in this article, lambdas can be documented.
Nevertheless, I'm still not entirely convinced python lambdas should be
used as anything except when an anonymous function is advantageous, i.e
during functional programming.

## What About Other Python Types?

Enough about lambdas, let's see what else we can do with docstrings.

### Functions and Docstrings

We know modifying docstrings of functions works, so we'll use it as a
'control'.

```python
# appended to test_docstrings.py
def test_functions():
    # Create a function and test it
    def doubler(x):
        "Doubles strings"
        return " ".join([x, x])
    assert doubler("fun") == "fun fun"
    assert doubler.__doc__ == "Doubles strings"

    # Change the docstring
    doubler.__doc__ = "Really doubles strings"

    # Test that calling __doc__ works
    assert doubler.__doc__ == "Really doubles strings"
```

### Strings and Docstrings

Let's go for something a bit harder. Strings, for example, come with a
docstring, but as Python strings are immutable types, it's read-only
access:

```python
# more appended to test_docstrings.py
def test_strings():
    # Assert that strings come with a built-in doc string
    s = "Hello, world"
    assert s.__doc__ == 'str(object) -> string\n\nReturn a nice string' \
        ' representation of the object.\nIf the argument is a string,' \
        ' the return value is the same object.'

    # Try to set the docstring of a string and you get an AttributeError
    with pytest.raises(AttributeError) as err:
        s.__doc__ = "Stock programming text"

    # The error's value explains the problem...
    assert err.value.message == "'str' object attribute '__doc__' is read-only"
```

Hmmm... does this mean that we can't assign a docstring to a string?
What if we subclass Python's `str` type?

```python
# Again appended to test_docstrings.py
def test_subclassed_string():

    # Subclass the string type
    class String(str):
        """I am a string class"""

    # Instantiate the string
    s = String("Hello, world")

    # The default docstring is set
    assert s.__doc__ == """I am a string class"""

    # Let's set the docstring
    s.__doc__ = "I am a string object"
    assert s.__doc__ == "I am a string object"
```

This looks like it works, but it doesn't do enough. Specifically, this
doesn't satisfy the needs of Python's `help()` function when called
against the instantiated object.

```python
>>> # REPL again so we can call the help() function
>>> class String(str):
...     """I am a string class"""
...
>>> s = String("Hello, world") # instantiate the String Object
>>> s.__doc__ = "I am a string object"
>>> help(s) # Called against the 's' object, not the 'String' class.
Help on built-in module __builtin__:

NAME
    __builtin__ - Built-in functions, exceptions, and other objects.

FILE
    (built-in)

DESCRIPTION
    Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
...
```

You'll notice in the result of the `help()` call on the 's' object,
that the phrase, "I am a string object" does not exist.

## Conclusion

In Python, everything might be an object, but not all objects are
created equal. Lambdas (and functions and objects) do allow for
docstrings, but many, if not all basic types (strings, lists, classes,
etc) for Python do not.

I wonder if I scratch this particular itch long enough I might be able
to create a string-like class that handles the `help()` issue. If that
happens, maybe I'll add it to [String
Theory](/fixing-pythons-string-class.html). ;-)

**Resource**: The entire `test_docstrings.py` module:
<https://gist.github.com/pydanny/9373279>

![image](/images/lambda_scoops.png)
