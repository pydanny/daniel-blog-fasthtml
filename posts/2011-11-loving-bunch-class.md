---
date: "2011-11-02T13:40:00.000-07:00"
description: ""
published: true
slug: 2011-11-loving-bunch-class
tags:
  - geek celebrities
  - python
  - legacy-blogger
time_to_read: 5
title: Loving the bunch class
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/11/loving-bunch-class.html)_.

<blockquote><h3>Warning</h3>This is me playing around with things in Python. It's not anything I use in real projects (except maybe the odd test). Please don't use these in anything important or you'll regret it.</blockquote>Every play with a <b>bunch</b> class? I love 'em and make them protected or unprotected. I started using them early in my [Python](https://python.org) career, although it wasn't nearly about 2 years ago that I learned what they were called and the best way to code them. In any case, here is a simple, unprotected Bunch class.
<pre class="prettyprint-py"># Simple unprotected Python bunch class
class Bunch(object):

```python
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

bunch = Bunch(name='Loving the bunch class')
print(bunch.name)
```

You can also make protected ones, that don't let pesky developers like me overwrite attributes, methods, and properties by accident:

```python
# Simple protected Python bunch class
class ProtectedBunch(object):
    """ Use this when you don't want to overwrite existing methods and data """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.__dict__:
                self.__dict__[k] = v
```

You can also write them to raise errors when a <b>key</b> is in <b>self.**dict**</b>. Or perhaps merely publish a warning. There are many ways to customize, but generally you want to keep these things as simple as possible. Anyway, let's get back to the main topic...

In the early days of my experiences with Python I found a small, nagging issue with <b>dictionaries</b> and <b>objects</b>. The notation wasn't as handy as what you got with JavaScript and some other languages I was using at the time. For example:

```javascript
// JavaScript object notation
o = {};
o.name = "Loving the bunch class";
o.name; // Calling with 'dot' notation
o["name"]; // Calling with 'bracket' notation
```

Unfortunately, in Python you can't do this with a normal bunch class:

```python
# Python bunch class failing on bracket notation
class Bunch(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

bunch = Bunch(name='Loving the bunch class')
print(bunch.name)
print(bunch['name'])
Traceback (most recent call last):
  File "", line 1, in
TypeError: 'Bunch' object is not subscriptable
```

The quick answer is found with a [little trick I found](https://code.activestate.com/recipes/52308/#c2) in the comments of a recipie by [Alex Martelli](https://en.wikipedia.org/wiki/Alex_Martelli) that gives you the ability to do:

```python
# Fancy dictionary/object trick
class Buncher(dict):
    """ Warning: DON'T USE THIS IN REAL PROJECTS """

    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__.update(kw)

bunch = Bunch(name='Loving the bunch class')
print(bunch.name)
print(bunch['name'])
```

I'm not the only one who likes Bunch classes. On PyPI I found a [really complete implementation](https://pypi.python.org/pypi/bunch).

Of course, in a lot of cases you probably don't want this '<i>weight of code</i>', right? Dictionaries being lighter than full objects and all that. Nevertheless, it's fun for noodling and playing around with code. Still, I'm thinking it might be a fun little project to take a group of bunch implementations and do performance checks on them versus each other and dictionaries. Maybe the 'performance hit' isn't so bad.

I should also dig into things like [defaultdict](https://docs.python.org/library/collections.html#defaultdict-objects) and other constructs to learn more. Part of the fun of any programming language is the depth of even the 'simplest' components of the language.
