from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app=FastAPI()

# Mounting Static Folder
app.mount(path="/static",
          app=StaticFiles(directory="static"),
          name="static")

# Getting the templates directory
templates=Jinja2Templates(directory="templates")

# Setting up Mongoclient
conn=MongoClient(host="mongodb+srv://ritishadhikari:ritishadhikari@ritishcluster.dhltw.mongodb.net/")


# @app.get(path="/")
# def readRoot():
#     return {"Hello":"World"}

@app.get(path="/",response_class=HTMLResponse)
async def readItem(request:Request):
    newDocs=[]
    docs=conn.notes.notes.find(filter={})
    for doc in docs:
        newDocs.append(
            {
                "id":doc.get("_id"),
                "note":doc.get("note")
            }
        )

    return templates.TemplateResponse(
        request=Request,
        name="index.html",  # fetch index.html file
        context={"request":request,
                 "newDocs":newDocs},
        )   


@app.get(path="/items/{itemId}")
def readItem(itemId:int,q:str|None=None):
    return {"itemId":itemId,"q":q}