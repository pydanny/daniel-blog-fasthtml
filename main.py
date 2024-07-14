import collections
import functools
import pathlib
from dataclasses import dataclass

from fasthtml.common import *
import yaml
import uvicorn

css_text = """
a {color: #0070f3 !important;}

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
    Style(css_text),
    )
)
rt = app.route

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
        A(H2('Daniel Roy Greenfeld')),
        P(A('About', href='/about'), '|', A('Articles', href='/posts'), '|', A('Books', href='/books'), '|', A('Jobs', href='/jobs'), '|', A('Tags', href='/tags'), '|', A('Search', href='/search')
        
        ), style="text-align: center;"
    )


@dataclass
class BlogFooter():
    def __xt__(self):
        return Footer(Hr(), P(
            A('Mastodon', href='https://fosstodon.org/@danielfeldroy'), '|',
            A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), '|',
            A('Twitter', href='https://twitter.com/pydanny'), '|',
            A('Atom Feed', href='/feeds/atom.xml')
        ),
        P('All rights reserved 2024, Daniel Roy Greenfeld')
    )


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


@dataclass
class Tag():
    slug: str
    def __xt__(self):
        return A(self.slug, href=f"/tags/{self.slug}")
    
@dataclass
class TagWithCount():
    slug: str
    count: int
    def __xt__(self):
        return A(Span(self.slug), Small(f"({self.count})"), href=f"/tags/{self.slug}")


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


# Static files
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): return FileResponse(f'public/{fname}.{ext}')



# Views start here

@app.get("/tags/")
def tags():
    tags = [TagWithCount(slug=x[0], count=x[1]) for x in list_tags().items()]
    return Title("Tags"), BlogHeader(), Main(
        Section(
            H1('Tags'),
            P('All tags used in the blog'),
            *tags
        )
    ), BlogFooter()


@app.get("/tags/{slug}")
def tag(slug: str):
    posts = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if slug in x.get("tags", [])]
    return Title(f"Tag: {slug}"), BlogHeader(), Main(
        Section(
            H1(f'Posts tagged with "{slug}" ({len(posts)})'),
            *posts
        )
    ), BlogFooter()


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


@app.get("/posts/")
def articles():
    posts = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    return Title("Daniel Roy Greenfeld"), BlogHeader(), Main(
        Section(
            H1(f'All Articles ({len(posts)})'),
            P('Everything written by Daniel Roy Greenfeld for the past 19 years'),
            *posts,
            A("← Back to home", href="/"),
        )
    ), BlogFooter()

@app.get("/posts/{slug}")
def article(slug: str):
    post = [x for x in filter(lambda x: x["slug"] == slug, list_posts())][0]
    content = pathlib.Path(f"posts/{slug}.md").read_text().split("---")[2]
    metadata = yaml.safe_load(pathlib.Path(f"posts/{slug}.md").read_text().split("---")[1])
    tags = [Tag(slug=x) for x in metadata.get("tags", [])]
    return Title(post["title"]), BlogHeader(), Main(
        Section(
            H1(post["title"]),
            Div(content,cls="marked"),
            P(Span("Tags: "), *tags),
            A("← Back to all articles", href="/"),
        )
    ), BlogFooter()


@app.get("/search")
def search(q: str = ""):
    def _s(obj: dict, name: str, q: str):
        content =  obj.get(name, "")
        if isinstance(content, list):
            content = " ".join(content)
        return q.lower().strip() in content.lower().strip()

    # q = request.query_params.get("q", "")
    posts = []
    if q:
        posts = [BlogPost(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if
                    any(_s(x, name, q) for name in ["title", "description", "content", "tags"])]
        
    if posts:
        messages = [H2(f"Search results on '{q}'"), P(f"Found {len(posts)} results")]
    elif q:
        messages = [P("No results found")]
    else:
        messages = []
    return Title("Search"), BlogHeader(), Body(Main(
        Form(Input(name="q", value=q, id="search", type="search"), Button("Search"), style="text-align: center;"),
        Section(
            *messages,
            *posts,
            # A("← Back home", href="/"),
        )
    ), onload="document.getElementById('search').focus()"), BlogFooter()


# Markdown views
class MarkdownPage():
    def __init__(self, slug: str):
        self.slug = slug
        text = pathlib.Path(f"pages/{slug}.md").read_text()
        self.content = ''.join(text.split("---")[2:])
        self.metadata = yaml.safe_load(text.split("---")[1])


@app.get("/about")
def about():
    page = MarkdownPage("about")
    return Title(page.metadata.get('Title', page.slug)), BlogHeader(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(page.content,cls="marked")
        )
    ), BlogFooter()

@app.get("/books")
def about():
    page = MarkdownPage("books")
    return Title(page.metadata.get('Title', page.slug)), BlogHeader(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(page.content,cls="marked")
        )
    ), BlogFooter()

@app.get("/books/tech")
def about():
    page = MarkdownPage("tech")
    return Title(page.metadata.get('Title', page.slug)), BlogHeader(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(page.content,cls="marked")
        )
    ), BlogFooter()


@app.get("/books/fiction")
def about():
    page = MarkdownPage("fiction")
    return Title(page.metadata.get('Title', page.slug)), BlogHeader(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(page.content,cls="marked")
        )
    ), BlogFooter()


@app.get("/jobs")
def about():
    page = MarkdownPage("jobs")
    return Title(page.metadata.get('Title', page.slug)), BlogHeader(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(page.content,cls="marked")
        )
    ), BlogFooter()
    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))