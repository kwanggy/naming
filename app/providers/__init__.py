from . import twitter, facebook, google

def get_provider(provider_id):
    provider = None
    if provider_id == 'twitter':
        provider = twitter.twitter
        provider = twitter
    elif provider_id == 'facebook':
        provider = facebook.facebook
        provider = facebook
    elif provider_id == 'google':
        provider = google.google
        provider = google
    return provider
