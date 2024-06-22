---
blogbook: 'True'
date: 2013-4-15
published: true
slug: generating-ncx-files-with-python
tags:
- python
- twoscoops
- book
- django
- howto
time_to_read: 2
title: Generating NCX files with Python
---

With the help of fellow Python developer Matt Harrison's excellent
[Ebook Formatting: KF8, Mobi &
EPUB](https://www.amazon.com/Ebook-Formatting-Mobi-EPUB-ebook/dp/B00BWQXHU6/ref=la_B0077BQLH6_1_2?ie=UTF8&qid=1366041987&sr=1-2&tag=ihpydanny-20),
we managed to create pretty decent looking Kindle and ePub versions of
[Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x).

One of many things we did was focus on providing an excellent table of
contents. Of course we provided one inside the content of the book, but
much like the PDF version we also provided one that various ebook
readers can display in sidebars or drop down menus. Unfortunately,
building this navigation isn't well documented (except for Matt's
book), and I've yet to see any good ways to generate it via code.

Which is why I present the following code. It looks at the HTML that
KindleGen and ePub generators demand and pulls from it a chapter-based
table of contents. Then constructs a .ncx file, which is what ebook
readers use to generate the sidebar/dropdown table of contents.

Our requirements:

    Jinja2
    Django
    BeautifulSoup4

And now the code:

``` python
#!/usr/bin/python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from django.utils.text import slugify
from jinja2 import Template

TEMPLATE = Template("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "https://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="https://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">
<head>

<!-- The content of dtb:uid must be exactly the same as the uuid specified in the OPF file. -->

<meta name="dtb:uid" content="urn:uuid:BLAH-BLAH-BLAH"/>
<meta name="dtb:depth" content="1"/>
<meta name="dtb:totalPageCount" content="0"/>
<meta name="dtb:maxPageNumber" content="0"/>
</head>

<docTitle><text>Two Scoops of Django: Best Practices for Django 1.5</text></docTitle>
<docAuthor><text>Greenfeld, Daniel</text></docAuthor>
<docAuthor><text>Roy, Audrey</text></docAuthor>
<navMap>
</navPoint>
{% for chapter in chapters %}
<navPoint id="{{ chapter.slug }}" playOrder="{{ loop.index }}">
<navLabel><text>{{ chapter.string.strip() }}</text></navLabel>
<content src="{{ chapter.href }}" />
</navPoint>
{% endfor %}
</navMap>
</ncx>
""")


def main(filename):

    # Grab the base file for review
    with open(filename) as f:
        text = f.read()

    # load the text into a bs4 object
    soup = BeautifulSoup(text)

    # grab the nav element
    nav = soup.find("nav")

    # loop through the TOC for chapters. 
    # Sections/Subsections can't be displayed, so don't worry about them
    # li.chapter is how we constructed our TOC. Your mileage may vary.
    chapters = []
    for li in nav.find_all("li", "chapter"):
        chapters.append(dict(
            href=li.a['href'],
            string=li.a.text,
            slug=slugify(li.a.string)
        ))

    # Render the template
    template = TEMPLATE.render(chapters=chapters)

    # convert to ASCII
    template = template.encode("ascii", "xmlcharrefreplace")

    # Save to the toc.ncx
    with open("toc.ncx", "w") as f:
        f.write(template)


if __name__ == '__main__':
    main('book.html')
```

There is more to adding a table of contents then just this simple
module. You also have to construct the .opf file, which is another
undocumented mess that I'll blog about.
