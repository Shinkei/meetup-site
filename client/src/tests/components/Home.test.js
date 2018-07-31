import { store }  from 'tests/common.mock'
import 'tests/localStorage.mock'

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'

import Home from 'components/Home'

describe('Home Component', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div')
    ReactDOM.render(<MuiThemeProvider><Provider store={store}><Home /></Provider></MuiThemeProvider>, div)
    ReactDOM.unmountComponentAtNode(div)
  })
})
