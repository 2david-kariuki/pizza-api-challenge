from flask import Blueprint

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas')
def index():
    return { "message": "Pizza route is working!" }
