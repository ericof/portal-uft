/**
 * PersonSummary view component.
 * @module components/PersonList/PersonSummary
 */

import React from 'react';
import PropTypes from 'prop-types';
import { List } from 'semantic-ui-react';

/**
 * PersonSummary view component class.
 * @function PersonSummary
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PersonSummary = (props) => {
  const { content } = props;

  return (
    <List.Item>
      <List.Icon name="user" size="large" verticalAlign="middle" />
      <List.Content>
        <List.Header>{content.title}</List.Header>
        <List.Description>{content.description}</List.Description>
      </List.Content>
    </List.Item>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
PersonSummary.propTypes = {
  content: PropTypes.shape({
    '@id': PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string,
  }).isRequired,
};

export default PersonSummary;
