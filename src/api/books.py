from flask_restful import Resource
from db import library, swen344_db_utils

class Books(Resource):
    def print_books(books):
        final = {}
        book_dict = {}
        temp_dict = {}

        for book in books:
            id = book[0]
            title = book[1]
            book_type = book[2]
            author = book[3]
            publish_date = book[4]
            summary = book[5]
            copies = book[6]
            libraries = library.get_libraries_with_book(id)

            temp_dict = {'title': title, 'type': book_type, 'author': author,
                'publish date': publish_date, 'summary': summary, 'copies': copies,
                'available at': libraries}
            book_dict = {id: temp_dict}

            final.update(book_dict)
        
        return final

    def get(self):
        books = library.get_all_books()
        output = Books.print_books(books)
        return output

class SearchFictionBooks(Resource):
    def get(self):
        books = library.get_fiction_books()
        output = Books.print_books(books)
        return output

class SearchNonfictionBooks(Resource):
    def get(self):
        books = library.get_nonfiction_books()
        output = Books.print_books(books)
        return output
