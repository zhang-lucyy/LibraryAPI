from urllib.parse import parse_qs, urlparse
from flask_restful import Resource
from db import library, swen344_db_utils

class Books(Resource):
    '''
    Helper method that returns the passed in books in a neat format.
    '''
    def format_books(books):
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
        output = Books.format_books(books)
        return output

class SearchBooksSingleTerm(Resource):
    def get(self, type):
        if (type == 'fiction'):
            books = library.get_fiction_books()
            output = Books.format_books(books)
            return output

        elif (type == 'non-fiction'):
            books = library.get_nonfiction_books()
            output = Books.format_books(books)
            return output

        else:
            if (library.search_by_title(type).__len__() != 0):
                books = library.search_by_title(type)
                output = Books.format_books(books)
                return output
            elif (library.search_by_author(type).__len__() != 0):
                books = library.search_by_author(type)
                output = Books.format_books(books)
                return output
            else:
                output = []
                return output

class SearchBooksMultipleTerms(Resource):
    def get(self, type, string):
        books = library.search_by_multiple_terms(type, string)
        if (books.__len__() != 0):
            output = Books.format_books(books)
            return output

        else:
            output = []
            return output