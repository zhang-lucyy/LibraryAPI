import json
import hashlib
import string
from flask_restful import Resource, reqparse, request
from db import library

class Login(Resource):
    '''
    Login method.
    '''
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type = str)
        parser.add_argument('password', type = str)
        args = parser.parse_args()

        username = args['username']
        password = args['password']

        hashed = hashlib.sha512(string.encode(password)).hexdigest()

        if (library.login(username, hashed).__len__() == 2):
            message, key = library.login(username, hashed)
            return message, key

        else:
            message = library.login(username, hashed)
            return message

class User(Resource):
    '''
    Gets user's checkouts.
    '''
    def get(self, user_id):
        final = {}
        checkout_list = {}
        temp_dict = {}

        checkouts = library.get_user_books(user_id)

        for book in checkouts:
            book_id = book[0]
            title = book[1]
            author = book[2]
            library_name = book[3]
            checkout_date = json.dumps(book[4], default=str)
            due_date = json.dumps(book[5], default=str)
            return_date = json.dumps(book[6], default=str)

            temp_dict = {'title': title, 'author': author, 'checked out at': library_name,
                'checked out': checkout_date, 'due date': due_date, 'returned': return_date}
            checkout_list = {book_id: temp_dict}

            final.update(checkout_list)

        return final
    
    '''
    Creates a new account given name and contact info.
    '''
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str)
        parser.add_argument('contact_info', type = str)
        parser.add_argument('username', type = str)
        parser.add_argument('password', type = str)

        args = parser.parse_args()

        name = args['name']
        contact = args['contact_info']
        username = args['username']
        password = args['password']

        message = library.create_account(name, contact, username, password)
        return message

    '''
    Updates user info.
    '''
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type = int)
        parser.add_argument('contact_info', type = str)
        args = parser.parse_args()

        username = args['username']
        contact = args['contact_info']
        key = request.headers['session']

        message = library.edit_account(username, contact, key)
        return message

    '''
    Deletes the account.
    '''
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add.argument('username', type = str)
        args = parser.parse.args()

        username = args['username']
        key = request.headers['session']

        message = library.delete_account(username, key)
        return message
        
class Checkout(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add.argument('library_id', type = int)
        parser.add.argument('title', type = str)
        parser.add.argument('username', type = int)
        parser.add.argument('checkout_date', type = str)
        args = parser.parse.args()

        library_id = args['library_id']
        title = args['title']
        username = args['username']
        checkout_date = args['checkout_date']
        key = request.headers['session']

        message = library.checkout_book(library_id, title, username, key, checkout_date)
        return message

class Users(Resource):
    '''
    Lists all users.
    '''
    def get(self):
        users = library.get_all_users()

        final = {}
        user_dict = {}
        temp_dict = {}

        for user in users:
            id = user[0]
            name = user[1]
            contact = user[2]

            temp_dict = {'name': name, 'contact': contact}
            user_dict = {id: temp_dict}

            final.update(user_dict)

        return final