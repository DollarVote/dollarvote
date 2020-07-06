import React from 'react';
import { useState, getState } from 'react';
import PropTypes from 'prop-types';
import {Paragraph, Tablist, Tab, Pane, SearchInput, Heading} from 'evergreen-ui';
import Bookmark from './components/bookmark';
import PopoverContent from './PopoverContent.js';
import './styles/popover.css';
import { Container, Row, Col } from 'reactstrap';
import Button from './components/button';

function CompanyCard(props) {
    // const state = useState({
    //   selectedIndex: 0,
    //   tabs: ['Traits', 'Event History', 'Identities']}
    // )
    
    return (
        <div>
        <Pane width={400} padding={20} margin={16} elevation={2} borderRadius={10}
          >
            
            <Pane flex="1" marginBottom={20}>
                <Pane>
                <Bookmark></Bookmark>
                <h3 className="company-title">Evil Company </h3>
                    <PopoverContent 
                        title="issue"
                        blm={1}
                        climate={0.5}
                        healthcare={0.2} 
                    />
                </Pane>
            </Pane>
            {/* <Button></Button> */}
            {/* <Tablist marginTop={16} flexBasis={240} marginRight={24}>
                <Tab
                backgroundColor="tint1"
                  key='hi'
                  id='hi'
                  isSelected={0}
                >
                  view company
                </Tab>
                <Tab
                background="tint1"
                  key='hi'
                  id='hi'
                  isSelected={0}
                >
                  track purchase
                </Tab>
            </Tablist> */}
          </Pane>
          </div>
        )
}

export default CompanyCard;