import React from 'react'
import Header from '../components/Header.js'
import MatchResults from '../components/MatchResults.js'
import Resumes from '../components/Resumes.js'
import Button from '../components/Button.js'
import './styles/Popup.css'

function Popup() {
  return (
    <div className='popup-body'>
    <Header />
    <MatchResults numberOfStars={3}/>
    <Resumes numResumes={4}/>
    <div className='footer'><Button name={'Upload Resume'} /></div>
    </div>
  )
}

export default Popup