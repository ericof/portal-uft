export const extractTweetId = (value) => {
  const re = /\/status\/(\d+)/g;
  const match = re.exec(value);
  if (match) {
    return match[match.length - 1];
  }
};
