---
date: '2015-02-22'
published: true
slug: setting-up-latex-on-mac-os-x
tags:
- book
- LaTeX
- howto
- python
time_to_read: 1
title: Setting up LaTeX on Mac OS X
---

These are my notes for getting LaTeX running on Mac OS X with the
components and fonts I want. Which is handy when you want to generate
PDFs from [Sphinx](https://sphinx-doc.org/). At some point I want to
replace this with a [Docker](https://www.docker.com/) container similar
<https://github.com/blang/latex-docker>, albeit with the components in
parts 3 and 4 below.

1.  Get mactex-basic.pkg from <https://www.ctan.org/pkg/mactex-basic>
2.  Click mactex-basic.pkg to install LaTeX.
3.  Update `tlmgr`:

        sudo tlmgr update --self

4.  Install the following tools via `tlmgr`:

        sudo tlmgr install titlesec
        sudo tlmgr install framed
        sudo tlmgr install threeparttable
        sudo tlmgr install wrapfig
        sudo tlmgr install multirow
        sudo tlmgr install enumitem
        sudo tlmgr install bbding
        sudo tlmgr install titling
        sudo tlmgr install tabu
        sudo tlmgr install mdframed
        sudo tlmgr install tcolorbox
        sudo tlmgr install textpos
        sudo tlmgr install import
        sudo tlmgr install varwidth
        sudo tlmgr install needspace
        sudo tlmgr install tocloft
        sudo tlmgr install ntheorem
        sudo tlmgr install environ
        sudo tlmgr install trimspaces

5.  Install fonts via `tlmgr`:

        sudo tlmgr install collection-fontsrecommended

**note:** Yes, I know I can install the basic LaTeX package using
[Homebrew](https://brew.sh/), but sometimes I like doing things manually.

[![image](https://upload.wikimedia.org/wikipedia/commons/9/9c/Latex_example.png)](https://en.wikipedia.org/wiki/LaTeX#mediaviewer/File:Latex_example.png)
