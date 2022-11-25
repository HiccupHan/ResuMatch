import React from 'react'
import './styles/Login.css'
import Button from './Button.js'

const Login = ({ open, setClose }) => {
  if (!open) return null

  const getUserInput = () => {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    alert(username+password);
  }

  return (
    <div className='login-container'>
      <div className='login-window'>
        <Button name={'X'} style={loginBtnStyle} func={setClose} />
        <form className='login-form'>
          <label for='username' className='username-label'>username: </label>
          <input type='text' id='username' className='username'></input>
          <label for='password' className='password-label'>password: </label>
          <input type='text' id='password' className='password'></input>
          <Button name={'Sign in'} style={signinBtnStyle} func={getUserInput}/>
        </form>
      </div>
    </div>
  )
}

const loginBtnStyle = {width: '25px', height: '25px', textAlign: 'center', backgroundColor: 'grey', justifySelf: 'right', gridColumnStart: '2'}
const signinBtnStyle = {width: '60px', textAlign: 'center', backgroundColor: 'grey', gridRowStart: '4', gridColumnStart: '2'}

export default Login