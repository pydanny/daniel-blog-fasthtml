---
date: '2025-03-21T19:45:39.845420'
description: Quick instructions for a drop-in FastHTML middleware for identifying performance bottlenecks in FastHTML apps
published: true
tags:
- python
- fasthtml
title: Using pyinstrument to profile FastHTML apps
---

FastHTML is built on Starlette, so we use Starlette's middleware tooling and then pass in the result. Just make sure you install pyinstrument. 

**WARNING: NOT FOR PRODUCTION ENVIRONMENTS** Including a profiler like this in a production environment is dangerous. As it exposes infrastructure it is highly risky to include in any location where end users can access it.

```python
"""WARNING: NOT FOR PRODUCTION ENVIRONMENTS"""
from fasthtml.common import *
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import Middleware
try:
    from pyinstrument import Profiler
except ImportError:
    raise ImportError('Please install pyinstrument')

class ProfileMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        profiling = request.query_params.get("profile", False)
        if profiling:
            profiler = Profiler()
            profiler.start()
            response = await call_next(request)            
            profiler.stop()        
            return HTMLResponse(profiler.output_html())
        return await call_next(request)

app, rt = fast_app(middleware=(Middleware(ProfileMiddleware)))

@rt("/")
def get():
    return Titled("FastHTML", P("Hello, world!"))

serve()
```

To invoke, make any request to your application with the GET parameter
`profile=1` and it will print the HTML result from pyinstrument.