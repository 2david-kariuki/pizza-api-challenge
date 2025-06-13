from flask import Blueprint

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants')
def index():
    return { "message": "Restaurant route is working!" }
