---
date: '2024-10-12T19:30:31.796570'
description: Here's a quick reference guide for Python's csv module. I use it periodicially, but not enough that I memorize the API. 
published: true
tags:
- howto
- python
- cheatsheet
title: Python CSV Cheatsheet
---

Here's a quick reference guide for Python's csv module. I use it periodicially, but not enough that I memorize the API. 

## csv.DictWriter

Works for when you have an iterable containing a list of dictionaries containing keys that match the values in the `fieldnames` list.

```python
import csv

lst = [
    {'first_name': 'Daniel', 'last_name': 'Roy Greenfeld'},
    {'first_name': 'Audrey', 'last_name': 'Roy Greenfeld'},
    {'first_name': 'Uma', 'last_name': 'Roy Greenfeld'}
]

with open('family.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in lst:
        writer.writerow(row)
        print(row)
```

```python
{'first_name': 'Daniel', 'last_name': 'Roy Greenfeld'}
{'first_name': 'Audrey', 'last_name': 'Roy Greenfeld'}
{'first_name': 'Uma', 'last_name': 'Roy Greenfeld'}
```

## csv.DictReader

Reads the first row as column names, then constructs dictionaries that contain values from the row columns.

```python
import csv
with open('family.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
```

```plaintext
Daniel Roy Greenfeld
Audrey Roy Greenfeld
Uma Roy Greenfeld
```