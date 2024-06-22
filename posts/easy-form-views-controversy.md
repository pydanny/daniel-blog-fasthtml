---
blogbook: "True"
date: "2013-05-10"
published: true
slug: easy-form-views-controversy
tags:
  - python
  - django
  - forms
  - howto
time_to_read: 3
title: The Easy Form Views Pattern Controversy
---

In the summer of 2010 [Frank Wiles](https://twitter.com/fwiles) of
[Revsys](https://revsys.com) exposed me to what I later called the
"**Easy Form Views**" pattern when creating Django form function
views. I used this technique in a variety of places, including [Django
Packages](https://www.djangopackages.com) and the documentation for
django-uni-form (which is rebooted as
[django-crispy-forms](https://github.com/maraujop/django-crispy-forms)).
At DjangoCon 2011 [Miguel Araujo](https://tothinkornottothink.com/) and I
opened our [Advanced Django Forms
Usage](https://lanyrd.com/2011/djangocon-us/shbrd/) talk at DjangoCon
2011 with this technique. It's a pattern that reduces the complexity of
using forms in Django function-based views by flattening the form
handling code.

# How the Easy Form Views pattern works

Normally, function-based views in Django that handle form processing
look something like this:

```python
def my_view(request, template_name="my_app/my_form.html"):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            do_x() # custom logic here
            return redirect('home')
    else:
        form = MyForm()
    return render(request, template_name, {'form': form})
```

In contrast, the Easy Form Views pattern works like this:

```python
def my_view(request, template_name="my_app/my_form.html"):

    form = MyForm(request.POST or None)
    if form.is_valid():
        do_x() # custom logic here
        return redirect('home')
    return render(request, template_name, {'form': form})
```

The way this works is that the `django.http.HttpRequest` object has a
POST attribute that defaults to an empty dictionary-like object, even if
the request's method is equal to "GET". Since we know that
request.POST exists in every Django view, and os at least as an empty
dictionary-like object, we can skip the `request.method == 'POST'` by
doing a simple boolean check on the `request.POST` dictionary.

In other words:

- If `request.POST` dictionary evaluates as `True`, then instantiate
  the form bound with `request.POST`.
- If `the request.POST` dictionary evaluates as `False`, then
  instantiate an unbound form.

Great! Faster to write and shallower code! What could possibly be wrong
with that?

# The Controversy

Before you jump to convert all your function-based form views to this
pattern, consider the following argument raised against it by a good
friend:

> This one of those things where "empty dictionary and null both
> evaluate as false" can bite you.
>
> There's a difference between "There is no POST data", and "This
> wasn't a POST".
>
> -- by [Russell Keith-Magee](https://cecinestpasun.com/) (paraphrased)

The problem he is talking about is data besides `multipart/form-data` or
`application/x-www-form-urlencoded` would still end up in the
`request.POST` dictionary-like attribute.

Where is the controversy? Well, I didn't write a retraction until now.
Arguably I should have done it earlier. However, since I never ran into
the edge case, I didn't see the need. Yet when it comes down to it, the
"Easy Forms" approach has an implicit assumption about the incoming
object, which in Python terms is not a good thing.

# Getting bit by the Easy Form Views method

Here's how it happens:

**Before Django 1.5** HTTP methods such as DELETE or PUT would see their
data placed into Django's `request.POST` attribute. The form would
fail, but it might not be clear to the developer or user why. HTTP GET
and POST methods work as expected.

**For Django 1.5 (and later)** if a non-POST comes in then the form
fails because request.POST is empty. HTTP GET and POST methods also work
as expected.

# Conclusion

Going forward, I prefer to use Django's class-based views or [Django
Rest Framework](https://djangorestframework.com) which make the issue of
this pattern moot. When I do dip into function-based views handling
classic HTML forms, I'm leery of using this pattern anymore. Yes, it is
an edge case, but to inaccurately paraphrase Russell, "edge cases are
where you get bit".

What I'm not going to do is rush to change existing views on existing
projects. That's because personally I've yet to run into an actual
problem with using this pattern. As they say, "_If it ain't broke,
don't fix it._" While I'm not saying my code isn't broken, I'm also
aware that 'fixing' things that aren't reporting errors is a
dangerous path to tread.

Also, next time I get called on something by a person I respect, I'll
respond more quickly. Nearly two years is too long a wait.

**Update:** Changed some of the text to be more succinct and took out
the leading sentence.
