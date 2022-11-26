import React from 'react'

const Signup = () => {

    const getUserInput = () => {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        alert(username + password);
    }

    return (
        <div className='signup-container'>
            <div className='signup-window'>
                <Button name={'X'} style={closeBtnStyle} func={setClose} />
                <form className='signup-form'>
                    <label for='username' className='username-label'>username: </label>
                    <input type='text' id='username' className='username'></input>
                    <label for='password' className='password-label'>password: </label>
                    <input type='text' id='password' className='password'></input>
                    <Button name={'Sign in'} style={signinBtnStyle} func={getUserInput} />
                    <Button name={'Sign up'} style={signupBtnStyle} />
                </form>
            </div>
        </div>
    )
}
const closeBtnStyle = {width: '25px', height: '25px', textAlign: 'center', backgroundColor: 'grey', justifySelf: 'right', gridColumnStart: '2'}
const signupBtnStyle = {width: '60px', textAlign: 'center', backgroundColor: 'grey', gridRowStart: '4', gridColumnStart: '2'}

export default Signup