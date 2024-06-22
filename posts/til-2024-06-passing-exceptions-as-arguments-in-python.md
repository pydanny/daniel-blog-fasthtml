---
date: '2024-06-07T11:13:05.553336'
description: Mypy needs an extra identifier to not choke on an exception passed as
  an argument.
image: /logos/til-1.png
published: true
tags:
- TIL
title: 'TIL: Passing exceptions as arguments in Python'
twitter_image: /logos/til-1.png
---

*Mypy needs an extra identifier to not choke on an exception passed as an argument.*

This will throw a mypy error:

```python
# code.py
class MyException(Exception):
    pass


def myfunc(custom_exception: Exception) -> None:
    try:
        print('Test')
    except custom_exception:
        print('error)

myfunc(MyException)
```

The error mypy will throw looks something like this:


```bash
$ mypy code.py

code.py:6: error: Exception type must be derived from BaseException (or be a tuple of exception classes)  [misc]
code.py:9: error: Argument 1 to "custom_exception" has incompatible type "type[MyException]"; expected "Exception"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

The solution is to use `typing.Type`:


```python
# code.py
from typing import Type


class MyException(Exception):
    pass


def myfunc(custom_exception: Type[Exception]) -> None:
    try:
        print('Test')
    except custom_exception:
        print('error)

myfunc(MyException)
```
