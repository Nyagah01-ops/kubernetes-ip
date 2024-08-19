from flask import Blueprint, jsonify
from app.models.user import User

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = [User('John Doe', 'john@example.com'), User('Jane Doe', 'jane@example.com')]
    return jsonify([user.__dict__ for user in users])
