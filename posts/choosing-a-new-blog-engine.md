---
date: "2012-04-05"
published: true
slug: choosing-a-new-blog-engine
tags:
  - python
  - blog
  - ruby
time_to_read: 4
title: Choosing a new python based blog engine
---

# Why a new blog engine?

On my [old blog](https://pydanny.blogspot.com/), I had been having
issues with Blogger for some time. The WYSIWYG text editor was annoying
in that it produced wonky HTML, so I had to hand craft the posts. Which
meant I often wrote the HTML formatted copy in a text editor and then
copy/pasted it into the browser. A few times this blew up and I really
wished I had version controlled back ups. Adding code examples was
problematic, even with a stylesheet helpfully provided by Google.
Finally, some of the changes to the blog engine itself were beginning to
worry me, so I started looking for alternatives.

After my fiancee, [Audrey Roy](https://audrey.feldroy.com/), converted her blog to
<https://github.com/mojombo/jekyll> at it's new location of
aroygreenfeld.com (now at [audrey.feldroy.com](https://audrey.feldroy.com/)), the static file hosting seemed
so awesome I was impressed enough to [give Jekyll a
try](/tried-out-jekyll.html). Why did Jekyll and
static file hosting interest me so much?

## I don't want to maintain my own server

A couple times I rolled out a blog on a site I stood up, but didn't
really feel like maintaining a site. I want someone else to do it. When
I write, I want someone else to worry about the details. I want to focus
on writing and nothing else.

Well... almost nothing else. You'll understand shortly.

## I want to be able to write without connection

With blogger, I needed an internet connection to get my blog posts to
format correctly. With Jekyll and other static file systems, I can just
type away.

## I want to publish via git

My <https://pydanny-event-notes.rtfd.org> has really exploded in my own
usage and continued because it uses the same patterns I use in software
development. I'm used to the pattern of using Git to push up content,
so why use naked HTML? Sure, there are RST-to-HTML processors that I
could use to generate that HTML, but they always require some amount of
manual correction. Jekyll, and it's alternatives, let me just write.

# Jekyll wasn't for me

I found Jekyll to be good and much more fun than Blogger, but not good
enough. To sum up:

- I prefer RestructuredText over Markdown.
- I don't know enough Ruby to easily customize things. I don't feel
  like diving into Ruby just to learn how to make modifications.
- The template engine was like Smarty/Django/Jinja2, but not as much
  fun. Debugging errors was very problematic. Which was a problem when
  I started to play with modifying the theme.

On the second and third bullets, you might wonder why I would care about
the underlying engine if all I wanted to do was write. Well, I'm well
aware of the fact that I change opinions now and then. :-)

It was after trying out Jekyll that I started looking for
[Python](https://python.org) based static file blog systems. The choices
that seemed appropriate were:

# [blogofile](https://github.com/EnigmaCurry/blogofile/)

This is probably the most mature, most common Python static file
generator around. It looks really awesome, and everyone who uses it
swears by it. Alas, it's powered by
[Mako](https://www.makotemplates.org/) templates, which is... um...
[not my
friend](https://pydanny.blogspot.com/2010/12/stupid-template-languages.html)
(apologies to [Mike
Bayer](https://techspot.zzzeek.org/2010/12/04/in-response-to-stupid-template-languages/)).
What I really wanted was something with templates powered by
[Jinja2](https://jinja.palletsprojects.com).

# [hyde](https://hyde.github.com/)

Hyde claims to have started as Jekyll's evil Python twin. On the
surface it looks awesome. Where it fails is documentation. There are
lots of wonderful features that appear to exist, but follow the links to
those features and you find yourself on placeholder pages.

In theory, I could have just looked at the hyde code and figured out
stuff myself. Maybe even document out the holes.

In practice, all I want to do is write blog posts. It's one thing to
customize things to suit your needs, it's another thing to make things
work. Or document a tool. Color me lazy if you will, but when it comes
to blogging, that's just how I am.

I think in the near future, once fully documented, Hyde is going to be
AWESOME. For now? Well, I wanted another option.

# [pelican](https://docs.getpelican.com/en/stable/)

I was immediately hooked. Python powered engine with Jinja2 templates
with **complete documentation**. In fact, every time I asked the author
for help, he resignedly pointed me at the documentation. How cool is
that?

At some point I'll use the `CSS` setting to change the color of
`pygments` to something with white background and black text. For now
I'm happy as things are now.

[![image](/images/6831339872_10d0c40171.jpg)](https://www.flickr.com/photos/77704901@N05/6831339872/)

[Discuss this post on Hacker News]()
