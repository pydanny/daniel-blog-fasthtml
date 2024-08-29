---
date: "2007-06-12T05:12:00.000-07:00"
description: ""
published: true
slug: 2007-06-thought-on-methods-in-plone
tags:
  - plone
  - zope
  - legacy-blogger
time_to_read: 5
title: A thought on methods in Plone
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/06/thought-on-methods-in-plone.html)_.

We just did a sprint on our big project at work. My first step was to create a bunch of methods in the content types that would traverse between items via the reference catalog (yes Virginia, we are using the Relations product along with Association Classes `getArchGenXML`).

Our first thought was to return a `tuple` of the title, description, and url of the referred item. Well, that turned out to be annoying because:

```html
<div content="python:item[1]"></div>
```

is not as much fun as:

```html
<div content="item/description"></div>
```

Also, for the graphic designers, having them start typing '`python:`' everywhere just seemed like fighting a battle we didn't need to fight.

Then we decided to return a dictionary containing title, url, and description. And in some cases, acronym, image, and more. Now we have:

```html
<div content="item/description"></div>
```

Hooray! Except that there are about 10+ and growing examples now of times when we missed something that needed to be returned.

So it hit me, why not just return the darn catalog brain? Sure, `reference_catalog` doesn't return a usable URL (you have to strip off the `/at_reference/md5_hash`), but I've already written an often reused python script that does this called `cleanUrl`. If we went this method, we get:

```html
<div content="itemBrain/description"></div>
```

And if we hit another snag where we need to also return field x, y, and z, we have them do this:

```html
<div define="item python:itemBrain.getObject()"
      content="item/funnyQuote"></div>
```
