import { defineMessages } from 'react-intl';

const messages = defineMessages({
  personBlock: {
    id: 'Person Block',
    defaultMessage: 'Person Block',
  },
  person: {
    id: 'Person',
    defaultMessage: 'Person',
  },
});

export const personSchema = (props) => {
  return {
    title: props.intl.formatMessage(messages.personBlock),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['href'],
      },
    ],

    properties: {
      href: {
        title: props.intl.formatMessage(messages.person),
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description', 'image_scales'],
        widgetOptions: {
          pattern_options: { selectableTypes: ['person'] },
        },
        allowExternals: false,
      },
    },
    required: ['href'],
  };
};
