import {
  LOGIN_ERROR,
  LOGIN_SUCCESS,
  FETCH_USER_ATTEMPT,
  FETCH_USER_ERROR,
  FETCH_USER_SUCCESS
} from 'action-types'
import request from 'api-client'

import { call, put, takeEvery, all } from 'redux-saga/effects'

const initialState = {
  isLoading: false,
  data: null,
  error: null
}

const actionHandlers = {
  [FETCH_USER_ATTEMPT]: (state) => ({
    ...state,
    isLoading: true,
    error: null
  }),
  [FETCH_USER_ERROR]: (state, {error: {message: error}}) => ({
    ...state,
    isLoading: false,
    error
  }),
  [FETCH_USER_SUCCESS]: (state, {me}) => ({
    ...initialState,
    data: me
  })
}

export const reducer = (state = initialState, action) => {
  const {type, ...payload} = action
  const actionHandler = actionHandlers[type]
  if (!actionHandler) return state
  return actionHandler(state, payload)
}

export const fetchUser = () => {
  return request(`
    query CurrentUser {
      me {
        name,
        avatarUrl,
        isAdmin
      }
    }
  `)
}

export function * loginHandler () {
  yield put({type: FETCH_USER_ATTEMPT})
  try {
    const res = yield call(fetchUser)
    if (res.data.errors) {
      let type
      for (let error of res.data.errors) {
        type = error.message === 'Authentication failed' ? LOGIN_ERROR : FETCH_USER_ERROR
        yield put({type, error})
      }
      return
    }
    const {data: {data}} = res
    yield put({type: FETCH_USER_SUCCESS, ...data})
  } catch (error) {
    yield put({type: FETCH_USER_ERROR, error})
  }
}

export function * saga () {
  yield all([
    takeEvery(LOGIN_SUCCESS, loginHandler)
  ])
}
