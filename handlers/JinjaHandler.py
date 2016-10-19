# -*- coding: utf-8 -*-
import webapp2
from webapp2_extras import jinja2
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
from jinja2 import Environment
from jinja2 import evalcontextfilter

from google.appengine.api import search

import cgi
import datetime
#~ from datetime import datetime
import urllib
import wsgiref.handlers
import os
import re
import json
from webob import Request
from google.appengine.api import taskqueue

from google.appengine.ext import db
from models import *
from google.appengine.api import mail

import string
import random
import csv

from engineauth import models
import models

import httplib2

def sup(self):
    session = self.request.session if self.request.session else None
    user = self.request.user if self.request.user else None
    profiles = None
    if user:
        profile_keys = [ndb.Key('UserProfile', p) for p in user.auth_ids]
        profiles = ndb.get_multi(profile_keys)
    return session, user, profiles


def getTemplateDetails(visibility):
    details = {}
    if visibility == "admin":
        details["name"] = "admin-theme"
    elif visibility == "public":
        details["name"] = "stylish"
    return details


def id_generator(database):
    size=11
    chars=string.ascii_uppercase + string.digits
    dupe_check = 1
    while dupe_check != 0:
        new_id = ''.join(random.choice(chars) for x in range(size))
        if database == "User":
            dupe_check = CustomUser.query(CustomUser.uid == new_id).count()
        if database == "Sites":
            dupe_check = Sites.query(Sites.uid == new_id).count()
        elif database == "Global":
            dupe_check = Global.query(Global.uid == new_id).count()
        elif database == "Post":
            dupe_check = Post.query(Post.uid == new_id).count()
        elif database == "Categories":
            dupe_check = Categories.query(Categories.uid == new_id).count()
        elif database == "Navs":
            dupe_check = Navs.query(Navs.uid == new_id).count()
        elif database == "Sources":
            dupe_check = Sources.query(Sources.uid == new_id).count()
        elif database == "Posts":
            dupe_check = Posts.query(Posts.uid == new_id).count()
        elif database == "Scrapers":
            dupe_check = Scrapers.query(Scrapers.uid == new_id).count()
        elif database == "ACLUsers":
            dupe_check = ACLUsers.query(ACLUsers.uid == new_id).count()
        elif database == "Broadcasts":
            dupe_check = Broadcasts.query(Broadcasts.uid == new_id).count()
        elif database == "Sessions":
            dupe_check = Sessions.query(Sessions.uid == new_id).count()
    return new_id


def password_generator():
    size=11
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def fetch_from_url(feed_url, username="", password=""):
    httplib2.Http(timeout=59)
    h = httplib2.Http()

    if username and password:
      h.add_credentials(username, password)

    resp, content = h.request(feed_url)
    resp, content = h.request(feed_url, 
        headers={'User-Agent':'Googlebot'})
    return content


def menuStructure():
    pages = [
        # [0]visibility, [1]permalink (path), [2]page title, [3]page icon, [4]permissions, [5]submenu
        ['live', '/d/subtitles', 'Subtitles', 'fa fa-paragraph', 'user', ''],
        # ['live', '/d/posts', 'Posts', 'fa fa-pencil-square-o','user', ''],
        # ['live', '/d/sites', 'Sites', 'fa fa-compass', 'user', ''],
        # ['live', '/d/sources', 'Sources', 'fa fa-rss', 'user', ''],
        # ['live', '/d/scrapers', 'Scrapers', 'fa fa-copy', 'user', ''],
        # ['live', '/d/users', 'Users (ACL)', 'fa fa-users','user', ''],
        # ['live', '/d/report', 'Reporting', 'fa fa-bar-chart', 'user',
            # [
                # [0]visibility, [1]permalink (path), [2]parent permalink (path), [3]page title, [4]page icon, [5]permissions
        #         ['live', '/d/report/posts', '/d/report', 'Posts ', 'fa fa-circle-o', 'user', ''],
        #         ['live', '/d/report/audience', '/d/report', 'Audience ', 'fa fa-circle-o', 'user', ''],
        #         ['live', '/d/report/geo', '/d/report', 'Geo ', 'fa fa-circle-o', 'user', ''],
        #         ['live', '/d/report/acquisition', '/d/report', 'Acquisition', 'fa fa-circle-o', 'user', ''],
        #     ]
        # ],
        # ['header', '', 'ADMIN', '', 'admin', ''],
        # ['live', '/d/settings', 'Settings', 'fa fa-cog', 'admin', ''],
        # ['live', '/d/sites', 'Sites', 'fa fa-compass', 'admin', ''],
        # ['live', '/d/settings', 'Settings', 'fa fa-cog','admin', ''],
    ]
    # pages = "amir"
    return pages


class Jinja2Handler(webapp2.RequestHandler):
    """
        BaseHandler for all requests all other handlers will
        extend this handler

    """
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, template_name, template_values={}):
        self.response.write(self.jinja2.render_template(
            template_name, **template_values))

    def render_string(self, template_string, template_values={}):
        self.response.write(self.jinja2.environment.from_string(
            template_string).render(**template_values))

    def json_response(self, json):
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        self.response.out.write(json)
