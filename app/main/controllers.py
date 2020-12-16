# app/main/controllers.py
# pylint: disable=missing-docstring

# Here __name__ contains name of the package => "app.main.controllers"

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/hello')
def home():
    return f"Goodbye from a Blueprint ! :)"
