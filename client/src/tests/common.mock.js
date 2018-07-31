import configureStore from 'redux-mock-store'

const initialState = {
  login: {
    isAuthenticated: false
  }
}

export const store = configureStore()(initialState)
