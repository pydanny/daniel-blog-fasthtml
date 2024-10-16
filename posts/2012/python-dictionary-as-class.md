---
date: '2012-09-01'
published: true
slug: python-dictionary-as-class
tags:
- python
- howto
time_to_read: 3
title: Python dictionary as a class
---

A long time ago, circa 1999, when I was working in a certain procedural
language I found a library that added objects to the language. It did so
by playing interesting tricks with key/value structures, which in
[Python](https://python.org) are called dictionaries. In 2005, as a new
Python user, I read something about how objects in Python are
essentially dictionaries with [syntactical
sugar](https://en.wikipedia.org/wiki/Syntactic_sugar).

Well, today while driving from Los Angeles to San Francisco, I started
to try and figure out how to replicate object or class-like behavior
using Python dictionaries. In this exercise, I wanted to code out the
following:

> -   methods with ability to write to self/this/whatever
> -   inheritance

The result isn't something I would use in production code, but it was
fun to write. Without further ado...

I present the 'newclass' function!
====================================

What `newclass` does is simple:

> -   Document implementation of inheritance.
> -   Include a simple `set` method for setting attribute values to
>     self/this/whatever.

``` python
def newclass(**kwargs):
    """ Use kwargs.update() method to handle inheritance """

    def set(key, value):
        """ Sets key/value to the kwargs.
            Replicates self/this clumsily
        """
        kwargs[key] = value
    kwargs['set'] = set
    return kwargs
```

Now that you've seen the code, let's try it out.

Demonstration: Methods with ability to write to self/this/whatever
------------------------------------------------------------------

Instantiating a `newclass` 'object' is straight-forward. See below:

``` python
>>> person = newclass(
...     name="Danny",
...     mental_age=4,
... )
>>> print(person)
{'mental_age': 4, 'set': <function set at 0x10bc902a8>, 'name': 'Danny'}
>>> person['set']("languages", ['Python', 'JavaScript'])
>>> print(person)
{'languages': ['Python', 'JavaScript'], 'mental_age': 4, 'set': <function set at 0x10bc902a8>, 'name': 'Danny'}    
```

Setting a value to an attribute can be done via the `set` method is not
pretty, but it works. Yes, you can shortcut `set`, but I wanted to see
if it worked. That it's working is important because since `set` works,
it means we can create much more complicated methods that touch on many
parts of the newclass object context.

Just like a normal Python `class` and `method`.

Demonstration: Inheritance
--------------------------

Here I show how to use the `dict.update()` method to display
inheritance. I'll demonstrate via the use of the Mammal/Cat/Dog
example.

``` python
def Mammal(**kwargs):
    """ The mammal base class """

    # dict.update handles the role of inheritance
    kwargs.update(newclass())

    # Mammals have 4 legs
    kwargs['legs'] = 4

    # Using lambda cause I'm lazy.
    kwargs['say'] = lambda: NotImplemented
    return kwargs

def Cat(**kwargs):

    # dict.update handles the role of inheritance
    kwargs.update(Mammal())

    # Make a sound
    kwargs['say'] = lambda: "Meow"
    return kwargs

def Dog(**kwargs):

    # dict.update handles the role of inheritance
    kwargs.update(Mammal()) # dict.update handles the role of inheritance

    # Make a sound
    kwargs['say'] = lambda: "Bark"
    return kwargs
```

Alright, we have our code. What happens when we try it out?

``` python
>>> # first we try just the Mammal
>>> mammal = Mammal()
>>> print(mammal['say']())
NotImplemented
>>> print(mammal['legs'])
4
>>> # Now the Cat
>>> cat = Cat()
>>> print(cat['say']())
Meow
>>> print(cat['legs'])
4
>>> # Finally the dog
>>> dog = Dog()
>>> print(dog['say']())
Bark
>>> print(dog['legs'])
4
```

Conclusion
==========

Compared to normal Python classes the syntax is a little bit on the ugly
side. Yet this works and as I said earlier, it was fun to write.

Some questions...

-   Should I change the name of the internal context variable from
    `kwargs` to `self`?
-   How fast is `newclass` compared to the standard Python `class`
    system?
-   What happens if you use `newclass` in a complex project?
-   Shouldn't I implement some way to track inheritance chains?
    Wouldn't it be nice to know the parent of an object?
