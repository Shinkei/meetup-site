import React from 'react'
import { reduxForm, Form, getFormValues } from 'redux-form'
import { connect } from 'react-redux'
import EditableInput from './EditableInput'
import './Event.css'

class Event extends React.Component {
  constructor (props) {
    super(props)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleSubmit (event) {
    event.preventDefault()
    debugger
    console.log(this.props.values)
  }

  render () {
    const { pristine, reset, submitting } = this.props
    return (
      <Form className='container' onSubmit={this.handleSubmit}>
        <div>
          <EditableInput isEditionMode
            titleProp='detail_title'
            titleHint='Titulo del campo de Detalles'
            inputProp='detail_input'
            inputHint='Contenido del campo de Detalles' />
          <EditableInput isEditionMode
            titleProp='agenda_title'
            titleHint='Titulo del campo de Itinerario'
            inputProp='agenda_input'
            inputHint='Contenido del campo de Itinerario' />
        </div>
        
        <div>
          <button type='submit' disabled={pristine || submitting}>Submit</button>
          <button type='button' disabled={pristine || submitting} onClick={reset}>
            Clear Values
          </button>
        </div>
      </Form>
    )
  }
}

export default reduxForm({form: 'event-form'})(connect(state => ({
  values: getFormValues('event-form')(state)
}))(Event))
