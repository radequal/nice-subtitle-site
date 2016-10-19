from engineauth import models

import logging
import cgi
import datetime
import urllib
import wsgiref.handlers
import os

from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class CustomUser(models.User):
    # added by classterize - extra fields for user settings
    uid = ndb.StringProperty()
    user_type = ndb.StringProperty(default="user")
    trust_autoPublish = ndb.BooleanProperty(default=False)

    username = ndb.StringProperty()
    display_name = ndb.StringProperty()

    first_name = ndb.StringProperty(default=None)
    last_name = ndb.StringProperty(default=None)

    default_language = ndb.StringProperty(default="en") #ISO 639-1 code
    display_picture = ndb.StringProperty(default=None) #location in serve/

    is_first_time_login = ndb.BooleanProperty(default=True)
    details_confirmed = ndb.BooleanProperty(default=False)
    terms_accepted = ndb.BooleanProperty(default=False)
    terms_version = ndb.StringProperty()

    experiments = ndb.StringProperty(repeated=True)
    @classmethod
    def _get_kind(cls):
        return 'UserDetails'

class Sessions(ndb.Model):
  date_added = ndb.DateTimeProperty(auto_now_add=True)
  last_modified = ndb.DateTimeProperty(auto_now=True)
  uid = ndb.StringProperty(required=True)
  description = ndb.StringProperty()
  content = ndb.TextProperty(default="")
