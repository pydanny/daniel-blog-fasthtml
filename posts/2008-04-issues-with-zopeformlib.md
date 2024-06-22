---
date: "2008-04-04T04:18:00.004-07:00"
description: ""
published: true
slug: 2008-04-issues-with-zopeformlib
tags:
  - django
  - interfaces
  - zope
  - legacy-blogger
  - forms
time_to_read: 5
title: Issues with zope.formlib
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/04/issues-with-zopeformlib.html)_.

**Disclaimer**: _I am not an expert on Zope 3, much less Five, which lets you integrate Zope 3 technology into your Plone efforts. on the other hand, that arguably lets me speak as joe developer trying to meet a deadline, so I think things balance out._

I was tasked with extending a Five based package to include several extra new forms. This post details my efforts, what pleases me about zope.formlib and what annoys me.

Zope.formlib is a Zope 3 product that lets you create HTMl forms with handy bits of Python code. In general I like this approach, because if done right it means less work (thanks to DRY or Don't repeat yourself), and instead of just hand-coding the same form elements again and again - you utilize easily understood libraries that take advantage of inheritance and polymorphism.

Since we weren't storing any of the data I just extended a few existing interfaces, added a new view, a new response template written in a few lines of TAl, and tied it together with ZCMl. It was very straightforward and I had lots of fun. I had done a few bits before with zope.formlib and things were so easy I was delighted. Zope technology is like this, in that you can accomplish tasks quickly.

The basic form looked good, the form submission worked without a hitch, now I just needed to change some checkboxes to radio buttons. I didn't do it earlier because the documentation didn't have that described, but I figured it would essentially be really fundamental to the bool type in zope.schema (for you Django folks, Zope schemas can be likened to your models).

After many efforts at googling the answer I was nowhere. I dove into my 3rd edition copy of Web Component Development with Zope 3. No answer. I started checking the Zope 3 APIDOCs which has tons of information but nothing on turning a field/attribute into a radio button. I did introspection everywhere and might have stumbled across it eventually but a coworker made a suggestion that answered the problem.

So that was done. Now I wanted to encapsulate my forms in a set of macros that other products could easily use. I wanted to wrap SubPageForms in template macros containing form tags so whoever used these forms just needed to a macro include. Again the documentation was lacking, and for the release going as I write this, we created a temporary work around.

So there are described a couple major annoyances. Another one to list right now would be that anything besides a template change in Zope 3 based technology requires a server restart. Now pardon me for saying this, but I thought modern application servers did refresh.

Now keep in mind that when I wasn't trying to unearth the hidden mysteries of zope 3 and five or waiting for my server to restart yet again, I was incredibly productive. The frustrating thing was enough time was wasted with monkeying around zope.formlib that I could have written the TAl for the forms and then used old style Plone forms and been done much more quickly. Yes, I won't make the same mistake again, but I shouldn't have had to poke around as long as I did.

Alright, it may not be quite that bad. But it's bad enough. In my opinion, every HTMl formlib should have in its core documentation working examples of all the standard HTML input tag types. Text, textarea, checkboxes, radio buttons, and so forth.

For example, with the Django Newforms library, you have clear documentation of how to substitute one widget type for another. You are also clearly told that the forms library does not handle wrapping your input fields with form tags. Zope.formlib, combined with the rest of the Zope 3 API is much more powerful, but the Django documentation makes it much more accessible. Here is the Django newforms documentation if you are curious:

[https://www.djangoproject.com/documentation/newforms](https://www.djangoproject.com/documentation/newforms)

And here is the current zope.formlib documentation:

[https://pypi.python.org/pypi/zope.formlib/3.4.0](https://pypi.python.org/pypi/zope.formlib/3.4.0)

The former is complete while the latter is verbose. That's an important distinction.

Just so it is known, I'm wouldn't mind documenting zope.formlib more and putting it somewhere useful on the web once someone gives me a good suggestion as to where to put it.

In any case soon after these issues were resolved I was essentially done and most of the remaining work is/was dealing with the normal sort of last minute unwritten requirements that makes life 'so much fun'. In fact, I rolled out another form in record time and using zope.formlib. I had fun! Just the learning experience was not.

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2008/04/issues-with-zopeformlib.html) on Blogger

**reedobrien said on 2008-05-01**

I disagree. The primary difference I see in the two document is styling.

Another thing to note is the zope.formlib stuff on pypi is also a doctest.

Further more if you want to read documentation you should follow the zope pattern and read the interfaces:

Interfaces are objects that specify (document) the external behavior of objects that "provide" them. An interface specifies behavior through:

_ Informal documentation in a doc string
_ Attribute definitions \* Invariants, which are conditions that must hold for
objects that provide the interface

You could also use z3c.form and if django.newestforms is avaiable as an egg you could use that too...

I don't know much about Django, so I am not knocking it...but I don't have any problems with zope.formlib either.
