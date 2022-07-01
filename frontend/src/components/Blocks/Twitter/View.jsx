import React from 'react';
import { extractTweetId } from '@package/helpers';
import { withBlockExtensions } from '@plone/volto/helpers';
import { TwitterTweetEmbed } from 'react-twitter-embed';

const TwitterBlockView = (props) => {
  const { data } = props;
  const tweetId = extractTweetId(data.href);
  return <>{tweetId && <TwitterTweetEmbed tweetId={tweetId} />}</>;
};

export default withBlockExtensions(TwitterBlockView);
