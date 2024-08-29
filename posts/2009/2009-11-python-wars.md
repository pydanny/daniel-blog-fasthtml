---
date: '2009-11-10T20:27:00.001-08:00'
description: ''
published: true
slug: 2009-11-python-wars
tags:
- november
- python
- blog
- legacy-blogger
time_to_read: 5
title: Python Wars
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/11/python-wars.html)*.

Python Wars Solo was the result of a few hours effort roughly duplicating a text-based Star Trek game I wrote back in 1980-1981. I wrote the game in Apple ][ basic, and it had you 'fly' the USS Enterprise against up to nine Klingon ships. You could fire phasers, launch photon torpedoes, take evasive actions, and it seemed pretty fun.  Beating one was a piece of cake. Three was a fun challenge. Five was tough. Seven was done only a few times. Nine was never done. The game was simple, fast, easy to learn, and tons of fun. Back in High School it was one of the games traded on floppy disks during the computer club so I considered it a success.

Back in 2007 I decided to try and reconstruct the software. One thing I did was was write most of it in one quick code dash of near stupidity. My theory was that it would more closely match the feel of my efforts as as 15 year old wrestling with Apple ][ basic without the benefits of a manual.

Some changes from the original:

 * Rather than name it after the Star Trek universe, I named it a bit generically.
 * Switched from phasers to a spinal mount weapon like what they used so wonderfully in Babylon 5.
 * Changed from photon torpedoes to missiles.

The result worked, and was fun to play in dribs and drabs. The code is embarrassing, but that was kind of the point.

[https://code.google.com/p/python-wars/wiki/PythonWarsSolo1](https://code.google.com/p/python-wars/wiki/PythonWarsSolo1)

Do a svn checkout (<tt id="checkoutcmd">svn checkout <strong><em>http</em></strong>://python-wars.googlecode.com/svn/trunk/ python-wars-read-only)</tt>, and then <span style="font-weight: bold;">python go.py</span>. Don't laugh too hard!

I'm toying with moving this this over to Github and even doing a formal release. That would be really funny.

21 more posts to go!