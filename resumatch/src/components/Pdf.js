import React from 'react'
import PropsTypes from 'prop-types'
import Button from './Button'
import './styles/Pdf.css'
import pdfIcon from '/dist/pdf.png'

//takes in a file name and creates a file icon
const Pdf = ({ name }) => {
  const removeSelf = () => {
    alert('Removing ' + name);
    chrome.storage.local.get(['storedResumes'], function (result) {
      if (typeof result.storedResumes === 'undefined') {
        chrome.storage.local.set({ 'storedResumes': [] });
      }
      else {
        const newArray = result.storedResumes;
        const index = newArray.indexOf(name);
        if (index > -1) {
          newArray.splice(index, 1);
        }
        else {
          alert('The file is already removed.');
        }
        chrome.storage.local.set({ 'storedResumes': newArray });
      }
    });
  }
  return (
    <div className='display-container'>
      <img className='pdf-icon' src={pdfIcon} alt='not found'></img>{name}
      <Button name={'X'} style={btnStyle} func={removeSelf} />
    </div>
  )
}
Pdf.defaultProps = {
  name: 'PDF',
}
Pdf.propsTypes = {
  name: PropsTypes.string,
}
const btnStyle = { backgroundColor: 'transparent', border: 'none', alignSelf: 'start', justifySelf: 'right', marginTop: '4px' }
export default Pdf