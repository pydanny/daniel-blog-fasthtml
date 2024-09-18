from fasthtml.common import *
from datetime import datetime
from dateutil import parser
import pytz
import pathlib
import yaml

__all__ = ['blog_post',"tag", "Layout",
           "tag_with_count", "markdown_page", "default_social_image"]

default_social_image = '/public/images/profile.jpg'

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
    
def format_datetime(dt: datetime):
    
    # Format the datetime object
    formatted_date = dt.strftime("%B %d, %Y")
    formatted_time = dt.strftime("%I:%M%p").lstrip('0').lower()
    
    return f"{formatted_date} at {formatted_time}"


def Layout(title, socials, *tags):
    return title, socials, (
        Header(
            A(Img(
                cls='borderCircle', alt='Daniel Roy Greenfeld', src='/public/images/profile.jpg', width='108', height='108')
                , href='/'),
            A(H2('Daniel Roy Greenfeld'), href="/"),
            P(
                A('About', href='/about'),' | ', 
                A('Articles', href='/posts'), ' | ',
                A('Books', href='/books'), ' | ',
                A('Jobs', href='/jobs'), ' | ',
                A('Tags', href='/tags'), ' | ',
                A('Search', href='/search')
            ), style="text-align: center;"
        ),
    Main(*tags),
    Footer(Hr(), P(
                A('Mastodon', href='https://fosstodon.org/@danielfeldroy'), ' | ',
                A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), ' | ',
                A('Twitter', href='https://twitter.com/pydanny'), ' | ',
                A('Atom Feed', href='/feeds/atom.xml')
            ),
            P(f'All rights reserved {datetime.now().year}, Daniel Roy Greenfeld')
        )
    )

def blog_post(title: str, slug: str, timestamp: str, description: str):
    return Span(
                H2(A(title, href=f"/posts/{slug}")),
                P(description, Br(), Small(Time(format_datetime(convert_dtstr_to_dt(timestamp))))),
        )


def tag(slug: str):
    return Span(A(slug, href=f"/tags/{slug}"), " ")

def tag_with_count(slug: str, count: int):
    return Span(A(Span(slug), Small(f" ({count})"), href=f"/tags/{slug}"), " ")

def markdown_page(slug: str):
    try:
        text = pathlib.Path(f"pages/{slug}.md").read_text()
    except FileNotFoundError:
        return Response("Page not found", status_code=404) 
    content = ''.join(text.split("---")[2:])
    metadata = yaml.safe_load(text.split("---")[1])
    return (Title(metadata.get('title', slug)),
        Socials(site_name="https://daniel.feldroy.com",
                        title=metadata.get('title', slug),
                        description=metadata.get('description', 'slug'),
                        url=f"https://daniel.feldroy.com/{slug}",
                        image=metadata.get("image", default_social_image),
                        ),                
        A("← Back to home", href="/"),
        Section(
            Div(content,cls="marked")
        )
    )
