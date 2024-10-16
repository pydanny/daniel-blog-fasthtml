---
blogbook: 'True'
date: 2013-4-01
published: true
slug: fixing-pythons-string-class
tags:
- python
time_to_read: 4
title: Fixing Python's String class
---

Ever wonder why Python's `str` or `unicode` types lack obvious length
methods? Yes, we can get the length via the special `__len__()` method,
but instead as Python developers we get the so-called 'luxury' of
discovering length via the Python's built-in `len()` function. So
instead of calling the length of objects the way Rubyists or
Javascripters do...

``` ruby
>> # ruby
>> s = "Hello, World!"
=> "Hello, World!"
>> s.length
13
```

``` javascript
// javascript
var s = "Hello, world!"
console.log(s.length)
13
```

...as Python developers we suffer through it like this:

``` python
>>> # python
>>> s = "Hello, World!"
>>> len(s)
13
>>> s.__len__()  # This is what len() calls to get the length
13
```

I'm sure Python luminaries like Guido Van Rossum, Alex Gaynor, David
Beazley, and Raymond Hettiger can explain why Python works this way.
Their opinions are probably full of logic, history, and grand reasoning.

None of that applies to this blog post.

Fixing the String Class
=======================

Clearly, it's time for Python to catch up with the other hip dynamic
languages. Therefore, after years of careful study, I give you a Fixed
String class.

``` python
class String(str):
    """ Adding critically unimportant functionality to Python's str type """

    def len(self):
        return self.__len__()
```

As you can see it improves on Python's `str` type by adding a built-in
`len()` method. Total success!

Improving the String Class
==========================

Now that I've fixed things in Python by creating the `String` class,
it's time to improve it. Ruby and Javascript both have a length
property/attribute/method/thingee that even my `String` class lacks.
Ruby's String object even beats up Javascript's String Prototype by
including a handy `size` method that serves as an alias for it's own
`length` method.

Fortunately, I come armed with the knowledge of how to use Python's
`property` decorator:

``` python
class String(str):
    """ Adding critically unimportant functionality to Python's str type """

    def len(self):
        return self.__len__()

    @property
    def length(self):
        return self.len()

    @property
    def size(self):
        return self.length
```

Bam! Python is now equal to Ruby!

Winning with the String Class
=============================

It's time for Python to take the lead. We've suffered for too long as
second class citizens in terms of string length discovery. Let's add
some more utility methods to our String class:

``` python
class String(str):
    """ Adding critically unimportant functionality to Python's str type """

    def len(self):
        return self.__len__()

    @property
    def length(self):
        return self.len()

    @property
    def size(self):
        return self.length

    @property
    def width(self):
        return self.length

    @property
    def height(self):
        return self.length

    @property
    def area(self):
        return self.height * self.width
```

Boom! Python now dominates with invaluable properties that provide
developers with the width, height, and area of a string. And to think
I'm just getting started...

Conquering with the String Class
================================

So far I've carefully changed the Python ecosystem with my brilliant
addition to the language. What if I want to get stupidly dangerous? What
if I want to allow developers the **dangerous capability to alter the
returned length of a String**? Fortunately for me, and unfortunately for
anyone who uses this code on a real project, I know how to be this
stupidly dangerous.

I present to you the `ConqueringString` class:

``` python
import math

class ConqueringString(String):
    """ Adding stupidly dangerous functionality to Python's str type """

    def __init__(self, text):
        super(ConqueringString, self).__init__(text)
        self._length = self.__len__()

    def __len__(self):
        try:
            return self._length
        except AttributeError:
            return super(ConqueringString, self).__len__()

    def len(self, value=None):
        if value is None:
            return self._length
        self._length = value

    @property
    def length(self):
        return self.len()

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def size(self):
        return self.length

    @size.setter
    def size(self, value):
        self.length = value

    @property
    def area(self):
        return self.height * self.width

    @area.setter
    def area(self, value):
        self.length = math.sqrt(value)
```

Does it work?

``` python
if __name__ == "__main__":
    s = ConqueringString("Hello, World!")
    print(s)
    print(s.length)
    s.length = 5
    print(s.length)
    print(s.area)
    s.area = 50
    print(s.area)
    print(len(s))
    print(s[5:10]) # slicing still works!
    print(s.upper()) # other methods still work!
```

Run it and see. Or grab it off PyPI with `pip install stringtheory`.

Summary
=======

Don't forget `pip install stringtheory`!

We can implement this power using Python lists, tuples, dictionaries,
and everything else we can imagine. Let's do it!

Resources:

-   <https://github.com/pydanny/stringtheory>
-   <https://pypi.python.org/pypi/stringtheory>

April Fool's Joke
==================

This was my 2013 [April Fool's
Joke](/fixing-pythons-string-class.html#april-fool-s-joke).

However, the code was a lot of fun to write and after Mike Bayer's
comment about `__new__` and a number of serious questions that people
emailed me yesterday, I plan to follow this post with some more
discussion on how to expand on native types in Python.
