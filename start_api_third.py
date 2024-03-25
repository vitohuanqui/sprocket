
from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
async def read_root():
    return {
        "production": 25,
        "goal": 32
    }
