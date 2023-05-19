tweets = []


def get_all_tweets():
  return tweets


def add_tweet(tweet, username):
  t = {'username': username, 'tweet': tweet}
  return tweets.append(t)


def get_tweets_by_username(username):
  #create a new list for the matching tweets
  user_tweets = []
  #iterate the list of tweets one by one
  for tweet in tweets:
    if tweet['username'] == username:
      user_tweets.append(tweet)

  #if the username matches include the tweet in the new list
  #return the new list of tweets
  return user_tweets
