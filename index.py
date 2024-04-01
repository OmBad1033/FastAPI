from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from routes.route import product

app=FastAPI()
app.include_router(product)


