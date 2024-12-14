from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from typing import List

# Initialize database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Book Endpoints
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

# User Endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Borrow Endpoints
@app.post("/borrow/", response_model=schemas.Borrow)
def borrow_book(borrow: schemas.BorrowBase, db: Session = Depends(get_db)):
    try:
        return crud.borrow_book(db, borrow)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/borrow/{borrow_id}/", response_model=schemas.Borrow)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    db_borrow = crud.return_book(db, borrow_id)
    if not db_borrow:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    return db_borrow