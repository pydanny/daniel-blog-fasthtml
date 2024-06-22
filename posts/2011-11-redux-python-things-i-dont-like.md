---
date: '2011-11-04T13:00:00.000-07:00'
description: ''
published: true
slug: 2011-11-redux-python-things-i-dont-like
tags:
- rant
- python
- legacy-blogger
time_to_read: 5
title: 'Redux: Python Things I Don''t Like'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/11/redux-python-things-i-dont-like.html)*.

Back in May of 2009, I wrote about [Eight Things I don't like about Python](https://pydanny.blogspot.com/2009/05/eight-things-i-dont-like-about-python.html). It was my attempt to come up with things I don't like about my programming language of choice. Consider this my update of that post.

<h3>1. Division sucks in Python</h3>In [Python](https://python.org) 3 this is fixed so that <b>2 / 3 = 0.6666666666666666</b> but in Python 2.7.x you have <b>2 / 3 = 0</b>. You can fix that in Python 2.7.x with doing a <i>from __future__ import division</i> before your division call. Can anyone tell me if a version of 2.7.x will natively support <b>2 / 3 = 0.6666666666666666</b> without that import?

<b>Note:</b> Chris Neugebauer pointed out that changing division in Python 2.7.x will break backwards compatibility. However that doesn't change that I don't like it in Python 2.7.x.

<h3><strike>2. TKinter blows</strike></h3>Honestly, it doesn't really matter to me anymore. I either use command-line scripts or things delivered to the web. Also, thanks to Brett Cannon, I know if I need to make TKinter look good, I can use [TK Themed Widgets](https://docs.python.org/library/ttk.html) right out of the standard library.

<h3>3. Lambdas make it easy to obfuscate code</h3>I'm known for [not liking lambdas in Python](https://pydanny.blogspot.com/2007/07/lambdas-no-more.html). These days, I do know of use cases for Lambdas, but those are far and few between. I might even try to turn that into a blog post this month - use cases for Lambdas in Python. Fortunately for me, these days I seem to work with people who mostly agree with me on this subject.

<h3>4. Sorting objects by attributes is annoying</h3>This is still annoying for me. As I said, "<i>... the snippet of code is trivial. Still, couldn't sorting objects by attributes or dictionaries by elements be made a bit easier? sort and sorted should have this built right in. I still have to look this up each and every time.</i>"

I've thought of proposing something easier as a PEP. Imagine that! Me submitting a PEP!

<h3><strike>5. Regex should be a built-in function</strike></h3>Before I got to do Python full-time I was a go-to person with regular expressions. Languages without them were weak in my opinion. Since then (2006-ish) my skills have faded somewhat in regards to regular expressions. And you know what? It hasn't been a problem. Python's string functions are fast and useful, and when I really need regular expressions, I import the library and do some research. I'm considering this one closed.

<h3>6. Reload could be less annoying</h3>Reload only works on modules. I want to be able to something like <b>reload(my_module)</b>, <b>reload(my_class)</b>, <b>reload(my_function)</b>, or even <b>reload(my_variable)</b>:
<pre class="prettyprint-py">>>> from my_module import MyClass, my_function, my_variable
>>> mc = MyClass(my_variable)
>>> mc 
5
# I go change something in my_module.MyClass and save the file
>>> reload(MyClass) # reload just MyClass
>>> mc = MyClass(my_variable)
>>> mc 
10
</pre>My current fix is to use unittest as my shell as much as possible. And that is probably a good thing.

<h3>7. Help doesn't let me skip over the '__' methods</h3>As I said way back when, "<i>Python's introspection and documentation features makes me happy. And yet when I have to scroll past __and__, __or__, and __barf__ each time I type help(myobject), I get just a tiny bit cranky. I want help to accept an optional boolean that defaults to True. If you set it to False you skip anything with double underscores.</i>

The [See project](https://github.com/inky/see) is one solution to the issue. A different approach I've used is the [Sphinx autodoc](https://sphinx.pocoo.org/ext/autodoc.html) feature, but Sphinx is a lot of work and doesn't cover every contigency.

<h3>8. Not enough female Pythonistas</h3>These days I know a lot of female Python developers. There is my own fiancee, [Audrey Roy](https://twitter.com/audreyr). Face-to-face I've met and talked to [Christine Cheung](https://twitter.com/webdevgirl), [Jackie Kazil](https://twitter.com/jackiekazil), [Leah Culver](https://twitter.com/leahculver), [Katharine Jarmul](https://twitter.com/kjam), [Katie Cunningham](https://twitter.com/kcunning), [Barbara Shaurette](https://twitter.com/bshaurette), [Esther Nam](https://twitter.com/estherbester), [Sandy Strong](https://www.twitter.com/sandymahalo), [Sophia Viklund](https://www.twitter.com/backcode), [Jessica Stanton](https://www.twitter.com/tiny_mouse) [Aurynn Shaw](https://www.twitter.com/aurynn), [Brenda Wallace](https://twitter.com/br3nda), [Jen Zajac](https://twitter.com/jenofdoom), and many more I know I'm missing. And there are even more with whom I've had in-depth online conversations.

So why didn't I put a strike-through on this one? Because the numbers still aren't good enough. I know a lot of female Pythonistas, but how many do you know? And even if you know a decent number, what percentage of a meetup group you attend are women?

I can say that things are improving, but they could be better - for women or minorities. Find ways to pitch in, be it [PyLadies events](https://pyladies.com/events/), [PyStar workshops](https://pystar.org/), or what have you. 

One last note on this subject, I've heard some unsubstantiated statements that the .Net world has a higher female-to-male ration then the Open Source world. Are we going to take that kind of thing sitting down?

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2011/11/redux-python-things-i-dont-like.html) on Blogger

**Andrew Dalke said on 2011-11-04**

Sorting by attributes is one of the few times when I use a lambda. list.sort(key=lambda x.attr). I know that operator.attrgetter(&quot;attr&quot;) would also work, but that requires a lot more effort, and it doesn't handle, say, x.attr[0].

Perhaps something like list.sort(key = (x.attr for x in list))? (Better probably to not reuse the 'key' keyword here.)

