import React, { Component } from 'react'
import AppBar from 'material-ui/AppBar'
import GeoInformation from './GeoInformation'

class Home extends Component {
  render () {
    return (
      <article>
        <AppBar showMenuIconButton={false} />
        <h1>{this.props.title}</h1>
        <p>{this.props.description}</p>
        <GeoInformation />
      </article>
    )
  }
}

export default Home
