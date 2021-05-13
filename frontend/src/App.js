import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import './index.css';

import Login from './components/auth/login.component';
import SignUp from './components/auth/signup.component';
import Books from './components/books.component';
import NavBar from './components/navbar.component';

function App() {
  return (
    <Router>
      <div className='App'>
        <NavBar />
        <Switch>
          <Route exact path='/' component={Books} />
          <Route path='/sign-in' component={Login} />
          <Route path='/sign-up' component={SignUp} />
          <Route path='/books' component={Books} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
