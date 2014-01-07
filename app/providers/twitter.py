from __future__ import absolute_import

import twitter


config = {
    'id': 'twitter',
    'name': 'Twitter',
    'base_url': 'http://api.twitter.com/1/',
    'request_token_url': 'https://api.twitter.com/oauth/request_token',
    'access_token_url': 'https://api.twitter.com/oauth/access_token',
    'authorize_url': 'https://api.twitter.com/oauth/authenticate',
    'callback': None
}


auth = None
consumer_key = None
consumer_secret = None


def get_api(token_key, token_secret):
    return twitter.Api(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token_key=token_key,
                       access_token_secret=token_secret)


def get_user_info(response=None, **kwargs):
    if not response:
        return None

    token_key = response['oauth_token']
    token_secret = response['oauth_token_secret']
    api = get_api(token_key, token_secret)
    user = api.VerifyCredentials()

    return dict(
        provider_id=config['id'],
        provider_user_id=str(user.id),
        token_key=token_key,
        token_secret=token_secret,
        display_name='@%s' % user.screen_name,
        full_name = user.name,
        profile_url="http://twitter.com/%s" % user.screen_name,
        image_url=user.profile_image_url
    )

