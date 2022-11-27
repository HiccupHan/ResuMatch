import React, { useState, useEffect } from 'react'
import './styles/Header.css'
import PropsTypes from 'prop-types'
import Button from './Button'

//takes in a greeting phrase to be displayed and a function that opens login window
const Header = ({ greeting, openLogin }) => {

  return (
    <header>
      <h1>ResuMatch</h1>
      <div className='login-info'>
        <h2>{greeting}</h2>
        <Button name={'Sign Out'} style={btnStyle} func={openLogin} />
      </div>

    </header>
  )
}

Header.defaultProps = {
  name: 'Please Sign In',
  openLogin: ()=>console.log('No login window!'),
}
Header.propsTypes = {
  name: PropsTypes.string,
  openLogin: PropsTypes.func,
}

const btnStyle = { backgroundColor: 'rgb(200,0,0)', border: 'none', borderRadius: '4px', margin: '10px', gridColumn: '3', width: '64px', justifySelf: 'right' }

export default Header