import collections, functools, pathlib, json, csv
from datetime import datetime
from dateutil import parser

import pytz
import yaml
from fasthtml.common import *
from nb2fasthtml.core import (
    render_nb, read_nb, get_frontmatter_raw,render_md,
    strip_list
)

default_social_image = '/public/images/profile.jpg'

# This redirects dict is a relic of previous blog migrations.
# It is used to redirect old URLs embedded in books, presentations,
# and more to the new locations.
redirects = json.loads(pathlib.Path(f"redirects.json").read_text()) 

def MermaidJS(
        sel='.language-mermaid',  # CSS selector for mermaid elements
        theme='base',  # Mermaid theme to use
        delay=500  # Delay in milliseconds before rendering
    ):
    "Implements browser-based Mermaid diagram rendering."
    return Script(src='/mermaid.js', type='module')    

hdrs = (
    MarkdownJS(),
    HighlightJS(langs=['python', 'javascript', 'html', 'css',]),
    Link(rel='stylesheet', href='/public/style.css', type='text/css'),
    MermaidJS()
)

class ContentNotFound(Exception): pass

def render_code_output(cell,lang='python', render_md=render_md):
    res = []
    if len(cell['outputs'])==0: ''
    for output in cell['outputs']:
        print(output['output_type'])
        if output['output_type'] == 'execute_result':
            data = output['data']
            if 'text/markdown' in data.keys(): 
                res.append(NotStr(''.join(strip_list(data['text/markdown'][1:-1]))))
            elif 'text/plain' in data.keys(): 
                res.append(''.join(strip_list(data['text/plain'])))
        if output['output_type'] == 'stream':
            res.append(''.join(strip_list(output['text'])))
    if res: return render_md(*res, container=Pre)

# The following functions are three content loading. They are cached in
# memory to boost the speed of the site. In production at a minumum the
# app is restarted every time the project is deployed.
@functools.cache
def list_posts(published: bool = True, posts_dirname="posts", content=False) -> list[dict]:
    """
    Loads all the posts and their frontmatter.
    Note: Could use pathlib better
    """
    posts: list[dict] = []
    # Fetch notebooks
    for post in pathlib.Path('.').glob(f"{posts_dirname}/**/*.ipynb"):
        if '.ipynb_checkpoints' in str(post): continue
        nb = read_nb(post)
        data: dict = get_frontmatter_raw(nb.cells[0]) 
        data["slug"] = post.stem
        data['cls'] = 'notebook'
        if content:
            data["content"] = render_nb(post,
                                cls='',
                                fm_fn=lambda x: '',
                                out_fn=render_code_output
                                )
        posts.append(data)   
    # Fetch markdown
    for post in pathlib.Path('.').glob(f"{posts_dirname}/**/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        data['cls'] = 'marked'
        if content:
            data["content"] = '\n'.join(post.read_text().split("---")[2:])
        posts.append(data)

    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]

@functools.lru_cache
def get_post(slug: str) -> tuple|None:
    posts = list_posts(content=True)
    post = next((x for x in posts if x["slug"] == slug), None)
    if post is None: raise ContentNotFound
    return (post['content'], post)

@functools.cache
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

# The next block of code is several date utilities
# We need these because I've been sloppy about defining dates
# TODO: Fix datetimes in all markdown files so this wouldn't be necessary
def convert_dtstr_to_dt(date_str: str) -> datetime:
    """
    Convert a naive or non-naive date/datetime string to a datetime object.
    Naive datetime strings are assumed to be in GMT (UTC) timezone.
    """
    try:
        dt = parser.parse(date_str)
        if dt.tzinfo is None:
            # If the datetime object is naive, set it to GMT (UTC)
            dt = dt.replace(tzinfo=pytz.UTC)
        return dt
    except (ValueError, TypeError) as e:
        return None
    
def format_datetime(dt: datetime) -> str:
    """Format the datetime object"""
    formatted_date = dt.strftime("%B %d, %Y")
    formatted_time = dt.strftime("%I:%M%p").lstrip('0').lower()
    return f"{formatted_date} at {formatted_time}"

# Most pages use a number of reusable components to 
# render out HTML. I follow the FT Component standard
# of TitleCasing these, even though they are functions.
# That makes them easier to identify as FT Components.
def Layout(title, socials, *tags):
    """Generic layout for pages"""
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
    Main(*tags, cls='container'),
    Footer(Hr(), P(
                A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), ' | ',    
                A('Bluesky', href='https://bsky.app/profile/pydanny.bsky.social'), ' | ',
                A('Twitter', href='https://twitter.com/pydanny'), ' | ',             
                'Feeds: ', A('All', href='/feeds/atom.xml'), NotStr(', ') ,A('Python', href='/feeds/python.atom.xml'), NotStr(', ') , A('TIL', href='/feeds/til.atom.xml')
            ),
            P(f'All rights reserved {datetime.now().year}, Daniel Roy Greenfeld'),
            cls='container'
        ),
    Div(
        Div(
            H2('Search'),            
            Input(name='q', type='text', id='search-input', hx_trigger="keyup", placeholder='Enter your search query...', hx_get='/search-results', hx_target='.search-results-modal'),
            Div(cls='search-results-modal'),
            cls='modal-content'
        ),
        id='search-modal',
        style='display:none;',
        cls='modal overflow-auto'
    ),
    Div(hx_trigger="keyup[key=='/'] from:body"),
    Script("""
    //document.documentElement.setAttribute('data-theme', 'light');
    document.body.addEventListener('keydown', e => {
    if (e.key === '/') {
        e.preventDefault();
        document.getElementById('search-modal').style.display = 'block';
        document.getElementById('search-input').focus();
    }
    if (e.key === 'Escape') {
        document.getElementById('search-modal').style.display = 'none';
    }
    });

    document.getElementById('search-input').addEventListener('input', e => {
    htmx.trigger('.search-results', 'htmx:trigger', {value: e.target.value});
    });
    """)
)

def BlogPostPreview(title: str, slug: str, timestamp: str, description: str):
    """
    This renders a blog posts short display used for the index, article list, and tags.
    """
    return Span(
                H2(A(title, href=f"/posts/{slug}")),
                P(description, Br(), Small(Time(format_datetime(convert_dtstr_to_dt(timestamp)))))
        )

def TILPreview(title: str, slug: str, timestamp: str, description: str):
    return Span(
                H3(A(title[4:], href=f"/posts/{slug}")),
                P(Small(Time(format_datetime(convert_dtstr_to_dt(timestamp)))))
        )        

def TagLink(slug: str):
    return Span(A(slug, href=f"/tags/{slug}"), " ")

def TagLinkWithCount(slug: str, count: int):
    return Span(A(Span(slug), Small(f" ({count})"), href=f"/tags/{slug}"), " ")

def MarkdownPage(slug: str):
    """Renders a non-sequential markdown file"""
    try:
        text = pathlib.Path(f"pages/{slug}.md").read_text()
    except FileNotFoundError:
        return Page404()
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

### Going forwards everything is mostly a view

def Page404():
    """404 view"""
    return FtResponse(Layout(Title("404 Not Found"),
        Socials(site_name="https://daniel.feldroy.com",
                    title="Daniel Roy Greenfeld",
                    description="Daniel Roy Greenfeld's personal blog",
                    url="https://daniel.feldroy.com",
                    image="https://daniel.feldroy.com/public/images/profile.jpg",
                    ),                  
        H1("404 Not Found"), P("The page you are looking for does not exist.")),

        status_code=404
        )

def not_found():
    return Page404()

exception_handlers = {
    404: not_found
}

app, rt = fast_app(hdrs=hdrs, debug=False, exception_handlers=exception_handlers)

@rt
def index():
    all_posts = list_posts()
    posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in all_posts if 'TIL' not in x.get('tags')]
    popular = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in all_posts if x.get("popular", False)]    
    tils = [TILPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description='') for x in all_posts if 'TIL' in x.get('tags')]    
    return Layout(
        Title("Daniel Roy Greenfeld"),        
        Socials(site_name="https://daniel.feldroy.com",
                    title="Daniel Roy Greenfeld",
                    description="Daniel Roy Greenfeld's personal blog",
                    url="https://daniel.feldroy.com",
                    image="https://daniel.feldroy.com/public/images/profile.jpg",
                    ),
        Div(cls='grid')(
            Section(
                    H1('Recent Writings'),
                    *posts[:4],
                    P(A('Read all articles', href=posts))
                ),
            Section(
                    H1('Popular Writings'),
                    *popular
            ),            
            Section(
                    H1('TIL', Small(' (Today I learned)')),
                    *tils[:7],
                    P(A('Read more TIL articles', href='/tags/til'))
                ),
        )
    )

@rt
def posts():
    duration = round((datetime.now() - datetime(2005, 9, 3)).days / 365.25, 2)
    description = f'Everything written by Daniel Roy Greenfeld for the past {duration} years.'
    posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
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
    try:
        content, metadata = get_post(slug)
    except ContentNotFound:
        return Page404()
    tags = [TagLink(slug=x) for x in metadata.get("tags", [])]
    specials = ()
    if 'TIL' in metadata['tags']:
        specials = (A(
                Img(src="/public/logos/til-1.png", alt="Today I Learned", width="200", height="200", cls="center"),
                href="/tags/TIL")
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
            P(I(metadata.get('description', ''))),
            P(Small(Time(format_datetime(convert_dtstr_to_dt(metadata['date']))))),
            Div(content,cls=metadata['cls']),
            Div(style="width: 200px; margin: auto; display: block;")(*specials),
            P(Span("Tags: "), *tags),
            A("← Back to all articles", href="/"),
        ),
    )

@rt("/tags")
def get():
    tags = [TagLinkWithCount(slug=x[0], count=x[1]) for x in list_tags().items()]
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
    posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if slug in x.get("tags", [])]
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


def _search(q: str=''):
    def _s(obj: dict, name: str, q: str):
        content =  obj.get(name, "")
        if isinstance(content, list):
            content = " ".join(content)
        return q.lower().strip() in content.lower().strip()    
    messages = []
    posts = []
    description = f"No results found for '{q}'"
    if q.strip():
        posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts() if
                    any(_s(x, name, q) for name in ["title", "description", "content", "tags"])]
    if posts:
        messages = [H2(f"Search results on '{q}'"), P(f"Found {len(posts)} entries")]
        description = f"Search results on '{q}'"
    elif q.strip():
        messages = [P(f"No results found for '{q}'")]
    return Div(
        Meta(property='description', content=description),
        Meta(property='og:description', content=description),        
        Meta(name='twitter:description', content=description),
        *messages,
        *posts
    )

@rt("/search")
def get(q: str|None = None):
    result = []
    if q is not None:
        result.append(_search(q))
    return Layout(Title("Search"), 
        Socials(site_name="https://daniel.feldroy.com",
                        title="Search the site",
                        description='',
                        url="https://daniel.feldroy.com/search",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),          
        Form(cls='center', role='group')(
            Input(name="q", id='q', value=q, type="search", autofocus=True),
            Button("Search", hx_get="/search-results", hx_target='.search-results', hx_include='#q', onclick="updateQinURL()")
        ),
        Section(
            Div(cls='search-results')(*result),
            P(Small('Hint: Use the "/" shortcut to search from any page.')),            
            A("← Back home", href="/"),
        ),
        Script("""function updateQinURL() {
            let url = new URL(window.location);
            const value = document.getElementById('q').value
            url.searchParams.set('q', value);
            window.history.pushState({}, '', url);            
        };
        """),           
    )

@rt('/search-results')
def get(q: str):
    return _search(q)


@rt
def fitness():
    with open('public/fitness-2024.csv') as f:
        rows = [o for o in csv.DictReader(f)]

    dates = collections.defaultdict(list)
    for row in rows: dates[row['Date'][:7]].append(row)

    config = {'responsive': True}
    config = json.dumps(config)

    charts = []
    for month, rows in dates.items():
        fitness = [{
            'type': 'bar',
            'x': [o['Date'] for o in rows],
            'y': [o['Weight'] for o in rows],
            'text': [o['Weight'] for o in rows],
            'textposition': 'auto',
            'hoverinfo': 'none',        
            'marker': {'color': 'blue',},
            'name': 'Weight kg'
        },
        {
                'type': 'bar',
                'x': [o['Date'] for o in rows],
                'y': [o['BJJ'] for o in rows],
                'text': [o['BJJ'] for o in rows],
                'textposition': 'auto',
                'hoverinfo': 'none',        
                'marker': {'color': 'green',},
                'name': 'BJJ'
        },
        {
                'type': 'bar',
                'x': [o['Date'] for o in rows],
                'y': [o['Other'] for o in rows],
                'text': [o['Other'] for o in rows],
                'textposition': 'auto',
                'hoverinfo': 'none',        
                'marker': {'color': 'red',},
                'name': 'Strength'
        }   
        ]
        layout = {
            'title': {
                'text': datetime.strptime(month, '%Y-%m').strftime("%B %Y")
            },
            'font': {'size': 18},
            'barcornerradius': 15,
        }
        layout = json.dumps(layout)        
        chart_name = f'weightChart-{month}'
        charts.insert(0, Div(id=chart_name))        
        charts.insert(1, Script(f"Plotly.newPlot('{chart_name}', {fitness}, {layout}, {config});"))
        current_weight = rows[-1]['Weight']

    return Layout(
        Title('Fitness Tracking'),
        Socials(site_name="https://daniel.feldroy.com",
                        title=f"Fitness Tracking",
                        description='Just weight right now',
                        url=f"https://daniel.feldroy.com/fitness",
                        image="https://daniel.feldroy.com/public/images/profile.jpg",
                        ),         
        Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),
        Section(
            P(
                'Wt Goal: ', Strong('77 kg / 169 lbs'), Br(),
                f'Current: {current_weight} kg / {float(current_weight) * 2.2} lb'  
            ),            
            H2(f'Fitness Tracking'),
            Ol(
                Li('Weight kg is how much I weight in kilograms.'),
                Li('BJJ is how many minutes of Brazilian Jiu-Jitsu in a day.'),
                Li('Strength is how many minutes of strength training in a day, most often weights or HIIT, somes alternative exercise like Yoga or Pilates.'),
            ),
            *charts,
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

@rt("/{slug}.ipynb")
def get(slug: str):
    try:
        nb = render_nb(f'nbs/{slug}.ipynb', wrapper=Div, cls='', fm_fn=None)
    except:
        return Page404()
    return Layout(
        Title("Demo JupyterA"),
        Socials(site_name="https://daniel.feldroy.com",
                        title="Demo Jupyter",
                        description='Demo Jupyter',
                        url=f"https://daniel.feldroy.com/{slug}.ipynb",
                        image=default_social_image,
                        ),  
        nb
    ) 


@rt("/{slug}")
def get(slug: str):
    redirects_url = redirects.get(slug, None)
    if redirects_url is not None:
        return RedirectResponse(url=redirects_url)
    try:
        return Layout(*MarkdownPage(slug))
    except TypeError:
        return Page404()

    
@rt("/{slug_1}/{slug_2}")
def get(slug_1: str, slug_2: str):
    try:
        return Layout(*MarkdownPage(slug_1 + "/" + slug_2))
    except TypeError:
        return Page404()

serve(reload_includes="*.md,*.ipynb,*.css")
