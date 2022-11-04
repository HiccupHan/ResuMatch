import './styles/Resumes.css'
import Pdf from './Pdf'
import PropsTypes from 'prop-types'

const Resumes = ({numResumes}) => {
  var resumes = [];
  for(var i = 0; i<numResumes;i++){
    resumes.push(<Pdf name={'resume.pdf'}/>);
  }

  return (
    <div className="content-box">
      {resumes}
    </div> 

  )
}

Resumes.defaultProps = {
  numResumes: 0,
}
Resumes.propsTypes = {
  numResumes: PropsTypes.number,
}
export default Resumes