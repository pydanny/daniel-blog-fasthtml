---
date: '2025-07-20T10:08:49.687342'
description: Using uv run with make to replace tox or nox for testing multiple versions of Python
  locally.
published: true
tags: 
- python
- testing
title: uv run for running tests on versions of Python
---

The [uv](https://pypi.org/project/uv/) library is not just useful for dependency management, it also comes with a `run` subcommand that doesn't just run Python scripts, it allows for specific Python versions and setting of dependencies within that run. Between runs it caches everything so it runs fast.

For example, if I have a FastAPI project I could run tests on it using this command:

```sh
uv run --with pytest --with httpx pytest
```

But what if I want to test a particular version of Python? Then I simple specify the version of Python to run the test:

```sh
uv run --python=3.13 --with pytest --with httpx pytest
```

Here's where it gets fun. I can use a `Makefile` (or a [justfile](https://github.com/casey/just)) to test on multiple Python versions.

```Makefile
testall:  ## Run all the tests for all the supported Python versions
	uv run --python=3.10 --with pytest --with httpx pytest
	uv run --python=3.11 --with pytest --with httpx pytest
	uv run --python=3.12 --with pytest --with httpx pytest
	uv run --python=3.13 --with pytest --with httpx pytest
```

If you want to use `pyproject.toml` dependency groups, switch from the `--with` flag to the `-extra` flag. For example, if your testing dependencies are in a `test` group:

```toml
[project.optional-dependencies]
test = [
    # For the test client
    "httpx>=0.28.1",   
    # Test runner
    "pytest>=8.4.0",
]
```

You could then run tests across multiple versions of Python thus:

```python
testall:  ## Run all the tests for all the supported Python versions
	uv run --python=3.10 --extra test pytest
	uv run --python=3.11 --extra test pytest
	uv run --python=3.12 --extra test pytest
	uv run --python=3.13 --extra test pytest
```

And there you have it, a simple replacement for Nox or Tox. Of course those tools have lots more features that some users may care about. However, for my needs this works great and eliminates a dependency+configuration from a number of my projects.

---

Thanks to Audrey Roy Greenfeld for pairing with me on getting this to work.