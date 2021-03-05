import React from 'react';
import { useAlert } from 'react-alert'

const AddMenu = () => {

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(e.target.name.value)
    let url = 'http://localhost:8000/addmenu'
    
    fetch (url, {
      method : 'POST',
      headers : {
        'Content-type' : 'application/json',
      },
      body : JSON.stringify({itemName : e.target.name.value, price : e.target.price.value})
    }).then ((response) => {
      alert.show('Task was sucessful !!', {type:'success'})
    }).catch ((error) => {
      alert.show('There was an error !!!', {type : 'error'})
    })
  }
  const alert = useAlert()

  return (
    <>

    <form onSubmit = {handleSubmit} >


      <label >name</label>
      <input type = 'text' name = 'name'/>
      <input type = 'number' name = 'price'/>

      <input type = 'submit' />
    </form>
    </>
  );

}

export default AddMenu