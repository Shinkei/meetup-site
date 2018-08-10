import {
  FETCH_USER_ATTEMPT,
  FETCH_USER_ERROR,
  FETCH_USER_SUCCESS
} from 'action-types'
import { fetchUser, loginHandler } from 'state-user'

import { call } from 'redux-saga/effects'
import { expectSaga } from 'redux-saga-test-plan'
import { throwError } from 'redux-saga-test-plan/providers'

it('fetches the user', () => {
  const mockResponse = {data: {me: {fullName: 'Foo Bar', avatar: 'img...'}}}
  return expectSaga(loginHandler)
    .provide([[call(fetchUser), {data: mockResponse}]])
    .put({type: FETCH_USER_ATTEMPT})
    .put({type: FETCH_USER_SUCCESS, ...mockResponse.data})
    .run()
})

it('handles errors', () => {
  const mockError = new Error('error')
  return expectSaga(loginHandler)
    .provide([[call(fetchUser), throwError(mockError)]])
    .put({type: FETCH_USER_ATTEMPT})
    .put({type: FETCH_USER_ERROR, error: mockError})
    .run()
})
