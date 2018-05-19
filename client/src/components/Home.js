import AppBar from 'material-ui/AppBar'
import React, { Component } from 'react'

import GeoInformation from 'GeoInformation'
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
	<GeoInformation />
      </article>
    )
  }
}

export default Home
