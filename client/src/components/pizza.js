import { useEffect, useState } from "react";

function Pizza() {
    const [pizzas, setPizzas] = useState([]);

    useEffect(() => {
        fetch("/pizzas")
            .then((r) => r.json())
            .then((pizzasArray) => {
                setPizzas(pizzasArray);
            });
    }, []);

    return (
        <ul className="pizzas">
            {pizzas.map((pizza) => (
                <li key={pizza.id}>
                    <h3>{pizza.name}</h3>
                    <p>{pizza.ingredients}</p>
                </li>
            ))}
        </ul>
    );
}

export default Pizza ;