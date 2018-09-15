import React from 'react'
import { reduxForm, Form } from 'redux-form'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { actions } from 'state/event'
import Toggle from 'material-ui/Toggle'
import EditableInput from './EditableInput'
import './Event.css'

class Event extends React.Component {
  constructor (props) {
    super(props)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleSubmit (event) {
    event.preventDefault()

    console.log(this.props)
  }

  render () {
    const { pristine, reset, submitting, toggleView, isAdmin, showEditionMode } = this.props
    return (
      <Form onSubmit={this.handleSubmit}>
        <div className='grid-container'>
          <div className='first-column' />
          <EditableInput type='header'
            className='middle-column'
            contentProp='titleContent'
            contentHint='name of the event'
          />
          <EditableInput type='combo'
            className='middle-column'
            titleProp='descriptionTitle'
            titleHint='header for event description'
            contentProp='desccriptionContent'
            contentHint='description of the event'
          />
          <EditableInput type='combo'
            className='middle-column'
            titleProp='agendaTitle'
            titleHint='header for event agenda'
            contentProp='agendaContent'
            contentHint='agenda of the event'
          />
          <EditableInput type='combo'
            className='middle-column'
            titleProp='presenterTitle'
            titleHint='header for event presenters'
            contentProp='presenter_content'
            contentHint='presenters of the event'
          />
          <EditableInput type='combo'
            className='middle-column'
            titleProp='requirementTitle'
            titleHint='header for event requirements'
            contentProp='requirementContent'
            contentHint='requirements for the event'
          />
          <div class='last-column'>
            {isAdmin && <Toggle toggled={showEditionMode} onToggle={toggleView} />}
            {showEditionMode &&
            <div>
              <button type='submit' disabled={pristine || submitting}>Submit</button>
              <button type='button' disabled={pristine || submitting} onClick={reset}>
                Clear Values
              </button>
            </div>
            }
          </div>
        </div>
      </Form>
    )
  }
}

Event.propTypes = {
  isAdmin: PropTypes.bool.isRequired,
  showEditionMode: PropTypes.bool.isRequired,
  toggleView: PropTypes.func.isRequired
}

export default reduxForm({form: 'event-form'})(connect(state => ({
  isAdmin: !!state.user.data && state.user.data.isAdmin,
  showEditionMode: state.event.showEditionMode
}), dispatch => ({
  toggleView: () => dispatch(actions.toggleView())
}))(Event))
