import { extractTweetId } from './Twitter';

describe('Twitter', () => {
  describe('extractTweetId', () => {
    it('can find the tweetId from a full url', () => {
      expect(
        extractTweetId(
          'https://twitter.com/ploneconf/status/1542568225527005184?s=20&t=vY2P0U5rhI6hjdOBVQxDlg',
        ),
      ).toBe('1542568225527005184');
    });
  });
});
