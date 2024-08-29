---
date: "2011-09-14T09:39:00.000-07:00"
description: ""
published: true
slug: 2011-09-history-of-my-most-used-shell-commands
tags:
  - git
  - MacOS
  - buildout
  - legacy-blogger
time_to_read: 5
title: History of my most used shell commands
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/09/history-of-my-most-used-shell-commands.html)_.

[I ran this a few years back](https://pydanny.blogspot.com/2008/04/history-of-my-most-used-shell-commands.html)&nbsp;and I'm running it again today.

What is interesting is that compared to the older history, [git](https://git-scm.org/) has replaced svn, [pip](https://pypi.python.org/pypi/pip) has replaced easy_install, and [virtualenv](https://pypi.python.org/pypi/virtualenv) has now completely subsumed buildout. Oh, how the mighty have fallen!
<pre class="prettyprint">$ history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn |head -n 20

209 git
123 python
34 ls
31 mate
18 cd
14 pwd
9 hg
8 touch
7 rm
6 cp
5 pip
5 mv
5 django-admin.py
4 mkvirtualenv
3 mysql
3 mkdir
3 bash
2 deactivate
2 add2virtualenv
1 workon</pre>

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2011/09/history-of-my-most-used-shell-commands.html) on Blogger

**Brent O'Connor said on 2011-09-14**

Here is mine currently... :)

78 ls
73 git
72 cd
35 vagrant
25 deactivate
21 workon
20 sudo
17 e
15 mkvirtualenv
14 fab
13 django-admin.py
13 cat
11 runserver
11 ex
9 rm
9 pip
6 ./bin/craigslist_import.py
5 grep
5 cdvirtualenv
4 ssh

**Dougal said on 2011-09-15**

If you add this to your .profile/bash_rc you can make the results more interesting.

export HISTSIZE=50000

My bash history then goes back until at least the start of this year. Very handy if you want to search for something and I've not noticed a slowdown (even of running the history command).

**Reinout van Rees said on 2011-09-15**

So you got rid of buildout, he? :-) How do you deal with the recipes that you're now missing? Or didn't you use them? I use buildout to generate my apache config, just to name an example, and to set up my django project.

I <i>assume</i> you also used some of those recipes. How do you handle such tasks now?

**pydanny said on 2011-09-15**

@Reinout - The final buildout project I was on got converted to pip/virtualenv + either apt or homebrew depending on who was developing it. The consensus has been to use native tools to build environments and that designers and developers find buildout cumbersome, kind of undocumented, and hard to debug. 

And I stand by that statement. I think buildout grew from a straightforward Python package management system and into something else that tried to be kind of like Chef or Puppet but purely focused on Python. 

I need to blog my thoughts about it. :P
