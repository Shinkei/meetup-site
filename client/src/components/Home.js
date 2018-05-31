import React, { Component } from 'react'
import AppBar from 'material-ui/AppBar'
import GeoInformation from './GeoInformation'
import './Home.css';

class Home extends Component {
  render () {
    return (
      <article>
        <AppBar showMenuIconButton={false} />
        <div className="container">
          <h1 className="title">{this.props.title}</h1>
          <p className="description">{this.props.description}</p>
          <GeoInformation direccion="Calle falsa 123"/>
        </div>
      </article>
    )
  }
}

export default Home
