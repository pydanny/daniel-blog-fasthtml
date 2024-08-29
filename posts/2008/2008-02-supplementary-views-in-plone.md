---
date: "2008-02-06T11:02:00.000-08:00"
description: ""
published: true
slug: 2008-02-supplementary-views-in-plone
tags:
  - plone
  - legacy-blogger
time_to_read: 5
title: Supplementary views in Plone
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/supplementary-views-in-plone.html)_.

I want to provide several views for certain content types for content loaders to choose from in our project. The suppl_views attribute in the archetype is the place to define these alternate views. So in your content type you have this:

```python
suppl_views = ('my_alternate_view',)
```

When the content loader goes to modify that particular content via the Plone front end, they could choose 'my_alternate_view' as one of the items under the **display** tab.

If you want to get fancy you can get this information in code as well:

```python
# returns the supplement views.
MyType.suppl_views
# gets Factory Type Info on the portal type
fti = MyType.getTypeInfo()
# Lists all the views for a type with the default one first.
fti.getAvailableViewMethods(MyType)
```

Very handy and works in both Plone 2.5x and Plone 3.0x.
