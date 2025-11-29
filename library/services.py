from datetime import datetime , timedelta
from library.models import Author, Book, Student, Borrow 
from library.db import get_db
from sqlalchemy.orm import Session


def create_author(name: str, bio: str = None) -> Author:
    author = Author(
        name = name,
        bio=bio
    )
    
    with get_db() as session:
        session.add(author)
        session.commit()

def get_author_by_id(author_id: int) -> Author | None:
    with get_db() as session:
        author = session.query(Author).filter(Author.id == author_id).first()
        return author
    
def get_all_authors() -> list[Author]:
    with get_db() as session:
        authors = session.query(Author).all()
    
    return authors

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    author_id: int | None = None,
    name: str | None = None, 
    bio: str | None = None
    author = get_author_by_id(author_id)

    if author:
        with get_db() as session:
            author.name = name if name else author.name
            author.bio = bio if bio else author.bio

            session.add(author)
            session.commit()

def delete_author(author_id: int) -> bool:
    author = get_author_by_id(author_id)

    if author:
        with get_db() as session:
            session.delete(author)
            session.commit() # commit bu daqat insert sellect update da ishlatiladi lkn kurishda tekshirishda yo'q faqat nmadir uzgarsa gina 

def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book | None:
    """Yangi kitob yaratish"""
    import random
    from library.models import Book, Author
    from library.db import get_db

    if isbn is None:
        isbn = str(random.randint(1000000000000, 9999999999999))  # Random ISBN codimiz error bermasligi  uchun yaratildi

    with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            return None  # Author topilmasa, kitob yaratilmaydi va None qaytadi

        book = Book(
            title=title,
            author_id=author_id,
            published_year=published_year,
            isbn=isbn
        )
        session.add(book)
        session.commit()

    return book

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    with get_db() as session:
        return session.query(Book).filter(Book.id==book_id).first()
    
def get_all_books() -> list[Book]:
    with get_db() as session:
        books = session.query(Book).all()
    
    return books

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni nomi bo'yicha qidirish"""
    with get_db() as session:
        books = session.query(Book).filter(Book.title.ilike(f'%{title}%')).all()
        return books
    
def delete_book(book_id: int) -> bool:
    book = get_book_by_id(book_id)

    if book:
        with get_db() as session:
            session.delete(book)
            session.commit()
        return True
    return False

def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    student = Student(
        full_name=full_name,
        email=email,
        grade=grade
    )
    with get_db() as session:
        session.add(student)
        session.commit()
    
    return student
def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    with get_db() as session:
        student = session.query(Student).filter(Student.id == student_id).first()
        return student
    
def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    with get_db() as session:
        students = session.query(Student).all()
    
    return students
def update_student_grade(student_id: int, grade: str) -> Student | None:
    """Talaba sinfini yangilash"""
    student = get_student_by_id(student_id)

    if student:
        with get_db() as session:
            student.grade = grade if grade else student.grade

            session.add(student)
            session.commit()

from datetime import date, timedelta

def borrow_book(student_id: int, book_id: int) -> Borrow | None:
    with get_db() as session:
        student = get_student_by_id(student_id)
        book = get_book_by_id(book_id)
        
        if not student or not book or not book.is_available:
            return None
        
        # Talabada 3 tadan ortiq qaytarilmagan kitob yo'qligini tekshirish
        active_borrows = session.query(Borrow).filter_by(student_id=student_id, returned_at=None).count()
        if active_borrows >= 3:
            return None
        
        due_date = date.today() + timedelta(days=14)
        borrow = Borrow(
            student_id=student_id,
            book_id=book_id,
            due_date=due_date
        )
        session.add(borrow)
        book.is_available = False
        session.commit()
        session.refresh(borrow)
        return borrow

def return_book(borrow_id: int) -> bool:
    """Kitobni qaytarish"""
    with get_db() as session:
        borrow = session.query(Borrow).filter_by(id=borrow_id).first()
        if not borrow or borrow.returned_at is not None:
            # Qaytarilgan yoki mavjud bo'lmagan borrow
            return False
        
        borrow.returned_at = datetime.now()  # Qaytarilgan vaqt
        borrow.book.is_available = True      # Kitobni mavjud qilish
        session.commit()
        return True