import React, { Component, useState } from 'react';
import { login } from '../../api';

export default () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const doLogin = async () => {
    console.log(username, password);
    if (await login(username, password)) {
      // loggedin
    } else {
      //error, wrong password or missing username
    }
  };

  return (
    <div className='content-wrapper'>
      <div className='auth-inner'>
        <form>
          <h3>Sign In</h3>

          <div className='form-group'>
            <label>Email address</label>
            <input
              type='email'
              className='form-control'
              placeholder='Enter email'
            />
          </div>

          <div className='form-group'>
            <label>Password</label>
            <input
              type='password'
              className='form-control'
              placeholder='Enter password'
            />
          </div>

          <div className='form-group'>
            <div className='custom-control custom-checkbox'>
              <input
                type='checkbox'
                className='custom-control-input'
                id='customCheck1'
              />
              <label className='custom-control-label' htmlFor='customCheck1'>
                Remember me
              </label>
            </div>
          </div>

          <button
            type='submit'
            onClick={doLogin}
            className='btn btn-primary btn-block'
          >
            Submit
          </button>
          <p className='forgot-password text-right'>
            Forgot <a href='#'>password?</a>
          </p>
        </form>
      </div>
    </div>
  );
};
