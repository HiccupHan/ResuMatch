import React from 'react'
import './styles/Header.css'
import PropsTypes from 'prop-types'
import Button from './Button'

const Header = ({ name }) => {  
  const closeModal = () => {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {type: "close-modal"});
    });
  }

  return (
    <header>
      <h1>ResuMatch</h1>
      <div className='login-info'>
        <h2>{name}</h2>
        <Button name={'login'} style={btnStyle} func={closeModal}/>
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

const btnStyle = {backgroundColor: 'green', border: 'none', borderRadius: '4px', margin: '10px', gridColumn: '3'}

export default Header