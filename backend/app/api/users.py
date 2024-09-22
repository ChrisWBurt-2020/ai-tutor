from flask import request, jsonify
from app.models import User
from app import db
from app.api import bp

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if username is None or username == '':
        return jsonify({'error': 'Username is required'}), 400
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'User {username} created successfully.'}), 201
