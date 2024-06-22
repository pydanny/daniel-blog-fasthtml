---
date: "2008-01-10T06:50:00.002-08:00"
description: ""
published: true
slug: 2008-01-reason-4293-why-im-happy-to-be-out-of
tags:
  - rant
  - python
  - coldfusion
  - legacy-blogger
time_to_read: 5
title: "Reason #4293 why I'm happy to be out of ColdFusion"
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/01/reason-4293-why-im-happy-to-be-out-of.html)_.

At my job the majority of developers do ColdFusion (CF). And most of them code in it as if it were still 1997 back in version 3, but they do it on modern CF 8 servers. That means using lots of deprecated bits or making it one giant procedural mess with the only complex data object being SQL query result sets (no arrays, structures, xml, etc). Unit testing is ignored, as is use of modern CF frameworks especially the useful ORMs that now exist. At best they use some of the reporting tools and thats all you get out of them.

Well, at another job location a pair of smart CF developers wrote an application using all the modern bits of CF8. That means object-oriented code that had fancy things like duck typing.

The software was brought here, and you know what? It was assigned to a 'senior developer' for slight modifications to accommodate some differences in business logic. And that 'senior developer' promptly yanked the code out of the objects and rendered it into lard... I mean procedural code. And the racehorse application turned into a turd.

Now in the Python world this would not happen. If we needed to change something, we inherit the modules needed from other people's work. I did that with Trac's admin console, mildly rewriting three methods to move them out of the console based atmosphere.

If you ever did do something like obfuscate and slowdown existing code in the Python world, you would get your knickers beaten. In the ColdFusion world, you are considered senior because of tenure.

Sigh.
