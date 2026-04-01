#James (Backend)
from fastapi import FastAPI
from app.routes import campaign

app = FastAPI()

app.include_router(campaign.router)

@app.get("/")
def home():
    return {"message": "Corporate Marketing API Running"}

@app.get("/health")
def health():
    return {"status":"ok"}