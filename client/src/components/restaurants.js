
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";


function Restaurants() {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch("/restaurants")
            .then((r) => r.json())
            .then((restaurantsArray) => {
                setRestaurants(restaurantsArray );
            });
    }, []);

    return (
       <div> 
        
        <ul className="restaurants">
        <p><b>Pizzas:</b></p>
            {restaurants.map((restaurant) => (
                <li key={restaurant.id}>
                    <h3>{restaurant.name}</h3>
                    <p>{restaurant.address}</p>
                    <button ><Link to={`/restaurants/${restaurant.id}`}>View</Link></button>
                </li>
            ))}
        </ul>
        </div>
    );

}

export default Restaurants;
