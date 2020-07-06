import React from 'react';
import './styles/basics.css';

class Bookmark extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div className="bookmark">
                <p>IMPACT SCORE</p>
                <h3>-1.0</h3>
            </div>
        )
    }
}

export default Bookmark;