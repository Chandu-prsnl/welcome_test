from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Welcome API")

class WelcomeRequest(BaseModel):
    name: str

@app.post("/api/v1/welcome")
def welcome(payload: WelcomeRequest):
    return {
        "message": f"Welcome, {payload.name}!"
    }
