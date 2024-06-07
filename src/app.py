from flask import Flask
from flasgger import Swagger
from user_view import user_blueprint
from recipe_view import recipe_blueprint

app = Flask(__name__)
swagger = Swagger(app=app)

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)

@app.route("/")
def index():
    return "OK", 200

@app.errorhandler(404)
def not_found_handler(e):
    return {"message": "route not found!"}, 404

# POST user/login
# POST user/register

if __name__ == "__main__":
    app.run(debug=True)