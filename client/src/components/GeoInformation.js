import React, {Component} from 'react'
import loadGoogleMapsAPI from 'load-google-maps-api'

const OPTIONS = {
  center: {
    lat: 6.2647816,
    lng: -75.5705099
  },
  zoom: 16
}

const API_CONFIG = {
  key: 'AIzaSyAuBEdfk-djsMYt8nSkNHUPplqrokZ4UPY',
  language: 'es'
}

const MAP_STYLES = {
  height: '450px',
  width: '100%'
}

class GeoInformation extends Component {
  componentDidMount () {
    loadGoogleMapsAPI(API_CONFIG).then(googleMaps => {
      new googleMaps.Map(this.refs.map, OPTIONS)
    }).catch(err => {
      console.warning('Something went wrong loading the map', err)
    })
  }

  render () {
    return (
      <article>
        <h3>Ubicacion</h3>
        <h4>Dirección</h4>
        <p>{this.props.direccion}</p>
        <div ref='map' style={MAP_STYLES} />
      </article>
    )
  }
}

export default GeoInformation
