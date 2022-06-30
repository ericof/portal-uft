import { defineMessages } from 'react-intl';

const messages = defineMessages({
  campusBlock: {
    id: 'Campus Block',
    defaultMessage: 'Campus Block',
  },
  campus: {
    id: 'Campus',
    defaultMessage: 'Campus',
  },
});

export const campusSchema = (props) => {
  return {
    title: props.intl.formatMessage(messages.campusBlock),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['href'],
      },
    ],

    properties: {
      href: {
        title: props.intl.formatMessage(messages.campus),
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description'],
        widgetOptions: {
          pattern_options: { selectableTypes: ['campus'] },
        },
        allowExternals: false,
      },
    },
    required: ['href'],
  };
};
