
from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from models.Product import Product
from config.db import conn
from schemas.schema import productsEntity,productEntity
from typing import List

product=APIRouter()

@product.get("/",response_model=Product)
async def root(request: Request,):
    docs_cursor = conn.FastAPI.test.find({})
    

    return productsEntity(docs_cursor)








