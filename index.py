from fastapi import FastAPI
from routes.note import (APIRouter,Note,
                         note  # To be created soon 
                         )  
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.include_router(router=note)