---
date: '2011-12-09T07:05:00.000-08:00'
description: ''
published: true
slug: 2011-12-my-basemodel
tags:
- django
- legacy-blogger
time_to_read: 5
title: My BaseModel
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/12/my-basemodel.html)*.

When I build projects in [Django](https://djangoproject.com) I like to have a 'core' app with all my common bits in it, including a [BaseModel](https://github.com/opencomparison/opencomparison/blob/master/apps/core/models.py). In that BaseModel I'll define the most basic fields possible, in this case a simple pair of created/modified fields built using custom [django-extension](https://djangopackages.com/packages/p/django-extensions/) fields. 

<pre class="prettyprint-py"># core/models.py
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.fields import CreationDateTimeField, ModificationDateTimeField

class BaseModel(models.Model):
    """ Base abstract base class to give creation and modified times """
    created     = CreationDateTimeField(_('created'))
    modified    = ModificationDateTimeField(_('modified'))
    
    class Meta:
        abstract = True
</pre>
You'll notice I also have core.fields defined. That is because (unless things have changed), django-extensions doesn't work with [South](https://djangopackages.com/packages/p/south/) out of the box. Hence the file below where I extend those fields to play nicely with my [migration tool](https://djangopackages.com/grids/g/database-migration/) of choice.

<pre class="prettyprint-py"># core/fields.py
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

class CreationDateTimeField(CreationDateTimeField):

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.DateTimeField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)    
        
        
class ModificationDateTimeField(ModificationDateTimeField):

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.DateTimeField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
</pre>
Unfortunately, this all shows up as red marks when I run [coverage.py](https://nedbatchelder.com/code/coverage/) reports. To deal with that I added in some tests. However, I'll readily I'm not super pleased with the tests below, but they are better then nothing, right?

<pre class="prettyprint-py"># core/tests/test_fields.py
from django.test import TestCase

from core.fields import CreationDateTimeField, ModificationDateTimeField

class TestFields(TestCase):
    
    def test_create_override(self):
        field = CreationDateTimeField()
        triple = field.south_field_triple()
        
        self.assertEquals(triple[0], 'django.db.models.fields.DateTimeField')
        self.assertEquals(triple[1], list())
        self.assertEquals(triple[2], {'default': 'datetime.datetime.now', 'blank': 'True'})
        
    def test_modify_override(self):
        field = ModificationDateTimeField()
        triple = field.south_field_triple()
        
        self.assertEquals(triple[0], 'django.db.models.fields.DateTimeField')
        self.assertEquals(triple[1], list())
        self.assertEquals(triple[2], {'default': 'datetime.datetime.now', 'blank': 'True'})
</pre>
<h3>Closing Thoughts</h3>My pattern is also If I need more stuff in this BaseModel I extend it with another abstract class instead of changing it. That way I can be sure at least this part works really well and any additions are isolated in another class.

I'll reiterate that I'm not happy with the tests. I'm open to suggestions. 

I pretty much got the BaseModel from [Frank Wiles](https://twitter.com/fwiles) of [RevSys](https://www.revsys.com/) back in the summer of 2010. What I added was sticking all the common bits into the core app, getting the South migration to play more nicely, and adding tests.

<h3>But much of this is moot!</h3><strong>Note</strong>: I added this segment several days after my original posting because of the stuff in the comments. Thanks [Jannis Leidel](https://twitter.com/jezdez) and someone named John - this is part of why I post. 

Jannis and John both pointed out that django_extensions now has a TimeStampedModel that does what my BaseModel does. They also pointed out that django_extensions comes with built-in South migrations for it's CreationDateTimeField and ModificationDateTimeField fields.

Which means thanks we can safely just do this and not worry about migrations:

<pre class="prettyprint-py"># core/models.py
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

class BaseModel(models.Model):
    """ Base abstract base class to give creation and modified times """
    created     = CreationDateTimeField(_('created'))
    modified    = ModificationDateTimeField(_('modified'))
    
    class Meta:
        abstract = True
</pre>

---

## 5 comments captured from [original post](https://pydanny.blogspot.com/2011/12/my-basemodel.html) on Blogger

**Sean O'Connor said on 2011-12-09**

Carl's [django-model-utils](https://bitbucket.org/carljm/django-model-utils/src) provides similar auto fields and base models that play nice with south.  Might be worth checking out :)

**John said on 2011-12-09**

I don't think you need your BaseModel abstract class at all as you don't need to add `created` and `modified` manually, just subclass the TimeStampedModel in django_extensions. I do this and don't need to do anything special to use south.
See https://packages.python.org/django-extensions/model_extensions.html

    from django_extensions.db.models import TimeStampedModel
    class MyModel(TimeStampedModel):
        # model now has 'created' and 'modified' fields
        pass

**pydanny said on 2011-12-09**

@John - I think this got added to django_extensions after I created my BaseModel class. But it's a wonderful development and I'm happy!

**Diederik van der Boor said on 2011-12-09**

Awesome idea to have the creationdate and modificationdate as base class fields.

In the recent Django versions (1.2?) it is no longer needed to have separate fields. You could also use:

created = DateTimeField(_('created'), auto_now_add=True)
modified = DateTimeField(_('modified'), auto_now=True)

Making the code even easier :-)

**pydanny said on 2011-12-15**

Diederik van der Boor,

auto_add_now and auto_add are deprecated. We aren't supposed to use them anymore. :D

