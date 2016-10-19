# -*- coding: utf-8 -*-
from handlers.JinjaHandler import *
import time

class Handler(Jinja2Handler):


    def save(self):
					message = self.request.get("text")
					session_uid = self.request.get("uid")

					session = Sessions.query(Sessions.uid == session_uid).get()
					session.content = session.content + message
					newSubtitleContent = session.content
					session.put()

					self.response.write(newSubtitleContent)

    def getContent(self):
					session_uid = self.request.get("uid")

					session = Sessions.query(Sessions.uid == session_uid).get()
					self.response.write(session.content)

    def clearData(self):
					session_uid = self.request.get("uid")
					view = self.request.get("view")

					session = Sessions.query(Sessions.uid == session_uid).get()
					session.content = ""
					session.put()
					time.sleep(0.1)
					self.redirect("/session/" + session_uid + "/" + view)