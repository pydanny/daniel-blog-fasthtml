---
date: "2018-01-26"
description: Short answer is you don't use MongoDB with Django. Read on for the specifics.
published: true
slug: when-to-use-mongodb-with-django
tags:
  - python
  - django
  - mongodb
  - fastapi
  - rant
time_to_read: 4
title: When to Use MongoDB with Django
---

# Short Answer

You don't.

# Long Answer

First off, let's get one thing out of the way. This isn't a bash on
MongoDB. MongoDB works great with lots of things (FastAPI, Flask, node,
etc), but it's a mismatch with Django. In other words, this article is
about using the right tool for the right job.

Second, I'm not speaking from ignorance. In fact, I have quite a bit of
experience combining MongoDB and Django. You can see some of my early
work with combining these tools in the defunct
[django-mongonaut](https://github.com/jazzband/django-mongonaut).

Okay then, let's get into the background of this post: On various
Django help forums, you'll hear requests from new-ish Django developers
on how to use MongoDB with Django. Most of the time they want to replace
the Django ORM with calls to MongoDB. Here are the reasons I've heard
so far.

# The 90% Reason: JSON storage

Most of the time people want to replace SQL with MongoDB in Django, the
reason is they want to store JSON data and search it.

In which case, they should use [Django's built-in implementation of
MariaDB, MySQL 5.7.8+, Oracle, PostgreSQL, and SQLite's JSON
field](https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.JSONField).
It's not just a string field, it's fully searchable. Implementation
example below:

```python
from django.db import models


class Product(models.Model):

    metadata = models.JSONField(null=True, blank=True)
```

Just save your data into this field using a JSON-serializable dict.
It's that easy. Even better, in this previous
[article](/pretty-formatting-json-django-admin.html),
I show how you can pretty print the JSON in the Django admin.

Using this field, you get all the built-in features of Django and a
searchable JSON field without the mess of stapling a non-relational
database (MongoDB) into a framework and vibrant ecosystem designed to
work with relational databases (Django).

# The 5% Reason: Performance

A fraction of people want to use MongoDB with Django because of supposed
performance reasons. Sure, if you run MongoDB without any write
safeguards and decide to forego database transactions, it will run
faster than any relational storage. However, that's a dangerously
insecure approach to things. It's simply not worth the risk of
corrupted data.

Don't take my word for it, spend an hour searching for articles about
write safety in MongoDB. Ignore the hype articles published by
mongodb.com, read what real businesses and projects case studies have to
say.

Also, if you want to speed database i/o up with Django, standard
practice is to employ asynchronous tools such as Celery before switching
out the datastore.

# The 4% Reason: Scaling Up

Anyone who tells you that relational databases can't scale as well as
MongoDB (or anything else) is selling you something. Or was sold on
something and don't want to admit they bought the hype.

Again, don't take my word for it, spend an hour searching for articles
about scaling issues with MongoDB. Again, ignore the marketing and read
real case studies.

# The 1% Reason: Management

Every once in a while someone tells me that using MongoDB with Django is
a management decision. In which case, they should send their boss(es) to
this blog post.

Management should know that Django is designed to be used with a
relational database backend (PostgreSQL, MySQL) and a key/value store
for ephemeral data (Redis, Memcached). Going beyond that design is going
to make development slower and frustrate the team. Even if your team can
work around this issue, they'll be hampered by not being able to fully
exploit tools within the Django ecosystem.

# What about Djongo, django-nonrel, etc?

Some people will argue that third-party tools like Djongo create easy-to-use bridges between MongoDB and Django. That they provide DB connector that gets you nearly all the way. The creators/maintainers of these packages do heroic coding to make this happen.

All you have to worry about is the odd edge case, right?

Unfortunately, it's the edge cases that are the problem. Edge cases can make it impossible to proceed further without problematic hackery. I know this is true as I've gone down this path myself.

Complicating things is that if maintenance on a Django/MongoDB bridge package stops, what then? The Django ecosystem is [littered with dead Django/MongoDB connectors](https://djangopackages.org/search/?q=mongo).

The issue is that Django is deep and complicated enough that a MongoDB abstraction takes a lot of careful, finicky work. Each release of Django makes maintenance of the bridge that much harder. For reference, Djongo, a project built with [admirable skill and effort](https://www.djongomapper.com/django-mongodb-connector-design-document/) is as of August 12, 2022 two months without an update. This isn't a slam on the maintainers of Djongo (whose talents I admire), rather it is a realistic appraisel of the challenges of maintaining a non-SQL bridge connector to Django.

# If You Must Use MongoDB, Use FastAPI or Flask Instead

There's nothing wrong with MongoDB. However, it's suboptimal when used
with Django. If you use it with correct write permissions, MongoDB
doesn't provide any speed benefits with Django. You also lose many of
the advantages of Django (database transactions, rock-solid security,
forms, easy Django REST framework use, hundreds of third-party packages,
etc). There is quite a lot of things you are going to have to rewrite.

And if you're going to have to rewrite that much of Django's
functionality to use MongoDB, you might as well be using FastAPI or Flask.
Honestly, this isn't a bad choice, as the flexibility of those tools makes them
perfect for use with non-relational databases.

I know, because this is how I've both FastAPI and Flask previously, which is not with
relational data. I've built dozens of microservices that rely on DynamoDB.
While DynamoDB isn't MongoDB, they are similar enough that I can tell
you this approach is delightful.

# Updates

- 2022-08-12 Updated link to modern Django JSONField implementation
- 2022-08-12 Explain why bridges don't work
