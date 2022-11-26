import React from 'react'
import './styles/Header.css'
import PropsTypes from 'prop-types'
import Button from './Button'

const Header = ({ name, openLogin }) => {  

  return (
    <header>
      <h1>ResuMatch</h1>
      <div className='login-info'>
        <h2>{name}</h2>
        <Button name={'sign out'} style={btnStyle} func={ openLogin }/>
      </div>

    </header>
  )
}

Header.defaultProps = {
  name: 'Please Sign In',
}
Header.propsTypes = {
  name: PropsTypes.string,
}

const btnStyle = {backgroundColor: 'red', border: 'none', borderRadius: '4px', margin: '10px', gridColumn: '3', width:'60px' }

export default Header