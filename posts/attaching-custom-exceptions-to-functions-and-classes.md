---
date: "2012-08-02"
published: true
slug: attaching-custom-exceptions-to-functions-and-classes
tags:
  - python
  - howto
  - django
time_to_read: 3
title: Attaching custom exceptions to functions and classes
---

Having too many custom exceptions on a project can be a pain, but a few
choices ones are really nice. The problem is that in complex libraries
having to import both functions and exceptions becomes a drag. To
mitigate having to remember to import custom exceptions, this is a handy
pattern you can use in a project and can be done on both functions and
classes.

# Attaching a custom exception to a function

This works because [Python](https://python.org) functions are first-class
objects. They can be passed around as things, and in this case, have
things assigned to them.

```python
# logic.py
class DoesNotCompute(Exception):
    """ Easy to understand naming conventions work best! """
    pass

def this_function(x):
    """ This function only works on numbers."""
    try:
        return x ** x
    except TypeError:
        raise DoesNotCompute

# Assign DoesNotCompute exception to this_function
this_function.DoesNotCompute = DoesNotCompute
```

Now I can import the function, and it won't just through
`DoesNotCompute` exceptions, it will also carry the function along with
the import:

```python
>>> from logic import this_function
>>> this_function(5)
3125
>>> this_function(4.5)
869.8739233809259
>>> this_function('will throw an error.')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "logic.py", line 10, in this_function
    raise DoesNotCompute
DoesNotCompute
```

Alright, that doesn't seem like much, but let's add in some exception
handling:

```python
>>> try:
...     this_function('is an example')
... except this_function.DoesNotCompute:
...     print('See what attaching custom exceptions to functions can do?')
...
...
See what attaching custom exceptions to functions can do?
```

# Attaching the custom exception to a class

All we have to do is enhance our existing logic.py file by adding
`ThisClass`:

```python
# logic.py
class DoesNotCompute(Exception):
    """ Easy to understand naming conventions work best! """
    pass

# removed the function example for clarity

class ThisClass(object):
    # Since the DoesNotCompute exception exists, let's just assign it
    # as an attribute of ThisClass
    DoesNotCompute = DoesNotCompute

    def this_method(self, x):
        """ This method only works on numbers."""
        try:
            return x ** x
        except TypeError:
            raise DoesNotCompute
```

Now to demonstrate in the shell (Python REPL for the semantic purists):

```python
>>> from t import ThisClass
>>> this_class = ThisClass()
>>> this_class.this_method(3.3)
51.415729444066585
>>> this_class.this_method('Jack Diederich warned against custom exceptions')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "logic.py", line 24, in this_method
    raise DoesNotCompute
DoesNotCompute
>>> try:
...     this_class.this_method('I need to write a follow-up on my OAuth post')
... except ThisClass.DoesNotCompute:
...     print('Waiting to see how the OAuth stuff pans out')
...
...
Waiting to see how the OAuth stuff pans out
```

# Admonition: Don't go crazy

Rather than use this trick all over the place, considering using it in a
few places to powerful effect. For example,
[Django](https://djangoproject.com) uses it only in a few places, and
publicly only on `MyModelClass.DoesNotExist` and
`MyModelClass.MultipleObjectsReturned`. By limiting Django's use of
this technique, Django libraries are that much easier to comprehend. In
this case, less complexity means more.

I say this because this pattern lends itself to creating custom
exceptions to the point of effectively replacing Python's stock
exceptions with your own. This makes for harder-to-maintain and
harder-to-learn projects.

Not that I've ever done that. Ahem.
