import json
import time

import ckan.plugins
from ckan.common import request, response, session
from ckan.lib.base import BaseController
from data_bot.main.main import handle_message
from plugin import agent

def get_response_from_rasa(text):
    # Need to handle sender_id
    if not session.get("sender_id"):
        session["sender_id"] = session.id
        session.save()

    response = agent.handle_message(text, sender_id=session["sender_id"])
    return response


class RasaPluginController(BaseController):
    def send_user_message(self):
        body = {}
        try:
            request_body = json.loads(request.body)
        except Exception:
            # Didn't get appropriate JSON format
            response.status = 404
            return

        # Didn't get JSON object or body doesn't have text field
        if not isinstance(request_body, dict) or not request_body.get("text"):
            response.status = 404
            return

        bot_response = get_response_from_rasa(request_body["text"])
        if not bot_response:
            body["error"] = True
            bot_response = "Something went wrong. Terminating and restarting..."

        body["bot"] = bot_response
        response.body = json.dumps(body)
        return
