import React from 'react'
import { Field, reduxForm } from 'redux-form'
import PropTypes from 'prop-types'
import TextField from 'material-ui/TextField'

const FieldTitle = (props) =>{
  return (
    props.isEditionMode? <EditionMode {...props} /> : <ViewMode {...props} />
  )
}

const EditionMode = (props) => {
  return (
    <div>
      <Field name="titleInput" component={TextField} type="text" floatingLabelText="title"/>
      <br/>
      <Field name="contentInput" component={TextField} multiLine={true} floatingLabelText="content"/>
    </div>
  )
}

const ViewMode = (props) => {
  return (
    <div>
      <h4>{props.labelValue}</h4>
      <p>{props.fieldValue}</p>
    </div>
  )
}

EditionMode.propTypes = {
  labelName: PropTypes.string.isRequired,
  fieldName: PropTypes.string.isRequired
}


export default reduxForm()(FieldTitle)