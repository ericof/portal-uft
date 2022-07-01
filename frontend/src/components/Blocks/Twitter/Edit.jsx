import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers';
import { SidebarPortal } from '@plone/volto/components';
import TwitterBlockData from './Data';
import TwitterBlockView from './View';

const TwitterBlockEdit = (props) => {
  const { data, onChangeBlock, block, selected } = props;
  return (
    <>
      <TwitterBlockView {...props} isEditMode />
      <SidebarPortal selected={selected}>
        <TwitterBlockData
          data={data}
          block={block}
          onChangeBlock={onChangeBlock}
        />
      </SidebarPortal>
    </>
  );
};

export default withBlockExtensions(TwitterBlockEdit);
