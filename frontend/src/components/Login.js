import React, { useEffect} from 'react';
import { useAlert } from 'react-alert';
import { useHistory} from 'react-router-dom';
import { useCookies } from 'react-cookie'
import Cookies from 'js-cookie';
const Login = (props) => {
  var history = useHistory();
  const [cookies, setCookie] = useCookies(['username'])
  useEffect(() => {
    
    console.log(Cookies.get('username'));
    if (Cookies.get('username')){
      history.push("/menu");
    }
  }, [])

  const handleSubmit = (e) => {
    e.preventDefault()
    let url = 'http://localhost:8000/login'
    
    fetch (url, {
      method : 'POST',
      headers : {
        'Content-type' : 'application/json',
      },
      body : JSON.stringify({name : e.target.name.value, password : e.target.pass.value})
    }).then ((response) => {
      if (response['ok']){
        let expires = new Date()
        console.log(expires.getTime())
    expires.setTime(expires.getTime() + 1*1000*60*60*60*10)
        setCookie('username', e.target.name.value, { path: '/',  expires })
        history.push("/menu");
      }
      else{
        alert.show('There was an error !!!', {type : 'error'})
      }

    })
  };
  const alert = useAlert()


  return (
    <>
    <form onSubmit = {handleSubmit} >


      <label >User name:</label>
      <input type = 'text' name = 'name'/>
      <label>Password</label>
      <input type = 'text' name = 'pass'/>

      <input type = 'submit' />
    </form>
    </>
  )
}

export default Login;