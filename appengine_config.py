import os
ON_DEV = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

engineauth = {
    # Login uri. The user will be returned here if an error occures.
    'login_uri': '/', # default 'login/'
    # The user is sent here after successfull authentication.
    'success_uri': '/d',
    'secret_key': '73028490jr4iontb2g9h0fingbu2',
    # Comment out the following lines to use default
    # User and UserProfile models.
    'user_model': 'models.CustomUser',
}

engineauth['provider.google'] = {
    'client_id': '',
    'client_secret': '',
    'api_key': '',
    'scope': 'https://www.googleapis.com/auth/plus.me',
    }

engineauth['provider.github'] = {
    'client_id': '',
    'client_secret': '',
    }

engineauth['provider.linkedin'] = {
    'client_id': '',
    'client_secret': '',
    }

engineauth['provider.twitter'] = {
    'client_id': '',
    'client_secret': '',
    }


if ON_DEV:
    # Facebook settings for Development
    FACEBOOK_APP_KEY = '616470655178549'
    FACEBOOK_APP_SECRET = '7c3fb1d9a39a7003d0420ef3736a9432'
else:
    # Facebook settings for Production
    FACEBOOK_APP_KEY = '616469895178625'
    FACEBOOK_APP_SECRET = '1a99b3742716c56c8e9eb5e51eee37de'

engineauth['provider.facebook'] = {
    'client_id': FACEBOOK_APP_KEY,
    'client_secret': FACEBOOK_APP_SECRET,
    'scope': 'email',
    }


def webapp_add_wsgi_middleware(app):
    from engineauth import middleware
    return middleware.AuthMiddleware(app)

