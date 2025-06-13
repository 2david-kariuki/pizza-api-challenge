# 🍕 Pizza Restaurant API

A RESTful API for managing restaurants, pizzas, and the pizzas offered by each restaurant — built using Flask, SQLAlchemy, and Flask-Migrate.

---

## 🚀 Setup Instructions

1. **Clone the repo** and enter the project folder:
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run database migrations:

bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database:

bash
Copy
Edit
PYTHONPATH=. python server/seed.py
Run the server:

bash
Copy
Edit
flask --app server/app.py run
🧠 Route Summary
Method	Route	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<id>	Show one restaurant + its pizzas
DELETE	/restaurants/<id>	Delete a restaurant and related RestaurantPizzas
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Create a new pizza-restaurant connection

🧾 Example Requests
✅ GET /restaurants
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kiki's Pizza",
    "address": "123 Flavor Ave"
  }
]
✅ GET /restaurants/1
json
Copy
Edit
{
  "id": 1,
  "name": "Kiki's Pizza",
  "address": "123 Flavor Ave",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Mozzarella"
    }
  ]
}
❌ GET /restaurants/999
json
Copy
Edit
{ "error": "Restaurant not found" }
✅ POST /restaurant_pizzas
Request Body:

json
Copy
Edit
{ "price": 10, "pizza_id": 1, "restaurant_id": 2 }
Success Response:

json
Copy
Edit
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Palace",
    "address": "456 Crust Rd"
  }
}
Invalid Price:

json
Copy
Edit
{ "errors": ["Price must be between 1 and 30"] }
✅ Validations
RestaurantPizza.price: must be between 1 and 30

GET /restaurants/<id> returns 404 if not found

DELETE /restaurants/<id> removes associated records via cascade

📬 Postman Testing
Open Postman

Click Import → Upload challenge-1-pizzas.postman_collection.json

Use each route to verify your API

✅ Tech Stack
Python 3.8+

Flask

Flask SQLAlchemy

Flask Migrate

SQLite (for development)

📂 Project Structure
bash
Copy
Edit
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   ├── controllers/
├── migrations/
├── challenge-1-pizzas.postman_collection.json
├── requirements.txt
├── README.md
✅ Submission Checklist
 MVC folder structure

 All models with validation and relationships

 All required routes implemented

 Postman tests passing

 README completed

🙌 Author
David Karumba — Moringa School Phase 4 Challenge (SDF-FT13AP4Hybrid)

yaml
Copy
Edit

---

### ✅ Final Step: Save and Commit

```bash
git add README.md
git commit -m "Add complete README with setup, routes, examples, and validation"