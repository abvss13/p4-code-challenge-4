import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Form = ({ pizzas: initialPizzas = [], restaurants: initialRestaurants = [] }) => {
  const [price, setPrice] = useState('');
  const [formErrors, setFormErrors] = useState([]);
  const navigate = useNavigate();
  const [selectedPizzas, setSelectedPizzas] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState('');
  const [pizzas, setPizzas] = useState([]);
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);

  useEffect(() => {
    fetch("/restaurants")
      .then((res) => res.json())
      .then(setRestaurants);
  }, []);

  const handlePizzaChange = (pizzaId) => {
    // Check if pizzaId is already in the selectedPizzas array
    if (selectedPizzas.includes(pizzaId)) {
      // If it's already selected, remove it
      setSelectedPizzas(selectedPizzas.filter(id => id !== pizzaId));
    } else {
      // If it's not selected, add it
      setSelectedPizzas([...selectedPizzas, pizzaId]);
    }
  };

  const handleRestaurantChange = (restaurantId) => {
    // Update the selected restaurant
    setSelectedRestaurant(restaurantId);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Perform validation here
    if (!price || selectedPizzas.length === 0 || !selectedRestaurant) {
      setFormErrors(['Please fill in all fields']);
      return;
    }

    // Reset errors
    setFormErrors([]);

    // Your existing fetch logic
    const formData = {
      pizza_ids: selectedPizzas,
      restaurant_id: selectedRestaurant,
      price: parseInt(price),
    };

    fetch('/restaurant_pizzas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((r) => {
        if (r.ok) {
          navigate('/restaurant_pizzas');
        } else {
          r.json().then((err) => setFormErrors(err.errors));
        }
      })
      .catch((error) => {
        console.error('Error adding pizza to restaurant:', error);
      });
  };

  return (
    
  <div className="row justify-content-center">
    <div className="col-md-6" style={{ backgroundColor: '#aaffc3', padding: '20px', borderRadius: '10px' }}>
      <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="price">Price:</label>
              <input
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                className="form-control"
              />
            </div>

            <div className="form-group">
              <label>Choose Pizzas:</label>
              {pizzas.map((pizza) => (
                <div key={pizza.id} className="form-check">
                  <input
                    type="checkbox"
                    id={`pizza-${pizza.id}`}
                    className="form-check-input"
                    checked={selectedPizzas.includes(pizza.id)}
                    onChange={() => handlePizzaChange(pizza.id)}
                  />
                  <label htmlFor={`pizza-${pizza.id}`} className="form-check-label">
                    {pizza.name}
                  </label>
                </div>
              ))}
            </div>

            <div className="form-group">
              <label>Choose Restaurant:</label>
              {restaurants.map((restaurant) => (
                <div key={restaurant.id} className="form-check">
                  <input
                    type="radio"
                    id={`restaurant-${restaurant.id}`}
                    name="selectedRestaurant"
                    className="form-check-input"
                    checked={selectedRestaurant === restaurant.id}
                    onChange={() => handleRestaurantChange(restaurant.id)}
                  />
                  <label htmlFor={`restaurant-${restaurant.id}`} className="form-check-label">
                    {restaurant.name}
                  </label>
                </div>
              ))}
            </div>

            {formErrors.length > 0 &&
              formErrors.map((err, index) => (
                <p key={index} style={{ color: 'red' }}>
                  {err}
                </p>
              ))}

            <button type="submit" className="btn btn-primary">
              Add To Restaurant
            </button>
          </form>
        </div>
      </div>
    
  );
};

export default Form;
