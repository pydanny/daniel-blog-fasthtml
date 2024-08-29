---
date: "2009-01-12T09:58:00.004-08:00"
description: ""
published: true
slug: 2009-01-django-uni-form-lives
tags:
  - django
  - pinax
  - legacy-blogger
time_to_read: 5
title: django-uni-form lives!
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/01/django-uni-form-lives.html)_.

[Django Uni-Form](https://github.com/pydanny/django-uni-form/) is my answer to a problem with the Django forms API in that they do not play so well in the arena of the disability access. The default view uses tables which is not disabled friendly. Other views build forms as paragraphs or lists, neither which is optimal for attractive display of HTML forms.

My answer was to create the application above. It incorporates the wonderful [uni-form](https://sprawsm.com/uni-form/) css and javascript combination to create disability-friendly yet attractive forms. Turn off JavaScript, CSS styles, or access it from a mobile phone and these forms should still work. Which is critical in my job. Best of all, you don't have to touch much HTML at all.

I tried to make it as Django generic as I could, but as a Django newbie it is probably a bit rough around the edges. The code, if you examine it, is really clean. I like that about Django efforts - there is no boilerplate!

Anyway, after a bit of setup, you do an easy modification of the form templates that are presenting your Django forms. You should also style it a bit to match your preferences.

Some final notes and comparisons:

1. Time to get a basic version running was about 45 minutes.
2. Time to get the styling working was about 1 hour (mostly a stupid mistake on my part).
3. I'm hoping the Pinax project will incorporate my efforts! ;)
4. The Django docs were very clear on everything I needed to do. I did not have to leave [https://docs.djangoproject.com](https://docs.djangoproject.com/) to accomplish my chosen task. I cannot stress enough that this is something I really enjoy about Django.
5. This was fun and easy.

**Edit on 7/15/2010**: Changed the link to django-uni-form on github.

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2009/01/django-uni-form-lives.html) on Blogger

**pydanny said on 2010-07-15**

John, please use the github version, not the google code version!
