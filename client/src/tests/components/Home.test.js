import React from 'react'
import ReactDOM from 'react-dom'
import Home from '../../components/Home'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

describe('Home Component', () => {
  it('renders without crashing', () => {
	  const div = document.createElement('div')
	  ReactDOM.render(<MuiThemeProvider><Home /></MuiThemeProvider>, div)
	  ReactDOM.unmountComponentAtNode(div)
  })
})
