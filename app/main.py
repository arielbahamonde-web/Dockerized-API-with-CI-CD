from fastapi import FastAPI
from app.routes.users import router as users_router

app = FastAPI()

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}