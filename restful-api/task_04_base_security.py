#!/usr/bin/python3
"""
a simple  http.server for testing
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


# Basic Auth User Verification
@auth.verify_password
def verify_password(username, password):
    """verify_password"""
    if username in users and check_password_hash(users[username]['password'], password):
        return users[username]
    return None


# Basic Auth Protected Route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """basic_protected"""
    return jsonify(message="Basic Auth: Access Granted")


# JWT Auth Login Route
@app.route('/login', methods=['POST'])
def login():
    """login"""
    username = request.json.get("username")
    password = request.json.get("password")
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]['role']})
        return jsonify(access_token=access_token)
    return jsonify(error="Invalid credentials"), 401


# JWT Protected Route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """jwt_protected"""
    return jsonify(message="JWT Auth: Access Granted")


# Role-based Protected Route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """admin_only"""
    claims = get_jwt()
    if claims["role"] == "admin":
        return jsonify(message="Admin Access: Granted")
    return jsonify(error="Forbidden"), 403


# Custom JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """handle_unauthorized_error"""
    return jsonify(error="Missing or invalid token"), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """handle_invalid_token_error"""
    return jsonify(error="Invalid token"), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """handle_expired_token_error"""
    return jsonify(error="Token has expired"), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """handle_revoked_token_error"""
    return jsonify(error="Token has been revoked"), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """handle_needs_fresh_token_error"""
    return jsonify(error="Fresh token required"), 401


if __name__ == '__main__':
    app.run()
