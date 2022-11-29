import React from 'react'
import PropsTypes from 'prop-types'
import Button from './Button'
import './styles/Pdf.css'
import pdfIcon from '/dist/pdf.png'
import whiteStar from '../img/whitestar.png'

//takes in a file name and creates a file icon
const Pdf = ({ name, score }) => {
  //remove file, to signal backend use chrome messaging api
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

  var stars = [];
  for (var i = 0; i < score; i++) {
    stars.push(<img className='white-star' key={i} src={whiteStar} alt='not found'></img>);
  }

  return (
    <div className='display-container'>
      <img className='pdf-icon' src={pdfIcon} alt='not found'></img>{name}
      <div className='star-container'>
        {stars}
      </div>
      <Button name={'X'} style={btnStyle} func={removeSelf} />
    </div>
  )
}
Pdf.defaultProps = {
  name: 'PDF',
  score: 0,
}
Pdf.propsTypes = {
  name: PropsTypes.string,
  score: PropsTypes.number,
}
const btnStyle = { backgroundColor: 'transparent', border: 'none', alignSelf: 'start', justifySelf: 'right', marginTop: '4px' }
export default Pdf