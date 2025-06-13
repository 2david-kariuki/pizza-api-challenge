from flask import Blueprint

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas')
def index():
    return { "message": "RestaurantPizza route is working!" }
