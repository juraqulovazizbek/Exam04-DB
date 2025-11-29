from datetime import date
from library.create_tables import init_db
from library.services import (
    create_author,
    get_author_by_id,
    get_all_authors,
    update_author,
    delete_author,
    create_book,
    get_book_by_id,
    get_all_books,
    search_books_by_title,
    delete_book,
    create_student,
    get_student_by_id,
    get_all_students,
    update_student_grade,
    borrow_book,    
    return_book
)    

init_db()


# Mualliflar yaratish
# create_author(name="xexa xexu", bio="exaxa uxaxaxaxaxa")
# print('Muallif yaratildi.')


# # ID bo'yicha muallifni olish
# author = get_author_by_id(author_id=1)
# print(author)


# Barcha mualliflarni olish
# authors = get_all_authors()
# for author in authors:
#     print(author)


# # Muallif ma'lumotlarini yangilash
# update_author(4, name='nimadir')
# print(get_author_by_id(4))



# Muallifni o'chirish
# success = delete_author(author_id=)
# if success:
#     print("Muallif o'chirildi.")


# Yangi kitob yaratish
create_book(title="xamsa ", author_id=1, published_year=2020, isbn="1234563870122")
print("Kitob yaratildi.")

# ID bo'yicha kitobni olish
# print(get_book_by_id(4))


# Barcha kitoblar ro'yxatini olish
# books = get_all_books()
# for book in books:
#     print(book)


# # Kitoblarni sarlavha bo'yicha qidirish (partial match)
# searched_books = search_books_by_title(title="Kitob")   
# for book in searched_books:
#     print(book)


# # Kitobni o'chirish
# success = delete_book(book_id=4)
# if success:
#     print("Kitob o'chirildi.")
# else:
#     print("Kitobni o'chirish mumkin emas.")


 #Yangi talaba yaratish
# create_student(full_name="ask", email="Ask@example.com" , grade='l')
# print("Talaba yaratildi.")


# ID bo'yicha talabani olish
# student = get_student_by_id(student_id=2)
# print(student)


# # Barcha talabalar ro'yxatini olish
# students = get_all_students()
# for student in students:
#     print(student)


# # update_student_grade(1, 'a')

# Talaba kitobni oldi
# borrowed = borrow_book(student_id=1, book_id=7)
# print("Berildi:", borrowed)

# # Keyin kitobni qaytaring
# success = return_book(borrow_id=borrowed.id)
# if success:
#     print("Kitob qaytarildi")
# else:
#     print("Qaytarib bo'lmadi")
