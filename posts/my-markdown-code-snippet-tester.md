---
date: "2019-10-15"
description: Ensuring that code in my articles actually works.
published: true
slug: my-markdown-code-snippet-tester
tags:
  - python
  - blog
time_to_read: 5
title: My Markdown Code Snippet Tester
---

I've always wanted to run tests on my code snippets in markdown files. Here's how I implemented it on a lazy sunday.

# A Little Bit of History

If you look back at some of the older articles on my blog you'll see I used [pytest](https://pytest.org) assertions to verify that code I wrote actually worked if you tried it out. Some examples:

- [cached-property: Don't copy/paste code](/cached-property.html)
- [Docstrings and Various Python Objects](/docstrings-and-various-python-objects.html)

I had a little Python script that would recursively search my blog for `ReStructuredText`, slurp out the Python blocks, write those to file, then run pytest against the generated files. This meant that while my blog might have grammar or spelling errors, the code was bug-free. Having moved to `Markdown`, this script is no longer valid.

# Requirements

With the advent of my new blog I decided to rewrite the testrunner script with these features:

- Works with individual Markdown files. For debugging of blog entries this is faster and easier.
- Rely on simple Python `assert` statements. Nothing against pytest, but if I'm testing individual files, it's overkill.

# How It Works

Let's say I have a code snippet with two asserts spread out over two code blocks:

```python
def times_5(x):
    return x * 5

assert times_5(3) == 15
```

```python
assert times_5(4) == 20
```

When I run it, the script slurps these code blocks up and combines them into a single Python file called `testfile.py`. It looks something like this:

```python
def times_5(x):
    return x * 5

assert times_5(3) == 15
assert times_5(4) == 20
```

Once saved as `testfile.py`, then `subprocess.Popen()` runs the code and captures the results. Any errors are reported to the user. If you change it to `assert times_5(4) == 200`, it's going to throw an `AssertionError` because 5 times 4 isn't 200.

# The Code

You'll notice that there is no highlighting in `md_testrunner.py` below. The reason is that if I did that, it breaks the testing process.

```
"""
Name: md_testrunner.py
Usage: python md_test_runner.py blogpost.md
Tested on: Python 3.7 and 3.8
"""
from sys import argv
import re
import subprocess

open_pattern = re.compile("\s*`{3}\s*python")
close_pattern = re.compile("\s*`{3}")
test_filename = "testfile.py"


def main(filename):
    # Create an array of the Python code called "code"
    code = []
    in_python = False
    with open(filename) as f:
        for line in f.readlines():
            if re.match(open_pattern, line) is not None:
                in_python = True
                continue
            if in_python == True and re.match(close_pattern, line):
                in_python = False
            if in_python == True:
                code.append(line)

    # Save the code as a string to the testfile
    # `tempfile.NamedTempFile` fails here because the `write()` doesn't seem to occur
    # until the `with` statement is finished. I would love to be wrong in that, using
    # a tempfile is the cleaner approach. Please let me know a better approach.
    with open(test_filename, mode="w") as f:
        f.writelines("".join(code))

    # Run the code
    cmd = ["python", test_filename]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()

    # Display the results
    print("Output: " + output.decode("ascii"))
    print("Error: " + error.decode("ascii"))
    print("Code: " + str(proc.returncode))

    # Cleanup
    os.remove(test_filename)


if __name__ == "__main__":
    main(argv[1])
```

# Next Steps

While this meets my requirements, there is lots of room for improvements. If you're so inclined, here are some ideas to explore:

- Make it more fault tolerant. For example, `sys.argv[1]` is fragile for gathering CLI arguments.
- Package it up so others can use it.
- Add capability to run against multiple files.
- Figure out how to make it not break the testing process if code highlighting is turned on itself.
- Include capability to test other languages.
