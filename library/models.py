from datetime import datetime
from unicodedata import name
from sqlalchemy import (
    Column, Integer, String, 
    Date, DateTime, Text, Float , Boolean, 
    ForeignKey, null, null
)

from sqlalchemy.orm import relationship 
from .db import Base


class Author (Base):
    __tablename__ = 'authors'

    id = Column('id' ,Integer, primary_key=True)
    name = Column('name',String(100))
    bio = Column('bio', Text, nullable=False)

    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    books = relationship('Book', back_populates='author')

    def __str__(self):
        return f'Author(id={self.id}, name="{self.name}")'

    def __repr__(self):
        return f'Author(id={self.id}, name="{self.name}")'
    

class Book(Base):
    __tablename__ = 'books' 
    
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(200))
    author_id = Column('author_id', Integer, ForeignKey('authors.id'))
    published_year = Column('published_year', Integer)
    isbn = Column('isbn', String(13), unique=True)
    is_available = Column('is_available' , Boolean , default=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    author = relationship('Author', back_populates='books')
    borrows = relationship('Borrow', back_populates='book')

    def __str__(self):
        return f'Book(id={self.id}, title="{self.title}")'

    def __repr__(self):
        return f'Book(id={self.id}, title="{self.title}")'
    

class Student(Base):
    __tablename__ = 'students'
    id = Column('id', Integer, primary_key=True)
    full_name = Column('full_name', String(100))
    email = Column('email', String(100), unique=True)
    grade = Column('grade', String(10))
    registered_at = Column('registered_at', DateTime, default=datetime.now)

    borrows = relationship('Borrow', back_populates='student')

    def __str__(self):
        return f'Student(id={self.id}, name="{self.full_name} , email={self.email}, grade={self.grade}")'

    def __repr__(self):
        return f'Student(id={self.id}, name="{self.full_name} , email={self.email}, grade={self.grade}")'
    

class Borrow(Base):
    __tablename__ = 'borrows'
    
    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    book_id = Column('book_id', Integer, ForeignKey('books.id'))
    borrow_date = Column('borrow_date', DateTime, default=datetime.now)
    due_date = Column('due_date', DateTime)
    returned_at = Column('returned_at', DateTime, nullable=True)

    student = relationship('Student', back_populates='borrows')
    book = relationship('Book', back_populates='borrows')
    
    def __str__(self):
        return f'Borrow(id={self.id}, student_id={self.student_id}, book_id={self.book_id})'

    def __repr__(self):
        return f'Borrow(id={self.id}, student_id={self.student_id}, book_id={self.book_id})'
    