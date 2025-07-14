
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/ui/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_items():
    with open("src/ui/templates/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
