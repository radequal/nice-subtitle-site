# -*- coding: utf-8 -*-
from JinjaHandler import *


class Handler(Jinja2Handler):

    def signout(self):
        self.response.delete_cookie('_mto_cloud')
        self.redirect('/')

    def error404(self):
        template_details = getTemplateDetails('public')

        self.render_template(template_details['name'] + '/error/404.html', {
            'template_details': template_details,
        })

    def wp(self, slug):
        self.response.write("You got it")
        self.response.write("Slug: " + slug)