import React from 'react'
import Header from '../components/Header.js'
import MatchResults from '../components/MatchResults.js'
import Resumes from '../components/Resumes.js'
import Button from '../components/Button.js'

function Options() {
  return (
    <div className='popup-body'>
    <Button name={'Erase App Data'} func={()=>{chrome.storage.local.clear();}}/>
    </div>
  )
}

export default Options