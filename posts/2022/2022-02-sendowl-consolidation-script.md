---
date: "2022-02-22T22:20:50.52Z"
published: true
tags:
  - python
  - book
  - self-publishing
time_to_read: 2
title: Sendowl Consolidation Script
description: Unifying our sendowl accounts into one
---

As self-published authors, Audrey and I use the awesome [sendowl](https://sendowl.com) service to distribute our digital files. We had multiple storefronts accounts for different countries but now we only need one. This is what I wrote to handle the migration of orders from multiple accounts into just one account.

```python
"""
This converts a Sendowl orders CSV export into a CSV
following Sendowl's import template. Useful for
consolidating Sendowl accounts.
"""

import csv
import sys
from pathlib import Path

try:
    import typer
except ImportError:
    print("Run 'pip install typer'")
    sys.exit()

fieldnames = """
Buyer Email (required)
Buyer Name
Transaction ID
Amount
Gateway Fee
Order date and time (YYYY-MM-DD hh::mm:ss)
""".strip().splitlines()

real_to_dollar = 5.25


def main(input_file: Path):

    typer.secho(
        f"Parsing data from '{input_file}'",
        fg=typer.colors.GREEN,
    )
    orders = []
    with open(input_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = row["Amount"]
            if not amount.strip():
                amount = "0"
            amount = float(amount)
            orders.append(
                {
                    "Buyer Email (required)": row["Buyer Email"],
                    "Buyer Name": row["Buyer Name"],
                    "Transaction ID": row["SendOwl Transaction ID"],
                    "Amount": amount / real_to_dollar,
                    "Gateway Fee": "0",
                    "Order date and time (YYYY-MM-DD hh::mm:ss)": row[
                        "Order date/time"
                    ],
                }
            )

    typer.secho(
        f"Converting {len(orders)} orders",
        fg=typer.colors.GREEN,
    )
    with open("output.csv", "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)

    typer.secho(f"Done!", fg=typer.colors.GREEN)


if __name__ == "__main__":
    typer.run(main)
```
