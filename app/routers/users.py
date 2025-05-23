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
    
    json = request.json
    name = json['name']
    password = json['password']
    age = json['age']

    user = users_services.create_user(name, password, age)
    return user
    

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
    
    json = request.json
    user = users_services.get_user(id)

    if 'name' in json:
        name = json['name']
        user = users_services.set_name(id, name)

    if 'password' in json:
        password = json['password']
        user = users_services.set_password(id, password)

    if 'info' in json:
        info = json['info']
        user = users_services.set_info(id, info)

    return user
    

@users_router.delete('/users/<int:id>')
def delete_user(id):
    deleted_user = users_services.delete_user(id)

    if not deleted_user:
        return {
            'status': 'error',
            'message': 'Invalid user id'
        }
    
    return deleted_user
