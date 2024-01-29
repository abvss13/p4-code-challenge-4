
import os
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_data = [
            {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': [
                    {'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}
                    for pizza in restaurant.pizzas
                ]
            }
            for restaurant in restaurants
        ]
        return make_response(jsonify(restaurant_data), 200)


class RestaurantsById(Resource):
    def get(self, id):
        try:
            restaurant = Restaurant.query.get(id)

            if restaurant is None:
                return make_response(jsonify({'error': 'Restaurant not found'}), 404)

            pizzas = Pizza.query.join(RestaurantPizza).filter_by(restaurant_id=id).all()

            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas]
            }

            return make_response(jsonify(restaurant_data), 200)

        except Exception as e:
            return make_response(jsonify({'error': 'An error occurred'}), 500)

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return make_response('', 204)
        else:
            return make_response(jsonify({'error': 'Restaurant not found'}), 404)


class Pizzas(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizza_data = [
            {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            for pizza in pizzas
        ]
        return make_response(jsonify(pizza_data), 200)


class RestaurantPizzas(Resource):
    def get(self):
        res_pizzas = RestaurantPizza.query.all()
        res_pizza_data = [
            {
                'price': res_pizza.price,
                'pizza_id': res_pizza.pizza_id,
                'restaurant_id': res_pizza.restaurant_id
            }
            for res_pizza in res_pizzas
        ]
        return make_response(jsonify(res_pizza_data), 200)
   
    def post(self):
        try:
            data = request.get_json()

            if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
                raise ValueError('Missing required fields')

            pizza = Pizza.query.get(data['pizza_id'])
            restaurant = Restaurant.query.get(data['restaurant_id'])

            if pizza is None or restaurant is None:
                raise ValueError('Invalid pizza_id or restaurant_id')

            new_rest_pizza = RestaurantPizza(
                price=data['price'],
                pizza_id=data['pizza_id'],
                restaurant_id=data['restaurant_id']
            )

            db.session.add(new_rest_pizza)
            db.session.commit()

            return make_response(jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201)

        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 400)
        except Exception as e:
            return make_response(jsonify({'errors': ['An error occurred']}), 500)


api.add_resource(Restaurants, '/restaurants', endpoint='restaurants')
api.add_resource(RestaurantsById, '/restaurants/<int:id>', endpoint='restaurants_by_id')
api.add_resource(Pizzas, '/pizzas', endpoint='pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas', endpoint='restaurant_pizzas')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
