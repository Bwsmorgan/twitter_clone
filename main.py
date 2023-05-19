from flask import Flask, request, redirect, url_for, render_template
from tweets import get_all_tweets, add_tweet, get_tweets_by_username

app = Flask(__name__)
# GLOBAL VARIABLE
current_user = '' 


def get_html_form(action, header, field_title, name, button_value):
  return render_template('form.html',
                         action=action,
                         header=header,
                         field_title=field_title,
                         name=name,
                         button_value=button_value)


@app.route('/')
def index():
  # if user is logged in redirect to tweet page
  if current_user:
    return redirect(url_for('tweet'))
  # if user is not logged in go to login page
  else:
    return render_template('form.html',
                           action='/login',
                           header='Please Login',
                           field_title='Username',
                           name='username',
                           button_value='Login')


@app.route('/login', methods=['POST'])
def login():
  global current_user
  current_user = request.form['username']
  return redirect(url_for('tweet'))
  # username = request.form.get('username')
  # return f'current user name is {current_user}'


#remove the current_user
#redirect to home page
@app.route('/logout')
def logout():
  global current_user
  current_user = ''
  return redirect(url_for('index'))
  # username = request.form.get('username')
  # return f'current user name is {current_user}'
  # index is our main page (/)


@app.route('/tweet')
def tweet():

  return render_template('form.html',
                         action='/save_tweet',
                         header='what is happening?',
                         field_title='Tweet',
                         name='tweet',
                         button_value='Tweet')


@app.route('/save_tweet', methods=['POST'])
def contact():
  tweet = request.form['tweet']
  add_tweet(tweet, current_user)
  return 'Successfully recieved tweet ' + tweet


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
  for tweet in get_tweets_by_username(username):
    return render_template('tweets.html', tweets = tweets, current_user = current_user)

 