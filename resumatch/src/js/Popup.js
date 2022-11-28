import React, { useState, useEffect } from 'react'
import Header from '../components/Header.js'
import MatchResults from '../components/MatchResults.js'
import Resumes from '../components/Resumes.js'
import Button from '../components/Button.js'
import Login from '../components/Login.js'
import './styles/Popup.css'

//main UI for the extension
function Popup() {
  
  //uses chrome messaging api to send a message to injected content script, which will open the pdf upload pop up menu in the current webpage
  const openModal = () => {
    // chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    //   chrome.tabs.sendMessage(tabs[0].id, { type: "open-modal" });
    // });
    chrome.tabs.create({
      url: "http://localhost:8501/Upload"
    })

    //chrome tabs sendMessage
  };

  //indicate if login page should be opened 
  const [isOpen, setOpen] = useState(false);
  //sets the greeting phrase used by Header
  const [greeting, setGreeting] = useState('Please Sign In');
  //array of resume file names 
  const [arrayOfResumes, setResumes] = useState([]);

  //run set up
  useEffect(() => {
    //set up a bool value in chrome storage to indicate if user is logged in, which determines if the login page should be opened
    chrome.storage.local.get(['loginStatus'], function (result) {
      if (typeof result.loginStatus === 'undefined') {
        chrome.storage.local.set({ 'loginStatus': false });
      }
      else {
        setOpen(!result.loginStatus);
      }
    });

    //set up a string value in chrome storage to indicate who the current user is, used to set greeting phrase
    chrome.storage.local.get(['currentUser'], function (result) {
      if (typeof result.currentUser === 'undefined') {
        chrome.storage.local.set({ 'currentUser': 'Please Sign In' });
      }
      else if (result.currentUser == 'Please Sign In') {
        setGreeting(result.currentUser);
      }
      else {
        setGreeting('Hello there, ' + result.currentUser)
      }
    });

    //to be deleted, exists for testing
    // Post a request to the backend /resume_names -> array 
    //chrome.storage.local.set({'storedResumes' : ['resume1.pdf', 'resume2.pdf', 'resume3.pdf', 'resume4.pdf', 'resume5.pdf', 'resume6.pdf', 'resume7.pdf']});

    //set up storedResumes in chrome storage, stores an array of resume file names
    chrome.storage.local.get(['storedResumes'], function (result) {
      if (typeof result.storedResumes === 'undefined') {
        chrome.storage.local.set({ 'storedResumes': ['resume1.pdf', 'resume2.pdf', 'resume3.pdf', 'resume4.pdf', 'resume5.pdf', 'resume6.pdf', 'resume7.pdf'] });
      }
      else {
        setResumes(result.storedResumes);
      }
    });
  });

  //close login page
  const closeLogin = () => {
    chrome.storage.local.set({ 'loginStatus': true });
    setOpen(false);
  };

  //open login page
  const openLogin = () => {
    chrome.storage.local.set({ 'loginStatus': false });
    chrome.storage.local.set({ 'currentUser': 'Please Sign In' });
    setOpen(true);
  };

  //set the current user
  const setUsername = (name) => {
    chrome.storage.local.set({ 'currentUser': name });
  };

  return (
    <div className='popup-body'>
      <Login open={isOpen} setClose={closeLogin} setOpen={openLogin} setName={setUsername} />
      <Header greeting={greeting} openLogin={openLogin} />
      <MatchResults numberOfStars={4} />
      <Resumes resumeArray={arrayOfResumes} />
      <div className='footer'><Button name={'Upload Resume'} func={openModal} /></div>
    </div>
  )
}

export default Popup