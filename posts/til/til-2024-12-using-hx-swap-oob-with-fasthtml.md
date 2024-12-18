---
date: '2024-12-18T17:04:06.575404'
description: How to have the injected content know where to go instead of assigning
  it from the form.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- python
- FastHTML
title: 'TIL: Using hx-swap-oob with FastHTML'
twitter_image: /public/logos/til-1.png
---

Until now I didn't use this HTMX technique, but today Audrey Roy Greenfeld and I dove in together to figure it out. Note that we use language that may not match HTMX's description, sometimes it's better to put things into our own words so we understand it better.

```python
from fasthtml.common import *

app,rt = fast_app()

def mk_row(name, email):
    return Tbody(
        # Only the Tr element and its children is being
        # injected, the Tbody isn't being injected
        Tr(Td(name), Td(email)),
        # This tells HTMX to inject this row at the end of
        # the #contacts-tbody DOM element
        hx_swap_oob="beforeend:#contacts-tbody",
    ),

@rt
def index():
    return Div(
            H2("Contacts"),
            Table(
                Thead(Tr(Th("Name"), Th("Email"))),
                Tbody(
                    Tr(Td("Audrey"), Td("mommy@example.com")),
                    Tr(Td("Uma"), Td("kid@example.com")),
                    Tr(Td("Daniel"), Td("daddy@example.com")),
                    # Identifies the contacts-tbody DOM element
                    id="contacts-tbody",
                ), 
            ),
            H2("Add a Contact"),
            Form(
                Label("Name", Input(name="name", type="text")),
                Label("Email", Input(name="email", type="email")),
                Button("Save"),
                hx_post="/contacts",
                # Don't swap out the contact form
                hx_swap='none',
                # Reset the form and put the focus onto the name field
                hx_on__after_request="this.reset();this.name.focus();"
            )
        )

@rt
def contacts(name:str,email:str):
    print(f"Adding {name} and {email} to table")
    return mk_row(name,email)

serve()
```

To verify the behavior, view the rendered elements in your browser of choice before, after, and during submitting the form.