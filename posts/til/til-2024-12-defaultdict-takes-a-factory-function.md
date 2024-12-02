---
date: '2024-12-02T22:32:41.336588'
description: Create a dictionary-like object that takes a factory function so you
  have lots of control over what the default value can be.
image: /public/logos/til-1.png
published: true
tags:
- TIL
title: "TIL: Python's defaultdict takes a factory function"
twitter_image: /public/logos/til-1.png
---

I've never really paid attention to this object but maybe I should have. It takes a single argument of a callable function. If you put in Python types it sets the default value to those types. For example, if I use an `int` at the instantiating argument then it gives us a zero.

```python
>>> from collections import defaultdict
>>>
>>> mydict = defaultdict(int)
>>> print(mydict['anykey'])
0
```

Note that defaultdict also act like regular dictionaries, in that you can set keys. So `mydict['me'] = 'danny'` will work as you expect it to with a standard dictionary.

It gets more interesting if we pass in a more dynamic function. In the exmaple below we use `random.randint` and a `lambda` to make the default value be a random number between 1 and 100. 

```python
>>> from random import randint
>>>
>>> random_values = defaultdict(lambda: randint(1,100))
```

Let's try it out!

```python
>>> for i in range(5):
>>>     print(random_values[i])
>>> print(random_values)
29
90
56
42
70
defaultdict(<function <lambda> at 0x72d292bb6de0>, {0: 29, 1: 90, 2: 56, 3: 42, 4: 70})
```

Attribution goes to Laksman Prasad, who pointing this out and encouraging me to closer look at `defaultdict`.