


def save_book_to_file(filedata):
    try:
        fileobj= open('books.txt','a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(filedata)
        fileobj.close()
        return True



def get_all_books_from_file():
    try:
        fileobj= open('books.txt','r')
    except Exception as e:
        print(e)
        return False
    else:
       lines = fileobj.readlines()
       return lines



def search_about_book(book_id):
    books = get_all_books_from_file()

    for index in range(len(books)):
        book = books[index]
        book_details = book.split(":")
        # print(book_details)
        if str(book_id)==book_details[0]:
            print("book found ")
            return index
    else:
        return None


def save_all_books(books):
    try:
        fileobj = open('books.txt', 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(books)
        fileobj.close()
        return True


def delete_book_from_file(book_index):
    ## delete book from the list
    books = get_all_books_from_file()
    del books[book_index]
    ## save list again to the file
    res=save_all_books(books)
    return res
