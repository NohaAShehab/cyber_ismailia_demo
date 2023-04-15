"""
 insert , update , delete
books

booktitle, no_of_pages ---> save data to a file -->

"""
import time
from fileoperations import save_book_to_file, get_all_books_from_file,\
    search_about_book, delete_book_from_file

def generate_id():
    return round(time.time())
def create_book():
    name=input("please enter name: ")
    no_of_pages = input("please enter no of pages ")
    print(name, no_of_pages)
    id = generate_id()
    book_details = f"{id}:{name}:{no_of_pages}\n"
    saved = save_book_to_file(book_details)
    if saved:
        print('--- book saved successfully')


def list_all_books():
    books = get_all_books_from_file()
    for book in books:
        print(book)

def delete_book():
    print("please choose the id of the book you want to delete ")
    list_all_books()
    book_id = input("please enter book_id")
    print(book_id)
    ## check if book_id --> exists
    book_index = search_about_book(book_id)
    if book_index != None:
        delete_book_from_file(book_index)
    else:
        print("--- please try again with valid book id ")


    ## if exits --> delete, update

def mainmenu():
    while True:
        choice = input("please enter c for create , l for list all:, d for delete ,e for exit")
        if choice=='c':
            create_book()
        elif choice=='l':
            list_all_books()
        elif choice=='d':
            delete_book()
        elif choice=='e':
            return

mainmenu()