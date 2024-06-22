from fasthtml.common import *
import uvicorn

# app = FastHTML()
app = FastHTMLWithLiveReload()
rt = app.route

@rt("/")
def get():
  return Title("FastHTML"), H1("Hello World!")

@app.get('/user/{nm}')
def get_nm(nm:str): return f"Good day to you, {nm}!"

@app.get('/html/{idx}')
async def _(idx:int):
    return Body(
        H4("Wow look here"),
        P(f'It looks like you are visitor {idx}! Next is {idx+1}.')
    )

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))