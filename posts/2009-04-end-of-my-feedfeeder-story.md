---
date: '2009-04-07T23:00:00.002-07:00'
description: ''
published: true
slug: 2009-04-end-of-my-feedfeeder-story
tags:
- beautiful soup
- feedfeeder
- feedparser
- plone
- apology
- xml
- legacy-blogger
time_to_read: 5
title: The end of my Feedfeeder story
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/04/end-of-my-feedfeeder-story.html)*.

Another post about [Plone](https://plone.org/)... but this time about me and not about Plone.

For about 18 months I have wrestled with consuming broken RSS feeds to pick up image of the day fields stipulated by customers. These are feeds so broken that no RSS parser, including the masterful [Feedparser](https://feedparser.org/), can handle them (for example, one image of the day feed usually puts the image in the RSS header and changes that each day - no history is maintained). They aren't actually RSS, they just possess a file name that ends with '.rss'. Plus, periodically the way they are written changes so custom logic fails.

I have forked R[einout van Rees](https://reinout.vanrees.org/) [FeedFeeder](https://plone.org/products/feedfeeder) project, and even proposed complicated logical revisions to handle broken these broken feeds and their shifting implementation. I called it Feedfeeder v2. Reinout always seemed hesitant, and I watched as other people extended on his work and despaired. I knew something was wrong but couldn't put my finger on it. I hesitated to work on it, even though funding for it was readily available.

Then between [Spacebook](https://pydanny.blogspot.com/search/label/spacebook), [Pinax](https://pydanny.blogspot.com/search/label/pinax), and other efforts I shelved this effort for months, hiding my head in the virtual sand. And yet I knew it needs to be addressed. How could I handle something that broke the otherwise wonderful Feedparser?

During [Pycon 2009](https://us.pycon.org/) I came up with the answer. I took an excellent tutorial on html scraping and learned lots of little tricks to reinforce my skills with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup). You see, screen scraping is a secret pleasure I have. Scraping out a bit of data from a page is like a little puzzle. When I talked about this to someone, in the middle of my discussion with them the answer became clear as day.

The answer was to turn the problem from a RSS interpretation problem to a simple web page scraping puzzle.


1. Fetch via urllib the XML file that pretends to be RSS.
- Parse it using BeautifulSoup or [html5lib](https://code.google.com/p/html5lib/).
- Get all the images listed.
- Discard all but the largest image.
- Guess out the meta-data from the XML file and store that for the image.

<span style="font-weight: bold;">Problem solved.</span>

Now I just need to make a Plone 3 package to do this for me and my angst is finished.

My apologies Reinout for the time spent on trying to cook a solution via Feedfeeder. Thank you for your insights and your extreme patience. I think you tried to tell me to take a different path.

---

## 2 comments captured from [original post](https://pydanny.blogspot.com/2009/04/end-of-my-feedfeeder-story.html) on Blogger

**Reinout van Rees said on 2009-04-08**

Using screen scraping on those horrible "RSS" feeds... Hi, hi, that totally made my day :-)

Yeah, screen scraping is probably the optimal solution in this case.

No problems with you trying to (ab)use feedfeeder for this :-)

**pydanny said on 2009-04-08**

@reinout,

I've thought of calling this <b>Feedscraper</b> as homage to Feedfeeder. That or <b>Image of the Day Feed Scraper</b>.

