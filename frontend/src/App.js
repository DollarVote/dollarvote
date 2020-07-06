import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route, Link } from 'react-router-dom'
import './styles.css';
import  CustomersList from './CustomersList'
import  CustomerCreateUpdate  from './CustomerCreateUpdate'
import './App.css';
import CompanyCard from './CompanyCard';
import Button from './components/button';
import {Paragraph, Tablist, Tab, Pane, SearchInput, Heading} from 'evergreen-ui';


class App extends Component {
  render() {
    return (
      <div>
        <div className="header">
          <h1 className="title">Dollar Vote</h1>
          <br></br>
          <h3 className="subtitle">It’s time to incorporate activism and advocacy into our daily lives.</h3> 
          <h3 className="subtitle-bold">Hold yourself accountable to your spending habits.</h3>
        </div>
        <div className="main">
          <CompanyCard></CompanyCard>
          <div className="impact-blurb">
          <SearchInput marginBottom={20} width={400} placeholder="Try searching for a company" height={40} marginTop={40}/>
            <h3>See the impact that companies are making before you hand over $$$</h3> <br></br>
            <p>
            Companies donate millions of dollars to political causes. We’ll tell you what these causes are.

            Public and freely accessible data such FEC, SEC, and USPTO filings offer insight into lobbying activity, how much top executives are paid, which companies own which brands, and more.</p>
            <a href="https://www.google.com" className="main-link">see how we calculate impact</a><br/>
            <Button>Chrome Extension</Button>
          </div>
        </div>
          <div className="impact-blurb">
            <h3>Track your own impact and make donations part of your budget.</h3>
            <br></br>
            <p>
            It’s better to shop fromm black owned businesses, shop secondhand, shop local, or even not shop at all, when we can. <br></br><br></br>
            Being aware of our impact as we’re changing our habits is the first step. 
            This tool is meant to help us hold ourselves accountable to putting our money where our mouths are.
            </p>
            <a href="https://www.google.com" className="main-link">see how we calculate impact</a><br/>
            <Button>Chrome Extension</Button>
          </div>
      </div>
    );
  }
}

export default App;