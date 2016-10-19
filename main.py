# -*- coding: utf-8 -*-
import sys
import os
import re
import webapp2
from webapp2 import Route
import os
from jinja2.filters import do_pprint

if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

routes = [
    # ------------------------------
    # Public pages
    Route(r'/', handler='handlers.Home.Handler:root'),
    Route(r'/session/<uid>', handler='handlers.Sessions.Handler:root'),
    Route(r'/session/<uid>/write', handler='handlers.Sessions.Handler:write'),
    Route(r'/session/<uid>/view', handler='handlers.Sessions.Handler:view'),


    # ------------------------------
    # Actions
    Route(r'/actions/subtitles-save', handler='handlers.ActionsSubtitle.Handler:save'),
    Route(r'/actions/subtitles-get-content', handler='handlers.ActionsSubtitle.Handler:getContent'),
    Route(r'/actions/session-crud/<crud_type>', handler='handlers.ActionsCRUD_session.Handler:crud'),
    Route(r'/actions/clear-session-data', handler='handlers.ActionsSubtitle.Handler:clearData'),


    # ------------------------------
    # Cron
    # Flush the datastore
    Route(r'/cron/flush-session-content', handler='handlers.Cron.Handler:flush_session_content'),


    # ------------------------------
    # Errors
    Route(r'/404', handler='handlers.MiscHandlers.Handler:error404'),
    # Route(r'/<url:.*>', handler='handlers.Redirect.Handler:error404'),
    ]

config = {
    'webapp2_extras.sessions': {
        'secret_key': 'sfoah908guas0g9uas0gd9a0sgya9g8yados8yghoai'
    },
    'webapp2_extras.jinja2': {
        'filters': {
            'do_pprint': do_pprint,
            },
        },
    }


application = webapp2.WSGIApplication(routes, debug=DEBUG, config=config)
