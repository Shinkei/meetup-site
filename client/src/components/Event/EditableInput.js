import React from 'react'
import { Field } from 'redux-form'
import PropTypes from 'prop-types'
import TextField from 'material-ui/TextField'

const EditableInput = (props) =>{
  return (
    props.isEditionMode? <EditionMode {...props} /> : <ViewMode {...props} />
  )
}

const EditionMode = (props) => {
  return (
    <div>
      <Field name={props.titleProp} component={renderTextField} type="text" floatingLabelText={props.titleLabel}/>
      <br/>
      <Field name={props.inputProp} component={renderTextField} multiLine={true} floatingLabelText={props.inputLabel}/>
    </div>
  )
}

const ViewMode = (props) => {
  return (
    <div>
      <h4>{props.titleContent}</h4>
      <p>{props.inputContent}</p>
    </div>
  )
}

const renderTextField = ({
  input,
  label,
  meta: { touched, error },
  ...custom
}) => (
  <TextField
    hintText={label}
    floatingLabelText={label}
    errorText={touched && error}
    {...input}
    {...custom}
  />
)

EditableInput.propTypes = {
  isEditionMode: PropTypes.bool.isRequired
}

EditionMode.propTypes = {
  titleProp: PropTypes.string.isRequired,
  inputProp: PropTypes.string.isRequired,
  titleLabel: PropTypes.string.isRequired,
  inputLabel: PropTypes.string.isRequired
}

ViewMode.propTypes = {
  titleContent: PropTypes.string.isRequired,
  inputContent: PropTypes.string.isRequired
}


export default EditableInput