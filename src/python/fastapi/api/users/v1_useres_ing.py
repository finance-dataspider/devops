from fastapi import FastAPI

app = FastAPI()

@app.get("/v1")
async def api_v1_users():
    return {"message": "Hello World"}