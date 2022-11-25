import React, { useState } from 'react'
import Header from '../components/Header.js'
import MatchResults from '../components/MatchResults.js'
import Resumes from '../components/Resumes.js'
import Button from '../components/Button.js'
import Login from '../components/Login.js'
import './styles/Popup.css'

function Popup() {
  const openModal = () => {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {type: "open-modal"});
    });
  }

  const [isOpen, setOpen] = useState(false)

  return (
    <div className='popup-body'>
    <Login open={isOpen } setClose={()=>setOpen(false)}/>
    <Header name={'Mike'} openLogin={()=>setOpen(true)}/>
    <MatchResults numberOfStars={3}/>
    <Resumes numResumes={4}/>
    <div className='footer'><Button name={'Upload Resume'} func={openModal}/></div>
    </div>
  )
}

export default Popup