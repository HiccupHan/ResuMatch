import React from 'react'
import './styles/Resumes.css'
import Pdf from './Pdf'
import PropsTypes from 'prop-types'

//takes in an array of resume file names, and renders out a series of file icons
const Resumes = ({ resumeArray }) => {
  const resumeList = resumeArray.map((pdf)  => <Pdf name={pdf}/>);
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