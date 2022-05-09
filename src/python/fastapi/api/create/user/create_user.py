from fastapi import FastAPI
import pymongo

app = FastAPI()

@app.get("/v1/create/user")
async def api_v1_create_user():
    return {"message": "Hello World"}