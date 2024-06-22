---
date: "2022-03-11T22:20:50.52Z"
published: true
tags:
  - python
  - conda
  - MacOS
  - Windows
  - Linux
time_to_read: 2
title: Pip Installing Dependencies Into Conda Envs
description: People think Conda is challenging to use or doesn't work with pip, when in truth it is easy and just works everywhere.
image: /images/python-conda.png
---

I prefer to use Conda because [once installed](https://docs.conda.io/en/latest/miniconda.html) it works essentially the same everywhere. Including Windows.

## Step 1: Create a Virtual Environment

```bash
conda create -n credible python=3.10
```

After agreeing to install some dependencies, it places them in an out-of-the way location. Here's where they are on my work, personal laptops, and a 2018-era Windows laptop I sometimes test on:

- `/Users/drg/opt/miniconda3/envs/`
- `/Users/danny/opt/miniconda3/envs/`
- `c:\Users\danielandaudrey\.conda\envs`

Get the list of current envs:

```bash
$ conda env list
base                  *  /Users/drg/opt/miniconda3
credible                 /Users/drg/opt/miniconda3/envs/credible
system                   /Users/drg/opt/miniconda3/envs/system
that                     /Users/drg/opt/miniconda3/envs/that
just                     /Users/drg/opt/miniconda3/envs/just
works                    /Users/drg/opt/miniconda3/envs/works
everywhere               /Users/drg/opt/miniconda3/envs/everywhere
```

## Step 2: Activate a Virtual Environment

```bash
conda activate credible
```

This prefixes the CLI shell with `(credible)`, exactly like `venv` or `virtualenv`.

```bash
(credible)
```

## Step 3: Install Dependencies Using Pip Into a Conda Env

Just like many any other virtual environments for Python, use pip to install/uninstall dependencies

```bash
(credible) python -m pip install typer
```

That's right. I'm using pip to manage packages in a conda env. Conda works great with pip. Conda has worked great with pip for years.

---

## Questions

Because I know you have them.

### 1. What about conda install for dependencies?

I rarely use `conda install` on MacOS or Linux. On Windows, `conda install` is sometimes useful because it handles non-python binaries that otherwise require Docker, [Chocolately](https://chocolatey.org/), or other tools.

### 2. Why not pyenv-win instead of conda?

Reasons:

1. I always struggled to get pyenv-win to work on Windows
2. Didn't handle non-python binaries well, requiring use of Chocalatey
3. Conda just works

### 3. Did you ever teach classes with Conda?

Yes. Conda was awesome when I used to teach. Conda is a universal installation system that works for everyone regardless of operating system. Once people got it installed we got to teaching instead of dealing with setup issues.

### 4. What about Docker instead of Conda?

My classes focused more on teaching Python and Django rather than Docker. Docker is a whole different world.

### 5. What does Audrey use?

[Audrey](https://audrey.feldroy.com) uses pyenv and loves it. Taught people to use pyenv and pyenv-win.

---

Updates:

- 2022-03-12 [Suggested by David R. Pugh](https://twitter.com/TheSandyCoder/status/1502577229607415808): Changed to use `python -m pip` to ensure the dependency is installed on the right place.

![Source: https://rna.colostate.edu/2020/lib/exe/detail.php?id=wiki%3Asoftwareinstall&media=wiki:python-conda.png](/images/python-conda.png)
_[Source of Image](https://rna.colostate.edu/2020/lib/exe/detail.php?id=wiki%3Asoftwareinstall&media=wiki:python-conda.png)_
