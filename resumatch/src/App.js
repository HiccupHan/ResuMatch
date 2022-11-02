import './App.css'
import React from 'react'
import Header from './components/Header'
import MatchResults from './components/MatchResults'

function App() {
  return (
    <div className="App">
      <Header />
      <MatchResults numberOfStars={3}/>
    </div>
  );
}

export default App;
