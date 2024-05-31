#!/usr/bin/python3
""" a simple flask app """
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    get
    home function return string
    content-type is text
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    get
    return dict’s key
    content-type is application/json
    """
    keys = []
    for key in users.keys():
        keys.append(key)
    return jsonify(keys)


@app.route('/status')
def get_status():
    """
    get
    return ok
    content-type is text
    """
    return "OK"


@app.route('/users/<username>')
def get_username(username):
    """
    get
    return user info
    content-type is application/json
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """add user"""

    data = request.get_json()

    if not data or 'username' not in data or not data['username']:
        return jsonify({"message": "Missing or empty username"}), 400

    if any(field not in data or not data[field] for field in ['name', 'age', 'city']):
        return jsonify({"message": "Missing required field"}), 400

    username = data['username']
    if username in users:
        return jsonify({"message": "User already exists"}), 409

    users[username] = {
                'username': data["username"],
                'name': data['name'],
                'age': data['age'],
                'city': data['city']
            }
    return jsonify({
        'message': 'User added',
        'user': {
                'username': data["username"],
                'name': data['name'],
                'age': data['age'],
                'city': data['city']
            }
        }), 201


if __name__ == '__main__':
    app.run()