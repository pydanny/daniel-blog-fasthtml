---
date: '2008-10-22T05:55:00.010-07:00'
description: ''
published: true
slug: 2008-10-morning-brainstorm-about-feedfeeder-v2
tags:
- NASA science
- feedfeeder
- feedparser
- plone
- legacy-blogger
time_to_read: 5
title: Morning brainstorm about FeedFeeder v2
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/10/morning-brainstorm-about-feedfeeder-v2.html)*.

I've been working on a .plan for FeedFeeder v2, but for some reason things were not really coming together.  Something seemed off.  In retrospect, what was off was that my proposed solution didn't immediately correct the current problem with the otherwise excellent current version of FeedFeeder.  And that problem is that any anomalous feeds force you to write and deploy code (ie - plugins) to correct the anomaly.

Sure, the Van Rees brothers had agreed that a future stage would correct the problem via a TTW function, and we would even consider a handy AJAX powered GUI to make it intuitive.  However, the issue with that is that it would occur at a future stage, not at a stage that worked with my current use case - that I get feeds from the customer that they want today to work in [nasascience.nasa.gov](https://nasascience.nasa.gov/).  Speaking on the finanical side, how could I get NASA to pay for work done on FeedFeeder v2 if it doesn't correct our current issues out of the box?

Well, this morning the answer came to me.  The solution to the problem was rather clear and simple.  Rather than a sophisticated plug-in system what about a definition system?  Currently FeedFeeder provides two content types:
 

- <span style="font-weight: bold;">FeedFolder</span>:
         

- includes a field listing the feeds consumed by this folder</li>            <li>and is a container for holding feed definitions and feed items</li>        </ul>    </li>
 <li><span style="font-weight: bold;">FeedItem</span>:
         

- individual feed content items provided by the feeds defined in the FeedFolder</li>        </ul>    

My solution proposes adding a third content type called '<span style="font-weight: bold;">FeedDefinition</span>' to handle defining of feeds:
 

- <span style="font-weight: bold;">FeedFolder</span>:
         

- a container for holding feed definitions and feed items</li>
     </ul>            </li>    <li><span style="font-weight: bold;">FeedItem</span>:
         

- individual feed content items provided by the feeds defined in the FeedFolder's FeedDefinitions</li>
     </ul>    </li>    <li><span style="font-weight: bold;">FeedDefinition</span>:
         

- Defines the source of a feed and how to handle the feed</li>        </ul>    

A FeedDefinition would likely include the following fields in addition to the defaults:
 

- <span style="font-weight: bold;">Source</span>:
         

- URI of the feed source</li>
     </ul>    </li>    <li><span style="font-weight: bold;">FeedTitle</span>:
         

- default: standard
- otherwise define location of feed title based on FeedParser output</li>        </ul>    </li>
 <li><span style="font-weight: bold;">FeedDescription</span>:
         

- default: standard</li>            <li>otherwise define location of feed description based on FeedParser output</li>        </ul>                </li>
 <li><span style="font-weight: bold;">ItemTitle</span>:
         

- default: standard</li>            <li>otherwise define location of item title based on FeedParser output</li>        </ul>    </li>
 <li><span style="font-weight: bold;">ItemDescription</span>:
         

- default: standard</li>            <li>otherwise define location of item description based on FeedParser output</li>        </ul>                </li>
 <li><span style="font-weight: bold;">Replacements</span>:
         

- default: empty</li>            <li>lines field that shows what text needs to be replaced with other values.</li>            <li>example: 'www.nasa.gov -> nasawww-origin1.hq.nasa.gov'</li>        </ul>    

When handling feeds, when a FeedFolder has its update_feed_item action triggered it would:


1. Iterate through its FeedDefinition children.
- Based off the rules in each FeedDefinition, fetch and parse each feed.

- The parsed feeds would be then added to the FeedFolder as FeedItems.

A supplementary view for FeedFolder would be provided that would not display the FeedDefinition.

Comments?  Thoughts?  Anyone think I should move my blog to a place that handles comments better?

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2008/10/morning-brainstorm-about-feedfeeder-v2.html) on Blogger

**Reinout van Rees said on 2008-10-22**

Sounds like your change only helps for that one horrific "RSS feed" you mentioned, the one without actual items and one picture. It doesn't seem to support any generic usecases.

