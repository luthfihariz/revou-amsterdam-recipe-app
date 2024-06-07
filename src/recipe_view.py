from flask import Blueprint, request
from flasgger import swag_from
from repository import recipes, token

recipe_blueprint = Blueprint("recipe", __name__, url_prefix="/recipe")

@recipe_blueprint.before_request
def authenticate():
    _token = request.headers.get("Authorization")
    if not _token:
        return {"message": "login required"}, 400
    
    username = token.get(_token)
    if not username:
        return {"message": "token is invalid!"}, 400
    
    request.username = username

@recipe_blueprint.route("/create", methods=["POST"])
@swag_from("docs/create_recipe.yml")
def create_recipe():
    recipe = request.json.get("recipe")
    if not recipe:
        return {"message": "Recipe required"}, 400

    username = request.username
    recipes.append({"username": username, "recipe": recipe})
    return {"message": "Recipe created"}, 201


@recipe_blueprint.route("/list", methods=["GET"])
@swag_from("docs/list_recipe.yml")
def get_recipes():
    return recipes
