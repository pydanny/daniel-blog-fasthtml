---
date: "2007-11-13T05:27:00.000-08:00"
description: ""
published: true
slug: 2007-11-im-serving-out-image-and-audio-files
tags:
  - zope
  - legacy-blogger
time_to_read: 5
title: What do you do when zope.Public refuses to be Public?
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/im-serving-out-image-and-audio-files.html)_.

I'm serving out image and audio files from Zope 3 for my Captcha application. Since the images and audio files are for public consumption, I marked their components in the zcml as having the permission of zope.Public. This works fine for the image, but not for the audio component. Is there something I'm missing? For reference, this is part of my [ZCML](https://docs.plone.org/4/en/develop/addons/components/zcml.html):

```xml
<browser:page name="captcha.wav"
  for="captchad.interfaces.ICaptchaContainer"
  class="captchad.browser.folder.CaptchaAudio"
  permission="zope.Public" />

<browser:page
  name="captcha.png"
  for="captchad.interfaces.ICaptchaContainer"
  class="captchad.browser.folder.CaptchaImage"
  permission="zope.Public" />
```

**Update 2007/11/14**: Looks like the object those things reside in need to have `zope.Public` declared for it as well. I'm not sure I like that approach, and I'm wondering if I'm just not getting something about Zope 3 security.
