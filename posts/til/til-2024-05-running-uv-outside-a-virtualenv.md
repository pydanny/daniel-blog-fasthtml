---
date: '2024-05-08T15:22:59.338527'
description: Breaking the rules to satisfy continuous integration.
published: true
tags:
- TIL
- python
- howto
title: 'TIL: Running UV outside a virtualenv'
image: /public/logos/til-1.png
twitter_image: /public/logos/til-1.png
---

*Breaking the rules to satisfy continuous integration.*

A few months ago I blogged about forcing [pip to require a virtualenv](/posts/til-2023-12-forcing-pip-to-use-virtualenv). However, when automating tests and deployments sometimes you work outside of virtualenvs. With `pip` this isn't a problem, you just don't set what I did in that article. However, what if you are using the rust-based [uv](https://pypi.org/project/uv/) where the default is to keep you in a virtualenv?

The answer is when you install dependencies using `uv` in this scenario, use the `--python` flag to specify the interpreter. According to the [uv docs](https://github.com/astral-sh/uv?tab=readme-ov-file#installing-into-arbitrary-python-environments), this flag is intended for use in continuous integration (CI) environments or other automated workflows.

So without further ado, this is what I did:

```bash
python -m pip install uv
uv pip install -p 3.12 -r requirements.txt
```

As a bonus, here's the command inside GitHub actions-flavored YAML:

```yaml
    - name: Install Dependencies
      run: |
        python -m pip install uv
        uv pip install -p 3.12 -r requirements.txt
```

Want to know how to handle multiple versions of Python? Here's how use a matrix on GitHub: [https://github.com/pydanny/dj-notebook/blob/main/.github/workflows/python-ci.yml#L18-L19](github.com/pydanny/dj-notebook/blob/main/.github/workflows/python-ci.yml#L18-L19)