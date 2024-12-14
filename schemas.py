from pydantic import BaseModel
from typing import Optional, List
import datetime

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    isbn: str
    available: Optional[bool] = True

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    membership_id: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class BorrowBase(BaseModel):
    user_id: int
    book_id: int
    due_date: datetime.datetime

class Borrow(BorrowBase):
    id: int

    class Config:
        orm_mode = True