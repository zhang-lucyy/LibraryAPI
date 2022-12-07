import json
from flask_restful import Resource, reqparse, request
from db import library

class User(Resource):
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
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str)
        parser.add_argument('contact_info', type = str)
        args = parser.parse_args()

        name = args['name']
        contact = args['contact_info']

        library.create_account(name, contact)

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type = int)
        parser.add_argument('contact_info', type = str)
        args = parser.parse_args()

        user_id = args['user_id']
        contact = args['contact_info']

        library.edit_account(user_id, contact)

    def delete(self):
        name = request.args.get('name')
        library.delete_account(name)

class Users(Resource):
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