---
date: '2009-04-09T11:33:00.010-07:00'
description: ''
published: true
slug: 2009-04-show-me-your-open-source-django-blog
tags:
- django
- foss
- javascript
- python
- pinax
- atom
- rss
- spacebook
- legacy-blogger
time_to_read: 5
title: Show me your open source Django blog application
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/04/show-me-your-open-source-django-blog.html)*.

Want your blog engine to be used by [NASA](https://www.nasa.gov/)?

Unlike everyone else in the [Django](https://djangoproject.com/) world, I have not written a blog application.

Instead I want to use your blog application. Definitely for my upcoming blog transfer to my own personal site (Blogger's limitations annoy me), and possibly for use in [NASA Science Mission Directorate](https://nasascience.nasa.gov/) [Spacebook](https://pydanny.blogspot.com/search/label/spacebook) project. So what am I looking for in your blog?

In no particular order these are the must-haves:


- Elegant user interface.

- Follows Django/Python best practices.
- Easy to integrate into another application (which should be the case if you followed the above point).

- Code highlighting via pygments.
- Relies on JQuery for JavaScript, and degrades properly.
- Publishes legal RSS feeds.
- Allows for use of several input formats (Restructured Text, Markdown, etc)

- Hooks for integrating WYSIWYG editor
- Allows for multiple users each with their own blog.
- Renders humanely in FF, Safari, and IE 6, 7, and 8.
- Any sort of decent documentation. 

In no particular order these are the nice-to-haves:


- Publishes ATOM feeds.
- Allows for multiple users on a particular blog.
- Already has a WYSIWYG editor.
- Handy import/export functions that follow whatever standards Blogger might have.

Candidate killers:


- I have my own server space. Plus, NASA has its own servers. So Google App Engine compliant blog systems need to also support the standard Django ORM.
- I am doing this in Django/Pinax/Python/PostGreSql on Linux. Systems that do not play well there need not apply.


What do you get out of this if I pick your blog engine?

Well, as much as I am a fan of [Pinax](https://pinaxproject.com/), the default blog application doesn't do everything we want it to do for Spacebook. So your application might become the blog engine used by us. And when we launch, we'll be sharing credit with anyone who contributed from the open source community to our efforts.

<b>Edit on August 26th, 2010</b>: I solved how to do this research by co-authoring [Django Packages](https://djangopackages.com/) which gives us this [handy referenc](https://www.djangopackages.com/grids/g/blogs/)e. Also, at this point in time, as part of larger systems, I've written several blog systems for clients.

---

## 21 comments captured from [original post](https://pydanny.blogspot.com/2009/04/show-me-your-open-source-django-blog.html) on Blogger

**Kurt Schwehr said on 2009-04-09**

NASA Ames is looking at django and I'm working with some people at JPL who might be interested in django.

I'll be curious to hear how it goes for your projects.

-kurt
https://schwehr.org

**Dyadya Zed said on 2009-04-09**

You should definetely check Byteflow https://byteflow.su/ . It has impressive number of features and very clean codebase. Actually I am going to use it for my personal blog.

**Marco said on 2009-04-09**

hostable on GAE would be a + ? :)

**pydanny said on 2009-04-09**

@kurt: I would love to talk with you guys! I wonder if there is a NASA Django mailing list. On Spacebook we will be able to create that easily enough, and within the NASA domain. 

If you have VPN access to the NASA network you could try out the Spacebook proof of concept! We are working on the real version now, but when it goes beta we'll invite you.

**pydanny said on 2009-04-09**

@Dyadya: Thanks for the recommendation! We'll take a look at it!

@1st Apple Hater: Hostable on GAE means nothing. I have my own server space. Working for a US Government agency means I can't host on GAE. I'll change the blog post to reflect the lack of need for GAE.

**pydanny said on 2009-04-09**

@Malcom: NASA as an agency uses RSS as a standard. Yes, RSS has something like 9 variations, but I do not call the shots and hence RSS is a requirement. ATOM support is therefore something that I wouldn't mind doing but is not a requirement.

**pydanny said on 2009-04-09**

@Barbara: Thanks for the recommendation!

**Alexander Solovyov said on 2009-04-10**

Actually Byteflow meets your requirements, except ability to integrate easily - it's not a application, it's a project. Though of course you can get only parts you need, I believe that code is pretty good. ;-)

**Doug Hellmann said on 2009-04-10**

Have you looked at Zine (https://zine.pocoo.org/)?

**pydanny said on 2009-04-10**

@Anonymous: Lets just say that I would really, really prefer to publish everything in Atom, but the formal requirement is for RSS.

**pydanny said on 2009-04-10**

@Doug Hellmann: I looked at Zine before I got into Django and Pinax. Looks spiffy! However, since I need a Django app that I can plug into Pinax, Zine just won't do. :(

**Bruce said on 2009-04-12**

@anon: I'm not sure you could say that RSS 1.0 is an "American standard" particularly since it's RDF (and so is extensible).

**Will McGugan said on 2009-04-12**

Hi,

You might want to consider my own offering, [Django Tech Blog](https://www.willmcgugan.com/tag/techblog/).  It's pretty close to what you are looking for -- and I could help you get it there!

Will McGugan

**Gert Van Gool said on 2009-04-13**

Would [mightylemon](https://github.com/mightylemon/mightylemon) do? It's the code from https://oebfare.com/

**pydanny said on 2009-04-13**

@Gert: Since it was created by one of the core-devs of Pinax, I have looked at Oebfare and I like it a lot. I may slurp out pieces of it.

**Jeff said on 2009-04-14**

Can Pinax's default blog tool be enhanced to provide what you are missing?

**pydanny said on 2009-04-14**

@jocknerd, Normally I would say yes. And it might come to that. The issue though is fitting that into my schedule by formal due dates.

**pydanny said on 2009-04-18**

@Will McGugan,

You wrote the Pygame book my son and I have! Awesome!

**Tobias McNulty said on 2010-01-12**

What did you end up using?  We're looking for something similar and the &quot;Easy to integrate into another application&quot; part is killing my search...

**Ivan said on 2010-01-25**

Dear Danny

Did you get very far with this?  

I am picking a choosing bits to go into a Django-base site.  I noticed your CMS call (and I'm now weighing up Django-CMS and FeinCMS).

Did you come to a shortlist for a blog app?

Best wishes

Ivan

**pydanny said on 2010-01-25**

Ivan, 

If I were to make a stand-alone blog for Django I would go with django-mingus. For something that goes into Pinax, I would choose https://github.com/eldarion/biblion once its ready.

