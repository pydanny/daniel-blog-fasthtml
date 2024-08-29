---
date: '2009-04-03T16:24:00.002-07:00'
description: ''
published: true
slug: 2009-04-what-i-would-change-in-plone-templates
tags:
- rant
- django
- plone
- zope
- legacy-blogger
time_to_read: 5
title: 'What I would change in Plone: Templates'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/04/what-i-would-change-in-plone-templates.html)*.

These are my thoughts. My thoughts are not those of the luminaries in any community, but just your average Joe Developer. I formed these thoughts over [Pycon 2009](https://us.pycon.org/2009), and my experiences with [Plone](https://plone.org), [Zope](https://zope.org) over 2 odd years and [Django](https://djangoproject.com) over the past 4-5 months. A lot of this is therefore inspired by my recent experiences with Django.

<span style="font-weight: bold;">Item #1 - Plone/Zope needs Django Templates out of the box</span>

You heard me.

I like the Template Attribute Language (TAL). TAL is stupid. Stupid in that it is very hard to encrypt my templates with business logic. I like this because I recognize I have no discipline when it comes to breaking the Model-View-Controller paradigm if a framework lets me. I also like TAL because it lets me create XML type documents very easily.

I like the Django Template Language (DTL). DTL is stupid. Stupid in that it is very hard to encrypt my templates with business logic. I like this because I recognize I have no discipline when it comes to breaking the Model-View-Controller paradigm if a framework lets me. I also like DTL because it lets me create non-XML type documents very easily.

I like both languages. Some people do not. Advocates of one template system style say very snarky things about the other template system style. Inevitably it comes down to that one is XML focused and the other is not. And from their point of view, they are completely right.

So I think that a version of DTL should be ported to the Plone/Zope world. And for Plone, it should be made readily available out of the box. This port should do all the default DTL filters and as many of the default tags as possible.

Which would I use? I would use either. More importantly, people who love XML based templates could use what they want and people who hate XML based templates could use what they want.

Everybody wins.

<span style="font-weight: bold;">Item #2 - Plone TAL documentation needs a cheat sheet of the good functions</span>

For Django, I can go to the [DTL tag/filter page](https://docs.djangoproject.com/en/dev/ref/templates/builtins/) and find a handy reference on all the tags and filters available out of the box with Django.

Where is the same with Plone? The documentation has gotten really <span style="font-weight: bold;">freaking</span> good, but where is this sort of handy developer reference?

Yes, I have learned that you can use string methods on strings, and that there are various utility methods you can call if you know the name of the right portal object, but these are not in one easy-to-find location.

We Joe Developers need and love this sort of thing.

---

## 6 comments captured from [original post](https://pydanny.blogspot.com/2009/04/what-i-would-change-in-plone-templates.html) on Blogger

**pydanny said on 2009-04-03**

@Alex Clark: This is a great document. But it is more description of usage of TAL and Macros, rather than a list of all the functions and methods available.

**Ian Bicking said on 2009-04-03**

If you want something <i>like</i> Django Templates, you should certainly use [Jinja](https://jinja.pocoo.org/2/).

**Martin Aspeli said on 2009-04-03**

I'm not sure everybody wins if we have two template languages. It means two things to learn for new developers, two things to test and maintain for the core developers, and I bet it'd be pretty hard to re-use a macro/snippet from one template in another.

I agree that non-XML templating should be easier. chameelon.zpt helps here by allowing standalone ${name} variable interpolations. Three may be a case for a different language for non-XML/HTML pages even, but not for producing HTML output.

**pydanny said on 2009-04-04**

@Ian Bicking: Thanks for suggesting jinja2. I've discovered this morning that getting Django templates to run inside of Plone is not trivial, but getting Jinja templates to run is. :)

**pydanny said on 2009-04-04**

@Martin Aspelli: While it does mean two things to learn for new developers, it also means that people who don't like (or more likely HATE - yes HATE in caps) XML style template have another option. 

As for getting DTL to run in Plone of 5 minutes of research leads me to believe it is not trivial. Yet another 5 minutes demonstrated that getting Jinja2 templates to run in Plone is. From inside a Plone debug shell:

&gt;&gt;&gt; from jinja2 import Template
&gt;&gt;&gt; t = Template('{{ name }} rocks!')
&gt;&gt;&gt;  t.render(name='Guido')
u'Guido rocks!'

Reusing TAL inside of Jinja2 and Jinja2 inside of TAL is another. But using Jinja2 as a template language inside Plone/Zope/Grok python code is easy. Which makes me wonder how useful it would be for helping to render AJAX, especially combined with KSS. I plan to write a blog post about this very subject.

**pydanny said on 2009-04-05**

@Alex: That cheat sheet is <b>awesome</b>. I learned some template tricks I didn't know just by looking at it. Now if we can just get a HTML version of it in the formal Plone docs I would be done complaining about this issue. :)

