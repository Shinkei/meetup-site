import React from 'react'
import renderer from 'react-test-renderer'
import GeoInformation from '../../components/GeoInformation'

describe('GeoInformation Component', () => {
  it('should not regress', () => {
    const tree = renderer.create(<GeoInformation />).toJSON()
    expect(tree).toMatchSnapshot()
  })
})
