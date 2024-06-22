---
date: 2013-8-17
published: true
slug: cookie-project-templates-made-easy
tags:
  - python
  - django
  - rant
  - flask
  - pypi
  - pypy
  - python3
  - javascript
  - audrey
  - cookiecutter
time_to_read: 5
title: "Cookiecutter: Project Templates Made Easy"
description: Cookiecutter makes creating and maintaining project templates easy and intuitive.
image: /images/cookiecutter_medium.png
og_url: https://daniel.feldroy.com/posts/cookie-project-templates-made-easy
---

Yesterday, Jeff Knupp wrote an amazing how-to article called "[Open
Sourcing a Python Project the Right
Way](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)".
While I was reading it, I was rather pleased by just how close it is to
my own practices. Considering Jeff's amazing
[Writing](https://www.amazon.com/gp/product/B00B5KG0F8/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00B5KG0F8&linkCode=as2&tag=mlinar-20)
[Idiomatic](https://www.amazon.com/gp/product/B00B5VXMRG/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00B5VXMRG&linkCode=as2&tag=mlinar-20)
[Python](https://www.jeffknupp.com/writing-idiomatic-python-ebook/), it
meant I was on the right track.

The downside, of course, is implementation. Creating reusable Python
packages has always been annoying. There are no defined/maintained best
practices (especially for `setup.py`), so you end up cutting and pasting
hacky, poorly understood, often legacy code from one project to the
other. Some of it does nothing and some of it fails catastrophically on
Python 3. There's a term for this sort of behavior, and it's called
[Cargo Cult
programming](https://en.wikipedia.org/wiki/Cargo_cult_programming).

Fortunately, while I was
[ranting](/made-up-statistics.html#debate-statistics)
and
[Jeff](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
(and [Hynek
Schlawack](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/))
was writing, someone was making
[cookiecutter](https://github.com/audreyr/cookiecutter).

## cookiecutter does one thing and it does it well

What [cookiecutter](https://github.com/audreyr/cookiecutter) does is
make creating and maintaining project templates easy and intuitive. This
allow developers of all languages (not just Python) the ability to break
free from cargo-cult configuration and follow patterns dictated by the
experts who present their own cookiecutter templates. So if you don't
like how the author of cookiecutter's creates her projects, you can use
someone else's or roll your own.

Okay, enough talk, let's use cookiecutter to build a Python project.
Assuming you have [virtualenv](https://www.virtualenv.org/) installed:

```bash
$ pip install cookiecutter
```

**note**: In the works is a [Homebrew](https://github.com/mxcl/homebrew)
package, and possibly packages for the various Linux distributions as
well.

Done? Okay, now use cookiecutter to create your Python project. For this
example, I'm going to create a sample project called "_cheese_".:

```bash
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
Cloning into 'cookiecutter-pypackage'...
remote: Counting objects: 183, done.
remote: Compressing objects: 100% (100/100), done.
remote: Total 183 (delta 87), reused 161 (delta 70)
Receiving objects: 100% (183/183), 29.36 KiB | 0 bytes/s, done.
Resolving deltas: 100% (87/87), done.
Checking connectivity... done
full_name (default is "Audrey Roy")? Daniel Greenfeld
project_name (default is "your project")? cheese
... snip for brevity
```

See how it asks my full name? Well, at this point,
[cookiecutter](https://github.com/audreyr/cookiecutter) begins to ask a
number of questions. These questions are actually specified in the
[cookiecutter.json](https://github.com/audreyr/cookiecutter-pypackage/blob/master/cookiecutter.json)
file for
[cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

Once you've answered everything that
[cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
wants, it generates your project. Let's go and check:

```bash
$ tree cheese
cheese/
├── AUTHORS.rst
├── CONTRIBUTING.rst
├── HISTORY.rst
├── LICENSE
├── MANIFEST.in
├── README.rst
├── docs
│   ├── Makefile
│   ├── authors.rst
│   ├── conf.py
│   ├── contributing.rst
│   ├── history.rst
│   ├── index.rst
│   ├── installation.rst
│   ├── make.bat
│   ├── readme.rst
│   └── usage.rst
├── requirements.txt
├── setup.py
├── simplicity
│   ├── __init__.py
│   └── simplicity.py
├── tests
│   ├── __init__.py
│   └── test_simplicity.py
└── tox.ini
```

While there are _some_ differences from Jeff Knupp's example in his
[article](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
(ReStructuredText vs Markdown, location of tests, etc), I would argue
that the general vision is the same. Better yet, if Jeff (or someone)
wants to implement Jeff's pattern, they can.

In fact...

## Creating cookiecutter templates is easy and intuitive

All you have to do is:

1.  **Fork**
    [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
    **and rename it**.
2.  **Make the changes you desire.** You can change anything you want,
    the setup.py, the test handling, or perhaps add or remove from the
    questions specified in
    [cookiecutter.json](https://github.com/audreyr/cookiecutter-pypackage/blob/master/cookiecutter.json).
    Right now **repo_name** is a mandatory
    [cookiecutter.json](https://github.com/audreyr/cookiecutter-pypackage/blob/master/cookiecutter.json)
    field, but there is an issue submitted to have that changed.
3.  **Remember that renders everything in**
    [Jinja2](https://jinja.pocoo.org/). Questions asked by
    [cookiecutter.json](https://github.com/audreyr/cookiecutter-pypackage/blob/master/cookiecutter.json)
    are rendered to the project's files (be those files in Python,
    Javascript, HTML, etc). So if you add a field to
    [cookiecutter.json](https://github.com/audreyr/cookiecutter-pypackage/blob/master/cookiecutter.json),
    all you have to do to see it in a templates is write:

```django
# Place in Python, HTML. Javascript, CSS, Markdown, or any other plaintext format.
{{cookiecutter.my_new_field}}
```

4.  **Submit a pull request to**
    [cookiecutter](https://github.com/audreyr/cookiecutter) asking for
    their project to be listed on the README.

It's not hard. In fact, there is already a growing ecosystem of
[cookiecutter
templates](https://github.com/audreyr/cookiecutter#available-templates),
including Python, [Flask](https://github.com/sloria/cookiecutter-flask),
[Django](https://www.djangopackages.com/grids/g/cookiecutter/) and
[JQuery](https://github.com/audreyr/cookiecutter-jquery) templates.

**Note**: There is already a
[fork](https://github.com/Nekroze/cookiecutter-pypackage) of
cookiecutter-pypackage that even more closely matches Jeff Knupp's
design.

## Additional cookiecutter features

Here are more things to like about cookiecutter:

### cookiecutter is focused

It doesn't handle deployment, serving of HTTP, testing, or anything
else. All it does is project templates. It follows those classic words,
"_It's programmed to do one thing and do it well_".

### Supports all modern versions of Python

- Python 2.6
- Python 2.7
- Python 3.3
- Even PyPy!

### cookiecutter is modular

It's not built off a single giant function, or a complex architecture.
Instead, it's comprised of a number of relatively simple functions.
Why? Well this way you can import easily elements of cookiecutter into
other projects, and it plays into the next feature:

### cookiecutter is tested

The project has as of August 20th 2013, [98% test
coverage](https://coveralls.io/r/audreyr/cookiecutter?branch=master),
with an intention to increase it to 100%. This makes handling the
following things much easier/safer:

1.  Implementing new features without breaking existing ones.
2.  Handling new versions of Python as they emerge.

### cookiecutter isn't just for Python packages

That's correct. While at the moment there is only
[cookiecutter-jquery](https://github.com/audreyr/cookiecutter-jquery),
there is nothing to stop developers from using
[cookiecutter](https://github.com/audreyr/cookiecutter) to create
templates for anything. The way it renders output is designed to
accommodate customizations for any tool.

Which brings me to my next point...

### cookiecutter isn't just for Python developers

Even if you don't know Python you can use
[cookiecutter](https://github.com/audreyr/cookiecutter). The templating
is done via [Jinja2](https://jinja.pocoo.org/), which isn't far off from
other template languages like Mustache, Handlebars, or Liquid. if you
are worried about collisions between templating systems, just use
Jinja2's `{% raw %}` template tag:

```django
{# Jinja2's raw template to escape the Liquid template inside #}
{% raw %} {# Liquid template from here on #}
<ul id="products">
{% for product in products %}
<li>
  <h2>{{ product.title }}</h2>
  Only {{ product.price | format_as_money }}

  <p>{{ product.description | prettyprint | truncate: 200  }}</p>

</li>
{% endfor %}
</ul>
{% endraw %}
```

[![Cookiecutter logo](/images/cookiecutter_medium.png)](https://github.com/audreyr/cookiecutter)

- **Update 09/20/2013**: Test coverage increased to 98% from 91%.
