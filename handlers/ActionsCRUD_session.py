# -*- coding: utf-8 -*-
from handlers.JinjaHandler import *
import time
from google.appengine.api import app_identity
import logging
import inspect, os
from inspect import currentframe, getframeinfo


class Handler(Jinja2Handler):


    def crud(self, crud_type):
        session, user, profiles = sup(self)

        if crud_type == "new":
            session = Sessions()
            session.uid = id_generator("Sessions")
            redirect_path = "/session/"+session.uid
        elif crud_type == "edit":
            session = ndb.Key(urlsafe=self.request.get("key")).get()
            redirect_path = "/session/"+session.uid
        elif crud_type == "delete":
            ndb.Key(urlsafe=self.request.get("key")).delete()
            redirect_path = "/session/"+session.uid

        if crud_type == "new" or crud_type == "edit":
            try:
                session.description = self.request.get('session-description')
                session.put()

            except:
                logging.error("""
                    Comment: There was an error saving the site
                    File: %s
                    Line number: %d
                """ % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno))

        time.sleep(0.1)
        self.redirect(redirect_path)