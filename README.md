# 🍕 Pizza Restaurant API

A RESTful API built with Flask to manage restaurants, pizzas, and their associations.

---

## 🚀 Setup

```bash
# Clone repo & enter project
git clone git@github.com:2david-kariuki/pizza-api-challenge.git
cd pizza-api-challenge

# Create & activate virtual env
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Set up DB
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed database
PYTHONPATH=. python server/seed.py

# Run server
flask --app server/app.py run
🧠 Routes
Method	Route	Description
GET	/restaurants	All restaurants
GET	/restaurants/<id>	One restaurant + pizzas
DELETE	/restaurants/<id>	Delete a restaurant
GET	/pizzas	All pizzas
POST	/restaurant_pizzas	Link pizza to restaurant

✅ Validations
price must be 50–300

404 if restaurant not found

Cascade deletes on restaurants

📬 Postman
Import challenge-1-pizzas.postman_collection.json to test all routes

👤 Author
David Karumba — Moringa School Phase 4 Challenge

