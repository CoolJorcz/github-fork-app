"""
  Github Fork App
  Largely Inspired from https://github.com/cenkalti/github-flask/blob/master/example.py
  Author: Andrew Jorczak
"""

from flask import Flask, request, g, session, redirect, url_for
from flask import render_template_string, jsonify
from flask_github import GitHub, GitHubError
from app.database import db_session, Database
from app.models import User

from dotenv import load_dotenv
load_dotenv()

import os

# setup flask
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# setup github-flask
github = GitHub(app)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@app.after_request
def after_request(response):
    db_session.remove()
    return response


@app.route('/')
def index():
    if g.user:
        t = 'Hello! %s <a target="_blank" href="{{ url_for("fork") }}">Fork this project!</a> ' \
            '<a href="{{ url_for("logout") }}">Logout</a>'
        t %= g.user.github_login
    else:
        t = 'Hello! <a href="{{ url_for("login") }}">Login</a>'

    return render_template_string(t)


@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token


@app.route('/github-callback')
@github.authorized_handler
def authorized(access_token):
    next_url = request.args.get('next') or url_for('index')
    if access_token is None:
        return redirect(next_url)

    user = User.query.filter_by(github_access_token=access_token).first()
    if user is None:
        user = User(access_token)
        db_session.add(user)

    user.github_access_token = access_token

    g.user = user
    github_user = github.get('/user')
    user.github_id = github_user['id']
    user.github_login = github_user['login']

    db_session.commit()

    session['user_id'] = user.id
    return redirect(next_url)

@app.route('/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize(scope="user,repo,write")
    else:
        return 'Already logged in'

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/fork', methods= ['POST', 'GET'])
def fork():
    response = github.post('/repos/CoolJorcz/github-fork-app/forks')
    return redirect(response['clone_url'])

@app.route('/repo')
def repo():
    return jsonify(github.get('/repos/CoolJorcz/github-fork-app/forks'))

if __name__ == '__main__':
    Database.init_db()
    app.run(debug=True)
