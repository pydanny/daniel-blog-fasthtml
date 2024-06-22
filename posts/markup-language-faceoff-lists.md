---
date: "2015-05-14"
published: true
slug: markup-language-faceoff-lists
tags:
  - python
  - LaTeX
  - RestructuredText
  - markdown
  - django
time_to_read: 6
title: "Markup Language Faceoff: Lists"
image: /images/bullets.png
---

Today I want to talk about lists. Not for shopping, not the programming
data type, but the display of items in both unordered and ordered
fashion.

[![Bullets faceoff](/images/bullets.png)](/markup-language-faceoff-lists.html)

Specifically this:

- Item A
- Item B
  1.  First Numbered Inner Item
  2.  Second Numbered Inner Item
- Item C

In other words, lists of bullets and numbers. This article explores some
of the different tools used by the programming world to render display
lists, specifically **HTML**, **reStructuredText**, **Markdown**, and
**LaTeX**.

# HTML

If you view the [HTML](https://en.wikipedia.org/wiki/HTML) source of this
web page, you'll find this:

```html
<ul class="simple">
  <li>Item A</li>
  <li>
    Item B
    <ol class="arabic">
      <li>First Numbered Inner Item</li>
      <li>Second Numbered Inner Item</li>
    </ol>
  </li>
  <li>Item C</li>
</ul>
```

Or more clearly:

```html
<ul class="simple">
  <li>Item A</li>
  <li>
    Item B
    <ol class="arabic">
      <li>First Numbered Inner Item</li>
      <li>Second Numbered Inner Item</li>
    </ol>
  </li>
  <li>Item C</li>
</ul>
```

This works, but is incredibly verbose. **HTML** requires closing tags on
every element (keep in mind browsers are not the same as
specifications). Working with lists in HTML becomes tedious quickly.
Which is why so many people use
[WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) tools or mark up
languages like **reStructuredText** and **Markdown**, as it expedites
creation of lists (and many other things).

# reStructuredText

This blog is written in
[reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) and
transformed into **HTML**. Let's see the markup for this blog post:

```
* Item A
* Item B

  #. First Numbered Inner Item
  #. Second Numbered Inner Item

* Item C
```

Notice the extra lines between bullets and numbers? A behavior of
**reStructuredText** is that you have to put those in nested lists in
order to make things display correctly. Also, 2 spaces indentation
generates a different result than 4 spaces, the former creating
sub-bullets, the latter creating an indented block quote with bullets.
They are there to remove ambiguity.

Interestingly enough, I did not know this until the day after I wrote
this article. Since understanding these behaviors can be challenging,
myself and Eric Holscher of [ReadTheDocs](https://readthedocs.org) fame
began a project last year to [clearly index and
document](https://restructuredtext.readthedocs.org/) all the details of
**reStructuredText** from the user's point of view. Our plan was to
provide this as an adjunct to the [formal
documentation](https://docutils.sourceforge.net/docs/) of
**reStructuredText**. Alas, time and work considerations got in the way.
If you want to help expand our effort, you can contribute at
<https://github.com/pydanny/restructuredtext>.

One thing to note about **reStructuredText** is that it's pretty much
Python only. Outside the Python world if you are writing plaintext
markup then odds are you are using **Markdown**.

# Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) does lists really
well. Terse and no weird quirks:

```markdown
- Item A
- Item B
  1. First Numbered Inner Item
  1. Second Numbered Inner Item
- Item C
```

Another nice feature about **Markdown** is that it's in use everywhere.
GitHub, Stack Overflow, my favorite tablet writing app, and a lot more.

# Markdown vs. reStructuredText

Why don't I switch from **reStructuredText** to **Markdown**? Here are
my reasons against switching:

1.  Force of habit.
2.  [PyPI](https://pypi.python.org/pypi) requires it to display package
    long descriptions nicely on Package pages.
3.  [Sphinx](<https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)>)
    is based on it.
4.  **reStructuredText** has one concrete standard, with extensions that
    people add. Markdown has many standards, which may or may not have
    shared features.
5.  I can use [Pandoc](https://pandoc.org) to help transform
    **reStructuredText** to **Markdown**.

# LaTeX

Finally, let's discuss [LaTeX](https://en.wikipedia.org/wiki/LaTeX).
While not a markup language it bears mentioning, and I'll explain why
later in this section.

Up to about 8-10 years ago **LaTeX** was used in a lot of technical
writing, including the Python core documentation. That ended with the
rise of mark up languages, relegating **LaTeX** to the world of
academics, mathematicians and computer scientists - anywhere complex
equations need to be specified.

LaTeX belongs in this article because it is so commonly used with
markup. In fact, as far as I can tell, in order to render
**reStructuredText** and **Markdown** content into the PDF format, the
most common approach is:

1.  Use a script to transform the markup into **LaTeX**.
2.  Use a tool like [XeTeX](https://en.wikipedia.org/wiki/XeTeX) to
    render the **LaTeX** into PDF.

Why the extra step? Why not just go directly from markup to PDF? Well,
the content in **reStructuredText** and **Markdown** have to be
formatted in order for them to be displayed, or they will just look like
plaintext markup. When they are converted to **HTML**, the browser does
the formatting for us. When they are translated to PDF, LaTeX is a very
common choice. That is because **LaTeX** isn't a markup language, but a
typesetting tool. Unlike **reStructuredText** and **Markdown** which are
designed for ease of use, **LaTeX** is designed to make documents look
good.

Here is how I define my sample list in **LaTeX**

```latex
\begin{itemize}
    \item Item A
    \item Item A
        \begin{enumerate}
            \item First Numbered Inner Item
            \item Second Numbered Inner Item
        \end{enumerate}
    \item Item C
\end{itemize}
```

Halfway between the markup languages and HTML in verbosity, **LaTeX**
lists are of medium difficulty to write. If this example makes **LaTeX**
look easy, please realize that while lists are easy to understand, other
structures like **LaTeX**
[tables](https://en.wikibooks.org/wiki/LaTeX/Tables) can quickly get out
of hand. **LaTeX**'s reputation for being an arcane tool is a well
deserved one.

# Modifying Generated LaTeX

Several book authors, including ourselves, have written books using
**reStructuredText** or **Markdown**, generated the **LaTeX**, then
modified the **LaTeX** before rendering the PDF. The approach is
seductive: You get the ease of a markup language combined with the
formatting precision of **LaTeX**.

Or do you?

The problem my wife and I have faced is that the combination of
**LaTeX** packages and tools we've assembled for ourselves to write
books like [Two Scoops of
Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) is
very, very different than what is rendered via
[docutils](https://pypi.python.org/pypi/docutils)' `rst2latex` or
Sphinx `make latex`. We've tried to write migration scripts, but have
found that we end up spending too much of our time on formatting.
That's why we have stuck with hand-crafted artisan **LaTeX**.

That isn't to say it isn't possible. In fact, Matt Harrison has
[released](https://www.amazon.com/Brief-Introduction-Python-Testing-Harrison-ebook/dp/B00AY4VE8E/?tag=mlinar-20)
a number
[handsome](https://www.amazon.com/Guide-Learning-Iteration-Generators-Python/dp/1492333514/ref=sr_1_7?tag=mlinar-20)
[Python](https://www.amazon.com/Treading-Python-1-Foundations/dp/1475266413/ref=sr_1_2?tag=mlinar-20)
[books](https://www.amazon.com/Treading-Python-2-Intermediate/dp/149055095X/ref=sr_1_1?tag=mlinar-20)
following this path (**reStructuredText** to **LaTeX**). I'm certain
there are **Markdown** books that follow this path too.

# Closing Thoughts

For better or for worse, lists of bullets and numbers are a foundation
of how we communicate via the written medium. They allow for terse
communication of ideas and thought, but that same terseness can mean we
skip over details. Interestingly enough, the very tools that we use to
create lists can color our ability and desire to use them.

- Update 2015/05/14 - Added note about closing `</li>` tags thanks to
  Ivan Sagalaev.
- Update 2015/05/14 - Made Markdown list more cross-compatible thanks
  to Tzu-ping Chung.
- Update 2015/05/14 - Fixed LaTeX list definition thanks to Mark van
  Lent.
- Update 2015/05/15 - Explained the behaviors of **reStructuredText**
  thanks to David Goodger.
