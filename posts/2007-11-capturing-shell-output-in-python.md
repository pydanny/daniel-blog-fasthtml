---
date: "2007-11-29T08:58:00.000-08:00"
description: ""
published: true
slug: 2007-11-capturing-shell-output-in-python
tags:
  - python
  - howto
  - legacy-blogger
time_to_read: 5
title: Capturing shell output in Python
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2007/11/capturing-shell-output-in-python.html)_.

I need to capture the terminal text returned after I run some shell commands to create SVN repos. Unfortunately, os.system() doesn't capture the text, just the numeric value. Fortunately, Python has the subprocess library. So now I can do this:

```python
>>> import subprocess as  sub
>>> process = sub.Popen(["ls", "-l"], stdout=sub.PIPE, stderr=sub.PIPE)
>>> output, errors = process.communicate()
>>> [x for x in output.decode().split('\n')]
[
    'total 80',
    '-rw-r--r--   1 drg  staff   511 May 10 08:59 Dockerfile',
    '-rw-r--r--   1 drg  staff   741 May 10 08:59 PULL_REQUEST_TEMPLATE.md',
    '-rw-r--r--   1 drg  staff  2724 May 10 08:59 README.md',
    'drwxr-xr-x   6 drg  staff   192 May 10 09:06 __pycache__',
    '-rw-r--r--   1 drg  staff    38 May 10 08:59 bandit.yml',
    'drwxr-xr-x  11 drg  staff   352 May 10 09:03 checks',
    'drwxr-xr-x   7 drg  staff   224 May 10 08:59 denied',
    '-rw-r--r--   1 drg  staff  1725 May 10 08:59 main.py',
    '-rw-r--r--   1 drg  staff   653 May 10 08:59 models.py',
    '-rw-r--r--   1 drg  staff    31 May 10 08:59 mypy.ini',
    '-rw-r--r--   1 drg  staff   337 May 10 08:59 requirements.txt',
    'drwxr-xr-x   3 drg  staff    96 May 10 08:59 scripts',
    '-rw-r--r--   1 drg  staff  1430 May 10 08:59 test_api.py',
    '-rw-r--r--   1 drg  staff  3736 May 10 09:12 test_checks.py',
    ''
]
```

Note: Updated for modern Python on May 25, 2022

---

## 1 comments captured from [original post](https://pydanny.blogspot.com/2007/11/capturing-shell-output-in-python.html) on Blogger

**Unknown said on 2010-12-28**

Thanks! I was using subprocess before but this looks pretty much suitable for short shell commands.
