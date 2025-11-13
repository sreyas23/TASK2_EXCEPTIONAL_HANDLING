from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookDetails(BaseModel):
    title: str
    author: str
    year: int
    summary: str
