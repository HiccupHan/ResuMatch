import React, { useState, useEffect } from 'react'
import './styles/Resumes.css'
import Pdf from './Pdf'
import PropsTypes from 'prop-types'

//takes in an array of resume file names, and renders out a series of file icons
const Resumes = ({ resumeArray, scoreArray, noRoundArray }) => {
  var scores = [];
  var noRound = [];
  if(scoreArray.length != resumeArray.length) {
    scores = resumeArray.map((resume) => 0);
  }
  else {
    scores = scoreArray;
  }
  if(noRoundArray.length != resumeArray.length) {
    noRound = resumeArray.map((resume) => 0);
  }
  else {
    noRound = noRoundArray;
  }
  const resumeList = resumeArray.map((pdf, index) => <Pdf name={pdf} score={scores[index]} noRound={noRound[index]}/>);
  return (
    <div className="content-box">
      {resumeList}
    </div>
  )
}

Resumes.defaultProps = {
  resumeArray: [],
  scoreArray: [],
  noRoundArray: [],
}
Resumes.propsTypes = {
  resumeArray: PropsTypes.array,
  scoreArray: PropsTypes.array,
  noRoundArray: PropsTypes.array,
}
export default Resumes