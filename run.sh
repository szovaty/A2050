#! /bin/sh
export OAUTHLIB_INSECURE_TRANSPORT=1
export OAUTHLIB_RELAX_TOKEN_SCOPE=1
export FLASK_APP=app.py
flask run