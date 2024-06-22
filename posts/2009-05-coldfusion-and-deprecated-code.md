---
date: '2009-05-25T12:48:00.008-07:00'
description: ''
published: true
slug: 2009-05-coldfusion-and-deprecated-code
tags:
- rant
- coldfusion
- legacy-blogger
- foxpro
time_to_read: 5
title: ColdFusion and deprecated code
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/05/coldfusion-and-deprecated-code.html)*.

Lets take a step back in time to 1999. At that point I had been doing a mix of [Foxpro](https://en.wikipedia.org/wiki/Foxpro) for DOS, [Perl](https://www.perl.org/), and an obscure language called WebML (don't bother looking it up, it doesn't seem to exist anymore). I admit I liked Foxpro but recognized it was a coder's dead end. Perl gave me regular expressions which I liked but I was uncomfortable with everything else. WebML was okay but it was clear that it was too obscure. Around that time I even talked to some people doing something weird with [Python](https://python.org/) and [Zope](https://zope.org/) in Fredericksburg, but that sounded even more obscure.

At my job we had someone throw together a [ColdFusion](https://en.wikipedia.org/wiki/ColdFusion) 4.51 application. They needed some help. I took a look and quickly figured out the issues, made corrections, and realized this language was really simple. One thing I noticed while pouring over the built-in documentation of the CF IDE (this was back when I used IDEs) was that there was a list of deprecated functions. You were supposed to stop using [parameterExists](https://www.cfquickdocs.com/cf8/#ParameterExists) and use [isDefined](https://www.cfquickdocs.com/cf8/#IsDefined) instead. I shrugged, followed the specification, and moved on.

Years went by. I did Java and ColdFusion. Both were annoying because of spaghetti code. Java was also annoying because of boilerplate and the static typing, ColdFusion was annoying because of the tags, the weird ecmascript implementation, and the insistence of developers on using the deprecated functions.

The most obvious example was the <span style="font-weight: bold;">parameterExists</span> vs <span style="font-weight: bold;">isDefined </span>issue. The former, paramExists accepts a variable, so you couldn't build dynamic code. Specifically you did something like <span style="font-weight: bold;">parameterExists(my_variable) </span>instead of like <span style="font-weight: bold;">isDefined("my_variable")</span>. This meant more cut-and-paste coding. Also, because it was a deprecated function, the owners of ColdFusion didn't care about the performance of the code. So instead of looping through an array of a hundred or so variables who existence you wanted to check using <span style="font-weight: bold;">isDefined</span>, people would still <span style="font-weight: bold;">@#$%ing</span> type out <span style="font-weight: bold;">parameterExists</span> a hundred times. Or more commonly, cut-and-paste from one code template to another, across applications. A good number of the <span style="font-weight: bold;">parameterExists </span>at the top of a CF page often have nothing to do with the purpose of the page and people would wonder why things ran so slow.

Sadly, this sort of behavior still happens today in the CF community. Worse yet, because in my experience the CF community tenure is more important than anything else, the worst offenders are often the people who have been using the tool the longest.

So lets go through a quick summary of my issues with ColdFusion and deprecation:


1. Deprecated language elements, even if deprecated over 5 releases, are... well... deprecated.
- Deprecated language elements are likely the last to be examined in a release for performance or security reasons.
- Deprecated language elements can go away.

- The worst offenders of using deprecated language elements tends to be those who have used the language the longest.



---

## 8 comments captured from [original post](https://pydanny.blogspot.com/2009/05/coldfusion-and-deprecated-code.html) on Blogger

**Sean Coyne said on 2009-05-25**

Sounds like you are surrounded by poor developers.  Every language/api/whatever will eventually get deprecated pieces.  Its up to the developers to learn and evolve with the language.  Why blame ColdFusion for the mistakes of developers who obviously work in a place where either no professional development happens, or just doesn't care about crap code making it to production.

**Unknown said on 2009-05-25**

I agree this can be really frustrating to see in people's code but there are two main issues at play here:

1. A lot of CFers don't seem to enhance their skillset beyond "what works". Sorry if that treads on anyone's toes but it's true: there are a lot of 9-to-5 CFers out there who know enough to get their job done and they have no incentive to improve - they don't attend user groups, they don't go to conferences, they don't read blogs (so they probably won't see this and won't even be offended!) and for the most part they don't participate in mailing lists. For many of them, CF is "just a job" and they didn't get into it because they particularly enjoy programming.

2. Allaire / Macromedia / Adobe has been very, very careful about backward compatibility and not breaking people's code. In particular, because so many CFers still use paramExists(), Adobe would have a hard time removing it because that would break so much code. They could start adding warnings to the logs for every deprecated function use or maybe even making deprecated functions deliberately "sleep" for a second - that might incentivize people to fix their code... but it also might mean those people simply wouldn't upgrade their servers (and, hey, there's a lot of people still on CF5 because CFMX broke a bunch of things).

I can tell you that across a broad range of languages, few deprecated features ever really go away. As soon as you have a large enough user base and a large enough "legacy" code base, you pretty much cannot remove a language feature. That's also true of frameworks and all sorts of libraries and even operating systems.

But I totally share your frustration!

**david said on 2009-05-26**

One argument is that a deprecated element should, eventually, stop being deprecated and actually become <i>removed</i>. 

In general, though, CF suffers from some of the same problems PHP does: is it possible to program in a non spaghetti manner? Sure.  But does the language, in some ways, make easy and even encourage that sort of code? Arguably, yes.

**pydanny said on 2009-05-26**

@Sean Coyne,

I can't help it if when I did ColdFusion the clear majority of developers were poor. In the years I did ColdFusion the sad truth was that my following of blogs, use of best practices, understanding of MVC, etc was the exception and not the norm. This was across multiple jobs across a major metropolitan area. 

All professional ColdFusion developers know Ben Forta. But how many know Sean Corfield or Ray Camden?

So yes, I feel I can blame the language on this issue.

**Unknown said on 2009-05-26**

are you referring to THIS (www.webml.org) webml? 
The (visual) language is actually alive and also has an associated CASE tool (www.webratio.com)

**pydanny said on 2009-05-26**

@seancorfield,

I've dealt with the code produced by all those 9-to-5 CFers and I'm sure you've experienced this as well. They have no passion for their tool, or any desire to learn anything new. Then you get stuck MULTIPLE times working with some '9-to-5 senior developer' whose code belongs on Daily WTF and you can't make real changes to his crappy code because management is terrified of losing his business knowledge. 

So yeah, I understand that even if you deprecate for 10 years and remove something, you catch them by surprise no matter what you do.

Allaire / Macromedia / Adobe protected their business interests and I understand their logic. However I think their logic was a mistake, which is why I think the CF language control board is a good idea. I hope you argue to nix the deprecated bits. 

Then again, I think all languages should be made open source and that vendors should sell support just like the model that RedHat, JBoss and other pricey firms use.

**pydanny said on 2009-05-26**

@David,

Yes, deprecated functions should be removed. Python does it and maybe Ruby does too. I think Java did it as well.

CF has some 'features' that absolutely do encourage Spaghetti code. I'm not talking about the loose typing, I'm talking about the ability of one template to include another without any ability to block it via a tag called CFINCLUDE. So what happens is that people might use on of the CF frameworks such as Fusebox or ColdBox, but then you *always* get that wanker who breaks the framework by sticking CFINCLUDEs inside a framework defined by XML, CFCs, or whatever.

Argh!

**pydanny said on 2009-05-26**

@Marco,

Nope! Not your webML! This was basically an obscure cgi style language set like PHP, Perl, or ColdFusion created by a small California company called Expertelligence.

