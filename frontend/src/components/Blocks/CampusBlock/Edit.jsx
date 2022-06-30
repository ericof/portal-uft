import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers';
import { SidebarPortal } from '@plone/volto/components';
import CampusBlockData from './Data';
import CampusBlockView from './View';

const CampusBlockEdit = (props) => {
  const { data, onChangeBlock, block, selected } = props;

  return (
    <>
      <CampusBlockView {...props} isEditMode />
      <SidebarPortal selected={selected}>
        <CampusBlockData
          data={data}
          block={block}
          onChangeBlock={onChangeBlock}
        />
      </SidebarPortal>
    </>
  );
};

export default withBlockExtensions(CampusBlockEdit);
