from fastapi import FastAPI
from .controllers.books_controller import router as books_router

app = FastAPI(title="Books API")

app.include_router(books_router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Books API"}
