import React, { useState, useEffect } from 'react'
import './styles/Resumes.css'
import Pdf from './Pdf'
import PropsTypes from 'prop-types'

//takes in an array of resume file names, and renders out a series of file icons
const Resumes = ({ resumeArray, scoreArray }) => {
  const [index, setIndex] = useState(-1);
  const addIndex = ()=>{
    setIndex(index+1);
    return index;
  }
  const resumeList = resumeArray.map((pdf) => <Pdf name={pdf} number={addIndex()}/>);
  return (
    <div className="content-box">
      {resumeList}
    </div>
  )
}

Resumes.defaultProps = {
  resumeArray: [],
}
Resumes.propsTypes = {
  resumeArray: PropsTypes.array,
}
export default Resumes