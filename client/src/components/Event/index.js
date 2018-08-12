import React from 'react'
import { reduxForm } from 'redux-form'
import EditableInput from './EditableInput'

const Event = ({ pristine, reset, submitting }) =>{
  return (
    <form onSubmit={handleSubmit}>
      <EditableInput isEditionMode={true}
        titleProp="detail_title"
        titleLabel="Detalles"
        inputProp="detail_input"
        inputLabel="Contenido"/>
      <EditableInput isEditionMode={true}
        titleProp="agenda_title"
        titleLabel="Itinerario"
        inputProp="agenda_input"
        inputLabel="Contenido"/>
      <div>
        <button type="submit" disabled={pristine || submitting}>Submit</button>
        <button type="button" disabled={pristine || submitting} onClick={reset}>
          Clear Values
        </button>
      </div>
    </form>
  )
}

const handleSubmit = (values) => {

  console.log(values)
}

export default reduxForm({form:'event-form'})(Event)
