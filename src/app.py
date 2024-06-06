from flask import Flask
from user_view import user_blueprint
from recipe_view import recipe_blueprint
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
