import functools
import pathlib
from datetime import datetime
from dataclasses import dataclass
from typing import Callable

from fasthtml.common import *
import yaml
import uvicorn

css_text = """
a {color: #0070f3 !important;}

header {text-align: center;}

h1 {
    font-size: 2.5rem;
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -0.05rem;
    margin: 1rem 0;
  }
  
h2 {
    font-size: 2rem;
    line-height: 1.3;
    font-weight: 800;
    letter-spacing: -0.05rem;
    margin: 1rem 0;
  }
  
h3 {
    font-size: 1.5rem;
    line-height: 1.4;
    margin: 1rem 0;
  }
  
h4 {
    font-size: 1.2rem;
    line-height: 1.5;
  }

.borderCircle {
  border-radius: 9999px;
  margin-bottom: 0rem;
  text-decoration: none;
}  
"""

# app = FastHTML()
app = FastHTMLWithLiveReload(hdrs=(
    MarkdownJS(),
    HighlightJS(langs=['python', 'javascript', 'html', 'css']),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css', type='text/css'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css', type='text/css'),
    Style(css_text)
    )
)

@dataclass
class BlogPost():
    title: str
    slug: str
    timestamp: str
    description: str

    def __xt__(self):
        return Span(
                H2(A(self.title, href=f"/posts/{self.slug}")),
                P(self.description, Small(Time(self.timestamp))),
                
        )
    
@dataclass
class BlogHeader():
    def __xt__(self):
        return Header(
        A(Img(
            cls='borderCircle', alt='Daniel Roy Greenfeld', src='https://daniel.feldroy.com/_next/image?url=%2Fimages%2Fprofile.jpg&w=256&q=75', width='108', height='108')
            , href='/'),
        A(H2('Daniel Roy Greenfeld'), href='/'),
        P(A('About', href='/about'), '|', A('Articles', href='/posts'), '|', A('Books', href='/books'), '|', A('Jobs', href='/jobs'), '|', A('News', href='/news'), '|', A('Tags', href='/tags')
        
        )
    )


@dataclass
class BlogFooter():
    def __xt__(self):
        return Footer(P(
            A('Mastodon', href='https://fosstodon.org/@danielfeldroy'), '|',
            A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), '|',
            A('Twitter', href='https://twitter.com/pydanny'), '|',
            A('Atom Feed', href='/feeds/atom.xml')
        ),
        P('All rights reserved 2024, Daniel Roy Greenfeld')
    )

@dataclass
class Tag():
    slug: str
    def __xt__(self):
        return A(self.slug, href=f"/tags/{self.slug}")

@functools.lru_cache
def list_posts(published: bool = True, posts_dirname="posts") -> list[dict]:
    posts: list[dict] = []
    for post in pathlib.Path(".").glob(f"{posts_dirname}/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        posts.append(data)

    posts = [x for x in filter(lambda x: x["published"] is True, posts)]
    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]

def Time(timestamp: str) -> str:
    """Placeholder"""
    return Small(timestamp)


@app.get("/")
def index():
    posts = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    popular = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if x.get("popular", False)]
    return Title("Daniel Roy Greenfeld"), BlogHeader(), Main(
        Section(
            H2(f'Recent Writings'),
            *posts[:3]
        ),
        Hr(),
        Section(
            H2(f'Popular Writings'),
            *popular
        )
    ), BlogFooter()


# This doesn't work the way it does in Django or FastAPI. No matter the positioning it is revaluated.
# @app.get("/{slug}")
# def markdown_page(slug: str):
#     content = pathlib.Path(f"{slug}.md").read_text().split("---")[2]
#     metadata = yaml.safe_load(pathlib.Path(f"{slug}.md").read_text().split("---")[1])
#     return Title(metadata.get('Title', slug)), BlogHeader(), Main(
#         A("Back to all articles", href="/"),
#         Section(
#             Div(content,cls="marked")
#         )
#     ), BlogFooter()


@app.get("/posts/")
def articles():
    posts = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    return Title("Daniel Roy Greenfeld"), BlogHeader(), Main(
        Section(
            H1(f'All Articles ({len(posts)})'),
            P('Everything written by Daniel Roy Greenfeld for the past 19 years'),
            *posts
        )
    ), BlogFooter()

@app.get("/posts/{slug}")
def article(slug: str):
    post = [x for x in filter(lambda x: x["slug"] == slug, list_posts())][0]
    content = pathlib.Path(f"posts/{slug}.md").read_text().split("---")[2]
    metadata = yaml.safe_load(pathlib.Path(f"posts/{slug}.md").read_text().split("---")[1])
    tags = [Tag(slug=x) for x in metadata.get("tags", [])]
    return Title(post["title"]), BlogHeader(), Main(
        A("Back to all articles", href="/"),
        Section(
            H1(post["title"]),
            Div(content,cls="marked"),
            P(Span("Tags: "), *tags)
        )
    ), BlogFooter()


    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))