import oauth2

#https://github.com/michaelhelmick/python-tumblpy
from tumblpy import Tumblpy
import json


with open('tokens.json') as json_data:
    tokens = json.load(json_data)

CONSUMER_KEY = tokens['CONSUMER_KEY']
CONSUMER_SECRET = tokens['CONSUMER_SECRET']
OAUTH_TOKEN = tokens['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = tokens['OAUTH_TOKEN_SECRET']


t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

posts = t.get('posts', blog_url="www.cloktahwho.tumblr.com")

print(posts)
