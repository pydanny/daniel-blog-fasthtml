---
date: "2009-05-29T10:53:00.004-07:00"
description: ""
published: true
slug: 2009-05-i-dont-like-integrated-development
tags:
  - rant
  - Windows
  - Linux
  - python
  - graphviz
  - MacOS
  - legacy-blogger
time_to_read: 5
title: I don't like Integrated Development Environments
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/05/i-dont-like-integrated-development.html)_.

I really don't like [Integrated Development Environments](https://en.wikipedia.org/wiki/Integrated_development_environment) (IDEs). I don't like code completion, class browsers, object inspectors, class heirarchy diagrams, source control management in whatever I am editing coding with. I find such tools arcane and frustrating.

Why?

Its because I want to be able to feel the design of a module. When I manually introspect things I feel like I am sifting through the sand of the module to see what it gives me. I feel it in my gut that this is how I learn a language and use it best of all. Python makes that very easy for you with its powerful introspection capabilities which you use on the shell. I find switching to the shell lets me separate the capabilities of the module from the code I are working on. Which for some reason I find a lot more comfortable and intuitive. Your own mileage may vary.

If I do need a class hierarchy diagram, I just write a fun little python script which generates some dot notation and run [graphviz](https://graphviz.org/)'s dot or neato utility.

If I do need source control management, thats what the command line is for!

Also, there are times I have to go and do things on systems besides my own. I can't expect to have Eclipse or NetBeans there. Or if they are there by some weird chance, they won't be configured the way I want.

Keep in mind I do like code highlighting. So I guess that makes me a text editor fan. And now on to my favorites:

<span style="font-weight: bold;">Textmates (Mac only)</span> [https://macromates.com/](https://macromates.com/)
[Kendall Clark](https://clarkparsia.com/about/profiles/kendall) introduced me to this tool back in April/May of 2006. I was very quickly hooked. It was much better than the [TextWrangler](https://en.wikipedia.org/wiki/TextWrangler) that was giving me grief. And also much less arcane than Emacs. It is the one piece of software I'll actually pay to buy to use on the Mac!

<span style="font-weight: bold;">Emacs</span> [https://en.wikipedia.org/wiki/Emacs](https://en.wikipedia.org/wiki/Emacs)
Back in the 1990s I did [Perl](https://perl.org/) for a short time and was introduced to Emacs and [Vi](https://en.wikipedia.org/wiki/Vi). Emacs clicked for me, because even its arcane commands worked better for me than Vi. These days my Emacs skills are not superb, but I can get by on any machine that has it installed. So that means any Mac or Linux machine I stumble across.

<span style="font-weight: bold;">Textpad</span> [https://textpad.com/](https://textpad.com/)
So my dark secret is that until December 2006 I did much of my work in Windows. Yes, my first python work was all developed on Windows! Anyway, I had stumbled across Textpad during a Java job and kept using it across other languages and efforts. It was light, did code highlighting, and kept out of the way. Perfect! Well, maybe not since it crashed about once a day. Still, it was better for me than more sophisticated alternatives.

---

## 2 comments captured from [original post](https://pydanny.blogspot.com/2009/05/i-dont-like-integrated-development.html) on Blogger

**lifewithryan said on 2009-05-30**

for linux users, gedit is awesome with its snippets and plugins...i use it for python, php, grails...the only thing i really use an IDE for is heavyweight java....

**Corey Goldberg said on 2010-08-06**

I use an IDE for some languages (Java/C#), but do all of my Python coding in SciTE. 

A few times a year I seem to try switching to an IDE, but always end up back with a simple editor (with syntax highlighting and built-in console)

SciTE is a great lightweight editor and works on Windows and \*nix : https://www.scintilla.org/SciTE.html
