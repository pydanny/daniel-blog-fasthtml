---
date: '2007-10-05T12:24:00.000-07:00'
description: ''
published: true
slug: 2007-10-case-sensitive-search-in-zope-297
tags:
- python
- zope
- legacy-blogger
time_to_read: 5
title: Case sensitive search in Zope 2.9.7
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/10/case-sensitive-search-in-zope-297.html)*.

I'm not 100% happy with this function, and I'm wondering if I'm doing too much work.  Especially waking up the object when the word "object" is not found in the `object.Description` attribute.  Is there a better way?

```python
def getWords(word):
   pc = app.msrd.portal_catalog
   results = []
   for brain in pc(SearchableText=word):
       if word in brain.Description:
           results.append(brain.getPath())
           continue
       try:
           content = brain.getObject()
           for field in content.schema.fields():
               name = field.dict['name']
               if 'body' in name or 'Body' in name:
                   accessor = field.dict['accessor']
                   text = contentaccessor
                   if word in text:
                       results.append(content.absolute_url())
                       continue
       except:
           continue
   return results
```