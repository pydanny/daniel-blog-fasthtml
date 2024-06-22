---
date: "2015-01-29"
published: true
slug: building-conda-packages-for-multiple-operating-systems
tags:
  - python
  - pypi
  - python3
  - conda
  - cookiecutter
  - packaging
  - howto
time_to_read: 3
title: Building Conda Packages for Multiple Operating Systems
---

On the [Cookiecutter](https://github.com/audreyr/cookiecutter) project,
recently we added [conda](https://conda.pydata.org/) to the open source
packaging systems we officially support (You can find Cookiecutter on
[PyPI](https://pypi.python.org/pypi/cookiecutter),
[homebrew](https://github.com/Homebrew/homebrew/blob/master/Library/Formula/cookiecutter.rb),
and apparently some Linux distros).

# Creating a conda recipe from a PyPI package

Prequisites:

- A [conda binary](https://conda.pydata.org/miniconda.html#miniconda)
  installed.
- A package deployed to
  [PyPI](https://pypi.python.org/pypi/cookiecutter) (in our case,
  <https://pypi.python.org/pypi/cookiecutter/0.9.1>).

Once those are ready, create a conda recipe for Cookiecutter.

```bash
$ conda skeleton pypi cookiecutter
```

This will create a conda recipe, which is a directory named
`cookiecutter` that contains several text files.

Inside the new `cookiecutter` recipe directory, find the `meta.yaml`
file and change the appropriate sections to have this content:

```yaml
source:
    # Change to match the most recent release
    git_tag: 0.9.1
    git_url: https://github.com/audreyr/cookiecutter.git

package:
    name: cookiecutter
    version: {{ environ['GIT_DESCRIBE_TAG'] }}

build:
    number: {{ environ.get('GIT_DESCRIBE_NUMBER', 0) }}

    # Note that this will override the default build string with the Python
    # and NumPy versions
    string: {{ environ.get('GIT_BUILD_STR', '') }}
```

# Building a conda package

Use the conda recipe to build a package for my operating system (in this
case, Mac OS X):

```bash
$ conda build cookiecutter
```

This creates a Cookiecutter conda package at
`~/miniconda/conda-bld/osx-64/cookiecutter-0.9.1_BUILDNUM.tar.bz2`.

**Note:** The official conda recipe for **cookiecutter** is at
<https://github.com/conda/conda-recipes/tree/master/cookiecutter>.

# Converting the conda package to other systems

Let's convert that to Windows and Linux systems:

```bash
$ conda convert ~/miniconda/conda-bld/osx-64/cookiecutter-0.9.1_BUILDNUM.tar.bz2 -p all
```

This creates five new directories, each with a new package. It looks
something like this:

```bash
$ ls
linux-32
linux-64
osx-64
win-32
win-64
```

Each one of these directories contains a conda build also named
`cookiecutter-0.9.1_BUILDNUM.tar.bz2`.

**Note:** I never left the Mac OSX operating system, yet I have packages
that are pretty much garaunteed to work on Windows and Linux. That said,
Cookiecutter is pure python and it's dependencies already have conda
packages. I haven't tried this yet on anything that includes compiling
C or C++, much less Fortran.

# Uploading conda packages to Binstar

With these packages created, it's time to upload them to
[binstar](https://binstar.org), the primary conda package index.

First, [register your binstar
account](https://binstar.org/account/register).

Then use conda to install the binstar client:

```bash
$ conda install binstar
```

Finally, start uploading the new packages:

```bash
$ binstar upload linux-32/cookiecutter-0.9.1-BUILDNUM.tar.bz2
$ binstar upload linux-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2
$ binstar upload osx-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2
$ binstar upload win-32/cookiecutter-0.9.1-BUILDNUM.tar.bz2
$ binstar upload win-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2
```

[Check out the results of my
work](https://binstar.org/pydanny/cookiecutter) or take a look right
below at what's on [Anaconda.org](https://anaconda.org):

[![image](/images/packages.png)](https://anaconda.org/search?q=cookiecutter)

# Try installing Cookiecutter with conda!

If you have **conda** installed, you should be able to get Cookiecutter
thus:

```bash
$ conda config --add channels https://conda.binstar.org/pydanny
$ conda install cookiecutter
```

# Summary

Writing about how to package software is hard, so figuring this out was
a [bit of detective
work](https://github.com/audreyr/cookiecutter/issues/232#issuecomment-71552905).
I think that's going to change, as the company behind conda, [Continuum
Analytics](https://www.continuum.io/) has stated their intentions to
improve conda's documentation. Furthermore, just as many [for-python
cookiecutter templates](https://github.com/audreyr/cookiecutter#python)
include carefully researched `setup.py` modules for use with
`distutils`, in 2015 I think we'll begin to see many of these templates
include carefully research conda recipes and instructions.

Many thanks go to [Fernando Perez](https://twitter.com/fperez_org) for
inspiring me to actually delve into conda. [Travis
Swicegood](https://twitter.com/tswicegood) gave me some useful pointers.
Last, but not least, none of this would have been figured out without
the help of [Wes Turner](https://twitter.com/westurner).

# Updates

- 2015/01/31 - Fixed a broken binstar link thanks to Russ Ferriday.
- 2015/01/30 - Wes Turner corrected a couple typos in the conda
  command statements.
