from fastapi import FastAPI, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal
from .services import book_lookup


app = FastAPI()


# APIリクエストごとにデータベースセッションを生成し、処理完了後に閉じるための依存関係
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}


@app.get("/api/lookup_book/{isbn}", response_model=schemas.BookCreate)
async def lookup_book_info(isbn: str):
    book_info = await book_lookup.lookup_book_info_by_isbn(isbn)
    if book_info is None:
        raise HTTPException(status_code=404, detail="Book not found in any external source")
    return book_info


@app.get("/api/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/api/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.put("/api/books/{book_id}", response_model=schemas.Book)
def update_book_endpoint(
    book_id: int, book_in: schemas.BookUpdate, db: Session = Depends(get_db)
):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db=db, db_book=db_book, book_in=book_in)


@app.delete("/api/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db=db, db_book=db_book)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/api/books/", response_model=schemas.Book, status_code=201)
def create_book_endpoint(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="ISBN already registered")
    return crud.create_book(db=db, book=book)
