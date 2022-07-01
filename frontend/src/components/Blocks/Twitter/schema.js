import { defineMessages } from 'react-intl';

const messages = defineMessages({
  twitterBlock: {
    id: 'Twitter',
    defaultMessage: 'Twitter',
  },
  href: {
    id: 'URL',
    defaultMessage: 'URL',
  },
});

export const twitterSchema = (props) => {
  return {
    title: props.intl.formatMessage(messages.twitterBlock),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['href'],
      },
    ],

    properties: {
      href: {
        title: props.intl.formatMessage(messages.href),
      },
    },
    required: ['href'],
  };
};
