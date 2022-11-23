import React from 'react'

import './styles/PdfUpload.css'

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