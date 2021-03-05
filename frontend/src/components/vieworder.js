import React, {useState, useEffect} from 'react';
// import {render} from 'react-dom';
// import { useHistory} from 'react-router-dom';
import ViewDetail from './viewDetail';

const ViewOrder = () => {
  const [items, setItems] = useState({list : []});
  const [details, setDetails] = useState(false);
  const [id, setId] = useState();
  useEffect (() =>{
    fetch('http://localhost:8000/vieworder').then(
      response => response.json()
      ).then(data => {
        setItems({list : data})   
    })}, [])

  const handleButtonClick = (e, id) => {
    setDetails(true);
    setId(id);
    //Call another component here like this
    //<SomeComponenet id=id/> 
    }  
    
  if (!details){
  return (
    <>
    {(items.list.map((item, index) => {
      return (
        <div key = {index}>
        <h3>{item.table.id}  {item.table.tableName}</h3>
        <button onClick = {(e) => handleButtonClick(e,item.id)}>View/Edit</button>
        
        </div>
      )
      }))}
      </>
 ); }
 else{
   return <ViewDetail id = {id}/>
 }
}
export default ViewOrder ;