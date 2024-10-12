from feedgen.feed import FeedGenerator
import main as contents
from dateutil import parser
import markdown
import pytz
from datetime import datetime

def convert_dtstr_to_dt(date_str):
    """
    Convert a naive or non-naive date/datetime string to a datetime object.
    Naive datetime strings are assumed to be in GMT (UTC) timezone.
    
    Args:
        date_str (str): The date or datetime string to convert.
        
    Returns:
        datetime: The corresponding datetime object.
    """
    try:
        dt = parser.parse(date_str)
        if dt.tzinfo is None:
            # If the datetime object is naive, set it to GMT (UTC)
            dt = dt.replace(tzinfo=pytz.UTC)
        return dt
    except (ValueError, TypeError) as e:
        print(f"Error parsing date string: {e}")
        return None


def filter_posts_by_tag(posts: list[dict], tag: str):
    """
    Generator function that filters posts by a single tag.
    """
    for post in posts:
        post_tags = [x.lower() for x in post.get('tags', [])]
        if tag in post_tags:
            yield post    


def github_markdown_to_html(markdown_str):
    """
    Convert a GitHub-flavored Markdown string to HTML.
    
    Args:
        markdown_str (str): The GitHub-flavored Markdown string to convert.
        
    Returns:
        str: The resulting HTML string.
    """
    html = markdown.markdown(
        markdown_str,
        extensions=['extra', 'codehilite', 'toc', 'tables']
    )
    return html

def add_entry(fg, raw):
    content, metadata = contents.get_post(raw['slug'])
    fe = fg.add_entry()
    linker = f'https://daniel.feldroy.com/posts/{raw["slug"]}'
    fe.id(linker)
    fe.link(href=linker)
    fe.title(metadata['title'])
    fe.summary(metadata['description'] or '')    
    fe.content(content=github_markdown_to_html(content), type='CDATA')  
    fe.contributor([{'name': 'Daniel Roy Greenfeld', 'email': 'daniel@feldroy.com'}])
    fe.author([{'name': 'Daniel Roy Greenfeld', 'email': 'daniel@feldroy.com'}])
    fe.pubDate(convert_dtstr_to_dt(metadata['date']))
    # Add tags to the entry
    for tag in metadata.get('tags', []):
        fe.category(term=tag)  


def build_feed(content_tag: str | None = None):

    fg = FeedGenerator()
    fg.id('https://daniel.feldroy.com')
    fg.title('Daniel Roy Greenfeld')
    fg.author({'name': 'Daniel Roy Greenfeld', 'email': 'daniel@feldroy.com', 'uri':'https://daniel.feldroy.com'})
    fg.link(href='https://daniel.feldroy.com', rel='alternate')
    fg.title('Inside the head of Daniel Roy Greenfeld')
    fg.logo('https://daniel.feldroy.com/images/pydanny-cartwheel.png')
    fg.rights(f'All rights reserved {datetime.now().year}, Daniel Roy Greenfeld')
    fg.language('en') 

    posts = contents.list_posts(published=True)             

    if content_tag is not None:
        posts = list(filter_posts_by_tag(posts, content_tag))

    for raw in posts[:3]:
        add_entry(fg, raw)


    if content_tag is not None:
        fg.atom_file(f'feeds/{content_tag}.atom.xml', pretty=True)
    else:
        fg.atom_file('feeds/atom.xml', pretty=True)


if __name__ == '__main__':
    import sys
    content_tag = sys.argv[1] if len(sys.argv) > 1 else None
    build_feed(content_tag)