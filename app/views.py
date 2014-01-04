from flask import *

from . import app, db
from .config import conf
from util import log
from providers import get_provider, twitter, facebook, google


@app.route('/')
def index_page():
    log('index page', request.remote_addr)
    best_namings = range(4)
    recent_namings = range(4)

    return render_template('main.html',
                            best_namings=best_namings,
                            recent_namings=recent_namings)

@app.route('/signin')
def signin_page():
    log('signin page', request.remote_addr)
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    return redirect(request.referrer or '/')
    return render_template('signin.html')

@twitter.auth.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/signup/twitter')
@twitter.auth.authorized_handler
def twitter_authorized(resp):
    next_url = request.args.get('next') or url_for('index_page')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    print resp
    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    return redirect(next_url)

@facebook.auth.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route('/signup/facebook')
@facebook.auth.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index_page')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    print resp
    session['facebook_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    return redirect(next_url)


@app.route('/auth/<provider_id>', methods=['POST'])
def provider_auth(provider_id):
    provider = get_provider(provider_id)
    if provider == None:
        return None
    return provider.auth.authorize()
