import './App.css'
import React from 'react'
import Header from './components/Header'
import MatchResults from './components/MatchResults'
import Resumes from './components/Resumes'

function App() {
  return (
    <div className="App">
      <Header />
      <MatchResults numberOfStars={3}/>
      <Resumes />
    </div>
  );
}

export default App;
