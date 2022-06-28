/**
 * PersonSummary view component.
 * @module components/PersonList/PersonSummary
 */

import React from 'react';
import PropTypes from 'prop-types';
import { Card } from 'semantic-ui-react';
import { Icon, UniversalLink } from '@plone/volto/components';
import userIcon from '@plone/volto/icons/user.svg';

/**
 * PersonSummary view component class.
 * @function PersonSummary
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PersonSummary = (props) => {
  const { content } = props;
  const url = content['@id'];
  return (
    <Card>
      <Icon name={userIcon} />
      <Card.Header>
        <UniversalLink href={url}>{content.title}</UniversalLink>
      </Card.Header>
      <Card.Description>{content.description}</Card.Description>
    </Card>
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
