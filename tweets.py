import db


def get_all_tweets():
  return db.get_all_tweets()


def add_tweet(tweet, username):
  return db.create_tweets(tweet, username)


def get_tweets_by_username(username):
  return db.get_tweets_by_username(username)
