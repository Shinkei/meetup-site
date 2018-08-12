import { createStore, combineReducers, applyMiddleware, compose } from 'redux'
import { reducer as formReducer } from 'redux-form'
import createSagaMiddleware from 'redux-saga'
import { all } from 'redux-saga/effects'

import {
  actions as loginActions,
  reducer as loginReducer,
  saga as loginSaga
} from 'state-login'
import {
  reducer as userReducer,
  saga as userSaga
} from 'state-user'

const reducer = combineReducers({
  login: loginReducer,
  user: userReducer,
  form: formReducer
})

function * rootSaga () {
  yield all([
    loginSaga(),
    userSaga()
  ])
}

// Use compose function from devtools browser plugin if available
const enhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const sagaMiddleware = createSagaMiddleware()

const initialState = {}

const store = createStore(reducer, initialState, enhancer(
  applyMiddleware(sagaMiddleware)
))

sagaMiddleware.run(rootSaga)

// Update login state on page load
if (window.localStorage.getItem('auth_token')) {
  store.dispatch(loginActions.restoreLogin())
}

export default store
