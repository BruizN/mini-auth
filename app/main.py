from fastapi import Fastapi, HTTPException
from pydantic import BaseModel


app = Fastapi()

@app.get("/health")
def health():
    return {"ok": True}


class LoginIn(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(body: LoginIn):
    if body.email and body.password:
        return {"access_token": "mock-token-123"}
    HTTPException(status_code=400, detail='Invalid credentials')