/**
 * CampusView view component.
 * @module components/View/CampusView
 */

import React from 'react';
import PropTypes from 'prop-types';
import { Image } from 'semantic-ui-react';
import EmailWidget from '@plone/volto/components/theme/Widgets/EmailWidget';
import PersonList from '@package/components/PersonList/PersonList';

const PreviewImage = ({ content }) => {
  const { image, image_caption } = content;
  const scale_name = 'preview';
  const scale = image.scales[scale_name];
  const { download } = scale;
  return (
    <Image
      src={download}
      alt={image_caption}
      size={'medium'}
      float={'right'}
      circular
    />
  );
};

/**
 * CampusView view component class.
 * @function CampusView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const CampusView = (props) => {
  const { content } = props;

  return (
    <div id="page-document" className="ui container viewwrapper person-view">
      <header>
        <h1 className="documentFirstHeading">{content.title}</h1>
      </header>
      <div className="ui card" style={{ width: '720px' }}>
        {content.image && (
          <div className="image">
            <PreviewImage content={content} />
          </div>
        )}
        <div className="content">
          {content.title && (
            <div className="header">Campus: {content.city.title}</div>
          )}
          <div>
            {content.description && (
              <div className="description">{content.description}</div>
            )}
          </div>
          <div>{content.city && <div>Cidade: {content.city.title}</div>}</div>
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
      <h2>People</h2>
      <div>
        <PersonList items={content.persons} />
      </div>
    </div>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
CampusView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    image: PropTypes.object,
    email: PropTypes.string.isRequired,
    extension: PropTypes.string.isRequired,
  }).isRequired,
};

export default CampusView;
