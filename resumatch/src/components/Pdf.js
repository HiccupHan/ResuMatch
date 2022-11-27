import React from 'react'
import PropsTypes from 'prop-types'
import './styles/Pdf.css'
import pdfIcon from '/dist/pdf.png'

//takes in a file name and creates a file icon
const Pdf = ({ name }) => {
  return (
    <div className='display-container'><img className='pdf-icon' src={pdfIcon} alt='not found'></img>{name}</div>
  )
}
Pdf.defaultProps = {
  name: 'PDF',
}
Pdf.propsTypes = {
  name: PropsTypes.string,
}

export default Pdf