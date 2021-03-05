import React, {useState, useEffect} from 'react';
// import {render} from 'react-dom';
import { useHistory} from 'react-router-dom';
import { useAlert } from 'react-alert'





const ViewDetail = (props) => {
  var alert = useAlert();
  var history = useHistory();
  const [items, setItems] = useState({foods : []})
  
  const [inputList, setInputList] = useState([]);


  useEffect(() => {

    fetch('http://localhost:8000/menu').then(
      response => response.json()
      ).then(data => {
        setItems({foods : data})
        
        
    });

    addData();

  }, [])

  const addData = () => {
    fetch ('http://localhost:8000/viewOrderedItem?id=' + props.id).then(
      response => response.json()
    ).then(data=>{
      data.map((item, index)=>{
        var list1 = {itemid:item.item.id, quantity : item.quantity}
        
        inputList.push(list1)
        setInputList([...inputList]);
        
      })
    })
  }


  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...inputList];
    list[index][name] = value;
    setInputList(list);
  };

  const handleAddClick = () => {
    setInputList([...inputList, { itemid: "", quantity: "" }]);
  };

  const handleSubmit = (e) => {
    e.preventDefault()
    
    let url = 'http://localhost:8000/editOrder'
   
    
    fetch (url, {
      method : 'POST',
      headers : {
        'Content-type' : 'application/json',
      },
      body : JSON.stringify({
        'ordId': props.id,
        'OrderedItem': inputList,
    })
    }).then ((response) => {
      console.log(response);
      if (response.ok){

        history.push("/");
      

      setInputList ([{ itemid: "", quantity: "" }])
      }
      else{
        throw new Error("Not Found")
      }
      
    }).catch ((error) => {
      
      alert.show('There was an error !!!' , {type : 'error'})
    })
    
  }
  

  return (
    
<>

<form onSubmit = {handleSubmit} >

    {inputList.map((x, i) => {
      return (
        <div className="box" key = {i}>
          <select name = "itemid" onChange = {e => handleInputChange(e, i)} value = {x.itemid || ''} >
            <option value = "">----</option>
            {items.foods.map(food =>
              <option key = {food.id} value = {food.id}> {food.itemName} </option>
            )}
          </select>

          <input type = "number" name = "quantity" key = {x + i} onChange = {e => handleInputChange(e, i)}
          value = {x.quantity} />
      
      
          <div className="btn-box">
            
            {inputList.length - 1 === i && <button onClick={handleAddClick}>Add</button>}
          </div>
        </div>
      );
    })}

<input type = 'submit' />
</form>
    

  </>

  );

};

export default ViewDetail;