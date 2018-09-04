import {
  LOGIN_ATTEMPT,
  LOGIN_ERROR,
  LOGIN_SUCCESS
} from 'action-types'

import { eventChannel, END } from 'redux-saga'
import { call, take, put, takeEvery, all } from 'redux-saga/effects'

const initialState = {
  isLoading: false,
  isAuthenticated: false,
  error: null
}

const actionHandlers = {
  [LOGIN_ATTEMPT]: () => ({
    ...initialState,
    isLoading: true
  }),
  [LOGIN_ERROR]: (state, {error: {message: error}}) => ({
    ...initialState,
    error
  }),
  [LOGIN_SUCCESS]: () => ({
    ...initialState,
    isAuthenticated: true
  })
}

export const reducer = (state = initialState, action) => {
  const {type, ...payload} = action
  const actionHandler = actionHandlers[type]
  if (!actionHandler) return state
  return actionHandler(state, payload)
}

export const actions = {
  attemptLogin () {
    return {type: LOGIN_ATTEMPT}
  },
  restoreLogin () {
    return {type: LOGIN_SUCCESS}
  }
}

const loginEvents = () => {
  return eventChannel(emitter => {
    const DOMAIN = process.env.API_BASE_URL

    const eventMethod = window.addEventListener ? 'addEventListener' : 'attachEvent'
    const removeMethod = window.addEventListener ? 'removeEventListener' : 'detachEvent'
    const addListener = window[eventMethod]
    const removeListener = () => window[removeMethod](MESSAGE_EVENT, messageHandler)
    const MESSAGE_EVENT = eventMethod === 'attachEvent' ? 'onmessage' : 'message'
    /*
     * Process incomming messages. The method receives an object containing:
     * data   object Object received
     * origin string URI with protocol, hostname and port
     * source object Reference to window object
     */
    function messageHandler (ev) {
      if (ev.origin !== DOMAIN) return
      if (ev.data.type === 'auth_success') {
        removeListener()
        ev.source.postMessage({type: 'close_window'}, DOMAIN)
        window.localStorage.setItem('auth_token', ev.data.token)
        emitter({type: LOGIN_SUCCESS})
        emitter(END)
      }
    }
    addListener(MESSAGE_EVENT, messageHandler, false)
    setTimeout(() => {
      removeListener()
      emitter({type: LOGIN_ERROR, error: new Error('LOGIN TIMED OUT')})
      emitter(END)
    }, 30000)
    return () => removeListener()
  })
}

function * loginHandler () {
  const channel = yield call(loginEvents)
  try {
    while (true) {
      const action = yield take(channel)
      yield put(action)
    }
  } finally {
    console.log('login flow ended')
  }
}

export function * saga () {
  yield all([
    takeEvery(LOGIN_ATTEMPT, loginHandler)
  ])
}
