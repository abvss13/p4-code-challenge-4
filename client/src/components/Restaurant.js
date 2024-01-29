import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const RestaurantDetails = () => {
    const { restaurantId } = useParams();
    const [restaurants, setRestaurants] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
      fetch(`/restaurants/${restaurantId}`)
        .then((r) => r.json())
        .then((restaurantsArray) => {
          setRestaurants(restaurantsArray);
          setLoading(false);
        })
        .catch((error) => {
          setError(error.message || 'An error occurred');
          setLoading(false);
        });
    }, [restaurantId]);
  
    if (loading) {
      return <p>Loading...</p>;
    }
  
    if (error) {
      return <p>Error: {error}</p>;
    }

    function handleDelete(id) {
        fetch(`/restaurants/${id}`, {
          method: "DELETE",
        }).then((r) => {
          if (r.ok) {
            setRestaurants((restaurants) =>
              restaurants.filter((restaurant) => restaurant.id !== id)
            );
          }
        });
      }
  
    return (
      <div>
        <h2>{restaurants.name}</h2>
        <p>Address: {restaurants.address}</p>
        <h3>Pizzas:</h3>
        <ul>
          {restaurants.pizzas.map((pizza) => (
            <li key={pizza.id}>
              <strong>{pizza.name}</strong>
              <p>Ingredients: {pizza.ingredients}</p>
            </li>
          ))}
        </ul> 
        <button onClick={handleDelete} >Delete</button>
      </div>
    );
  };

export default RestaurantDetails;

