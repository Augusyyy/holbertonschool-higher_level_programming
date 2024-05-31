#!/usr/bin/python3
""" A simple Flask app with OpenAPI documentation """
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

ns = api.namespace('users', description='User operations')

users = {}

user_model = api.model('User', {
    'username': fields.String(required=True, description='The user unique identifier'),
    'name': fields.String(required=True, description='The user name'),
    'age': fields.Integer(required=True, description='The user age'),
    'city': fields.String(required=True, description='The user city'),
})


@ns.route('/')
class Home(Resource):
    @api.doc('home')
    def get(self):
        """Home function return string, content-type is text"""
        return "Welcome to the Flask API!"


@ns.route('/data')
class Data(Resource):
    @api.doc('get_data')
    def get(self):
        """Return dict's keys, content-type is application/json"""
        keys = list(users.keys())
        return keys


@ns.route('/status')
class Status(Resource):
    @api.doc('get_status')
    def get(self):
        """Return OK, content-type is text"""
        return "OK"


@ns.route('/<username>')
@api.response(404, 'User not found')
@api.param('username', 'The user identifier')
class User(Resource):
    @api.doc('get_username')
    def get(self, username):
        """Return user info, content-type is application/json"""
        if username in users:
            return users[username]
        else:
            return {'error': 'User not found'}, 404


@ns.route('/')
class AddUser(Resource):
    @api.doc('add_user')
    @api.expect(user_model)
    @api.response(201, 'User added')
    @api.response(400, 'A duplicate username')
    @api.response(404, 'Without a username')
    def post(self):
        """Add a new user"""
        data = request.get_json()

        if 'username' not in data:
            return {'error': 'Without a username'}, 404

        username = data.get('username')
        if username in users:
            return {'error': 'A duplicate username'}, 400

        users[username] = {
            'username': data["username"],
            'name': data['name'],
            'age': data['age'],
            'city': data['city']
        }
        return {
            'message': 'User added',
            'user': users[username]
        }, 201


if __name__ == '__main__':
    app.run(debug=True)
