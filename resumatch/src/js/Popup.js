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
      url: "http://localhost:8501"
    })

    //chrome tabs sendMessage
  };

  //indicate if login page should be opened 
  const [isOpen, setOpen] = useState(false);
  //sets the greeting phrase used by Header
  const [greeting, setGreeting] = useState('Please Sign In');
  //array of resume file names 
  const [arrayOfResumes, setResumes] = useState([]);
  //number of stars
  const [numStars, setNumStars] = useState(0);

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

    chrome.storage.local.get(['resumeScores'], function (result) {
      if (typeof result.resumeScores === 'undefined') {
        chrome.storage.local.set({ 'resumeScores': [] });
      }
      // else{
      //   const starNum = Math.max(result.resumeScores);
      //   setNumStars(starNum);
      // }
      
    })

    // const request = new Request('http://localhost:8000/resume_names', { method: 'POST' });
    // fetch(request)
    //   .then((response) => response.json())
    //   .then((data) => {
    //     chrome.storage.local.set({ 'storedResumes': data });
    //     setResumes(data);
    //     console.log(data);
    //   });

    //set up storedResumes in chrome storage, stores an array of resume file names
    chrome.storage.local.get(['storedResumes'], function (result) {
      if (typeof result.storedResumes === 'undefined') {
        chrome.storage.local.set({ 'storedResumes': [] });
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

  const matchResume = () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { type: "analyze" });
      var tab = tabs[0];

      const request = new Request('http://localhost:8000/scores?linkedin_url=https://www.linkedin.com/jobs/view/3371068785', { method: 'GET'});
      fetch(request)
        .then((response) => response.json())
        .then((data) => {
          chrome.storage.local.set({ 'resumeScores': data });
          console.log(data)
        });

    });          
    const starNum = Math.floor(Math.random() * 6);
    setNumStars(starNum);
  }

  return (
    <div className='popup-body'>
      <Login open={isOpen} setClose={closeLogin} setOpen={openLogin} setName={setUsername} />
      <Header greeting={greeting} openLogin={openLogin} />
      <MatchResults numberOfStars={numStars} />
      <Resumes resumeArray={arrayOfResumes} />
      <div className='footer'>
        <Button name={'Upload Resume'} func={openModal} />
        <Button name={'Match'} func={matchResume} />
      </div>
    </div>
  )
}

export default Popup