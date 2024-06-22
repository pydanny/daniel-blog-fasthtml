---
date: '2010-12-03T05:57:00.000-08:00'
description: ''
published: true
slug: 2010-12-stupid-template-languages
tags:
- rant
- django
- javascript
- plone
- python
- xml
- zope
- legacy-blogger
time_to_read: 5
title: Stupid Template Languages
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/12/stupid-template-languages.html)*.

For years I've been absolutely certain that I really prefer stupid template languages any time I'm generating HTML. The less the template language can do the better. Since I spend most of my time coding in [Python](https://python.org/) you might assume this applies just to Python, but I think it also applies to anything where you have the power to readily mix HTML generation and code.

The biggest annoyance I have with smart template languages ([Mako](https://www.makotemplates.org/), [Genshi](https://genshi.edgewall.org/), [Jinja2](https://jinja.pocoo.org/), [PHP](https://php.org/), [Perl](https://www.perl.org/),&nbsp;[ColdFusion](https://en.wikipedia.org/wiki/ColdFusion),&nbsp;etc) is that you have the capability to mix core business logic with your end views, hence violating the rules of Model-View-Controller architecture. While the web can be hard to match to MVC, in general you aren't supposed to do that sort of thing.&nbsp;I've made the mistake of putting core logic in the wrong places in the past, but I'm proud to say I've gotten good at avoiding that particular mistake.

<b>I don't work in a vacuum.</b>

I often work on projects crafted by others, some who decided for arcane/brilliant/idiotic reasons to mix the&nbsp;kernel&nbsp;of their applications in template function/macros. This is only possible in Smart Template Languages! If they were using a Stupid Template Language they would have been forced put their kernel code in a Python file where it applies, not in a template that was supposed to just render HTML or XML or plain text.

What it comes down to is that Smart Template Languages designers assume that developers are smart enough to avoid making this mistake. Stupid Template Languages designers assume that developers generally lack the discipline to avoid creating horrific atrocities that because of unnecessary complexity have a bus factor of 1.

<b>So what is a Smart Template Language?</b>

<div style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;"><b></b>In my own vernacular, template languages that let you write functions/macros are what I call a <b>Smart Template Language</b>. Some of them are brilliantly executed, the example of Jinja2 comes to mind, but invariably I suffer through abuse of its Macro control structure as implemented by others.</div><div style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;"><b>
</b></div><div style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;"><b>Misery Cubed a.k.a. Genius Template Languages</b></div>
Next comes&nbsp;<b>Genius Template Languages</b>, which take things a step further. These template languages allow you to not only define functions/macros, but also let you embed unrestricted Python (or [Java](https://www.ruby-lang.org/en/) or [Ruby](https://www.ruby-lang.org/en/) or whatever) in the template. This 'feature' lets you code your entire application in the templates! &nbsp;In the Python world what comes to mind is Mako and Genshi, but I'm sure there are many other tools with this 'capability'.

<b>I like Stupid Template Languages!</b>

<b></b>Stupid Template Languages don't let you define functions/macros. They don't let you embed Python code. They barely let you define variables and often have simplistic control architectures.

For Django efforts, which is about 70% of my work, I like the [Django Template Language](https://docs.djangoproject.com/en/dev/topics/templates/) (DTL). Since it is used by a huge community, there are a ton of useful apps which have it as a dependency. Switching away from it would mean cutting myself off from a [large ecosphere of tools](https://djangopackages.com/)&nbsp;I can use to not reinvent the wheel.

Back in my [Zope](https://bluebream.zope.org/)/[Plone](https://plone.org/) days I really, really enjoyed the [Template Attribute Language](https://en.wikipedia.org/wiki/Template_Attribute_Language) (TAL) because it was stupid too. If I needed an XML generation template language and could import it easily I might consider using it again, or perhaps [Chameleon](https://chameleon.repoze.org/docs/latest/zpt.html), which is a new, improved version . The downside is that they come paired with another tool paired with it, METAL, which gave it macros. My own experience with METAL is that it was all too easy to do what we developers do with Smart Template Languages.

<b>But DTL and TAL are slow!</b>

<b></b>So what?

If you want to boost your performance, first try caching. There are a ton of tools you can use, with [Varnish](https://www.varnish-cache.org/) being one I keep seeing in action. Read the docs on your favorite web framework's caching engine and apply what you learn. And Djangonauts should read up on [Mike Malone](https://www.slideshare.net/mmalone/scaling-django-1393282) as much as possible.

If after all that the site still delivers slow content and it appears to be a template language issue, then identify the bottleneck content and consider alternatives for that one portion. My favorite response is a bit of [AJAX](https://en.wikipedia.org/wiki/AJAX). Use your framework to render the content as [JSON](https://en.wikipedia.org/wiki/JSON) and have [JavaScript](https://en.wikipedia.org/wiki/JavaScript) parse it into legible content, a task which [JQuery](https://en.wikipedia.org/wiki/JQuery) makes trivial.

---

## 12 comments captured from [original post](https://pydanny.blogspot.com/2010/12/stupid-template-languages.html) on Blogger

**pydanny said on 2010-12-03**

Hanno,

Thanks for the clarification. Chameleon looks awesome, and if I ever used it I would write something that would check for xmlns:metal=&quot;https://xml.zope.org/namespaces/metal&quot; in the templates and raise an error if it found it. :)

**Unknown said on 2010-12-03**

Look at Twig and PHPTAL (for PHP templates)

**pydanny said on 2010-12-04**

Petri - You are correct, METAL indeed does not let you put business logic in your templates. But it lets you hide critical parts of your views in obscure places. How do I know? I did it myself!

**pydanny said on 2010-12-04**

huxley - Brilliant! https://www.codeirony.com/?p=9

**brad clements said on 2010-12-04**

Hmm, I don't recall seeing any logic features in metal.  I don't quite see how business logic can be implemented using metal because it doesn't have any control flow terms. (vs. tal:condition)

anyway I have a TAL implementation in xsl that also does METAL. I love it, I use it client side in the browser or server side with libxslt or lxml.

I also have a javascript version of just tal, client-side.. works well enough for my needs.

**cats2ndlife said on 2010-12-04**

You can turn off Python code blocks in Genshi's configurations. You can also do that in ASP and JSPs too. If you don't want your team to put code blocks in templates, just turn it off. I always do that with Genshi and JSPs. While I agree with you on most of the points, I don't see having code blocks support in the template language is such a big deal. There are many instances using code blocks is clearer/easier to reason with. The only reason I turn off code blocks is because I don't want to mess up my markup IDE.

**Eric said on 2010-12-04**

The way we use templating engines are really counter to the way that HTTP and hypertext was designed. 

There's an aspect of hypertext that we rarely talk about, but use blindlessly when we put an image on a page.  It's the idea of transclusions.  We use it all the time to insert an image on a page, but we rarely use it to include text on a page.

I have found with some preliminary testing that by using RESTful resources, which can be cached edge side and then transcluding the resources client side with Ajax or &quot;iframe seamless&quot; performs extremely well.


You can see a preliminarily example of doing client-side
transclusion at this URI:

https://dl.dropbox.com/u/1890692/hyperblog/index.html

That URI presents two resources, an index page and an entry page with all the redundant site elements into the HTML pulled in using current transclusion techniques.

If you view the source code on that page, you can see how the header and footers, because they are site elements and not resource elements, they're transcluded client side, just like any other static content.  They can utilize the benefits of edge-side and client-side caching because they rarely change.  This makes the only thing actually in the response, the actual resource being requested, which can be cached independently of the header and footer. 

I am not sure how constructive or destructive to SEO this is.  I'd like to think that since only the relative resources are in the HTML, that it would help SEO because the HTML is a highly concentrated view of the content instead of a diluted version with dozens of unrelated links in the header and navigation.

**pydanny said on 2010-12-06**

@cats2ndlife - Turning off Python code blocks in Genshi's configuration sounds useful, but my contention is that it shouldn't have the code blocks there in the first place.

**pydanny said on 2010-12-06**

@jalpino - I think a language or tool should be flexible, but a few hard or soft rules mean the difference between a big plate of spaghetti code and a maintainable project.

For example, a lot of people don't like Python's use of whitespace to delineate code blocks. Yet I consider that a feature and probably 95% of the Python community agree with me. Should we add a setting to Python that lets you have the flexibility to turn that feature off or on as your developer feels it suits their needs?

**Sergey Shepelev said on 2010-12-06**

Don't you feel like Stupid Template Languages must be far faster than Smart ones? And the opposite sounds like a huge fail in, DTL, in particular?

**pydanny said on 2010-12-06**

@temoto - Are you saying that stupid must mean fast and DTL is slow? And that is a big failure of DTL?

The speed of your template language is generally a small issue when it comes to performance problems and is normally the last thing you need to worry about. Which is why this article is so amusing! https://www.codeirony.com/?p=9

In a nutshell, before you care about template performance, take a look at business logic and database access speeds.

**rlacko said on 2010-12-06**

Hi, You can also look at C# incarnation of TAL in project SharpTAL: https://sharptal.codeplex.com (which was ported from python implementation - project SimpleTAL). I added sme interesting extension to METAL such as macro paameters and macro imports. Some ideas could be implemenmted in my favourite python template engine Chameleon :)

Regards
-Roman

