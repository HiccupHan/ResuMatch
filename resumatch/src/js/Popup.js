import React, { useState, useEffect } from 'react'
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
  };

  const [isOpen, setOpen] = useState(false);
  const [greeting, setGreeting] = useState('Please Sign In');

  useEffect(()=>{
    chrome.storage.local.get(['loginStatus'], function(result){
      if(typeof result.loginStatus === 'undefined') {
        chrome.storage.local.set({'loginStatus': false});
      }
      else{
        setOpen(!result.loginStatus);
      }
    });

    chrome.storage.local.get(['currentUser'], function(result){
      if(typeof result.currentUser === 'undefined') {
        chrome.storage.local.set({'currentUser': 'Please Sign In'});
      }
      else if (result.currentUser == 'Please Sign In') {
        setGreeting(result.currentUser);
      }
      else {
        setGreeting('Hello there, '+ result.currentUser)
      }
      
    });
  });

  const closeLogin = () => {
    chrome.storage.local.set({'loginStatus': true});
    setOpen(false);
  };

  const openLogin = () => {
    chrome.storage.local.set({'loginStatus': false});
    chrome.storage.local.set({'currentUser': 'Please Sign In'});
    setOpen(true);
  };

  const setUsername = (name) => {
    chrome.storage.local.set({'currentUser': name});
  };


  return (
    <div className='popup-body'>
    <Login open={isOpen} setClose={closeLogin} setOpen={openLogin} setName={setUsername}/>
    <Header greeting={greeting} openLogin={openLogin}/>
    <MatchResults numberOfStars={3}/>
    <Resumes numResumes={4}/>
    <div className='footer'><Button name={'Upload Resume'} func={openModal}/></div>
    </div>
  )
}

export default Popup