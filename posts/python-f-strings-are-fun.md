---
date: '2017-04-27'
published: true
slug: python-f-strings-are-fun
tags:
- twoscoops
- python
- django
- python
- python3
time_to_read: 3
title: Python F-Strings Are Fun!
---

[![Python F-Strings Are Fun!](/images/python-tip-from-pydanny.png)](/python-f-strings-are-fun.html)

In python 3.6 we saw the adoption of [Literal String
Interpolation](https://www.python.org/dev/peps/pep-0498/), or as they
are known more commonly,
[f-strings](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings).
At first I was hesitant because\... well\... we've got multiple string
tools already available:

``` python
one, two = 1, 2
_format = '{},{}'.format(one, two)
_percent = '%s,%s' % (one, two)
_concatenation = str(one) + ',' + str(two)
_join = ','.join((str(one),str(two)))
assert _format == _percent == _concatenation == _join
```

Adding f-strings to this mix didn't seem all that useful:

``` python
_fstring = f'{one},{two}'
assert _fstring == _format == _percent == _concatenation == _join
```

I was doubtful, but then I tried out f-strings on a non-trivial example.
Now I'm hooked. Be it on local utility scripts or production code, I
now instinctively gravitate toward their usage. In fact, f-strings are
so useful that going back to earlier versions of Python now feels
cumbersome.

The reason why I feel this way is that f-strings are concise but easy to
understand. Thanks to intuitive expression evaluation I can compress
more verbose commands into smaller lines of code that are more legible.
Take a look:

``` python
_fstring = f'Total: {one + two}'  # Go f-string!
_format = 'Total: {}'.format(one + two)
_percent = 'Total: %s' % (one + two)
_concatenation = 'Total: ' + str(one + two)
assert _fstring == _format == _percent == _concatenation
```

The f-string example is four characters shorter than the closest
alternative and is extremely easy to read. Indeed, put the f-string
example in front of a non-programmer and they'll understand it fast.
The same won't apply to the alternatives, odds are they'll ask what
`.format()`, `str()`, and the `%` mean.

F-Strings Are Addictive
=======================

The conciseness and power of the intuitive expression evaluation can't
be understated. On the surface f-strings seem like a small step forward
for Python, but once I started using them I realized they were a huge
step in codability for the language.

Now I'm hooked. I'm addicted to f-strings. When I step back to Python
3.5 or lower I feel like less of a Python coder. Yes, I have a problem
with how much I lean on f-strings now, but I acknowledge my problem. I
would go to therapy for it, but I believe I can manage the addiction for
now.

Okay, enough joking, f-strings are awesome. Try them out.

A Utility Script Example
========================

We just released [Two Scoops of Django
1.11](https://www.roygreenfeld.com/products/two-scoops-of-django-1-11),
which is written in [LaTeX](https://en.wikipedia.org/wiki/LaTeX). Like
most programming books we provide [code examples in a
repo](https://github.com/twoscoops/two-scoops-of-django-1.11/tree/master/code)
for our readers. However, as we completey revised the code-highlighting,
we had to rewrite our code extractor from the ground up. In a flurry of
cowboy coding, I did so in thirty minutes using Python 3.6 while leaning
on f-strings:

``` python
"""Two Scoops of Django 1.11 Code Extractor"""
import os
import shutil
from glob import glob

try:
    shutil.rmtree('code')
    print('Removed old code directory')
except FileNotFoundError:
    pass
os.mkdir('code')
print('Created new code directory')

STAR = '*'

LEGALESE = """LEGAL TEXT GOES HERE"""

LANGUAGE_START = {
    '\\begin{python}': '.py',
    '\\begin{badpython}': '.py',
    '\\begin{django}': '.html',
    '\\begin{baddjango}': '.html',
    '\\begin{plaintext}': '.txt',
    '\\begin{badplaintext}': '.txt',
    '\\begin{sql}': '.sql',
    '\\begin{makefile}': '',
    '\\begin{json}': '.json',
    '\\begin{bash}': '.txt',
    '\\begin{xml}': '.html',
}

LANGUAGE_END = {x.replace('begin', 'end'):y for x,y in LANGUAGE_START.items()}


def is_example(line, SWITCH):
    for key in SWITCH:
        if line.strip().startswith(key):
            return SWITCH[key]
    return None

def makefilename(chapter_num, in_example):
    return f'code/chapter_{chapter_num}_example_{str(example_num).zfill(2)}{in_example}'


if __name__ == '__main__':

    in_example = False
    starting = False
    for path in glob('chapters/*.tex'):
        try:
            chapter_num = int(path[9:11])
            chapter_num = path[9:11]
        except ValueError:
            if not path.lower().startswith('appendix'):
                print(f'{STAR*40}\n{path}\n{STAR*40}')
            continue
        example_num = 1
        with open(path) as f:
            lines = (x for x in f.readlines())
        for line in lines:
            if starting:
                # Crazy long string interpolation that should probably
                # be broken up but remains because it's easy for me to read
                filename =  f'code/chapter_{chapter_num}_example_{str(example_num).zfill(2)}{in_example}'
                dafile = open(filename, 'w')
                if in_example in ('.py', '.html'):
                    dafile.write(f'"""\n{LEGALESE}"""\n\n')
                else:
                    dafile.write(f'{LEGALESE}\n{STAR*20}\n\n')
                print(filename)
            if not in_example:
                mime = None
                in_example = is_example(line, LANGUAGE_START)
                if in_example:
                    starting = True
                continue
            mime = is_example(line, LANGUAGE_END)
            starting = False
            if mime:
                print(mime)
                in_example = False
                example_num += 1
                dafile.close()
            else:
                dafile.write(line)
```
