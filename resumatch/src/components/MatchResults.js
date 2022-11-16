import React from 'react'
import star from '/dist/star.png'
import PropsTypes from 'prop-types'
import './styles/MatchResults.css'

const MatchResults = ({ numberOfStars }) => {
    var stars = [];
    for (var i = 0; i < numberOfStars; i++) {
        stars.push(<img className='star' key={i} src={star} alt='not found'></img>);
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