import AppBar from 'material-ui/AppBar'
import React, { Component } from 'react'

import LoginButton from 'components/LoginButton'
import Event from './Event';

class Home extends Component {
  render () {
    return (
      <article>
        <AppBar
          title={process.env.TITLE}
          showMenuIconButton={false}
          iconElementRight={<LoginButton />}
        />
        <Event/>
      </article>
    )
  }
}

export default Home
