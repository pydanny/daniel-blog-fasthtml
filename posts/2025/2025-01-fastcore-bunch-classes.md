---
date: "2025-01-01T19:30:00.00Z"
description: "For the past six months or so I've been using fastcore. It provides two handy bunch-class style that I've leveraged into projects."
published: true
tags:
  - python
  - fastcore
  - bunch
time_to_read: 2
title: "Exploring fastcore bunch classes"
type: post
---

The fastcore library has a lot of really useful tools. As a fan of bunch classes, here's two useful utilities for working with them.

## AttrDict

`AttrDict` adds attributes to python `dict` without changing equality or how it prints.


```python
from fastcore.basics import AttrDict
```

```python
daughter = AttrDict(name='Uma', age=6)
daughter
```

```json
{'age': 6, 'name': 'Uma'}
```



Equality is the same as a `dict`.


```python
daughter == {'age': 6, 'name': 'Uma'}
```




    True



Values can be accessed either as `dict` or with `dot` notation.


```python
daughter['name']
```




    'Uma'




```python
daughter.name
```




    'Uma'



## NS

`NS` extends `types.SimpleNamespace` (which I covered [here](/posts/til-2024-12-types-simplenamespace-is-a-bunch-class)), providing useful access functionality similar to that of `AttrDict`. Unlike `AttrDict`, equality is not that of a `dict` and is covered below.


```python
from fastcore.basics import NS
```


```python
daughter = NS(name='Uma', age=6)
# daughter
```




    namespace(name='Uma', age=6)



Equality of `NS` is with `types.SimpleNamespace`, which is the difference between it and `AttrDict`, whose equality is as a `dict` type.


```python
import types
daughter == types.SimpleNamespace(name='Uma', age=6)
```




    True



Values can be accessed either as `dict` or with `dot` notation.


```python
daughter['name']
```




    'Uma'




```python
daughter.name
```




    'Uma'




```python
list(daughter)
```




    ['name', 'age']


