import React, { Component } from 'react'
import './App.css'
import Home from './components/Home'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

class App extends Component {
  render () {
    const title = process.env.REACT_APP_TITLE; 
    const description = process.env.REACT_APP_DESCRIPTION;
    return (
      <MuiThemeProvider>
        <Home title={title} description={description}/>
      </MuiThemeProvider>
    )
  }
}

export default App
