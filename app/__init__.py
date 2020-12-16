# app/__init__.py
# pylint: disable=missing-docstring

# Here __name__ contains name of the package => "app"

from flask import Flask

# Without Blueprint
# def create_app():
#     app = Flask(__name__)

#     @app.route('/hello')
#     def hello():
#         return f"Hello World ! :) ----- Flask app name={app.name}"

#     return app

# With Blueprint
def create_app():
    app = Flask(__name__)

    from .main.controllers import main
    app.register_blueprint(main)

    return app
