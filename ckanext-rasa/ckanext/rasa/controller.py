import json
import time
import logging

import ckan.plugins
from ckan.common import request, response, session
from ckan.lib.base import BaseController, render
from data_bot.main.main import instantiate_agent, agent
from ckanext.rasa.data_bot.main.extended import ExtendedAgent

logger = logging.getLogger(__name__)

def get_response_from_rasa(text):
    if not session.get("sender_id"):
        # Prevents pylon from assigning a new session id to this user
        session["sender_id"] = session.id
        session.save()

    # Bot's response is a list
    global agent

    if not isinstance(agent, ExtendedAgent):
        response = ["Bot hasn't loaded yet - please try again in a few moments."]
    else:
        try:
            # handle incoming message
            response = agent.handle_message(text, sender_id=session["sender_id"])
        except Exception:
            logger.exception("Handling error in get_response_from_rasa")
            return 
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
            bot_response = "DataBot didn't get any response. UDL CKAN server is probably down. Please report this to system administrators."
        body["bot"] = bot_response
        response.body = json.dumps(body)
        return

    def databot_index(self):
        
        global agent
        note = ""
        print(agent)
        print(agent.interpreter.interpreter)
        if isinstance(agent, ExtendedAgent):
            if  agent.interpreter.interpreter is not None:
                note = ""
            else:
                note = "It will take around 90 seconds for DataBot to respond to your first message. Please do not refresh until the bot responds. Thank you for waiting! "
        else:
            agent = instantiate_agent()
            note = "It will take around 90 seconds for DataBot to respond to your first message. Please do not refresh until the bot responds. Thank you for waiting! "

        return render('databot.html', extra_vars={"note":note})