from starlette.responses import Response
from datetime import datetime
from fastcore.utils import *
from dataclasses import dataclass, asdict


def todict(req): return {k:str(v) for k,v in req.items()}


app = FastHTML()
rt = app.route

@app.get("/")
def _(req): return todict(req.scope)


cli = TestClient(app)
r = cli.get('/')
print(r.text)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))