import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers';
import { Card } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';

const CampusBlockView = (props) => {
  const { data } = props;
  const campus =
    data.href !== undefined && data.href.length === 1 ? data.href[0] : null;
  return (
    <>
      {campus && (
        <Card>
          <Card.Header>
            <UniversalLink href={campus['@id']}>{campus.title}</UniversalLink>
          </Card.Header>
          <Card.Description>{campus.Description}</Card.Description>
        </Card>
      )}
    </>
  );
};

export default withBlockExtensions(CampusBlockView);
