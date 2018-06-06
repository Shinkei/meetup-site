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
          <GeoInformation 
            direccion="Calle falsa 123"
            latitude={6.2647816}
            longitud={-75.5705099}
            zoom={16}/>
        </div>
      </article>
    )
  }
}

export default Home
