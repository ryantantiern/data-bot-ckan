import json
import time
import logging

import ckan.plugins
from ckan.common import request, response, session
from ckan.lib.base import BaseController, render
from data_bot.main.main import agent, run_initialize_interpreter_job, instantiate_agent, ipreter, rasa_interpreter
from rasa_core.agent import Agent

logger = logging.getLogger(__name__)

def get_response_from_rasa(text):
    if not session.get("sender_id"):
        # Prevents pylon from assigning a new session id to this user
        session["sender_id"] = session.id
        session.save()
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
            bot_response = "Something went wrong. Terminating and restarting..."

        body["bot"] = bot_response
        response.body = json.dumps(body)
        return

    def databot_index(self):
        
        global ipreter
        global agent
        
        # Job isn't running
        if ipreter is None:
            note = "The DataBot had failed to initialize. Re-initializing DataBot. Please refresh the page in 90 seconds"
            run_initialize_interpreter_job()
        
        elif isinstance(agent, Agent):
            note = ""

        # Agent is still a Job object
        elif hasattr(ipreter, "result"): 
            
            # Handle case load has failed

            if ipreter.result is None:
                # Agent hasn't finished loading
                ipreter_data = ipreter.to_dict()
                from pprint import pprint as pp
                pp(ipreter_data)
                note = "Welcome! DataBot is initializing! Please refresh the page in 90 seconds."
            else:
                global rasa_interpreter
                agent = instantiate_agent(rasa_interpreter)
                note = ""

        return render('databot.html', extra_vars={"note":note})