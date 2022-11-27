import React from 'react'
import Button from '../components/Button.js'

//options page has a button that clears the chrome local storage, deleting all saved accounts and resume array. 
function Options() {
  return (
    <div className='popup-body'>
    <Button name={'Erase App Data'} style={btnStyle} func={()=>{chrome.storage.local.clear();}}/>
    </div>
  )
}

const btnStyle = { backgroundColor: 'rgb(200,0,0)', border: 'none', borderRadius: '4px' }

export default Options