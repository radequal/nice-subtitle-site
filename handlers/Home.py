# -*- coding: utf-8 -*-
from handlers.JinjaHandler import *

class Handler(Jinja2Handler):
  
    def root(self):
        session, user, profiles = sup(self)
        if user:
	      self.redirect('/d/dash')

        template_details = getTemplateDetails('public')

        self.render_template(template_details['name'] + '/home.html', {
            'template_details': template_details,
        })
