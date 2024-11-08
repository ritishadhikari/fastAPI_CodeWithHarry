from fastapi import APIRouter
from models.note import Note  # Contains the Models Structure (Pydantic defined)
from config.db import conn  # Contains the connection
from schemas.note import noteEntity,notesEntity  # Contains the converted entities. Clarification Needed
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


note=APIRouter()

# Getting the templates directory
templates=Jinja2Templates(directory="templates")

@note.get(path="/",response_class=HTMLResponse)
async def readItem(request:Request):
    newDocs=[]
    docs=conn.notes.notes.find(filter={})
    for doc in docs:
        newDocs.append(
            {
                "id":doc.get("_id"),
                "title":doc.get("title"),
                "desc":doc.get("desc"),
                "important":doc.get("important")
            }
        )

    return templates.TemplateResponse(
        request=Request,
        name="index.html",  # fetch index.html file
        context={"request":request,
                 "newDocs":newDocs},
        ) 


@note.post(path="/")
async def createItem(request:Request):
    form=await request.form()
    formDict=dict(form)
    print(formDict)
    formDict['important']=True if formDict.get('important')=="on" else False 
    conn.notes.notes.insert_one(document=formDict)
    return {"Success":True}

# @note.post(path="/",response_class=HTMLResponse)
# async def addNote(document:Note):
#     insertedNote=conn.notes.notes.insert_one(document=dict(document))
#     return noteEntity(item=insertedNote)