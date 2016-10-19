# -*- coding: utf-8 -*-
from handlers.JinjaHandler import *
import time
from google.appengine.api import app_identity
import logging
import inspect, os
from inspect import currentframe, getframeinfo
import datetime

class Handler(Jinja2Handler):


    def flush_session_content(self):
			sessions = Sessions.query(Sessions.last_modified < datetime.datetime.now()-datetime.timedelta(hours=12))
			for session in sessions:
				session.content = ""
				session.put()