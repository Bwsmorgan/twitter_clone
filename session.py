from flask import session

USER_KEY = 'user'


def create_session(username):
  session[USER_KEY] = username


def get_session():
  return session[USER_KEY]


def has_session():
  return USER_KEY in session


def del_session():
  del session[USER_KEY]
