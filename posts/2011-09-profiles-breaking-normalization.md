---
date: "2011-09-23T09:49:00.000-07:00"
published: true
slug: 2011-09-profiles-breaking-normalization
tags:
  - django
  - legacy-blogger
time_to_read: 5
title: "Profiles: Breaking Normalization"
description: "How my Django profile models looked over 10 years ago."
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/09/profiles-breaking-normalization.html)_.

In the summer of 2010 I either saw this pattern or cooked it up myself. It is specific to the [Django](https://djangoproject.com/) [profiles](https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users) system and helps me get around some of the limitations/features of [django.contrib.auth](https://docs.djangoproject.com/en/1.3/topics/auth/). I like to do it on my own projects because it makes so many things (like performance) so much simpler. The idea is to replicate some of the fields and methods on the[ django.contrib.auth.model.User ](https://docs.djangoproject.com/en/1.3/topics/auth/#users) model in your user profile(s) objects. I tend to do this usually on the [email](https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.models.User.email) , [first_name](https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.models.User.first_name) , [last_name](https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.models.User.last_name) fields and the [get_full_name](https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.models.User.get_full_name) method. Sometimes I also do it on the [username](https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.models.User.username) field, but then I also ensure that the username duplication is un-editable in any context.

Sure, this breaks [normalization](https://pydanny.blogspot.com/2011/07/normalization-noitazilamron.html), but the scale of this break is tiny. Duplicating four fields each with a max of 30 characters for a total of 120 characters per record is nothing in terms of data when you compare to avoiding the mess of doing lots of <b>profile-to-user</b> joins on very large data sets.

One more thing, I've found that most users don't care about or for the division between their accounts and profiles. They are more than happy with a single form, and if they aren't, well you can still use this profile model to build both account and profile forms.

Alright, enough talking, let me show you how my Profile models tend to look:

```python
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    """ Normalization breaking profile model authored
        by Daniel Greenfeld """

    user = models.OneToOneField(User)
    email = models.EmailField(_("Email"), help_text=("Never given out!"), max_length=30)
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=30)

    # username field notes:
    #     used to improve speed, not editable!
    #     Never changed after original auth.User and profiles.Profile creation!
    username = models.CharField(("User Name"), editable=False)

    def save(self, **kwargs):
        """ Override save to always populate changes to
            auth.user model """
        user_obj = User.objects.get(username=self.user.username)
        user_obj.first_name = self.first_name
        user_obj.last_name = self.last_name
        user_obj.email = self.email
        user_obj.is_active = self.is_active
        user_obj.save()
        super(Profile,self).save(**kwargs)

    def get_full_name(self):
        """ Convenience duplication of the auth.User method """
        return "{0} {1}".format(self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ("profile_detail", (), {"username": self.username})

    def __str__(self):
        return self.username
```

All of this is good, but you have to be careful with emails. Django doesn't let you duplicate existing emails in the <b>django.contrib.auth.model.User</b> model so we want to catch that early and display an elegant error message. Hence this Profile form:

```python
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from profiles.models import Profile

class ProfileForm(forms.ModelForm):
    """ Email validation form authored by Daniel Greenfeld """

    def clean_email(self):
        """ Custom email clean method to make sure the user doesn't
        use the same email as someone else"""
        email = self.cleaned_data.get("email", "").strip()
        if User.objects.filter(email=email).exclude(username=self.instance.user.username):
            self._errors["email"] = self.error_class(["%s is already in use in the system" % email])
            return ""
        return email

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        model = Profile

```

---

## 4 comments captured from [original post](https://pydanny.blogspot.com/2011/09/profiles-breaking-normalization.html) on Blogger

**Unknown said on 2011-09-23**

Would it be prudent to just inherit from the User model for the profile model and still do the same save method? Cut off some code that way.

**pydanny said on 2011-09-23**

Cezar - I should have put this in my post and that is &quot;Don't inherit from the auth.User model.&quot; Yeah, it is how we should be able to do it, but you end up with weirdness and problems. Hence the get_profile() model and this blog post.

**Chris Adams said on 2011-09-23**

Two notes: 
_ I'd add a post_save signal handler on User which would propagate changes forward if there's any possibility that something else will change those values directly
_ in the save() method you can simply do a User.objects.filter(email=self.email).update(… denormalized fields…) to save a database query.

**pydanny said on 2011-09-23**

Chris - I use signals as little as possible. I keep getting bit by them. They are generally documented poorly, can make system migrations unreasonably difficult. And in this case, they can cause infinite loops because your Profile.save() will change the User which will change the Profile which will change the User, ad infinitum...

I do like the User.objects.filter(email=self.email).update(… denormalized fields…) idea. :)
