
from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import notesEntity,noteEntity


note=APIRouter()
templates = Jinja2Templates(directory="templates")



@note.route("/", methods=['GET'])
async def root(request: Request):
    docs=conn.FastAPI.test.find({})
    newDoc=[]
    for doc in docs:
        print(doc)
        newDoc.append({
            "id":doc['_id'],
            "title":doc['title'],
            "desc":doc['desc'] 
        })
    return templates.TemplateResponse("index.html",{'request':request, "docs":newDoc})

@note.post("/")
async def insert(request:Request):
    form=await request.form()
    note= conn.FastAPI.test.insert_one(dict(form))
    return {"sucess":True}

@note.route("/edit",methods=['GET','POST'])
async def edit(req: Request):
    doc = conn.FastAPI.test.find_one({'_id': '660989ab663c739222d5d214'})
    print(doc)
    if not doc:
        return {"doc":False}
    form_data = await req.form()
    updated_values = {"title":doc["title"] or "title", "desc":doc["desc"] or "desc"} 

    conn.FastAPI.test.update_one({'_id': id}, {'$set': updated_values})

    return templates.TemplateResponse("edit.html", {"doc": doc, "form_data": form_data})


