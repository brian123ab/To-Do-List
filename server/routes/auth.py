from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user
from ..models import db, login_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username - data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and Password expected"}), 400
    
    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 400

    login_user(user)
    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.user_id,
            "username": user.username,
            "email": user.email
        }
    })