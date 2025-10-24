from fastapi import Fastapi

app = Fastapi()

@app.get("/health")
def health():
    return {"ok": True}