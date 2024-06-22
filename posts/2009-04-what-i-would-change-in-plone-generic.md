---
date: '2009-04-06T15:27:00.003-07:00'
description: ''
published: true
slug: 2009-04-what-i-would-change-in-plone-generic
tags:
- rant
- geek celebrities
- plone
- legacy-blogger
time_to_read: 5
title: 'What I would change in Plone: Generic Setup'
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/04/what-i-would-change-in-plone-generic.html)*.

At the [Washington, DC 2008 Plone Conference](https://plone.org/events/conferences/2008-washington-dc) I took [Joel Burton](https://plonebootcamps.com/)'s awesome [two day tutorial on Plone Theming](https://plonebootcamps.com/courses/conf2008-theming). I don't do design myself, but I have implemented them from time to time. My CSS skills are weak, but [Plone](https://plone.org) gives us lots out of the box so I figured this would be a great way to ramp up on skinning. Also, from a work perspective it made sense, because many Plonistas seem to care more about the engineering/database side of things rather than on the front end.

Joel's class, to put it succinctly, was magnificent. If you want to learn Plone, take one of his classes. It is well worth the money.

We learned about reorganizing viewlets on the fly, making css changes, tab controls, content well manipulation and lots, lots more. Two days of knowledge that didn't just go in one ear and out the other, but really stuck.

I was one of the tech-heavy guys in the room, and the rest were graphic designers. At first the ZMI terrified them, and the two different types of views did not go over so easily. But thanks to Joel, by the end of the two days the designers were really enjoying what they could do with Plone. Everyone felt confident and ready to move forward. The positive energy in the room was energizing!

Then it came time to 'save' the site design we had been working on. In other words, export it so it could be reused. Or sold even! We fired off Generic Setup to export things, and then...

<span style="font-weight: bold;">The positive energy diminished</span>

I'm capable of searching through Generic Setup XML files to figure out what is needed in order to capture a Plone skin. I'm sure anyone bothering to read this blog entry is the same way. Yet graphic designer skills tend to end at Photoshop, sometimes at CSS and JavaScript, rarely at PHP. Asking them to go through a few thousand lines of XML is not the way to garner good will.

There was grumbling, and mumbling. Some that were happy until that moment left the class unhappy. Not because of Joel, but because of the export tool that Plone gives us.

When I brought this up with Joel after the class, he said he was aware of it but it was beyond his control. When I brought it up with others, I got a mix of apathy or rejection of the issue. I was told by several that the designer could hand it off to a developer if this was beyond them. Or that it would be too challenging to address. I mentioned it to Tres Seaver and I believe he said he would look into it.

In retrospect<span style="font-weight: bold;">, I should have made a bigger stink about it.</span>

In my opinion, Plone should be as developer friendly as possible. Generic Setup should have an 'Export Skin' function, available via the Plone Control Panel. Not the ZMI.

And I think that this should be part of core Plone. As soon as possible. Preferably Plone 3.3.

Why?

At least half the customers you will ever have care very little about the back end. They just want a pretty and functional site. Which is why graphic designers are often so important to them. For example, how many customers do you have who care more about the comps of the graphic designers than the engineering that publishes it?

By making Plone more accessible and friendly to graphic designers, it means they will stay excited about it. Which will attract more of the graphic designer friendly customers.

<span style="font-weight: bold;">It gets better.</span>

This export utility would empower graphic designers. They will be able to create Plone skins and publish them. They can make money doing this, advertising their craft. In fact, I predict dedicated on-line stores for this sort of thing will become popular, making the cottage industry for plone skins much more viable.

Which is great for us developers who lack decent design skills. If exporting skins is easy, then I can find (and purchase) them and modify to suit customer needs. And if I need one from scratch, I can rely on a larger crowd of graphic designers.

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2009/04/what-i-would-change-in-plone-generic.html) on Blogger

**Martin Aspeli said on 2009-04-06**

I agree fully with your sentiment, but the title of your post isn't right. GenericSetup as a concept is a good thing, and has much wider applicability than skins. The problem, as I see it, is that skins involve ZODB-level configuration at all that *needs* to be exported or imported. Fiddling with viewlets and the like is too hard to start with, let alone exporting/importing them. 

We want to arrive at a situation where skins are created almost entirely from HTML and CSS, mapping "chunks" of Plone's UI to your own brand and applying custom styles. The thing you deploy would be an HTML file, some static resources (images, CSS) and a rules file that determines how Plone's standard, semantic markup is pulled into your theme HTML file.

This is how the new plone.org was created, by the way. :-)

**pydanny said on 2009-04-06**

@martin: Deliverance I presume? Can that be part of stock Plone?

**Matthew Wilkes said on 2009-04-07**

https://quintagroup.com/services/plone-development/products/skin-dump

Works on Plone 2.1 and 2.5, updating it to 3.x would probably be a good idea.

**pydanny said on 2009-04-08**

@Rob - I assume GenericSetup is the right way because it is the way taught in the theming tutorial. Normally I do my work on the file system, but I'm not your normal graphic designer. This isn't for me. Its for the people who download the binaries and play around.

@Martin, @limi - Deliverance/xdv looks to be great stuff. Ian Bicking rocks and so do you. I'm sure given a little bit of time I could use it. However, it ain't stock plone. Can Joe Average graphic designer use it out of the box with Plone or do they have to hunt down a developer? If they have to hunt down a developer, then the solution doesn't match what I was complaining about.

@Matthew - No offense but I was not completely please with the results of skin-dump back in early 2007. If ported to Plone 3 you would need to handle viewlets and all the other p3 specific additions to Plone.

