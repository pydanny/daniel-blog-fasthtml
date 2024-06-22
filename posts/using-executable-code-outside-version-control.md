---
date: '2018-08-03'
description: Fighting the local_settings.py antipattern
published: true
slug: using-executable-code-outside-version-control
tags:
- python
- django
- twoscoops
time_to_read: 4
title: Stop Using Executable Code Outside of Version Control
---


There's an anti-pattern in the development world, and it's for using executable code as a means to store configuration values. In the Python universe, you sometimes see things like this in settings modules:

```python
# Warning: This is an anti-pattern!
try:
    from .local_settings import *
except ImportError:
    pass
```

What people do is have a `local_settings.py` file that has been identified in a `.gitignore` file. Therefore, for local development you have your project running through an **executable code file outside of version control**.

If this sounds uncomfortable to you, then you are on the right track. Executable code **always** needs to be in version control.

A better approach is to place secrets and keys into environment variables. If you don't like that, or can't use it due to your environment, stick those values into JSON, YAML, or TOML files.

So what can happen if you allow the `local_settings` anti-pattern into your project?

### The `local_settings` anti-pattern

The `local_settings` anti-pattern means that you can have executable code in production that usually can't be viewed by developers trying to debug problems. If you've ever experience it, this is one of the worst production debugging nightmares.

### It worked fine on my laptop!

What works locally and tests successfully can throw subtle bugs that won't be discovered until it's too late. Here's a real-world example of what can happen that I helped resolve for a client last year:

1. Project had been using a third-party package for slugification for years. Configuration done in settings.
2. Developer decided to write their own slugification project. Worked great locally, so they made changes across the site to account for the new behavior.
3. Tests did not account for edge cases in the new slugification library.
4. Appeared to work in local development, staging, and even production.
5. A few days later customers in certain regions of the world started to complain about records being unreachable.
6. No one can figure out why production is behaving differently.

I was brought in (and I billed them). First thing I check is for this sad code snippet in their settings modules

```python
# Warning: This is an anti-pattern!
try:
    from .local import *
except ImportError:
    pass
```

They had `executable` code outside of version control. What worked for the developer, didn't work the same everywhere else. Enough that it caused subtle bugs that weren't caught by humans or formal tests. Subtle developer bugs grew into serious bugs when encountered by real users. 

And what was really bad is that these serious bugs were impossible to debug at first because the deployed code didn't match what was in someone's `local_settings.py` file.

### But I won't make these mistakes!

People often say indignantly, "I'm not stupid like you, I don't make this kind of mistake."

Yet about once a year for the past 20 years I resolve or help resolve an issue stemming from executable code that wasn't tracked in version control.

I believe that all of us coders, no matter how talented and experienced, can and will make stupid mistakes. That's why good engineers/coders follow best practices - to help catch ourselves when we do something stupid. If you believe you can personally avoid making stupid mistakes in programming, I've got a bridge in New York City I can sell you.

With all of this in mind, why not do the `smart` thing and put all executable code in version control? You can put your secrets and keys in environment variables or configuration files. Done! Argument over!

### How to handle location specific variables

Use either either environment variables or config files. Really. And don't take my word for it, look at all the deployment tools and hosting services that recommend it (all of them do).

To do this, either figure out your own process for handling them or use a third-party package. Personally, for Django I like the simplicity of having this function in my various settings modules:

```python
# Good code!
from django.core.exceptions import ImproperlyConfigured


def get_env_var(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_var("SECRET_KEY")
```

### I wrote a book to stop antipatterns

In 2012 I kept getting offered rescue projects because people were using anti-patterns, especially this one. It was frustrating to see the same mistakes again and again. So I started to write a book, [Two Scoops of Django](https://roygreenfeld.com/products/two-scoops-of-django-1-11), designed to instruct people on how not to fall into anti-patterns like the one described in this article.

If you don't want to buy my [book](https://roygreenfeld.com/products/two-scoops-of-django-1-11), please read and embrace the config section of [The Twelve Factor App](https://12factor.net/config). Your future self will thank me for it.
