from flask_restful import Resource
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