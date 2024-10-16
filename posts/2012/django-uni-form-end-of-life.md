---
date: "2012-02-18"
published: true
slug: django-uni-form-end-of-life
tags:
  - django
  - python
  - forms
time_to_read: 7
title: django-uni-form end of life
---

I started on django-uni-form in January 2009. In order to use
[Pinax](https://pinaxproject.com) on an internal social network for
[NASA](https://www.nasa.gov) HQ, we had to render all content, including
forms, [Section
508](https://django-uni-form.readthedocs.org/en/latest/concepts.html#section-508)
compliant. Rather than rewrite the html for all 50+ forms that existed
in the Pinax 0.5.x framework at that time, I decided to minimize my work
and automate things. [James Tauber](https://jtauber.com) gave guidance
and insight, my co-workers were supportive, and [Jannis
Leidel](https://enn.io) suggested the Uni-form library. The name **Django
Uni-Form** was obvious, and lo the project was named.

Looking at the old, extremely deprecated [Google Code site for
django-uni-form](https://code.google.com/p/django-uni-form/), I see that
the first commit happened on January 7th, 2009. That was for version
0.1, with some core code that was literally a merger between the Django
form example on how to integrate divs into forms and the simplest
template tag I could figure out.

The python code in `uni_form/templatetags/uni_form.py`:

```python
from django.template import Context, Template
from django.template.loader import get_template
from django import template


register = template.Library()

@register.filter
def as_uni_form(form):
    template = get_template('templates/uni_form.html')
    c = Context({'form':form})

    return template.render(c)
```

The template tag code was nearly exactly copy/pasted from the starter
[Django docs on
forms](https://docs.djangoproject.com/en/1.0/topics/forms/#looping-over-the-form-s-fields):

```django
{% for field in form %}
    <div class="ctrlHolder {% if field.errors %}error{% endif %}">
        {% for error in field.errors %}
            <p class="errorField">
                <strong>{{ error }}</strong>
            </p>
        {% endfor %}
        {{ field.label_tag }}
        {{ field }}
        {% if field.help_text %}
        <p class="formHint">
            {{ field.help_text }}
        </p>
        {% endif %}

    </div>
{% endfor %}
```

Using it was trivial, you just wrote out:

```django
{% load uni_form %}

<form>
    {{ form|as_uni_form }}
</form>
```

# Days of django-uni-form

Leading up to PyCon 2009 James Tauber suggested some things that lead to
the
[FormHelpers](https://django-uni-form.readthedocs.org/en/latest/concepts.html#form-helpers),
and we hammered out the API on IRC. We knew it crossed the rigid lines
between Model-View-Template, but sometimes it's advantageous to break a
few rules and abstractions in order to get better things down the road

At PyCon 2009 with the mentoring of Jannis, James, and [Brian
Rosner](https://twitter.com/brosner), I moved the project from google
code to [Github](https://github.com/pydanny/django-uni-form). Jannis
released it on [PyPI](https://pypi.python.org/pypi/) and I followed the
pattern he showed me for two years. Yeah, I learned tons under those
guys.

After PyCon 2009 a pull request with the
[Layout](https://django-uni-form.readthedocs.org/en/latest/helpers.html#layouts)
helper was provided. It took some work to make it pass all the tests and
use cases, but the end result was definition of form layout in the
Python. This broke the rigid battle lines of Model-View-Template and
left purists screaming in agony, but it certainly made working with
forms in Django trivially easy.

Lots of people started to use the project across projects like Pinax and
organizations like NASA, [PBS](https://pbs.org), Discovery Channel,
various newspapers and many others. Lots of pull requests came in and
the features grew.

In 2010, [Alice Rowland](https://twitter.com/arowla) submitted the first
[Sphinx](https://sphinx.pocoo.org/) docs, and it was her work that really
helped get me started on doing lots of Sphinx work.

And, all the way into 2011, pull requests for Django Form Sets started
to come rolling in, and almost none were of acceptable quality. They
never came with documentation, tests, and almost always broke existing
tests really hard. Since I'm not a huge fan of Django FormSets, I
didn't want to put in a ton of effort making them work. I believe one
of them was pretty good, but life was crazy busy at the time and I let
it slide. Apologies to whoever it was gave me a working FormSet pull
request with documentation, tests, and working code.

Long periods were going by without new versions. I admit I often slow
about accepting pull requests. Life was busy and reviewing the incoming
code took a lot of time. Browser cross-checking, running tests, and more
was really time consuming. I tried to get others to become co-leads on
the project, but invariably they didn't have time to do it. Note: If
someone asks you to co-lead something, respond in 24 hours.

# Enter Miguel Araujo

After PyCon 2011, when there was some unpleasant stress in my life, I
woke up cranky one morning and mouthed off on twitter to this guy who
asked me to accept a pull request on django-uni-form. This guy tweeted
back to me saying I ought to be nicer since I had a library people
liked.

He was right.

I apologized to the guy ([Miguel Araujo](https://twitter.com/maraujop))
and remembered my manners. Over the next couple of months we chatted via
Twitter and Github's messaging system. He was smart, trustworthy, and
passionate about everything he did. I knew I had found my co-lead. He
responded promptly and I gave him commit rights.

Working together (with him doing the vast majority of the work), we
moved the project into new releases. The architecture and design
changed, driven by discussions we had together. The code was cleaned up,
gnarly bits in there to support old versions of Python and Django kicked
out, and the documentation revised. The project had new life!

The only blip I saw with Miguel is my own fault of sometimes being too
nice as a project leader when it comes to accepting pull requests. [I
believe pull requests should be really
atomic](https://django-uni-form.readthedocs.org/en/latest/contributing.html#how-to-get-your-pull-request-accepted)

- for one thing and one thing only with support tests and documentation.
  Otherwise it becomes nigh impossible to incorporate them and these days
  I reject multi-purpose pull requests. One pull request in particular
  took a huge amount of debate and discussion to work in. I think after
  that Miguel is much better at being upfront at the beginning about
  rejecting pull requests with giant scopes.

During all this I asked Miguel to take over the project, he accepted,
and [I even blogged my announcement his role as project
leader](https://pydanny.blogspot.com/2011/06/announcing-django-uni-form-080-beta.html).
Miguel is indeed very nice and after that fact he asked me to remain on
board as co-lead.

We finally met in September of 2011 and co-presented on [Advanced Django
Form Usage at DjangoCon
2011](https://www.slideshare.net/pydanny/advanced-django-forms-usage).
The deepest technical material we presented was authored by Miguel.
During our research he uncovered at least one bug in Django and got an
ancient bug closed. It was a great experience and I hope he'll
co-present with me in the future.

# django-uni-form is dead, long live django-crispy-forms

The upside of django-uni-form is that it grew in features organically
thanks to my own needs and general community effort. The downside of
django-uni-form is that it grew in features organically thanks to my own
needs and general community effort. In any long running project there is
cruft and weird patterns that start to hurt after a while.
django-uni-form was no different.

So I'm making this absolutely official as of now. **django-uni-form is
at it's end of life**. It's done and kaput. No more pull requests will
be accepted and the issue tracker will be turned off shortly. Just so no
one is mistaken:

> **django-uni-form is deprecated. Use django-crispy-forms**

Miguel asked if he could start the project anew, under a different name.
We both had been uncomfortable with the name _django-uni-form_ for some
time, especially since it had almost nothing to do with Uni-form
anymore. In fact, I often using template overrides to avoid the Uni-form
HTML layout - the most common alternative being [Twitter
Bootstrap](https://twitter.github.com/bootstrap/).

We tossed around names for the project, but all of them were stupid,
especially mine. We are both huge fans and users of
[django-floppyforms](https://github.com/brutasse/django-floppyforms)
(HTML5 form widget app), so my fiancee (now wife), [Audrey
Roy](https://audrey.feldroy.com), suggested django-crispy-forms. And lo, the
project was named.

Right now
[django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
has an improved API, better performance, and supports both Twitter
bootstrap forms 2.0 and UniForm. Adding new form layouts will be easier,
and feature controls will be better.

What you should be using now is
[django-crispy-forms](https://github.com/maraujop/django-crispy-forms).
Don't worry about changing over as there are [migration
instructions](https://django-crispy-forms.readthedocs.org/en/d-0/migration.html)
on the [excellent
documentation](https://django-crispy-forms.readthedocs.org/).

Try it. You'll like it. :-)
