import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';

const Order = () => {

  const [items, setItems] = useState({list : []});
  
  useEffect (() =>{
    
    fetch('http://localhost:8000/menu').then(
      response => response.json()
      ).then(data => {
        
        setItems({list : data})
        
    })}, [])
    
  
 
  return (
    <>
    {(items.list.map((item, index) => {

      return (
        <div key = {index}>
        <h3>{item.itemName} {item.price}</h3>

        </div>
      )
      

      }))}

<Link to="/addmenu">Add Menu</Link>
<Link to="/addorder">Add Order</Link>
<Link to="/vieworder">View Order</Link>

      </>
       )
}
  


export default Order