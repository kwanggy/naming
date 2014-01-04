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

def handle_signup(provider_id, resp):
    next_url = request.args.get('next') or url_for('index_page')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    if provider_id == 'twitter':
        display_name = resp['screen_name']
        full_name = resp['screen_name']

    data = {
        'provider_id': provider_id,
        'display_name': display_name,
        'full_name': full_name,
        'token_key': resp['oauth_token'],
        'token_secret': resp['oauth_token_secret'],
    }
    print resp

    session[provider_id] = (data['token_key'], data['token_secret'])
    key, sec = session[provider_id]
    api = get_provider(provider_id).get_api(key, sec)
    log(dir(api))
    cred = api.VerifyCredentials()
    return jsonify.dumps(cred)
    return redirect(next_url)

@twitter.auth.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/signup/twitter')
@twitter.auth.authorized_handler
def twitter_authorized(resp):
    provider_id = 'twitter'
    return handle_signup(provider_id, resp)

@facebook.auth.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route('/signup/facebook')
@facebook.auth.authorized_handler
def facebook_authorized(resp):
    provider_id = 'facebook'
    return handle_signup(provider_id, resp)


@app.route('/auth/<provider_id>', methods=['POST'])
def provider_auth(provider_id):
    provider = get_provider(provider_id)
    if provider == None:
        return None
    return provider.auth.authorize()
