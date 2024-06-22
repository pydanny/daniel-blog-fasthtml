---
date: '2017-05-15'
published: true
slug: using-python-and-google-docs-to-build-books
tags:
- python
- django
- python
- python3
- cookiecutter
time_to_read: 7
title: Using Python and Google Docs to Build Books
description: Using Python to combine multiple Google docs into one cohesive whole that can be published as a book.
image: /images/python-tip-from-pydanny.png
---


[![Python tips and tricks](/images/python-tip-from-pydanny.png)](/using-google-docs-and-python-to-assemble-fiction-books.html)

When I started my latest fiction book, [The Darkest
Autumn](https://www.roygreenfeld.com/products/darkest-autumn-ambria-book-1), I
wrote out the chapters as individual files. I did it in a text editor
(Sublime) and saved the files to a git repo. The names of the files
determined their order, chapters being named in this pattern:

    the-darkest-autumn $ tree
    .
    ├── 01_Beginnings.md
    ├── 02_Town_of_Ravenna.md
    ├── 03_Walls_of_Ravenna.md

As the book developed I thought about moving it to
[Scrivener](https://www.literatureandlatte.com/scrivener.php). If you
don't know, Scrivener is an excellent tool for writing. It encourages
you to break up your work into chapters and scenes. The downside is that
Scrivener is complex (I want to write, not figure out software) and
[Scrivener isn't designed for simultaneous
collaboration](https://www.literatureandlatte.com/forum/viewtopic.php?f=2&t=11725).
The latter issue is a very serious problem, as I like to have others
review and comment on my writing as I go.

What I really wanted to do is combine the chapter breaking of Scrivener
with the simplicity and collaboration of Google Docs. Preferably, I
would put the book chapters into Google Docs as individual files and
then send invites to my editor, wife, and my beta readers. By using
Google Docs I could ensure anyone could access the work without having
to create a new account and learn an unfamiliar system.

Unfortunately, at this time Google Docs has no way to combine multiple
Google Docs contained in one directory into one large document for
publication. To use Google Docs thhe way I want involves manually
copy/pasting content from dozens of files into one master document any
time you want to update a work. With even 5 to 10 documents this is time
consuming and error prone (for me) to the point of being unusable. This
is a problem because my fiction books have anywhere from 30 to 50
chapters.

Fortunately for me, I know how to code. By using the Python programming
language, I can automate the process of combining the Google Docs into
one master file which can be converted to epub, mobi (kindle), or PDF.

# How I Combine Google Doc Files

First, I download all the files in the book's Google Docs directory.

![Selecting Files With Google Docs](/images/selecting-files.png?12346)

This generates and downloads a zip file called something like
drive-download-20170505T230011Z-001.zip. I use `unzip to open it`:

    unzip drive-download-20170505T230011Z-001.zip -d the-darkest-autumn

Inside the new the-darkest-autumn folder are a bunch of MS
Word-formatted files named identically to what's stored on Google Docs:

    $ tree the-darkest-autumn/
    the-darkest-autumn
    ├── 01. Beginnings.docx
    ├── 02. Town of Ravenna.docx
    ├── 03. Walls of Ravenna.docx
    ├── 04. Gatehouse of Ravenna.docx
    ├── 05. Courage.docx
    ├── 06. To the Upper Valley.docx
    ├── _afterward.docx
    ├── _copyright.docx
    ├── _dedication.docx
    └── _title.docx

Now it's time to bring in the code. By leveraging the
[python-docx](https://python-docx.readthedocs.io/en/latest/index.html) library,
I combine all the Word files into one large Word files using this Python
(3.6 or higher) script:

```python
"""bookify.py: Combines multiple Word docs in a folder.

"""

import os
import sys
from glob import glob

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.text import WD_COLOR_INDEX
    from docx.shared import Inches, Pt
except ImportError:
    raise ImportError("You need to 'pip install python-docx'")

TEXT_FONT = "Trebuchet MS"


def add_matter(master_document, filename, chapter, after=False):
    """Builds """
    if not os.path.exists(filename):
        return master_document

    if after:
        master_document.add_page_break()

    # Build the heading
    heading = master_document.add_heading('', level=1)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    runt = heading.add_run(chapter)
    runt.font.color.theme_color = WD_COLOR_INDEX.WHITE

    # Add the material
    document = Document(docx=filename)
    for index, paragraph in enumerate(document.paragraphs):
        new_paragraph = master_document.add_paragraph()
        new_paragraph.paragraph_format.alignment = paragraph.paragraph_format.alignment
        new_paragraph.style = paragraph.style
        # Loop through the runs of a paragraph
        # A run is a style element within a paragraph (i.e. bold)
        for j, run in enumerate(paragraph.runs):
            # Copy over the old style
            text = run.text
            # Add run to new paragraph
            new_run = new_paragraph.add_run(text=text)
            # Update styles for run
            new_run.bold = run.bold
            new_run.italic = run.italic
            new_run.font.size = run.font.size
            new_run.font.color.theme_color = WD_COLOR_INDEX.BLACK
    master_document.add_page_break()
    print(f'Adding {chapter}')
    return master_document


def add_chapter(master_document, filename, chapter):
    """Build chapters, i.e. where the story happens."""
    # Build the chapter
    document = Document(docx=filename)

    # Build the heading
    heading = master_document.add_heading('', level=1)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

    heading.add_run(chapter).font.color.theme_color = WD_COLOR_INDEX.BLACK
    heading.paragraph_format.space_after = Pt(12)

    for index, paragraph in enumerate(document.paragraphs):
        new_paragraph = master_document.add_paragraph()
        # Loop through the runs of a paragraph
        # A run is a style element within a paragraph (i.e. bold)
        for j, run in enumerate(paragraph.runs):

            text = run.text
            # If at start of paragraph and no tab, add one
            if j == 0 and not text.startswith('\t'):
                text = f"\t{text}"
            # Add run to new paragraph
            new_run = new_paragraph.add_run(text=text)
            # Update styles for run
            new_run.font.name = TEXT_FONT
            new_run.bold = run.bold
            new_run.italic = run.italic

        # Last minute format checking
        text = new_paragraph.text

    master_document.add_page_break()
    # Destroy the document object
    del document
    return master_document


def main(book):
    master_document = Document()

    master_document = add_matter(
      master_document,
      filename=f'{book}/_title.docx',
      chapter='Title Page'
    )
    master_document = add_matter(
        master_document,
        filename=f'{book}/_copyright.docx',
        chapter='Copyright Page'
    )
    master_document = add_matter(
        master_document,
        filename=f'{book}/_dedication.docx',
        chapter='Dedication'
    )

    for filename in glob(f"{book}/*"):
        if filename.startswith(f"{book}/_"):
            print(f'skipping {filename}')
            continue

        # Get the chapter name
        book, short = filename.split('/')
        chapter = short.replace('.docx', '')
        if chapter.startswith('0'):
            chapter = chapter[1:]
        print(f'Adding {chapter}')
        master_document = add_chapter(master_document, filename, chapter)

    master_document = add_matter(
        master_document,
        filename=f'{book}/_aboutauthor.docx',
        chapter='About the Author',
        after=True
    )
    master_document = add_matter(
        master_document,
        filename=f'{book}/_afterward.docx',
        chapter='Afterward',
        after=True
    )
    master_document.save(f'{book}.docx')
    print('DONE!!!')

if __name__ == '__main__':
    try:
        book = sys.argv[1]
    except IndexError:
        msg = 'You need to specify a book. A book is a directory of word files.'
        raise Exception(msg)

    main(book)
```

This is what it looks like when I run the code:

    $ python bookify.py the-darkest-autumn/
    Adding Title Page
    Adding Copyright Page
    Adding Dedication
    Adding 1. Beginnings
    Adding 2. Town of Ravenna
    Adding 3. Walls of Ravenna
    Adding 4. Gatehouse of Ravenna
    Adding 5. Courage
    Adding 6. To the Upper Valley
    skipping the-darkest-autumn/_afterward.docx
    skipping the-darkest-autumn/_copyright.docx
    skipping the-darkest-autumn/_dedication.docx
    skipping the-darkest-autumn/_title.docx
    Adding Afterward
    DONE!!!

And now I've got a Word document in the same directory called
the-darkest-autumn.docx.

# Converting Word to EPUB

While Kindle Direct Publishing (KDP) will accept .docx files, I like to
convert it to .epub using [Calibre](https://calibre-ebook.com/):

    $ ebook-convert the-darkest-autumn.docx the-darkest-autumn.epub \
    --authors "Daniel Roy Greenfeld" \
    --publisher "Two Scoops Press" \
    --series Ambria \
    --series-index 1 \
    --output-profile kindle

And now I can check out my results by using Calibre's book viewer:

    $ ebook-viewer the-darkest-autumn.epub

# Add the Links!

As `python-docx` doesn't handle HTTP links at this time, I manually add
them to the book using Calibre's epub editor. I add links to:

- My personal author site at
  [danielroygreenfeld.com](https://www.danielroygreenfeld.com/)
- The book's [review page on
  Amazon](https://www.amazon.com/the-darkest-autumn-ebook/product-reviews/B071L2G8SL?tag=mlinar-20)
- The book's upcoming sequel, [The River Runs
  Uphill](https://www.danielroygreenfeld.com/books/the-river-runs-uphill/).

# How Well Does It Work?

For me it works wonders for my productivity. By following a "chapters
as files" pattern within Google Docs I get solid collaboration power
plus some (but not all) of the features of Scrivener. I can quickly
regenerate the book at any time without having to struggle with
Scrivener or have to add tools like Vellum to the process.

I have a secondary script that fixes quoting and tab issues, written
before I realized Calibre could have done that for me.

The book I started this project for, [The Darkest
Autumn](https://www.danielroygreenfeld.com/books/the-darkest-autumn/),
is available now on
[Amazon](https://www.amazon.com/Darkest-Autumn-Ambria-I-ebook/dp/B071L2G8SL/?tag=mlinar-20).
Check it out and let me know what you think of what the script
generates. Or if you want to support my writing (both fiction and
non-fiction), [buy The Darkest Autumn on
Amazon](https://www.amazon.com/Darkest-Autumn-Ambria-I-ebook/dp/B071L2G8SL/?tag=mlinar-20)
and leave an honest review.

# Thinking About the Future

Right now this snippet of code generates something that looks okay, but
could be improved. I plan to enhance it with better fonts and chapter
headers, the goal to generate something as nice as what
[Draft2Digital](https://draft2digital.com/) generates.

I've considered adding the OAuth components necessary in order to allow
for automated downloading. The problem is I loathe working with OAuth.
Therefore I'm sticking with the manial download process.

For about a week I thought about leveraging it and my
[Django](https://www.djangoproject.com/) skills to build it as a paid
subscription service and rake in the passive income. Basically turn it
into a startup. After some reflection I backed off because if Google
added file combination as a feature, it would destroy the business
overnight.

I've also decided not to package this up on Github/PyPI. While
[Cookiecutter](https://github.com/audreyr/cookiecutter) makes it trivial
for me to do this kind of thing, I'm not interested in maintaining yet
another open source project. However, if someone does package it up and
credits me for my work, I'm happy to link to it from this blog post.

