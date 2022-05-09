from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/create/user")
async def create_user():
    return {"message": "Hello World"}