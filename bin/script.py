import oauth2
from tumblpy import Tumblpy

CONSUMER_KEY = 'MN6llW04QBngyH2e31PCT3R0gMEaY656zQQFmwCyKdNKLr2dJ9'
CONSUMER_SECRET = '82lF0LGIGsLvXfuHfQV1c7YkdjR6KL9wnSI1hXfpjpLu7Npgz8'

t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET)

auth_props = t.get_authentication_tokens(callback_url='http://michaelhelmick.com')
auth_url = auth_props['auth_url']

OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']

print('Connect with Tumblr via: {}'.format(auth_url))