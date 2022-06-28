/**
 * PersonView view component.
 * @module components/View/PersonView
 */

import React from 'react';
import PropTypes from 'prop-types';
import EmailWidget from '@plone/volto/components/theme/Widgets/EmailWidget';
import { Image } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';

/**
 * PersonView view component class.
 * @function PersonView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PersonView = (props) => {
  const { content } = props;

  return (
    <div id="page-document" className="ui container viewwrapper person-view">
      <header>
        <h1 className="documentFirstHeading">{content.title}</h1>
      </header>
      <div className="ui card" style={{ width: '720px' }}>
        {content.image && (
          <div className="image">
            <Image
              src={content.image.scales.preview.download}
              alt={content.image_caption}
              size={'medium'}
              float={'right'}
              circular
            />
          </div>
        )}
        <div className="content">
          {content.title && (
            <div className="header">Person: {content.title}</div>
          )}
          <div>
            {content.description && (
              <div className="description">{content.description}</div>
            )}
          </div>
        </div>
        <div className="extra content">
          <div>
            {content.email && (
              <div>
                Email: <EmailWidget value={content.email} />
              </div>
            )}
          </div>
          <div>
            {content.extension && <div>Ramal: {content.extension}</div>}
          </div>
        </div>
      </div>
      <h2>Campus</h2>
      <div>
        <ul>
          {content.campus.map((item) => (
            <li>
              <UniversalLink href={item['@id']}>{item.title}</UniversalLink>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
PersonView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string,
    image: PropTypes.object,
    email: PropTypes.string.isRequired,
    extension: PropTypes.string.isRequired,
    campus: PropTypes.arrayOf(
      PropTypes.shape({
        '@id': PropTypes.string.isRequired,
        title: PropTypes.string.isRequired,
        description: PropTypes.string,
      }),
    ),
  }).isRequired,
};

export default PersonView;
