#James (Backend)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Corporate Marketing API Running"}