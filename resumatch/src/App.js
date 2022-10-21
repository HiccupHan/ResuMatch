import './App.css';
import star from './assets/star.png'
import React from 'react';

function App() {
  return (
    <div className="App">
      <header>ResuMatch</header>
      <div className="match-results">
        <img className="rating" src={star}/>
        <img className="rating" src={star}/>
        <img className="rating" src={star}/>
      </div>
    </div>
  );
}

export default App;
