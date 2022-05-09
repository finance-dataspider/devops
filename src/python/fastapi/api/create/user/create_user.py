from fastapi import FastAPI
import pymongo

app = FastAPI()

@app.post("/v1/create/user")
async def api_v1_users():
    return {"message": "Hello World"}