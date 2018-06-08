import React, {Component} from 'react'
import PropTypes from 'prop-types'
import loadGoogleMapsAPI from 'load-google-maps-api'

const API_CONFIG = {
  key: process.env.REACT_APP_MAPS_KEY,
  language: 'es'
}

const MAP_STYLES = {
  height: '450px',
  width: '100%'
}

class GeoInformation extends Component {
  componentDidMount () {
    
    const center= {
      lat:this.props.latitude,
      lng:this.props.longitude
    };

    const options = {
      center,
      zoom: this.props.zoom    
    }

    loadGoogleMapsAPI(API_CONFIG).then(googleMaps => {
      const map = new googleMaps.Map(this.refs.map, options)
      new googleMaps.Marker({position:center, map})
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

GeoInformation.propTypes = {
  latitude: PropTypes.number.isRequired,
  longitude: PropTypes.number.isRequired,
  zoom: PropTypes.number.isRequired
}

export default GeoInformation
