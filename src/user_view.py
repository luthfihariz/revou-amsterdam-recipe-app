from flask import Blueprint, request
from repository import user, token
from uuid import uuid4
from flasgger import swag_from

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

@user_blueprint.route("registration", methods=["POST"])
@swag_from("docs/user_registration.yml")
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return {"message": "username and password required"}, 400
    
    if username in user:
        return {"message": "user already exist!"}, 400
    
    user[username] = password
    return {"message": "user created!"}, 201


@user_blueprint.route("login", methods=["POST"])
@swag_from("docs/user_login.yml")
def login():    
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return {"message": "username and password required"}, 400
    
    if user.get(username) != password:
        return {"message": "invalid username or password"}, 400
    
    new_token = str(uuid4()) # abcdef-jkhsdkjf-123123-asdsd
    token[new_token] = username
    return {"message": "logged in boss!", "token": new_token}
