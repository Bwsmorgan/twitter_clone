from flask import Flask, request, redirect, url_for

app = Flask(__name__)
# GLOBAL VARIABLE
tweets = []
current_user = ''


def get_html_form(action, header, field_title, name, button_value):
  return f'''
          <form method="POST" action="{action}">
              <h3>{header}</h3>
              {field_title}: <input type="text" name="{name}"/>
              <input type="submit" value="{button_value}"/>
          </form>
    '''


@app.route('/')
def index():
  # if user is logged in redirect to tweet page
  if current_user:
    return redirect(url_for('tweet'))
  # if user is not logged in go to login page
  else:
    return get_html_form('/login', 'Please Login', 'Username', 'username',
                         'Login')


@app.route('/login', methods=['POST'])
def login():
  global current_user
  current_user = request.form['username']
  return redirect(url_for('tweet'))
  # username = request.form.get('username')
  # return f'current user name is {current_user}'


@app.route('/tweet')
def tweet():
  return get_html_form('/save_tweet', 'what is happening?', 'Tweet', 'tweet',
                       'Tweet')


@app.route('/save_tweet', methods=['POST'])
def contact():
  tweet = request.form['tweet']
  tweets.append(tweet)
  return 'Successfully recieved tweet ' + tweet


@app.route('/my-tweets')
def my_tweets():
  tweet_html = ""
  for tweet in tweets:
    tweet_html += f'<li>{tweet}</li>'

  return f'''
    <h1>All my tweet</h1>
    <ol>{tweet_html}<ol>
  '''


app.run(host='0.0.0.0', port=81)


# app.run(host='0.0.0.0', port=81)
 