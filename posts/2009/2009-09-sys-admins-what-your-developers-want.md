---
date: '2009-10-09T08:06:00.001-07:00'
description: ''
published: true
slug: 2009-09-sys-admins-what-your-developers-want
tags:
- rant
- django
- legacy-blogger
time_to_read: 5
title: 'Sys Admins: What your Developers want you to know'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/09/sys-admins-what-your-developers-want.html)*.

This is my response to Katie Cunningham's post telling [Developers what System Administrators want you to know](https://elephantangelchild.blogspot.com/2009/05/developers-what-your-system-admins-want.html).

Of course, this is mostly for shops with large groups such as our own. But some of this applies anywhere.

<span style="font-weight: bold;">Publish your damned system specifications</span>

If [rackspace](https://rackspace.com/), [webfaction](https://www.webfaction.com/), and the rest of the web hosting world does it for $10/month, then why can't well-paid system administrators do it?

Alas, I've yet to go to a shop where I could find on a wiki page or an otherwise easily accessible document an exact specification of the target production environment. Invariably you have to ask in person, go to another department, ask managers, or go searching through word documents. Word documents?!?

Unnacceptable.

As a developer I should be able to pull up for each server a consistently formatted web page that lists the operating system, operating system specifications, patches, database(s), compilers, shell, disk space, languages, hosted applications, and anything else you as a system administrator can think of adding. If your organization doesn't support a wiki or anything like that, then consider sending out a weekly email. Something as simple as this:


- <span style="font-weight: bold;">Production01</span> (prod.mycompany.com): RHEL Linux, Python 2.4.4, 2.6.1, Java 1.6, Ports Open: 80, 443



- <span style="font-weight: bold;">Staging02</span> (staging.mycompany.com): RHEL Linux, Python 2.4.3, 2.6.3, Java 1.6, Ports Open: 80

<span style="font-style: italic;">Look - discrepancies between servers! What a surprise! Glad this is documented!</span>

Based off of this we can build our development environments to match production environments. The QA group can also build their staging environments to match as well. Also, we might be able to better exploit a service you are providing for us rather than writing something from scratch, which means we end up saving time, energy, and money. Everybody wins!

<span style="font-weight: bold;">Communication is king</span>

A system administrator needs to be accessible via phone. It just kills me that in some shops their phone numbers are only accessible via their boss. So if you have a problem and that boss is not around the rest of us are plain screwed. Can't our boss have the system administration contact information? Or maybe even us lowly developers?

Also, squirting off emails that you are starting/finishing things is really useful. Or send an email every 30-60 minutes with status. Or jump on IRC/IM and let the very tense developer/QA/business teams know you are still working.

<span style="font-weight: bold;">Stick to the schedule</span>

When you have 15 people waiting on you, start the deployment on time. Besides the simple expense of keeping that many people on the clock, delaying a start on people who have already been there for 8 hours is a good way to earn developer/QA/management enmity. Then you'll wonder why they always blame you right off the bat.

<span style="font-weight: bold;">Follow the deployment instructions</span>

When it comes to deployment, the hard truth is that your job as a system administrator is to follow instructions. Don't improvise. If the developer instructions don't work (for example, changing to a non-existent directory), don't fix the problem right then and there by opening files and twiddling stuff. Instead, it's time to call this a failed deployment.

That might make you look bad in the short run. Developers might howl. Sometimes you just have to stand firm. A good way to address this issue is to ask to look at a project's deployment instructions before the deployment date. Which brings us to the next point...

<span style="font-weight: bold;">Review the deployment instructions early</span>

Smart developers run their deployment instructions early past a system administrator. Take a good hard look at what they are trying to do and let them know if they are doing anything wrong. Good developers will really appreciate what you are doing for them.

<span style="font-weight: bold;">Clone the production environment daily</span>

Its 2009. Shouldn't we have fresh staging servers every morning for continuous integration? Yes, I know that when you built server X it matched server Y, but that was 6 months ago. Things have changed on both servers. A smart system administrator can script this out, or so they always tell me...

<span style="font-weight: bold;">Communication is king II</span>

So the deployment had problems. Or maybe it didn't. Maybe you had to do a tiny tweak on the instructions to turn an understandable developer mistake into a shining success. Here is what you can do to help defend yourself when things go wrong and to provide developers with a window into what you are doing.

Share the bash session history by use of the [Tee](https://en.wikipedia.org/wiki/Tee_%28command%29) command, the logs, and everything else. Without us asking for it! Dump the data and make it easy for us to find. We'll appreciate it and so will you.

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2009/09/sys-admins-what-your-developers-want.html) on Blogger

**Unknown said on 2009-10-09**

As a sysadmin that seems a bit backwards.  Usually the developers tell me what they need and I match the server specs / software to their needs.

**pydanny said on 2009-10-09**

@G Mack,

Depends on your environment. In most ig shops I've been in getting servers upgraded as a developer is really hard. You mostly just pray that they are running current software and work around things when they are not.

**Unknown said on 2009-10-10**

@ PyDanny, 

It is a bit of a trade off.  If the OS/Distro makers haven't packaged something then it must be manually installed.  

Manually installing means needing to remember it's there and that it needs updating across all live and dev servers otherwise you get different versions on each server or worse yet no one remembers to update with security patches.  On my systems I get an email first thing in the morning for each server that's behind on it's security patches but there is no such mechanism for anything I've manually installed.

There is also the issue that updating between OS versions can break existing software.

**Unknown said on 2009-10-10**

Deployment is something I do on the staging and production environments.

If I would let the sys admins do it I doubt it will ever get deployed.

