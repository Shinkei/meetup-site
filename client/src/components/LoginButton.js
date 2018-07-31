import FlatButton from 'material-ui/FlatButton';
import React from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { actions } from 'state-login'

const LoginButton = ({isUserAuthenticated, attemptLogin}) => (
  isUserAuthenticated ? 'YES'
  : <FlatButton
      onClick={attemptLogin}
      label='Log In'
      />
)

LoginButton.propTypes = {
  isUserAuthenticated: PropTypes.bool.isRequired,
  attemptLogin: PropTypes.func.isRequired
}

export default connect(state => ({
  isUserAuthenticated: state.login.isAuthenticated
}), dispatch => ({
  attemptLogin: () => {
    window.open(`${process.env.API_BASE_URL}/login`)
    dispatch(actions.attemptLogin())
  }
}))(LoginButton)
