import React, {useEffect, useState} from 'react';
import { useAlert } from 'react-alert'

const AddOrder = () => {
  const [table, setTable] = useState({tables : []})
  const [items, setItems] = useState({foods : []})
  const [refresh , setRefresh] = useState(true)
  const [inputList, setInputList] = useState([{ itemid: "", quantity: "" }]);


  useEffect(() => {

    fetch('http://localhost:8000/menu').then(
      response => response.json()
      ).then(data => {
        setItems({foods : data})
        
    });

    fetch('http://localhost:8000/tables').then(
      response => response.json()
      ).then(data => {
        setTable({tables : data})
        
    })

  }, [refresh])


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
    
    let url = 'http://localhost:8000/createorder'
   
    
    fetch (url, {
      method : 'POST',
      headers : {
        'Content-type' : 'application/json',
      },
      body : JSON.stringify({
        'tid': e.target.table.value,
        'OrderedItem': inputList,
    })
    }).then ((response) => {
      console.log(response);
      if (response.ok){

      alert.show('Task was sucessful !!', {type:'success'})
      setRefresh (!refresh)

      setInputList ([{ itemid: "", quantity: "" }])
      }
      else{
        throw new Error("Not Found")
      }
      
    }).catch ((error) => {
      setRefresh (!refresh)
      alert.show('There was an error !!!' , {type : 'error'})
    })
    
  }
  const alert = useAlert()

  return (
    
<>
<form onSubmit = {handleSubmit} >

  <select name='table' required>
  <option value = "">----</option>
        {table.tables.map(tab =>
          <option key={tab.id} value={tab.id} >{tab.tableName}</option>
          )};
      </select>

    {inputList.map((x, i) => {
      return (
        <div className="box">
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

}

export default AddOrder;