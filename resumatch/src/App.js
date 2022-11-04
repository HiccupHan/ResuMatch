import './App.css'
import React, { useState } from 'react'
import Header from './components/Header'
import MatchResults from './components/MatchResults'
import Resumes from './components/Resumes'
import Button from './components/Button'

function App() {
  return (
    <div className="App">
      <Header />
      <MatchResults numberOfStars={3}/>
      <Resumes numResumes={4}/>
      <div className='footer'><Button name={'Upload Resume'} /></div>
    </div>
  );
}

export default App;
