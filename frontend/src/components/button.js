

import React from 'react';
import './styles/basics.css';
import { Container, Row, Col } from 'reactstrap';


class Button extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div className="buttons">
            <a href="https://www.google.com" className="link"><div className="slab-button left">sup</div></a>
            <a href="https://www.google.com" className="link"><div className="slab-button right">up</div></a>
            </div>
        )
    }
}

export default Button;