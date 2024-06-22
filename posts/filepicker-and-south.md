---
blogbook: 'True'
date: 2013-4-23
published: true
slug: filepicker-and-south
tags:
- django
- python
- howto
time_to_read: 2
title: Filepicker.io and South
---

I've heard good things about filepicker.io, which is a service that
makes file uploading a much better experience. Unfortunately, the Django
package for filepicker.io doesn't work with South. When I try to create
a migration using the filepicker.io field using code like the
following...

``` python
# products/models.py
from django.db import models
from django_filepicker.models import FPFileField

class Product(models.Model):
    title = models.CharField(max_length=255)
    file = FPFileField(upload_to='uploads')
```

...when I try to run the command:

    (tsd)$ python manage.py schemamigration products --initial

It results in this unpleasant looking response:

    (tsd)$ python manage.py schemamigration products --initial
    Creating migrations directory at '/Users/danielgreenfeld/code/tsp/tsp/products/migrations'...
    Creating __init__.py in '/Users/danielgreenfeld/code/tsp/tsp/products/migrations'...
     ! Cannot freeze field 'products.product.fpfile'
     ! (this field has class django_filepicker.models.FPFileField)
     ! Cannot freeze field 'products.release.fpfile'
     ! (this field has class django_filepicker.models.FPFileField)

     ! South cannot introspect some fields; this is probably because they are custom
     ! fields. If they worked in 0.6 or below, this is because we have removed the
     ! models parser (it often broke things).
     ! To fix this, read https://south.aeracode.org/wiki/MyFieldsDontWork

The last line in the error report is important. I'll repeat it to
illustrate it more clearly:

    ! To fix this, read https://south.aeracode.org/wiki/MyFieldsDontWork

Experience working on other projects has taught me I can simply add two
lines of code to `products/models.py` and everything should just work:

``` python
# South migration rules for the FPFileField field
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["django_filepicker.models.FPFileField"])
```

In case it's not clear, here's my new `products/models.py` file:

``` python
# products/models.py
from django.db import models
from django_filepicker.models import FPFileField

# South migration rules for the FPFileField field
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["django_filepicker.models.FPFileField"])

class Product(models.Model):
    title = models.CharField(max_length=255)
    file = FPFileField(upload_to='uploads')
```

Now I can create South migrations and they'll just work.

Unfortunately, the problem is that for any model where I need to use
filepicker's FPFileField I need to add those two lines of code. I
don't like this approach, since it violates **Don't Repeat Yourself**
(DRY).

At some point I'll demonstrate how to fix this violation of DRY with an
easy fix. In fact, I plan submit that fix as a pull request to
django-filepicker.

**Update 2013/12/24:** django-filepicker has been patched to address
this issue. This blog post therefore describes a historical version of
the package.
