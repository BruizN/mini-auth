from fastapi import Fastapi, HTTPException, Header
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
    raise HTTPException(status_code=400, detail='Invalid credentials')


@app.get('/profile')
def profile(authorization: str | None = Header(default=None)):
    if authorization == 'Bearer mock-token-123':
        return {'email': 'user@example.com', 'name': 'Ada Lovelace'}
     
    raise HTTPException(status_code=401, detail='Unauthorized')