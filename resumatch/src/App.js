import './App.css'
import React from 'react'
import Header from './components/Header'
import MatchResults from './components/MatchResults'
import Resumes from './components/Resumes'
import Button from './components/Button'

export const getCurrentTabUId = (callback) => {
  const queryInfo = { active: true, currentWindow: true };

  chrome.tabs &&
    chrome.tabs.query(queryInfo, (tabs) => {
      callback(tabs[0].id);
    });
};

function App() {

  const sendMessage = () => {
    getCurrentTabUId((id) => {
      id &&
        chrome.tabs.sendMessage(id, {
          value: "openPopup",
        });
      window.close();
    });
  };

  return (
    <div className="App">
      <Header />
      <MatchResults numberOfStars={3}/>
      <Resumes />
      <Button />
    </div>
  );
}

export default App;
