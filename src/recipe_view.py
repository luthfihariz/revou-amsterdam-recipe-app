from flask import Blueprint, request, jsonify
from repository import recipes, tokens
from flasgger import swag_from

recipe_blueprint = Blueprint("recipe", __name__, url_prefix="/recipe")


@recipe_blueprint.before_request
def authenticate():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Login required"}), 401

    username = tokens.get(token)
    if not username:
        return jsonify({"message": "Login required"}), 401

    print(f"Authenticated user: {username}")

    request.username = username


@recipe_blueprint.route("/create", methods=["POST"])
@swag_from("docs/create_recipe.yml")
def post_recipe():
    recipe = request.json.get("recipe")
    if not recipe:
        return jsonify({"message": "Recipe required"}), 400

    username = getattr(request, "username", "anonymous")
    recipes.append({"username": username, "recipe": recipe})
    return jsonify({"message": "Recipe created"}), 201


@recipe_blueprint.route("/list", methods=["GET"])
@swag_from("docs/list_recipe.yml")
def get_recipes():
    return jsonify(recipes), 200
