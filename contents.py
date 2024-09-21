import collections
import functools
import pathlib
import yaml

__all__ = ["list_posts", "get_post", "list_tags"]

@functools.lru_cache
def list_posts(published: bool = True, posts_dirname="posts", content=False) -> list[dict]:
    posts: list[dict] = []
    for post in pathlib.Path(".").glob(f"{posts_dirname}/**/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        if content:
            data["content"] = '\n'.join(post.read_text().split("---")[2:])
        posts.append(data)

    posts = [x for x in filter(lambda x: x["published"] is True, posts)]
    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]


def get_post(slug: str):
    posts = list_posts(content=True)
    post = next((x for x in posts if x["slug"] == slug), None)
    return (post['content'], post)


@functools.lru_cache
def list_tags() -> dict[str, int]:
    unsorted_tags = {}
    for post in list_posts():
        page_tags = post.get("tags", [])
        for tag in page_tags:
            if tag in unsorted_tags:
                unsorted_tags[tag] += 1
            else:
                unsorted_tags[tag] = 1  

    tags: dict = collections.OrderedDict(
            sorted(unsorted_tags.items(), key=lambda x: x[1], reverse=True)
        )      

    return tags