---
date: '2012-08-19'
published: true
slug: python-dictionary-vs-javascript-object
tags:
- python
- javascript
time_to_read: 1
title: 'Python dictionary vs JavaScript object: Dynamic Keys'
---

One of the things I noticed a long time ago with JavaScript is that when
you create objects you can define keys outside of strings:

``` javascript
> var o = {city: "San Francisco"}
  Object
```

In JavaScript, this is valid. In Python, you'll get a `NameError`:

``` python
>>> o = {city: "San Francisco"}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'city' is not defined
```

Normally this isn't too big of an issue, except when you want to use
JavaScript to create object keys based off of values in a variable.
Which means that while this code works fine in Python...

``` python
>>> region_name = 'state'
>>> o = {region_name: "Californa", "city": "San Francisco"}
>>> o["state"]
'Californa'
```

...it fails in JavaScript:

``` javascript
> var region_name = 'state'
  "state"
> var o = {region_name: "Californa", "city": "San Francisco"}
  Object
> o["state"]
  undefined
> o["region_name"]
  "Californa"
```

What this means is that if you want to define object keys dynamically in
JavaScript, you need to add an extra line(s) of code:

``` javascript
> var region_name = "state""
  "state"
> var o = {"city": "San Francisco"}
  Object     
> o[region_name] = "California" // Add dynamic key here
  "California"
> o["state"]
  "California"
```

Summary
=======

-   Python is consistent in how it deals with named objects. If you
    haven't named something, Python throws the `NameError`.
-   JavaScript seems to send out an `undefined` unless you are defining
    an object.
