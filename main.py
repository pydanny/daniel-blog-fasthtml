import json
import pathlib

from fasthtml.common import *
from components import *
from contents import *

from datetime import datetime

# This redirects dict is a relic of previous blog migrations.
# It is used to redirect old URLs embedded in books, presentations,
# and more to the new locations.
redirects = json.loads(pathlib.Path(f"redirects.json").read_text())   

hdrs = (
    MarkdownJS(),
    HighlightJS(langs=['python', 'javascript', 'html', 'css']),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css', type='text/css'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css', type='text/css'),    
    Link(rel='stylesheet', href='/public/style.css', type='text/css'),        
)

def Page404():
    return Layout(Title("404 Not Found"),
        Socials(site_name="https://daniel.feldroy.com",
                    title="Daniel Roy Greenfeld",
                    description="Daniel Roy Greenfeld's personal blog",
                    url="https://daniel.feldroy.com",
                    image="https://daniel.feldroy.com/public/images/profile.jpg",
                    ),                  
        H1("404 Not Found"), P("The page you are looking for does not exist."))

def not_found(req, res):
    res.status = 404
    return Page404()

exception_handlers = {
    404: not_found
}

app, rt = fast_app(hdrs=hdrs, pico=False, debug=True, exception_handlers=exception_handlers)

@rt("/")
def get():
    posts = [blog_post(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    popular = [blog_post(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if x.get("popular", False)]    
    return Layout(
        Title("Daniel Roy Greenfeld"),        
        Socials(site_name="https://daniel.feldroy.com",
                    title="Daniel Roy Greenfeld",
                    description="Daniel Roy Greenfeld's personal blog",
                    url="https://daniel.feldroy.com",
                    image="https://daniel.feldroy.com/public/images/profile.jpg",
                    ),
        Section(
                H1('Recent Writings'),
                *posts[:3]
            ),
        Hr(),
        Section(
                H1('Popular Writings'),
                *popular
        ),
    )

@rt("/posts")
def get():
    duration = round((datetime.now() - datetime(2005, 9, 3)).days / 365.25, 2)
    description = f'Everything written by Daniel Roy Greenfeld for the past {duration} years.'
    posts = [blog_post(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    return Layout(
        Title("All posts by Daniel Roy Greenfeld"),
        Socials(site_name="https://daniel.feldroy.com",
                        title="All posts by Daniel Roy Greenfeld",
                        description=description,
                        url="https://daniel.feldroy.com/posts/",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),
        Section(
                H1(f'All Articles ({len(posts)})'),
                P(description),
                *posts,
                A("← Back to home", href="/"),
        ))

@rt("/posts/{slug}")
def get(slug: str):
    # post = [x for x in filter(lambda x: x["slug"] == slug, list_posts())][0]
    content, metadata = get_post(slug)
    # content = pathlib.Path(f"posts/{slug}.md").read_text().split("---")[2]
    # metadata = yaml.safe_load(pathlib.Path(f"posts/{slug}.md").read_text().split("---")[1])    
    tags = [tag(slug=x) for x in metadata.get("tags", [])]
    specials = ()
    if 'TIL' in metadata['tags']:
        specials = (
            A(href="/tags/TIL")(
                Img(src="/public/logos/til-1.png", alt="Today I Learned", width="200", height="200", cls="center"),
            )
        )
    return Layout(
        Title(metadata['title']),
        Socials(site_name="https://daniel.feldroy.com",
                        title=metadata["title"],
                        description=metadata.get("description", ""),
                        url=f"https://daniel.feldroy.com/posts/{slug}",
                        image="https://daniel.feldroy.com" + metadata.get("image", default_social_image),
                        ),        
        Section(
            H1(metadata["title"]),
            Div(content,cls="marked"),
            Div(style="width: 200px; margin: auto; display: block;")(*specials),
            P(Span("Tags: "), *tags),
            A("← Back to all articles", href="/"),
        ),
    )

@rt("/tags")
def get():
    tags = [tag_with_count(slug=x[0], count=x[1]) for x in list_tags().items()]
    return Layout(Title("Tags"),
        Socials(site_name="https://daniel.feldroy.com",
                        title="Tags",
                        description="All tags used in the site.",
                        url="https://daniel.feldroy.com/tags/",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),               
        Section(
            H1('Tags'),
            P('All tags used in the blog'),
            *tags,
            Br(), Br(),
            A("← Back home", href="/"),
        )
    )

@rt("/tags/{slug}")
def get(slug: str):
    posts = [blog_post(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if slug in x.get("tags", [])]
    return Layout(Title(f"Tag: {slug}"),
        Socials(site_name="https://daniel.feldroy.com",
                        title=f"Tag: {slug}",
                        description=f'Posts tagged with "{slug}" ({len(posts)})',
                        url=f"https://daniel.feldroy.com/tags/{slug}",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),                       
        Section(
            H1(f'Posts tagged with "{slug}" ({len(posts)})'),
            *posts,
            A("← Back home", href="/"),
        )
    )

@rt("/search")
def get(q: str = ""):
    def _s(obj: dict, name: str, q: str):
        content =  obj.get(name, "")
        if isinstance(content, list):
            content = " ".join(content)
        return q.lower().strip() in content.lower().strip()

    posts = []
    if q:
        posts = [blog_post(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if
                    any(_s(x, name, q) for name in ["title", "description", "content", "tags"])]
        
    if posts:
        messages = [H2(f"Search results on '{q}'"), P(f"Found {len(posts)} entries")]
        description = f"Search results on '{q}'. Found {len(posts)} entries"
    elif q:
        messages = [P(f"No results found for '{q}'")]
        description = f"No results found for '{q}'"
    else:
        messages = []
        description = ""
    return Layout(Title("Search"), 
        Socials(site_name="https://daniel.feldroy.com",
                        title="Search the site",
                        description=description,
                        url="https://daniel.feldroy.com/search",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),                    
        Form(Input(name="q", value=q, id="search", type="search", autofocus=True), Button("Search"), style="text-align: center;"),
        Section(
            *messages,
            *posts,
            A("← Back home", href="/"),
        )
    )

@rt("/feeds/{fname:path}.{ext}")
def get(fname:str, ext:str): 
    return FileResponse(f'feeds/{fname}.{ext}')

reg_re_param("static", "ico|gif|jpg|jpeg|webm|css|js|woff|png|svg|mp4|webp|ttf|otf|eot|woff2|txt")

@rt("/{slug}.html")
def get(slug: str):
    url = redirects.get(slug, None) or redirects.get(slug + ".html", None)
    if url is not None:
        return RedirectResponse(url=url)
    return Page404()

@rt("/{slug}")
def get(slug: str):
    redirects_url = redirects.get(slug, None)
    if redirects_url is not None:
        return RedirectResponse(url=redirects_url)
    try:
        return Layout(*markdown_page(slug))
    except TypeError:
        return Page404()

    
@rt("/{slug_1}/{slug_2}")
def get(slug_1: str, slug_2: str):
    try:
        return Layout(*markdown_page(slug_1 + "/" + slug_2))
    except TypeError:
        return Page404()

serve()