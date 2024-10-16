---
date: '2012-02-20'
published: true
slug: parsing-mongodb-uri
tags:
- python
- mongodb
- howto
time_to_read: 1
title: Parsing MongoDB URI
---

Rather than hard-code the configuration into a Python based settings
file, when using a PaaS such as Heroku you want to pick up the MongoDB
URI from the system settings. Here's what I do:

``` python
# get the dynamic elements from the MongoURI
import os
import re
r = r'^mongodb\:\/\/(?P<username>[_\w]+):(?P<password>[\w]+)@(?P<host>[\.\w]+):(?P<port>\d+)/(?P<database>[_\w]+)$'
regex = re.compile(r)
mongolab_url = os.environ['MONGOLAB_URI']
match = regex.search(mongolab_url)
data = match.groupdict()

# Save the data to settings
MONGO_HOST = data['host']
MONGO_PORT = int(data['port'])
MONGO_NAME = data['username']
MONGO_DATABASE = data['database']
MONGO_PASSWORD = data['password']

# Connect to MongoEngine
from mongoengine import connect as me_connect
me_connect(
    data['database'], 
    host=data['host'], 
    port=int(data['port']), 
    username=data['username'], 
    password=data['password'])    
```
