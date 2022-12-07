from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import HelloWorld
from api.users import User, Users
from api.books import *

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user/<user_id>')
api.add_resource(Users, '/users')
api.add_resource(Books, '/books')
api.add_resource(SearchBooksSingleTerm, '/books/<type>')
api.add_resource(SearchBooksMultipleTerms, '/books/<type>/<string>')

if __name__ == '__main__':
    app.run(debug=True)