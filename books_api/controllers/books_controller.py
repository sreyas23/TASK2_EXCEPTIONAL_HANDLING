from typing import List
from fastapi import APIRouter, HTTPException
from ..models.book_models import Book, BookCreate, BookDetails
from ..services.books_service import get_all_books, create_book, get_book_details

router = APIRouter()

@router.get("/books", response_model=List[Book])
def list_books():
    try:
        return get_all_books()
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching books")

@router.post("/books", response_model=Book, status_code=201)
def add_book(payload: BookCreate):

    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")
    if not payload.author or not payload.author.strip():
        raise HTTPException(status_code=400, detail="Author is required")
    if payload.year is None:
        raise HTTPException(status_code=400, detail="Year is required")

    try:
        return create_book(payload)
    except ValueError as ve:                  
        raise HTTPException(status_code=409, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Error creating book")

@router.post("/books/details", response_model=BookDetails)
def details(payload: BookCreate):
    # same simple checks
    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")
    if not payload.author or not payload.author.strip():
        raise HTTPException(status_code=400, detail="Author is required")

    try:
        return get_book_details(payload)
    except Exception:
        raise HTTPException(status_code=500, detail="Error getting book details")
