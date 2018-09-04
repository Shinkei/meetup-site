import {
  LOGIN_ERROR,
  SAVE_EVENT_ATTEMPT,
  SAVE_EVENT_ERROR,
  SAVE_EVENT_SUCCESS,
  TOGGLE_EVENT_MODE
} from 'action-types'
import request from 'api-client'

import { call, put, takeEvery, all } from 'redux-saga/effects'

const initialState = {
  isLoading: false,
  showEditionMode: false,
  current: null,
  data: null,
  error: null
}

const actionHandlers = {
  [TOGGLE_EVENT_MODE]: (state) => ({
    ...state,
    showEditionMode: !state.showEditionMode
  }),
  [SAVE_EVENT_ATTEMPT]: (state) => ({
    ...state,
    isLoading: true,
    error: null
  }),
  [SAVE_EVENT_ERROR]: (state, {error: {message: error}}) => ({
    ...state,
    isLoading: false,
    error
  })
}

export const reducer = (state = initialState, action) => {
  const {type, ...payload} = action
  const actionHandler = actionHandlers[type]
  if (!actionHandler) return state
  return actionHandler(state, payload)
}

export const actions = {
  toggleView () {
    return {type: TOGGLE_EVENT_MODE}
  }
}

export function * saveEvent () {
}

export function * saga () {
  yield all([
    takeEvery(SAVE_EVENT_ATTEMPT, saveEvent)
  ])
}
