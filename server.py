#!/usr/bin/env python3

"""
Columbia's COMS W3101.003 Python Project
TUMBLR MASS EDITOR
by Anfal Boussayoud | ab3750
and Nina Sabado | mcs2225

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
import json
import oauth2
#https://github.com/michaelhelmick/python-tumblpy
from tumblpy import Tumblpy
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# private variables currently hardcoded for ease of use
CONSUMER_KEY        = 'MN6llW04QBngyH2e31PCT3R0gMEaY656zQQFmwCyKdNKLr2dJ9'
CONSUMER_SECRET     = '82lF0LGIGsLvXfuHfQV1c7YkdjR6KL9wnSI1hXfpjpLu7Npgz8'
OAUTH_TOKEN         = 'lvUpN9aukdFxa17CRhlfFEpfbIoEeefdVW0prDUu7kXOw4FI3i'
OAUTH_TOKEN_SECRET  = 'K548qCNr7YrFBegFxRLmUmYJ2GIxwjjsDc39uq0UV2PxHiYKQs'

t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

posts = t.get('posts', blog_url="www.cloktahwho.tumblr.com")

#print(posts)


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  print("Hello this is trying to work.")

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  print("Hello this is trying to close.")


# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request

@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # render_template looks in the templates/ folder for files.
  return render_template("index.html")

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on {0}:{1}".format(HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
