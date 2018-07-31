import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import React, { Component } from 'react'
import { Provider } from 'react-redux'

import 'App.css'
import Home from 'components/Home'
import store from 'store'

class App extends Component {
  render () {
    return (
      <MuiThemeProvider>
        <Provider store={store}>
          <Home />
        </Provider>
      </MuiThemeProvider>
    )
  }
}

export default App
