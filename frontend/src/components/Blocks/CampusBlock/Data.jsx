import React from 'react';
import { BlockDataForm } from '@plone/volto/components';
import { campusSchema } from './schema';
import { useIntl } from 'react-intl';

const CampusBlockData = (props) => {
  const { data, block, onChangeBlock } = props;
  const intl = useIntl();
  const schema = campusSchema({ ...props, intl });

  return (
    <BlockDataForm
      schema={schema}
      title={schema.title}
      onChangeField={(id, value) => {
        onChangeBlock(block, {
          ...data,
          [id]: value,
        });
      }}
      formData={data}
      block={block}
    />
  );
};

export default CampusBlockData;
