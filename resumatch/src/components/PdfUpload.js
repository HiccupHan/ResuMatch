import React from 'react'
import './styles/PdfUpload.css'

//not used, for future use if team can figure out how to inject React components to a non react page without violating security policies by inserting script tags
const PdfUpload = () => {
  return (
    <div className='upload-container'>
        <div className='upload-window'>
            <button className='close-btn'>X</button>
            <div className='upload-box'></div>
        </div>
    </div>
  )
}

export default PdfUpload