import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers';
import { Card, Image } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';

const PersonImage = ({ content }) => {
  const { image, image_scales, title } = content;
  let download =
    'https://react.semantic-ui.com/images/avatar/large/matthew.png';
  if (image || image_scales) {
    const base_image = image ? image : image_scales.image[0];
    const scale_name = 'preview';
    const scale = base_image.scales[scale_name];
    download = scale.download;
    if (download.startsWith('@@')) {
      download = `${content['@id']}/${download}`;
    }
  }
  return <Image src={download} alt={title} wrapped ui={false} />;
};

const PersonBlockView = (props) => {
  const { data } = props;
  const person =
    data.href !== undefined && data.href.length === 1 ? data.href[0] : null;
  return (
    <>
      {person && (
        <Card>
          <PersonImage content={person} />
          <Card.Header>
            <UniversalLink href={person['@id']}>{person.title}</UniversalLink>
          </Card.Header>
          <Card.Description>{person.Description}</Card.Description>
        </Card>
      )}
    </>
  );
};

export default withBlockExtensions(PersonBlockView);
