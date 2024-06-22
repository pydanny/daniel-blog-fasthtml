---
date: "2022-02-25T11:50:50.52Z"
published: true
tags:
  - blog
  - python
time_to_read: 2
title: Blogger to Markdown Script
description: Converting hundreds of posts from blogger to markdown
image: /images/2022-02-old-blog-archive.png
---

I started writing blog posts on [Blogger](https://www.blogger.com/) in 2007. I did so on multiple accounts. On one blog I wrote about software programming, on another I wrote about fiction, and on yet another I wrote about personal things. The HTML form interface was convienant and as the years went by I wrote hundreds of articles.

Five years later in 2012 I started writing on a static site generator. I always thought of bringing my old posts over but it was nearly 10 years before I did so.

This is the script I wrote to migrate 449 articles spread across three blogger accounts. It brought them in three batches:

- [See all 318 articles migrated](/tags/legacy-blogger) from pydanny.blogspot.com
- [See all 114 articles migrated](/tags/legacy-dannygreenfeld) from dannygreenfeld.blogspot.com
- [See all 17 articles migrated](/tags/legacy-danielroygreenfeld) from danielroygreenfeld.blogspot.com

The script does the following:

- Converts blogger XML to markdown
- Most content kept as simple HTML rather than cast into commonmark
- Adds metadata as frontmatter in YAML format
- Includes the Blogger comments so one doesn't lose old conversations

```python
"""
How to use this script:
1. Go to your blogger account settings
2. Search for the "Back up content" link
3. Download the content as an XML file
4. Run the script with:

    Usage: python legacy.py [OPTIONS] INPUT_FILE OUTPUT_DIR

    Arguments:
      INPUT_FILE  [required]
      OUTPUT_DIR  [required]

    Options:
        --tag TEXT
            Tag to add to frontmatter
            [default: legacy-blogger]
        --show-original / --no-show-original
            Link MD files to original articles
            [default: show-original]

TODOs
1. Remove the odd 'pydanny' specific items
2. Add pure python way to convert HTML to markdown
"""

import sys
from pathlib import Path

try:
    import feedparser
    import typer
    import yaml
except ImportError:
    print("Run 'pip install feedparser typer yaml'")


def main(
    input_file: Path,
    output_dir: Path,
    tag: str = typer.Option("legacy-blogger", help="Tag to add to frontmatter"),
    show_original: bool = typer.Option(True, help="Link MD files to original articles"),
):

    typer.secho(f"Parsing data from '{input_file}'", fg=typer.colors.GREEN)
    raw_text = input_file.read_text()
    # parse the historical data
    data = feedparser.parse(raw_text)
    posts = {}
    for entry in data.entries:
        try:
            # Filter out config data and other junk
            if "tag:blogger.com" in entry.link:
                continue
            if "comments" in entry["href"]:
                continue
            if "#settings" in entry.category:
                continue
            if entry.title == "Template: pydanny":
                continue

            # add comments to entries
            if "#comment" in entry.category:
                posts[entry["thr_in-reply-to"]["href"]].comments.append(entry)
                continue

            # Add entries to the posts and prep for comments
            entry["comments"] = []
            posts[entry.link] = entry
        except KeyError:
            continue

    # Write the markdown files
    typer.secho(
        f"Writing {len(posts)} blogger posts to markdown files", fg=typer.colors.GREEN
    )
    with typer.progressbar(posts.items()) as posts_progress:
        for key, value in posts_progress:
            # Get a MD filename from the original HTML URL
            filename = key.replace(".html", ".md")
            filename = filename.replace(data["feed"]["link"], "")
            link = data["feed"]["link"].replace("http", "https")
            filename = filename.replace(link, "")
            # print('\n',link, data['feed']['link'], filename)
            # Catches some of the configuration elements
            if len(filename.strip()) == 0:
                continue
            # bypasses simple pages, TODO: Provide option to create MD pages
            if filename.startswith("p-"):
                continue
            filename = filename.replace("/", "-")
            # Get a list of tags
            tags = [x["term"] for x in value.tags]
            tags = [
                x
                for x in tags
                if x != "https://schemas.google.com/blogger/2008/kind#post"
            ]
            # Add the tag option to list of tags
            tags.append(tag)
            frontmatter = {
                "date": value["published"],
                "published": True,
                "slug": filename.replace(".md", ""),
                "tags": tags,
                "time_to_read": 5,
                "title": value["title"],
                "description": "",
            }
            with open(f"{output_dir.joinpath(filename)}", "w") as f:
                # Set the frontmatter
                f.write("---\n")
                f.write(yaml.dump(frontmatter))
                f.write("---\n\n")
                if show_original:
                    # Set a link to the original content
                    f.write(
                        f"*This was originally posted on blogger [here]({key})*.\n\n"
                    )
                # Write the HTML, TODO: consider converting to markdown
                f.write(value["summary"])
                # If any comments, add them
                if value["comments"]:
                    f.write("\n\n---\n\n")
                    f.write(
                        f'## {len(value["comments"])} comments captured from [original post]({key}) on Blogger\n\n'
                    )
                    for comment in value["comments"]:
                        f.write(
                            f"**{comment['author_detail']['name']} said on {comment['published'][:10]}**\n\n"
                        )
                        f.write(comment["summary"])
                        f.write("\n\n")


if __name__ == "__main__":
    typer.run(main)
```

![](/images/2022-02-old-blog-archive.png)
