from __future__ import absolute_import

import facebook


config = {
    'id': 'facebook',
    'name': 'Facebook',
    'base_url': 'https://graph.facebook.com/',
    'request_token_url': None,
    'access_token_url': '/oauth/access_token',
    'authorize_url': 'https://www.facebook.com/dialog/oauth',
    'request_token_params': {
        'scope': 'email'
    },
    'callback': '/signup/facebook'
}


auth = None
consumer_key = None
consumer_secret = None


def get_api(token_key, token_secret):
    return facebook.GraphAPI(token_key)

def get_user_info(response=None, **kwargs):
    if not response:
        return None

    token_key = response['access_token']
    token_secret = None
    api = get_api(token_key, token_secret)
    profile = api.get_object("me")
    profile_url = "http://facebook.com/profile.php?id=%s" % profile['id']
    image_url = "http://graph.facebook.com/%s/picture" % profile['id']

    return dict(
        provider_id=config['id'],
        provider_user_id=profile['id'],
        token_key=token_key,
        token_secret=token_secret,
        display_name=profile.get('username', None),
        full_name = profile.get('name', None),
        profile_url=profile_url,
        image_url=image_url
    )

