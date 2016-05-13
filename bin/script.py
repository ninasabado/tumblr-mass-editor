
from tumblpy import Tumblpy
import json

# private variables currently hardcoded for ease of use
CONSUMER_KEY        = 'MN6llW04QBngyH2e31PCT3R0gMEaY656zQQFmwCyKdNKLr2dJ9'
CONSUMER_SECRET     = '82lF0LGIGsLvXfuHfQV1c7YkdjR6KL9wnSI1hXfpjpLu7Npgz8'
OAUTH_TOKEN         = 'lvUpN9aukdFxa17CRhlfFEpfbIoEeefdVW0prDUu7kXOw4FI3i'
OAUTH_TOKEN_SECRET  = 'K548qCNr7YrFBegFxRLmUmYJ2GIxwjjsDc39uq0UV2PxHiYKQs'

t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_posts(blog):
	'''
	returns a list of posts in format dictionary
	'''
	return t.get('posts', blog_url=blog)['posts']


def get_info(blog):
	'''
	returns a dictionary of blog information
	'''
	return t.get('posts', blog_url=blog)['blog']




