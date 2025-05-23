from app.models import users_services

from flask import Blueprint, request, jsonify, session
from sqlalchemy.exc import IntegrityError

users_router = Blueprint('users', __name__)

@users_router.get('/users')
def get_users():
    return jsonify(users_services.list_users())

@users_router.post('/users')
def add_user():
    if request.headers.get('Content-Type') != 'application/json':
        return {
            'status': 'error',
            'message': 'Need a json body'
        }
    
    if 'name' in request.json and 'password' in request.json and 'age' in request.json:
        return users_services.create_user(request.json['name'], request.json['password'], request.json['age'])
    
    return {
      'status': 'error',
      'message': 'Not enough or incorrect data'
    }

@users_router.get('/users/<int:id>')
def get_user(id):
    user = users_services.get_user(id)

    if not user:
        return {
            'status': 'error',
            'message': 'Invalid user id'
        }
    
    return user

@users_router.patch('/users/<int:id>')
def update_user(id):
    if request.headers.get('Content-Type') != 'application/json':
        return {
            'status': 'error',
            'message': 'Need a json body'
        }
    
    user = users_services.get_user(id)
    changes = 0

    if 'name' in request.json:
        user['name'] = request.json['name']
        changes += 1

    if 'password' in request.json:
        user['password'] = request.json['password']
        changes += 1

    if 'info' in request.json:
        user['info'] = request.json['info']
        changes += 1

    if changes > 0:
      return users_services.update_user(user)

    return {
      'status': 'error',
      'message': 'No parameters specified'
    }

@users_router.delete('/users/<int:id>')
def delete_user(id):
    deleted_user = users_services.delete_user(id)

    if not deleted_user:
        return {
            'status': 'error',
            'message': 'Invalid user id'
        }
    
    return deleted_user
