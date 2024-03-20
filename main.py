

from fastapi import FastAPI,BackgroundTasks, Request
from chartink import trasferDataToGoogleSheet
from datetime import datetime, timedelta
import asyncio
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Fetch data in the startup context
#     trasferDataToGoogleSheet()
#     yield
#     # No need to explicitly close resources here
# app = FastAPI(lifespan=lifespan)

# @app.get("/")
# async def root(lifespan):
#     print("Hello")
#     return {"message": "started"}

# Mount the static directory containing your CSS and image files

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
@app.get('/')
async def st():

    return {"Message" : "Hello"}

@app.get('/start')
async def start():
    try:
        trasferDataToGoogleSheet()
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'Market is close'}
    



