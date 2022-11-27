import React, { useState } from 'react'
import './styles/Login.css'
import Button from './Button.js'

const Login = ({ open, setClose, setOpen, setName }) => {
  if (!open) return null

  const [needSignup, setSignup] = useState(false);

  const getUserInput = () => {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    if (username == '' || password == '') {
      alert('Enter username and password');
      return false;
    }

    chrome.storage.local.get(username, function (result) {
      if (typeof result[username] === 'undefined') {
        alert('wrong username or sign up first')
        setOpen();
      }
      else if (result[username] == password) {
        setClose();
        setName(username);
      }
      else {
        alert('wrong password');
        setOpen();
      }
    })
  }

  function setupAccount() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username == '' || password == '') {
      alert('Enter username and password');
      return false;
    }

    else if (username.length > 10) {
      alert('Username can be at most 10 characters long');
      return false;
    }

    else if (password.length < 4) {
      alert('Password needs to be at least 4 characters');
      return false;
    }

    chrome.storage.local.get(username, function (result) {
      if (typeof result[username] === 'undefined') {
        chrome.storage.local.set({ [username]: password });
      }
      else {
        alert('account already exists');
      }
    });
  }

  if (needSignup) {
    return (
      <div className='login-container'>
        <div className='login-window'>
          <Button name={'X'} style={closeBtnStyle} func={() => setSignup(false)} />
          <form className='signin-form'>
            <label for='username' className='username-label'>username: </label>
            <input type='text' id='username' className='username'></input>
            <label for='password' className='password-label'>password: </label>
            <input type='text' id='password' className='password'></input>
            <Button name={'Sign up'} style={signinBtnStyle} func={setupAccount} />
          </form>
        </div>
      </div>
    )
  }

  return (
    <div className='login-container'>
      <div className='login-window'>
        <form className='login-form'>
          <label for='username' className='username-label'>username: </label>
          <input type='text' id='username' className='username'></input>
          <label for='password' className='password-label'>password: </label>
          <input type='text' id='password' className='password'></input>
          <Button name={'Sign in'} style={signinBtnStyle} func={getUserInput} />
          <Button name={'Sign up'} style={signupBtnStyle} func={() => setSignup(true)} />
        </form>
      </div>
    </div>
  )
}

const closeBtnStyle = { width: '25px', height: '25px', textAlign: 'center', backgroundColor: 'grey', justifySelf: 'right', gridColumnStart: '2' }
const signinBtnStyle = { width: '62px', textAlign: 'center', backgroundColor: 'grey', gridRowStart: '4', gridColumnStart: '2' }
const signupBtnStyle = { width: '62px', marginLeft: '4px', textAlign: 'center', backgroundColor: 'grey', gridRowStart: '4', gridColumnStart: '3' }

export default Login