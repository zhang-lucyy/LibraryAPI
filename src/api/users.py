from flask_restful import Resource, reqparse, request
from db import library

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