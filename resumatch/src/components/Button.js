import React from 'react'
import PropsTypes from 'prop-types'

const Button = ({ name, style, func }) => {
  return (
    <button className='btn' onClick={func} style={style} >{name}</button>
  )
}

Button.defaultProps = {
  name: 'Button',
  style: { backgroundColor: 'green', border: 'none', borderRadius: '4px'},
  func: () => alert("clicked"),
}
Button.propsTypes = {
  name: PropsTypes.string,
  style: PropsTypes.object,
  func: PropsTypes.func,
}


export default Button