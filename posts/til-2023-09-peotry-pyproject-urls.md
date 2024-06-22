---
date: "2023-09-07T15:45:00.00Z"
published: true
slug: til-2023-09-poetry-pypi-project-urls
tags:
  - python
  - packaging
  - TIL
time_to_read: 1
title: "TIL: Poetry PyPI Project URLS"
description: Adding sidebar links to PyPI projects powered by Poetry
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

Poetry has its own location for `urls` in the [tool.poetry.urls] table. Per the [Poetry documentation on urls](https://python-poetry.org/docs/pyproject/#urls):

> "In addition to the basic urls (homepage, repository and documentation), you can specify any custom url in the urls section."

```toml
[tool.poetry.urls]

changelog = "https://github.com/myghname/projectname/releases"
documentation = "https://myghname.github.io/dataclasses-json/"
issues = "https://github.com/myghname/projectname/issues"
````
