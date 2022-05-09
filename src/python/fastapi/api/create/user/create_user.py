from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/create/user")
async def api_v1():
    return {"message": "Hello World"}