

from fastapi import FastAPI,BackgroundTasks, Request
from chartink import trasferDataToGoogleSheet
from datetime import datetime, timedelta
import asyncio
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from btsc import firstRun,secondRun,btstgsclean



app = FastAPI()
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

@app.get('/clean')
def clean():
    try:
        btstgsclean()
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'Clean up completed'}

@app.get('/first')
async def firstup():
    try:
        firstRun()
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'First run completed'}

@app.get('/second')
async def secondup():
    try:
        secondRun()
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'Second Run'}
    


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=4)



