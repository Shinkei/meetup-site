import React from 'react'
import { connect } from 'react-redux'
import { Field, getFormValues } from 'redux-form'
import PropTypes from 'prop-types'
import TextField from 'material-ui/TextField'

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

const ComboEdition = (props) => {
  return (
    <div>
      <Field
        className='input-field'
        name={props.titleProp}
        component={renderTextField}
        hintText={props.titleHint}
        type='text'
      />
      <Field
        className='input-field'
        name={props.contentProp}
        component={renderTextField}
        hintText={props.contentHint}
        multiLine
      />
    </div>
  )
}

ComboEdition.propTypes = {
  titleProp: PropTypes.string.isRequired,
  titleHint: PropTypes.string.isRequired,
  contentProp: PropTypes.string.isRequired,
  contentHint: PropTypes.string.isRequired
}

const ComboView = connect(state => ({
  values: getFormValues('event-form')(state)
}))(({titleProp, contentProp, values}) => {
  return (
    <div>
      <h4>{values && values[titleProp]}</h4>
      <p>{values && values[contentProp]}</p>
    </div>
  )
})

ComboView.propTypes = {
  titleProp: PropTypes.string.isRequired,
  contentProp: PropTypes.string.isRequired
}

const HeaderEdition = (props) => {
  return (
    <Field
      className='input-field'
      name={props.contentProp}
      component={renderTextField}
      hintText={props.contentHint}
      type='text'
    />
  )
}

HeaderEdition.propTypes = {
  contentProp: PropTypes.string.isRequired,
  contentHint: PropTypes.string.isRequired
}

const HeaderView = connect(state => ({
  values: getFormValues('event-form')(state)
}))(({contentProp, values}) => {
  return (
    <div>
      <h2>{values && values[contentProp]}</h2>
    </div>
  )
})

HeaderView.propTypes = {
  contentProp: PropTypes.string.isRequired
}

const component = {
  combo: {
    edition: ComboEdition,
    view: ComboView
  },
  header: {
    edition: HeaderEdition,
    view: HeaderView
  }
}

const EditableInput = (props) => {
  const {type, showEditionMode} = props
  const Element = component[type][showEditionMode ? 'edition' : 'view']
  return (
    <Element {...props} />
  )
}

EditableInput.propTypes = {
  type: PropTypes.oneOf(Object.keys(component)).isRequired,
  showEditionMode: PropTypes.bool.isRequired
}

export default connect(state => ({
  showEditionMode: state.event.showEditionMode
}))(EditableInput)
