---
date: '2010-03-05T10:11:00.003-08:00'
description: ''
published: true
slug: 2010-03-pycon-2010-report-iii-sprints
tags:
- pycon
- django
- python
- pinax
- legacy-blogger
time_to_read: 5
title: 'Pycon 2010 report III: Sprints'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/03/pycon-2010-report-iii-sprints.html)*.

<div>My report for the sprints of [Pycon 2010](https://us.pycon.org/2010). This isn't a general review of the sprints, just how it affected me.</div><div>
</div><div><b>[Pinax](https://pinaxproject.com/) Sprint</b></div><div>
</div><div>I don't have a hard count of how many people participated on Pinax this year. Last year's sprint looked like we had a lot more, but last year the Pinax room was home to people doing other things, albeit mostly [Django](https://djangoproject.com/) related stuff. In any case, this year we had probably about 10 people working on Pinax, or things that went directly into Pinax.</div><div>
</div><div>While [James Tauber](https://jtauber.com/) is the leader of the Pinax community, this year [Brian Rosner](https://oebfare.com/) stepped up and did an amazing job being both a technical resource and director of geeks. The mutual clarity of vision and obvious telepathy between Brian and James is truly a joy to behold. </div><div>
</div><div>I also appreciate the entire Pinax community. Besides coaching me on [Git](https://git-scm.org/) branches (work uses SVN so I just don't get enough Git practice) they also gracefully understood that [I was a bit distracted this year](https://pydanny.blogspot.com/2010/02/pycon-2010-report-i.html). </div><div>
</div><div><b>My specific contributions to Pinax</b></div><div>
</div><div>One of the things that had bugged me about Pinax for some time were the individual project tag apps. These were a per project extension of [django-tagging](https://code.google.com/p/django-tagging/), and were used to simply display tagged data. I was never happy about the displays of the tags, the lack of pagination, or that you had to create/modify an entire project level application just to control a display.</div><div>
</div><div>So last [DjangoCon](https://www.djangocon.org/) I wrote [django-tagging-ext](https://github.com/pydanny/django-tagging-ext). What it does is let you control the displays of tags via a root urlconf wiring. It still needs some work (cleaning a query, 100% test coverage, better documentation), but its a big step up from the alternative.</div><div>
</div><div>For Pycon I volunteered to go into all the Pinax projects that used tags and replace the tag_app there with django-tagging-ext wiring. I thought it would be relatively trivial, but in practice it was not.</div><div>
</div><div>The issue was that immediately prior to the conference, changes had been made to Pinax trunk that caused a small number of errors. All them passed existing tests but failed when you actually clicked through pages. Yeah, that does mean that Pinax [code coverage ](https://nedbatchelder.com/code/coverage/)needs improvement, but that is something we are working feverishly on. In any case, what that meant was that by implementing the new tag display system, I got the chance to fix a number of small but poignant bugs.</div><div>
</div><div>I also worked some to help the code coverage of tests. Brian Rosner worked with me and gave me some excellent pointers. I feel sad because I think we had a disconnect on what we consider pair programming, and want to assure him that the time he gave me was a high mark of the conference.</div><div>
</div><div><i>In regards to pair programming, I don't mind working with someone until you figure something out, but spending hours and hours sharing a computer drives me nuts. Once a person 'gets it', go do something else and let them go forward.</i></div><div>
</div><div><b>Volume of Contribution</b></div><div>
</div><div>Looking at the [Pinax impact chart on github](https://github.com/pinax/pinax/graphs/impact) I can claim that I had the most impact during the sprint. Heck, [I even jokingly claimed it on Twitter](https://twitter.com/pydanny/status/9908711789). </div><div>
</div><div>Except that claim is false.</div><div>
</div><div>The truth of the matter is that how many commits I did in a brief period is nothing compared to what Brian and James did to equip others to make commits. Or what they've done during the history of Pinax. Or what they might have done to side projects that touch Pinax. Also, during the sprints my work was really focused to a specific area of Pinax, and besides some work I did with [Skylar Saveland](https://skyl.org/), I worked mostly by myself.</div><div>
</div><div>So that claim is full of hubris and rather silly. If that claimed annoyed anyone in the Pinax community I'll buy your forgiveness with a beer.</div>

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2010/03/pycon-2010-report-iii-sprints.html) on Blogger

**Jerry Seutter said on 2010-03-05**

I was annoyed by that beer^H^H^H^Hclaim!  

Wait, what's Pinax? :)

