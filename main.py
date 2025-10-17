from fastapi import FastAPI
from routers import contact

app = FastAPI()

# @app.get("/")
# async def read_hello():
    # return {"response":"Hello! World!"}

app.include_router(contact.router)