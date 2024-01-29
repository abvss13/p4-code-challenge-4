from models import  Restaurant, Pizza, RestaurantPizza
from app import db,app

with app.app_context():
    #Delete the existing data
    print('Deleting existing data...')
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    # Create Restaurants
    restaurant1 = Restaurant(name='Pizza Place 1', address='123 Main St')
    restaurant2 = Restaurant(name='Italian Bistro', address='456 Oak St')
    restaurant3 = Restaurant(name='Pizza Palace', address='789 Elm St')
    restaurant4 = Restaurant(name='Mamma Mia Pizzeria', address='101 Pine St')
    restaurant5 = Restaurant(name='Slice of New York', address='789 Broadway Ave')
    restaurant6 = Restaurant(name='Papa John\'s Pizza', address='2100 4th St')
    restaurant7 = Restaurant(name='Domino\'s Pizza', address='15 Market St')
    restaurant8 = Restaurant(name='Little Italy Pizzeria', address='500 State St')
    restaurant9 = Restaurant(name='Giordano\'s', address='100 Michigan Ave')

    # Create Pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato Sauce, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato Sauce, Mozzarella, Pepperoni')
    pizza3 = Pizza(name='Vegetarian', ingredients='Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms')
    pizza4 = Pizza(name='Supreme', ingredients='Tomato Sauce, Mozzarella, Pepperoni, Sausage, Onions, Olives')
    pizza5 = Pizza(name='BBQ Chicken', ingredients='BBQ Sauce, Mozzarella, Grilled Chicken, Red Onions, Cilantro')
    pizza6 = Pizza(name='Hawaiian', ingredients='Tomato Sauce, Mozzarella, Ham, Pineapple')
    pizza7 = Pizza(name='Meat Lovers', ingredients='Tomato Sauce, Mozzarella, Pepperoni, Sausage, Bacon')
    pizza8 = Pizza(name='Mushroom and Truffle', ingredients='White Sauce, Mozzarella, Mushrooms, Truffle Oil, Parmesan')
    pizza9 = Pizza(name='Spinach and Feta', ingredients='Tomato Sauce, Mozzarella, Spinach, Feta Cheese, Garlic')


    # Add Pizzas to Restaurants
    restaurant1.pizzas.append(pizza1)
    restaurant1.pizzas.append(pizza2)
    restaurant2.pizzas.append(pizza2)
    restaurant3.pizzas.append(pizza3)
    restaurant4.pizzas.append(pizza3)
    restaurant4.pizzas.append(pizza4)
    restaurant5.pizzas.append(pizza5)
    restaurant6.pizzas.append(pizza6)
    restaurant7.pizzas.append(pizza7)
    restaurant8.pizzas.append(pizza8)
    restaurant9.pizzas.append(pizza9)

    # Create Restaurant Pizzas
    restaurant_pizza1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    restaurant_pizza2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=restaurant1.id)
    restaurant_pizza3 = RestaurantPizza(price=15, pizza_id=pizza2.id, restaurant_id=restaurant2.id)
    restaurant_pizza4 = RestaurantPizza(price=11, pizza_id=pizza3.id, restaurant_id=restaurant3.id)
    restaurant_pizza5 = RestaurantPizza(price=14, pizza_id=pizza4.id, restaurant_id=restaurant4.id)
    restaurant_pizza6 = RestaurantPizza(price=13, pizza_id=pizza5.id, restaurant_id=restaurant5.id)
    restaurant_pizza7 = RestaurantPizza(price=16, pizza_id=pizza6.id, restaurant_id=restaurant6.id)
    restaurant_pizza8 = RestaurantPizza(price=18, pizza_id=pizza7.id, restaurant_id=restaurant7.id)
    restaurant_pizza9 = RestaurantPizza(price=20, pizza_id=pizza8.id, restaurant_id=restaurant8.id)
    restaurant_pizza10 = RestaurantPizza(price=17, pizza_id=pizza9.id, restaurant_id=restaurant9.id)

    # Add objects to the session and commit to the database
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3,restaurant3, restaurant4, pizza3, pizza4, restaurant_pizza4, restaurant_pizza5,
                        restaurant5, restaurant6, restaurant7, restaurant8, restaurant9, pizza5, pizza6, pizza7, pizza8, pizza9, restaurant_pizza6, restaurant_pizza7, restaurant_pizza8, restaurant_pizza9, restaurant_pizza10])
    db.session.commit()

