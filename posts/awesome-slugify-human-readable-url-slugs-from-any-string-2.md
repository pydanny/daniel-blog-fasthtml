---
date: "2014-01-22"
published: true
slug: awesome-slugify-human-readable-url-slugs-from-any-string-2
tags:
  - python
  - django
  - unicode
  - i18n
time_to_read: 3
title: "awesome-slugify: Human-readable URL slugs from any string (part 2)"
---

In my previous [blog
post](/awesome-slugify-human-readable-url-slugs-from-any-string.html)
I covered using
[awesome-slugify](https://pypi.python.org/pypi/awesome-slugify) to
capture slugs in both ASCII and unicode. Today I'm covering the
definition custom language `slugify` translation functions.

## Defining Custom Language `slugify` Translation Functions

For those times we need ASCII representation of unicode characters, we
can't always use the default unicode-to-ASCII mappings. A powerful
feature of **awesome-slugify** is we can quickly and easily create our
own translation functions. Just follow these two steps:

1.  Define a translation dictionary. Keys are the names of things you
    want translated, and the associated values are what the keys are
    translated into.
2.  Generate a translation function using `slugify.main.get_slugify()`.

Explaining this in depth will take paragraphs of text, so I'll just
demonstrate it using [emoji](https://en.wikipedia.org/wiki/Emoji):

```python
# -*- coding: utf-8 -*-
# test_slugify_emoji.py

from slugify import get_slugify
import pytest

# Step 1: Define the translation dictionary
ALT_EMOJI = {
    u'ʘ‿ʘ': u'smiling',
    u'ಠ_ಠ': u'disapproval',
    u'♥‿♥': u'enamored',
    u'♥': u'love',
}

# Step 2: Generate a translation function
slugify_emoji = get_slugify(pretranslate=ALT_EMOJI)

def test_basic_emoji():
    assert slugify_emoji(u"ʘ‿ʘ") == u"smiling"
    assert slugify_emoji(u"ಠ_ಠ") == u"disapproval"

def test_sentence():
    txt = u"I ♥ Audrey Roy Greenfeld"
    assert slugify_emoji(txt) == u"I-love-Audrey-Roy-Greenfeld"

if __name__ == "__main__":
    pytest.main()
```

![I ♥ your unicode smile](/images/i-♥-your-unicode-smile.png)

### More Practical Applications

While writing an **emoji**-based translation function is fun, most of
the time we need more practical translation functions. Built into
**awesome-slugify** is a cyrillic translation function that works like
this:

```python
# -*- coding: utf-8 -*-
# test_slugify_cyrillic.py
from slugify import get_slugify
import pytest

# The following code is nearly identical to the source code of
#   awesome-slugify. All credit goes to Dmitry Voronin.

# Step 1: Define the translation dictionary
ALT_CYRILLIC = {
    u'ё': u'e',    # instead of 'io' / 'yo'
    u'ж': u'j',    # instead of 'zh'
    u'у': u'y',    # instead of 'u'
    u'х': u'h',    # instead of 'kh'
    u'щ': u'sch',  # instead of 'shch'
    u'ю': u'u',    # instead of 'iu' / 'yu'
    u'я': u'ya',   # instead of 'ia'
}

# Step 2: Generate a translation function
slugify_ru = get_slugify(pretranslate=ALT_CYRILLIC)

def test_some_cyrillic():
    txt = u"ж and я are really fun letters."
    assert slugify_ru(txt) == u"j-and-ya-are-really-fun-letters"

if __name__ == "__main__":
    pytest.main()
```

[Michael P. Jung](https://bikeshedder.com/) created a German translation
function, which I've included below:

```python
# -*- coding: utf-8 -*-
# test_slugify_german.py
from slugify import get_slugify
import pytest

# Step 1: Define the translation dictionary
ALT_GERMAN = {
    u'ä': u'ae',
    u'Ä': u'Ae',
    u'ö': u'oe',
    u'Ö': u'Oe',
    u'ü': u'ue',
    u'Ü': u'Ue'
}

# Step 2: Generate a translation function
slugify_de = get_slugify(pretranslate=ALT_GERMAN)

def test_german_dumpling():
    # According to Michael P. Jung, this looks like ice cream.
    assert slugify_de(u'Thüringer Klöße') == u"Thueringer-Kloesse"

def test_german_road():
    txt = u"I've never been in a car on a German straße"
    assert slugify_de(txt) == u"Ive-never-been-in-a-car-on-a-German-strasse"

if __name__ == "__main__":
    pytest.main()
```

## Summary

I really like the flexibility and power of **awesome-slugify**. During
slugification it provides functions to preserve unicode characters,
convert unicode characters to ASCII, and even define new translation
functions. As **awesome-slugify** is a relatively new project, there are
[a few issues](https://github.com/dimka665/awesome-slugify/issues), but
most of those are for my quirky edge cases (such as when trying to use
parenthesis in translation dictionaries for
[emoticons](https://en.wikipedia.org/wiki/Emoticons)) or perhaps stem
from my poor understanding of how unicode-to-ASCII functions.

In any case, this is a very useful package.

**Update 2013/01/23** Thanks to [Dmitry
Voronin](https://github.com/dimka665), I removed references to a couple
issues with **awesome-slugify**. It no longer forces capitalization in
custom translation functions and the `get_slugify()` can be imported
directly from the base `slugify` package.
