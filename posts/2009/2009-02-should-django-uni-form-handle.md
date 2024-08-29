---
date: "2009-02-10T17:17:00.005-08:00"
description: ""
published: true
slug: 2009-02-should-django-uni-form-handle
tags:
  - django
  - forms
  - pinax
  - legacy-blogger
time_to_read: 5
title: Should django-uni-form handle boilerplate HTML?
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/02/should-django-uni-form-handle.html)_.

This is in regards to my [django-uni-form](https://code.google.com/p/django-uni-form/) project, which lets you do proper fieldset forms in Django, letting you do prettily formatted forms that meet the Section 508 specification, not to mention various accessibility and usability guidelines.

Basically, I think django-uni-form could be a little more helpful. So what do I mean?

Standard uni-form looks like:

```html
<form class="login uniForm" method="POST" action="">
  <fieldset class="inlineLabels">
    <legend>* Required fields</legend>
    <div class="ctrlHolder ">
      <label for="id_username"> * User Name</label>
      <input id="id_username"
              type="text"
              name="username"
              maxlength="30" />
    </div>
  </fieldset>
  <div class="buttonHolder">
    <button type="reset" class="resetButton">Reset</button>
    <button type="submit" class="primaryAction">Submit</button>
  </div>
</form>
```

django-uni-form gives just:


```html
<div class="ctrlHolder ">
  <label for="id_username"> * User Name</label>
  <input id="id_username" type="text" name="username" maxlength="30" />
</div>
```


Does it make sense for django-uni-form to provide the following?

```html
<fieldset class="inlineLabels">
  <legend>* Required fields</legend>
  <div class="ctrlHolder ">
    <label for="id_username"> * User Name</label>
    <input id="id_username" type="text" name="username" maxlength="30" />
  </div>
</fieldset>
```

With this, you can still add in buttons elegantly. Thoughts?

**Update:**</span>** I'm working with James Tauber and some others to figure out the best way to make this work.
