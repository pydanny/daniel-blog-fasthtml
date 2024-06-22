---
date: "2023-10-11T15:45:00.00Z"
published: true
slug: til-2023-10-capture-stdout-stderr-with-pytest
tags:
  - python
  - TIL
time_to_read: 2
title: "TIL: Capture stdout & stderr with pytest"
description: How to capture printed text using pytest, something I wish I knew sooner.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

I wish I knew this earlier, but I know it now thanks to [Cody Antunez](https://www.codyantunez.com/). Here it is:


```python
import sys

def test_myoutput(capsys):  # or use "capfd" for fd-level

    # Write some text
    print("hello")
    sys.stderr.write("world\n")

    # Capture the text
    captured = capsys.readouterr()

    # Test the captured output, both std and err
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
```

In the [pytest docs](https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function) it describes the fixtures to capture binary and more.