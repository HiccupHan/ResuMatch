import React from 'react'
import star from '../img/star.png'
import PropsTypes from 'prop-types'
import './styles/MatchResults.css'

//takes in a number and renders stars according to that number
const MatchResults = ({ numberOfStars }) => {
    if (numberOfStars > 5){
        numberOfStars = 5;
    }
    var stars = [];
    for (var i = 0; i < numberOfStars; i++) {
        stars.push(<img className='star' key={i} src={star} alt='not found'></img>);
    }
    if(numberOfStars == 0){
        stars = 'Click Match to Get Result';
    }
    return (<div className='match-results'>{stars}</div>);
}

MatchResults.defaultProps = {
    numberOfStars: 0,
}
MatchResults.propsTypes = {
    numberOfStars: PropsTypes.number,
}

export default MatchResults