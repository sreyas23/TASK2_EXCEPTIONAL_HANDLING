from typing import List, Optional
from ..models.book_models import Book, BookCreate, BookDetails

_DB: List[Book] = [
    Book(id=1, title="Atomic Habits", author="James Clear", year=2018),
    Book(id=2, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=3, title="The Alchemist", author="Paulo Coelho", year=1988),
]

def get_all_books() -> List[Book]:
    return _DB

def _next_id() -> int:
    return max((b.id for b in _DB), default=0) + 1

def create_book(payload: BookCreate) -> Book:
    if any(b.title == payload.title and b.author == payload.author and b.year == payload.year for b in _DB):
        raise ValueError("book already exists")
    book = Book(id=_next_id(), **payload.dict())
    _DB.append(book)
    return book

def get_book_details(payload: BookCreate) -> BookDetails:
    b: Optional[Book] = next(
        (book for book in _DB
         if book.title == payload.title and book.author == payload.author and book.year == payload.year),
        None
    )
    base = b or Book(id=0, **payload.dict())
    summary = f"'{base.title}' by {base.author}, published in {base.year}, is a popular book loved by readers."
    return BookDetails(title=base.title, author=base.author, year=base.year, summary=summary)
