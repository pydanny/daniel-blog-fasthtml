---
date: '2024-01-19T12:00:00'
description: To my surprise writing decorators for classes is easier than for functions.
published: true
tags:
- TIL
- python
title: 'TIL: Writing decorators for classes'
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

To my surprise writing decorators for classes is easier than for functions. Here's how to do it in annotated fashion with an unnecessary decorator that doesn't accept any additional arguments.

```python
# Write a callable that accepts a cls as an argument 
def tools(cls):
    # Write functions that accept "self: object" as an argument.
    def simplistic_attribute_count(self: object) -> int:
        """Returns the number of attributes."""
        return len(self.__dict__)

    def docs(self: object) -> str:
        """Returns the docstring for the class."""
        return self.__doc__

    # Attach the functions as methods
    cls.simplistic_attribute_count = simplistic_attribute_count
    cls.docs = docs

    # Return the modified class
    return cls
```

Let's test it out:

```python
@tools
class A:
    """Docstring for testing the tools decorator"""


a = A()
a.one = 1

assert a.simplistic_attribute_count() == 1
assert a.docs() == 'Docstring for testing the tools decorator'
```

Next up, how to do this while passing in arguments!