---
date: "2022-02-14T23:50:50.52Z"
published: true
tags:
  - audrey
  - holidays
  - python
time_to_read: 2
title: More Married
description: In honor of Valentine's Day, this script calculates how long you've been married (or other types of relationships) in relation to how long you've known each other
image: /images/2022-02-14-hearts-a.png
---

Audrey and I met in early 2010 and within days were in love. We were married in late 2013. This program calculates how much more we've been married than not married.

For example:

1. At some point in November of 2017 our time married was equal to the time we had been together
2. In September of 2021 our time married was twice as much as we knew each other
3. In July of 2025 we'll have been married for three times as long as we've known each other

Here's the code:

```python
# more_married.py
from datetime import datetime

import typer


def main(met: datetime, celebration: datetime):
    premarried = celebration - met

    for i in range(2, 10):
        duration = i * premarried
        typer.secho(
            f"{i-1}x {(met + duration).date()}",
            fg=typer.colors.RED
        )


if __name__ == "__main__":
    typer.run(main)
```

Here's how to run it if we had met on February 14, 2010 and got married on February 14, 2013:

```bash
python more_married.py 2010-02-14 2013-02-14
```

Results:

```bash
1x 2016-02-15
2x 2019-02-15
3x 2022-02-15
4x 2025-02-15
5x 2028-02-16
6x 2031-02-16
7x 2034-02-16
8x 2037-02-16
```

Use this little script to impress the special person in your life!

![](/images/2022-02-14-hearts-a.png)
