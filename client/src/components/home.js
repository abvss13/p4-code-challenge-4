import React from 'react';
import {Link }from 'react-router-dom';

function Home() {
  return (
    <div className='home'>
      <p>Welcome to pizzas and Restaurants</p>
      <div className='buts'>
               <button><Link to="/pizzas">Pizzas</Link></button> 
        <button><Link to="/restaurants">Restaurants</Link></button> 
        <button><Link to="/form">Add</Link>  </button>
      </div>

    </div>
  );
}
export default Home ;