# -*- coding: utf-8 -*-
from handlers.JinjaHandler import *

class Handler(Jinja2Handler):
  
    def root(self, uid):
        template_details = getTemplateDetails('public')

        session = Sessions.query(Sessions.uid == uid).get()

        self.render_template(template_details['name'] + '/session.html', {
            'template_details': template_details,
            'session': session,
        })

    def write(self, uid):
        template_details = getTemplateDetails('public')

        session = Sessions.query(Sessions.uid == uid).get()

        self.render_template(template_details['name'] + '/session-write.html', {
            'template_details': template_details,
            'session': session,
        })

    def view(self, uid):
        template_details = getTemplateDetails('public')

        session = Sessions.query(Sessions.uid == uid).get()

        self.render_template(template_details['name'] + '/session-view.html', {
            'template_details': template_details,
            'session': session,
        })
