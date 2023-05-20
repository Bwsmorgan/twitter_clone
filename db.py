import sqlite3

conn = sqlite3.connect('tweets.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
  '''CREATE TABLE IF NOT EXISTS tweets (_id integer primary key autoincrement, tweets text, username text)'''
)
conn.commit()


def create_tweets(tweets, username):

  cursor.execute('INSERT INTO tweets VALUES (NULL, :tweets, :username)', {
    'tweets': tweets,
    'username': username
  })
  conn.commit


def get_all_tweets():

  cursor.execute('SELECT * FROM tweets')
  tweets = cursor.fetchall()

  return tweets


def get_tweets_by_username(username):

  cursor.execute('SELECT * FROM tweets WHERE username = :username',
                 {'username': username})
  tweets = cursor.fetchmany(10)

  return tweets