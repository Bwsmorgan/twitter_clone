from flask import Flask, request, redirect, url_for, render_template, session
from tweets import add_tweet, get_all_tweets, get_tweets_by_username
from users import create_user, password_match, get_user_by_username

app = Flask(__name__)
app.secret_key = 'OurSuperSecretSessionSecret'

from db import init

init()


def get_html_form(action, header, fieldtitle, fieldname, buttonvalue):
  return render_template('form.html',
                         action=action,
                         header=header,
                         fieldtitle=fieldtitle,
                         fieldname=fieldname,
                         buttonvalue=buttonvalue)


@app.route('/')
def index():
  # Check if the user is logged in
  if 'user' in session:
    return redirect(url_for('tweet'))
  else:
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
  global current_user
  username = request.form['username']
  password = request.form['password']
  authenticated = password_match(username, password)
  if authenticated:
    # Use Flask session
    session['user'] = username
    return redirect(url_for('tweet'))
  else:
    return "Login Failed. Invalid username or password <br> <a href='/'>Try again</a>"


@app.route('/logout')
def logout():
  # Use Flask session
  del session['user']
  return redirect(url_for('index'))


@app.route('/tweet')
def tweet():
  return render_template('form.html',
                         action='/save-tweet',
                         header='What is happening?',
                         fieldtitle='Tweet',
                         fieldname='tweet',
                         buttonvalue='Tweet')


@app.route('/save-tweet', methods=['POST'])
def contact():
  tweet = request.form['tweet']
  # Change to use user info from Session
  add_tweet(tweet, session['user'])
  return 'Successfully received tweet ' + tweet


@app.route('/tweets/<username>')
@app.route('/tweets')
def user_tweets(username=None):
  if username:
    tweets = get_tweets_by_username(username)
  else:
    tweets = get_all_tweets()

  # Change to use user info from Session
  return render_template('tweets.html',
                         tweets=tweets,
                         current_user=session['user'],
                         username=username)


@app.route('/register', methods=['GET'])
def register():
  return render_template('register.html')


@app.route('/register-post', methods=['POST'])
def register_post():
  username = request.form['username']
  password = request.form['password']

  create_user(username, password)
  user = get_user_by_username(username)
  print(user)
  return f'Successfully registered {username} <br> <a href="/">Login</a>'


app.run(host='0.0.0.0', port=81)




