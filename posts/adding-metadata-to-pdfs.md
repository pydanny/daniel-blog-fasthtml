---
date: "2020-02-28T04:30:00.00Z"
description: How to use Python to combine PDFs and then add metadata to them.
published: true
slug: adding-metadata-to-pdfs
tags:
  - python
  - pdf
  - book
  - django
  - twoscoops
  - django-crash-course
time_to_read: 3
title: Adding Metadata to PDFs
type: post
---

For both [our books](https://www.feldroy.com) we're using a new process to render the PDFs. Unfortunately, until just a few days ago that process didn't include the cover. Instead, covers were inserted manually using Adobe Acrobat.

While that manual process worked, [it came with predictable consequences](https://github.com/roygreenfeld/django-crash-course/issues/132).

## Merging the PDFs

This part was easy and found in any number of blog articles and Stack Overflow answers.

- Step 1: Install [pypdf2](https://pypi.org/project/PyPDF2/)
- Step 2: Write a script as seen below

```python
from PyPDF2 import PdfFileMerger

now = datetime.now()

pdfs = [
  'images/Django_Crash_Course_5.5x8in.pdf',
  '_output/dcc.pdf',
]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("releases/beta-20200226.pdf")
merger.close()
```

It was at this point that we discovered that our new file, `releases/beta-20200226.pdf`, was missing most of the metadata. Oh no!

## Adding the Metadata

According to the PyPDF2 docs, [adding metadata is very straight-forward](https://pythonhosted.org/PyPDF2/PdfFileMerger.html#PyPDF2.PdfFileMerger.addMetadata). Just pass a `dict` into the `addMetadata()` function. I inserted this code right before the call to `merger.write()`:

```python
merger.addMetadata({
    "Title": "Django Crash Course",
    "Authors": 'Daniel Roy Greenfeld, Audrey Roy Greenfeld',
    "Description": "Covers Python 3.8 and Django 3.x",
    "ContentCreator": "Two Scoops Press",
    "CreateDate": "2020-02-26",
    "ModifyDate": "2020-02-26",
})
```

The PDF built! Yeah! Time to open it up and see the results!

Alas, no metadata showed up.

Then I spent a long time with trial-and-error trying to get the metadata to show up properly. While there are lots of Python-related articles on **extracting** metadata using PyPDF2, I struggled to find anything that explained how to add metadata.

## Doing My Homework

After a bunch of research (googling, stack overlow-ing, and visiting forums) I found a wonderful book on O'Reilly called [PDF Explained](https://www.oreilly.com/library/view/pdf-explained/9781449321581/) by John Whitington. Much credit to John Whitington, he's a good writer and very knowledgable on the topic of PDF.

For my purposes, the two critical sections were found in Chapter 4 of PDF Explained:

- [oreilly.com/library/view/pdf-explained/9781449321581/ch04.html#didentries](https://www.oreilly.com/library/view/pdf-explained/9781449321581/ch04.html#didentries)
- [oreilly.com/library/view/pdf-explained/9781449321581/ch04.html#dates](https://www.oreilly.com/library/view/pdf-explained/9781449321581/ch04.html#dates)

Based off what I read, I established the following rules:

- Every metadata field name had to be prefixed with `/`
- Stick to the metadata names found in chapter 4
- Follow the date format supplied in chapter 4

## Writing the Code!

Now armed with my rules I returned to the code. This is what I came up with:

```python
from datetime import datetime
from PyPDF2 import PdfFileMerger

pdfs = [
  'images/Django_Crash_Course_5.5x8in.pdf',
  '_output/dcc.pdf',
]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

# Make PDF datestamp
now = datetime.now()
pdf_datestamp = now.strftime("D:%Y%m%d%H%M%S-8'00'")

# https://www.oreilly.com/library/view/pdf-explained/9781449321581/ch04.html#didentries
# Fields are **precisely** named
merger.addMetadata({
    "/Author": 'Daniel Roy Greenfeld, Audrey Roy Greenfeld',
    "/Title": "Django Crash Course",
    "/Subject": "Covers Python 3.8 and Django 3.x",
    "/Creator": "Two Scoops Press",
    "/CreationDate": pdf_datestamp,
    "/ModDate": pdf_datestamp,
})

# Write the release
version = f"beta-{now.strftime('%Y%m%d')}"
merger.write(f"releases/{version}.pdf")
merger.close()
```

## Conclusion

The lesson I learned writing this little utility is that as useful as Google and Stack Overflow might be, sometimes you need to explore reference manuals. Which, if you ask me, is a lot of fun. :-)

Speaking of reference manuals, while I referenced the online version of [PDF Explained](https://www.amazon.com/dp/B006H4DAE6/?tag=mlinar-20) to get my work done, I've ordered a kindle version of the book. It's the least I can do.
