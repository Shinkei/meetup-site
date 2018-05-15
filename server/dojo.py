from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'runo'

oauth = OAuth()

github = oauth.remote_app('github',
        consumer_key='55c03bf7535a58408b2c',
        consumer_secret='44c2a481bffd481d982d7fe5eaf6e06fc3addeb6',
        request_token_params={'scope': 'read:user'},
        base_url='https://api.github.com/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize'
        )

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized', _external=True))

@app.route("/login/authorized")
def authorized():
    resp = github.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason=%s error=%s resp=%s' % (
            request.args['error'],
            request.args['error_description'],
            resp
        )
    session['github_token'] = (resp['access_token'], '')
    me = github.get('user')
    return jsonify(me.data)

@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
