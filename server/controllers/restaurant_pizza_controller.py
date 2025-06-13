from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.app import db

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = data["price"]
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        return jsonify(rp.to_dict()), 201

    except KeyError:
        return jsonify({"errors": ["Missing required fields"]}), 400
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
