from flask import Blueprint, jsonify, request, abort
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.app import db

restaurant_bp = Blueprint("restaurants", __name__)

@restaurant_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200


@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant_data = restaurant.to_dict()
    restaurant_data["pizzas"] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    return jsonify(restaurant_data), 200


@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return "", 204
