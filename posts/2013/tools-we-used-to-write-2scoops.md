---
date: 2013-5-03
published: true
slug: tools-we-used-to-write-2scoops
tags:
- django
- python
- twoscoops
- book
- LaTeX
time_to_read: 9
title: Tools we used to write Two Scoops of Django
---

Because of the ubiquitousness of
[reStructuredText](https://en.wikipedia.org/wiki/Restructured_Text) in
the lives of [Python](https://python.org) developers and the advocacy of
it, it's not uncommon for people to assume we used it to write our
book. However, that's not really the case.

The short answer is we used:

-   reStructuredText (RST)
-   Google Documents
-   Apple Pages
-   [LaTeX](https://en.wikipedia.com/wiki/LateX)

The long answer is the rest of this posting. Since writing the book was
broken up into three major stages '*alpha*', '*beta*', and
'*final*', so have I broken up blog article.

Alpha Days
==========

Some of the original alpha material was written in rough draft form as
RST since it was what we were used to using. Unfortunately, the PDF
generation wasn't to our liking, so we immediately began looking at
other options. Since she enjoyed using it at MIT and because it gave us
greater individual control, [Audrey](https://audrey.roygreenfeld.com) wanted to
switch to [LaTeX](https://en.wikipedia.com/wiki/LateX). I was worried
about the challenges of learning LaTeX, so we compromised and moved to
Google Documents.

For the most part, Google Documents was great in the early stages. The
real-time collaborative nature was handy, but the gem was the comment
system. It gave us the ability to have line-by-line written dialogues
with our technical reviewers. However, Google Documents makes it
nigh-impossible to use WYSIWYG editor styles, add in better print fonts,
forced us to cut-and-paste code examples, and finally the PDF export
system was flakey on our massive document.

Our original thought was to convert the Google Document output to PDF
and then modify it with Adobe InDesign. Upon trying it, we found it had
a lackluster user interface that had a steep learning curve and was
prohibitively expensive ($550-$700). Our friend and reviewer, Kenneth
Love of [Getting Started with
Django](https://gettingstartedwithdjango.com) fame, offered to do the
conversion work, but we wanted to be able to update our work at will.
Awesome as Kenneth might be, we couldn't expect him to drop what he was
doing to update the final output of our work whenever we wanted.

Therefore, what we did in the week of January 10th-16th was convert the
book to Apple Pages, which is the word processor in Apple iWorks. This
was as painful as it sounds. We also discovered the day before launch
that Apple Pages doesn't create a sidebar PDF table of contents, which
a lot of people enjoy (including ourselves). Tired and exhausted from
weeks of 16 hour days, we launched anyway on January 17th with the book
weighing in at 5.1 MB.

Beta Experiences
================

People were so positive it really gave us a boost. Hundreds of people
sent us feedback and we were delighted beyond words, with a significant
portion sending us commentary/corrections about our writing and code.
I'll admit I did get tired over a certain 'moat' mistake since I got
corrected on it over 50 times. However, the number of code corrections
we were getting was higher than expected. It was clear we needed to be
able to import the code modules from testable chunks of real code. We
had so many kindle/epub requests we also needed the ability to render
the text attractively across multiple formats.

After stumbling through RST, Google Documents, and Apple Pages different
tools, I finally agreed with Audrey that the challenges of learning
LaTeX was worth it. While we could have used RST, we would have had to
use LaTeX anyway for our customizations since when RST is converted to
PDF it actually uses an interim step of LaTeX!

So while I handled the corrections and feedback from thousands, Audrey
built the fundamentals of the LaTeX file structure. Audrey really got
her hands dirty by teaching me LaTeX, since my brain is slow and thick.
Here's a sample of what I've learned how to do, taken from Chapter 6,
Section 1, Subsection 5 (6.1.5):

``` latex
\subsection{Model Inheritance in Practice: The TimeStampedModel}
It's very common in Django projects to include a \inlinecode{created} and \inlinecode{modified} timestamp field on all your models. We could manually add those fields to each and every model, but that's a lot of work and adds the risk of human error. A better solution is to write a \inlinecode{TimeStampedModel} \index{TimeStampedModel} to do the work for us:

\goodcodefile{chapter_06/myapp/core/timestampedmodel.py}

Take careful note of the very last two lines in the example, which turn our example into an abstract base class: \index{abstract base classes}

\goodcodefile{chapter_06/myapp/core/class_meta.py}

By defining \inlinecode{TimeStampedModel} as an abstract base class \index{abstract base classes} when we define a new class that inherits from it, Django doesn't create a \inlinecode{model\_utils.time\_stamped\_model} table when syncdb is run.
```

Once I got the hang of LaTeX, then began the hard work of converting the
book's current content from Apple Pages. That was a couple weeks of
grueling effort on my part while Audrey wrote more book material. Daily
I would request a new LaTeX customizations, which Audrey would address.
However, as she was working on literally rewriting the content of a
dozen chapters including templates, testing, admin, and logging my
interruptions became an issue. So we enlisted the help of Italian
economist and LaTeX expert Laura Gelsomino. Thanks to her the desired
text formatting was achieved.

During the conversion process we rewrote every single code example,
putting them into easily testable projects, and pulled them into the
book via use of custom LaTeX commands called `\goodcodefile{}` and
`\badcodefile{}`.

Eventually I joined Audrey on rewriting and reviewing chapters and on
February 28th, the beta was launched. LaTeX generates lean PDFs so the
book came in at just 1.6 MB while adding a whopping 50 pages (25% more)
of content.

Final Efforts
=============

The final effort was focused on cleanup, new formats, presentation, and
art.

For cleanup, our amazing readers gave us so much feedback we could
barely keep up. We fought to keep our dialogues with them personal yet
brief. With reader oversight we corrected many of the 'quirks' of my
writing style (Audrey is a stickler for Strunk and White, I am not). We
also made numerous corrections based on feedback and our own
observations.

With the guidance of fellow Python author [Matt
Harrison](https://hairysun.com/) I wrote scripts that took the archaic
HTML generated by LaTeX module tex4ht and rendered it into something
that Kindlegen could use to generate Kindle .mobi files. At first the
results looked awesome on modern kindles and other new ebook readers,
but was terrible on older devices. So I toned back the fancy stuff to
what you see today. Getting technical books to look nice on all readers
is really, really hard - and unfortunately some publishers take
shortcuts that hurt the efforts of the authors. If you have problem with
an e-book's format, please consider that before writing a negative
review about the final output.

Speaking of mobile editions, we also wrote a second version of each
Python example to deal with the smaller format. While libraries exist to
do the work for you, since I did a lot of it from scratch (albeit
coached by Matt) I had to dig into the lackluster .mobi/.epub
documentation to figure out things like .ncx files.

**note:** If you want to be the self-published author of a technical
book I *strongly recommend* you read Matt's [Ebook Formatting: KF8,
Mobi &
EPUB](https://www.amazon.com/Ebook-Formatting-Mobi-EPUB-ebook/dp/B00BWQXHU6/ref=la_B0077BQLH6_1_2?ie=UTF8&qid=1366041987&sr=1-2&tag=ihpydanny-20).
Also check out his rst2epub2 library for converting RST files to various
formats.

While I worked on the mobile editions, Audrey focused on the print
version and adding more art and bits and pieces of new content. She
focused on clarity and flow, and the result is that the book feels even
lighter to read and yet is dense with useful information. To test how
the book launched, she would order a copy from the printer and wait
several days for it to arrive. Then she would inspect the cover and
interior with her incredibly exacting eye. It's a slow process, but
Audrey wanted to make absolutely certain our readers would enjoy and use
the print edition.

On April 10th we launched the final in PDF, Kindle, and ePub form. The
PDF weighs in at 2.7 MB, and the Kindle file is a bit heaver. At some
point we'll do the work to reduce file size, but for now we're working
on other things.

A week later we announced the launch of the [print version of the
book](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/1481879707/ref=sr_1_2?ie=UTF8&qid=1366166104&sr=8-2&tag=ihpydanny-20).
People seem to really like the design and feel of the physical book, and
we've even had requests for t-shirts.

Thoughts
========

Writing a technical book was really hard. Crazy hard. Also very
satisfying. We could have made more money doing just client work, but
this was a dream come true. Sometimes money doesn't matter.

Whither Two Scoops of Django?
-----------------------------

[Two Scoops of Django: Best Practices for Django
1.5](https://roygreenfeld.com/products/two-scoops-of-django-1-5) will still receive periodic corrections,
but won't see new content unless it's security related for Django 1.5.
Don't worry though, for when Django 1.6 comes nigh, we'll commence
work on Two Scoops of Django: Best Practices for Django **1.6** (**TSD
1.6**). The plan is to update practices as needed and hopefully add more
content on testing, logging, continuous integration, and more. Like
it's predecessor TSD 1.6 will be written using LaTeX.

That said, if I ever fulfill my dream of writing fiction I'll just use
Matt Harrison's [rst2epub2](https://github.com/mattharrison/rst2epub2)
library.

Concerns About Open Sourcing
----------------------------

We've considered open sourcing our current book generation system, but
installation is rather challenging and requires serious
Audrey/Laura-level LaTeX knowledge combined with my experience with
Python. Unfortunately, from our experience on managing other open source
projects, dealing with requests for documentation and assistance would
take up a prohibitive amount of our time. Honestly, we would rather
write another book or sling code.

Book Generation as a Service?
-----------------------------

Another option is turning our system into a service, which would convert
existing RST or even MarkDown to LaTeX so it could generate books in the
Two Scoops format. Doing this would require at least a month of
full-time work on both of our parts, and we have no idea as to the
interest level. We think it would be a low amount of interest, but then
again, hasn't [leanpub](https://leanpub.com) done pretty well using this
model of business?

In any case we're working on other projects. Maybe even a new technical
book...
