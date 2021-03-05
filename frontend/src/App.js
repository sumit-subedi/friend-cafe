import './App.css';
import React from 'react';


import Order from './components/order';
import AddMenu from './components/addmenu';
import ViewOrder from './components/vieworder';
import AddOrder from './components/addorder';
import Login from './components/Login';
import ViewDetail from './components/viewDetail';




import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
// import ViewDetail from './components/viewdetail';

const App = () =>  {

  


  return (
    <Router>
    <Switch>
      <Route exact path = "/">
        <Login />

        </Route>
      <Route exact path = "/menu">
        <Order />
      </Route>
      <Route path = "/viewdetail">
        <ViewDetail />
      </Route>
      
      <Route path = "/addmenu">
        <AddMenu />
      </Route>
      <Route path = "/vieworder">
        <ViewOrder />
      </Route>
      
      <Route path = "/addorder">
        <AddOrder />
      </Route>

    </Switch>
      
    
    </Router>
  );
  }


export default App;

