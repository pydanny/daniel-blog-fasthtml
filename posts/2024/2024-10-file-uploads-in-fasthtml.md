---
date: '2024-10-11T10:20:33.471691'
description: A reference for handling single and multiple file uploads in FastHTML. 
published: false
tags:
- python
- FastHTML
- howto
title: File uploads in FastHTML
---

A reference for handling single and multiple file uploads in FastHTML.

The docs already contain instructions for single file uploads, this adds in multiple file uploads.


```python
# uploads_demo.py

# PyPI dependency is "python-fasthtml"
from fasthtml.common import *
from pathlib import Path

app, rt = fast_app()

upload_dir = Path("filez")
upload_dir.mkdir(exist_ok=True)

@rt('/')
def get():
    return Titled("File Upload Demo",
        Div(cls='grid')(
            Article(
                Header(H2('Choose a single file')),
                Form(
                    Input(
                        type="file",
                        name="file"),
                    Button("Upload",
                        type="submit",
                        cls='secondary'),
                    hx_post="/upload-single", 
                    hx_target="#result-one"                        
                ),
                Div(id="result-one")
            ),
            Article(
                Header(H2('Choose multiple files')),
                Form(
                    Input(
                        type="file",
                        name="files",
                        multiple=True),
                    Button("Upload",
                        type="submit",
                        cls='contrast'),
                    hx_post="/upload-multiple",
                    hx_target="#result-multiple"            
                ),
                Div(id="result-multiple")
            )            
        )
    )

def FileMetaDataCard(file):
    return Article(
        Header(H3(file.filename)),
        Ul(
            Li('Size: ', file.size),            
            Li('Content Type: ', file.content_type),
            Li('Headers: ', file.headers),
        )
    )    

@rt('/upload-single')
async def post(file: UploadFile):
    card = FileMetaDataCard(file)
    filebuffer = await file.read()
    (upload_dir / file.filename).write_bytes(filebuffer)
    return card

@rt('/upload-multiple')
async def post(files: list[UploadFile]):
    # To account for this bug:
    #   https://github.com/AnswerDotAI/fasthtml/issues/513
    try: iter(files)
    except TypeError: files = [files]

    # All that this view handler should contain
    cards = []
    for file in files:
        filebuffer = await file.read()
        (upload_dir / file.filename).write_bytes(filebuffer)
        cards.append(FileMetaDataCard(file))
    return cards    

serve()
```