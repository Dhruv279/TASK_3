from sqlalchemy.orm import Session
import models, schemas

# Book CRUD

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

# User CRUD

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

# Borrow CRUD

def borrow_book(db: Session, borrow: schemas.BorrowBase):
    db_book = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()
    if not db_book or not db_book.available:
        raise Exception("Book is not available")
    
    db_borrow = models.Borrow(**borrow.dict())
    db_book.available = False
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def return_book(db: Session, borrow_id: int):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.id == borrow_id).first()
    if db_borrow:
        db_book = db.query(models.Book).filter(models.Book.id == db_borrow.book_id).first()
        if db_book:
            db_book.available = True
        db.delete(db_borrow)
        db.commit()
    return db_borrow