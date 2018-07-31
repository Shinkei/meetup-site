import { createStore, combineReducers, applyMiddleware, compose } from 'redux'
import createSagaMiddleware from 'redux-saga'
import { all } from 'redux-saga/effects'

import {
  reducer as loginReducer,
  saga as loginSaga
} from 'state-login'

const reducer = combineReducers({
  login: loginReducer
})

function * rootSaga () {
  yield all([
    loginSaga()
  ])
}

// Use compose function from devtools browser plugin if available
const enhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const sagaMiddleware = createSagaMiddleware()

const initialState = {}

export default createStore(reducer, initialState, enhancer(
  applyMiddleware(sagaMiddleware)
))

sagaMiddleware.run(rootSaga)
