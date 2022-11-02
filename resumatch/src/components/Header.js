import './styles/Header.css'
import PropsTypes from 'prop-types'

const Header = ({ name }) => {
  return (
    <header>
        <h1>ResuMatch</h1>
        <h2>{name}</h2>
    </header>
  )
}

Header.defaultProps = {
    name: 'Please Sign In',
}
Header.propsTypes = {
    name: PropsTypes.string,
}

export default Header