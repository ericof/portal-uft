/**
 * PersonList view component.
 * @module components/PersonList/PersonList
 */

import React from 'react';
import PropTypes from 'prop-types';
import { Card } from 'semantic-ui-react';
import PersonSummary from './PersonSummary';

/**
 * PersonList view component class.
 * @function PersonList
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PersonList = (props) => {
  const { items } = props;

  return (
    <Card.Group>
      {items.map((item) => (
        <PersonSummary content={item} />
      ))}
    </Card.Group>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
PersonList.propTypes = {
  items: PropTypes.arrayOf(
    PropTypes.shape({
      '@id': PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      description: PropTypes.string,
    }),
  ).isRequired,
};

export default PersonList;
