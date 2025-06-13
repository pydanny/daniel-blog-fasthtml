---
date: '2025-06-13T04:23:23.230032'
description: For those times when FastAPI is serving web pages and users go to the
  wrong place.
image: /public/logos/til-1.png
published: true
tags:
- python
- fastapi
- TIL
title: 'TIL: HTML 404 errors for FastHTML'
twitter_image: /public/logos/til-1.png
---


```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


async def custom_404_exception_handler(request, exc):
    return HTMLResponse(
        f'<p>404 Not Found at "{request.url.path}"</p>', status_code=404
    )

# Add more HTTP exceptions as needed
HTTP_EXCEPTIONS = {404: custom_404_exception_handler}

app = FastAPI(exception_handlers=HTTP_EXCEPTIONS)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

```

Try it out by running the app and going to a non-existent path, like `/not-found`. You should see a simple HTML page with a 404 message.