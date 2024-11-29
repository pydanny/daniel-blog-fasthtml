---
date: '2024-11-29T14:18:22.222177'
description: "Did you know there's a merge operator for Python dictionaries? I didn't until today!"
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: Python Dictonary Merge Operator'
twitter_image: /public/logos/til-1.png
---

## The function way

Until today I did this:

```python
# Make first dict
num_map = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
    'nine': '9'
}
# Add second dict
num_map.update({str(x):str(x) for x in range(1,10)})
print(num_map)
```

## The operator way

Now thanks to Audrey Roy Greenfeld now I know I can do this:

```python
# Make first dict while adding second dict
num_map = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
    'nine': '9'
} | {str(x):str(x) for x in range(1,10)}
print(num_map)
```