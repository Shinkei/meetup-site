import AppBar from 'material-ui/AppBar'
import React, { Component } from 'react'

import LoginButton from 'components/LoginButton'

class Home extends Component {
  render () {
    return (
      <article>
        <AppBar
          title={process.env.TITLE}
          showMenuIconButton={false}
          iconElementRight={<LoginButton />}
          />
      </article>
    )
  }
}

export default Home
