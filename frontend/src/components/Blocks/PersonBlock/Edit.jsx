import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers';
import { SidebarPortal } from '@plone/volto/components';
import PersonBlockData from './Data';
import PersonBlockView from './View';

const PersonBlockEdit = (props) => {
  const { data, onChangeBlock, block, selected } = props;

  return (
    <>
      <PersonBlockView {...props} isEditMode />
      <SidebarPortal selected={selected}>
        <PersonBlockData
          data={data}
          block={block}
          onChangeBlock={onChangeBlock}
        />
      </SidebarPortal>
    </>
  );
};

export default withBlockExtensions(PersonBlockEdit);
