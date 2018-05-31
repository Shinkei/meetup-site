import React, { Component } from 'react'
import logo from './logo.svg'
import './App.css'
import Home from './components/Home'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

class App extends Component {
  render () {
    return (
      <MuiThemeProvider>
        <Home title="Coding Dojo" description="coding dojo description"/>
      </MuiThemeProvider>
    )
  }
}

export default App
