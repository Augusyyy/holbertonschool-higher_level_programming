#!/usr/bin/python3
""" a simple flask app """
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

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
    if username in users.keys():
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
                'name': data['name'],
                'age': data['age'],
                'city': data['city']
            }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == '__main__':
    app.run()
