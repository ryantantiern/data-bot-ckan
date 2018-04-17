 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning
import json
import logging
import urllib2
import ckan.plugins.toolkit as toolkit
from ckan.common import request, response, session
from ckan.lib.base import BaseController, render
from ckanext.rasa.action_manager import execute_next_action

logger = logging.getLogger(__name__)

def _update_slot_and_next_action(data, response):
    """
    Sets the necessary data attributes
    """
    next_action = response.get("next_action")
    slots =(response["tracker"]).get("slots") if response.get("tracker") else {}
    data["next_action"] = next_action
    data["slots"] = slots
    if response.get("error"):
        data["error"] = response["error"]

class RasaPluginController(toolkit.BaseController):

    def send_user_message(self):
        body = {}
        try:
            request_body = json.loads(request.body)
        except Exception:
            # Didn't get appropriate JSON format
            bot_response = "Inappropriate body format - body must be application/json"
            logger.info(bot_response)
            body["bot"] = bot_response
            body["error"] = True
            response.body = json.dumps(body)
            return 
        if not session.get("sender_id"):
            session["sender_id"] = session.id
            session.save()
        sender_id = session["sender_id"]
        message = request_body["text"]
        version_connector = VersionConnector()
        if not version_connector.query_rasa():
            body["bot"] = ["Rasa server is down"]
            body["error"] = True
        else:
            bot_response = self.rasa_handle_message(message, sender_id) # Returns a list of responses
            if not bot_response:
                body["error"] = True
                bot_response ={
                    "type": "string",
                    "data" : "DataBot didn't get any response. DataBot server is probably down."
                }
            body["bot"] = bot_response
        response.body = json.dumps(body)
        from pprint import pprint as pprint
        pprint(response.body)
        return

    def databot_index(self):
        
        note = ""
        return render('databot.html', extra_vars={"note": note})
    

    def rasa_handle_message(self, message, sender_id):
        """
        Handles a message by executing a sequence of actions until an action_listen
        is predicted
        """
        parse_connector = ParseConnector() 
        continue_connector = ContinueConnector()
        response = parse_connector.query_rasa(sender_id, message)
        data = {}
        _update_slot_and_next_action(data, response)
        response_channel = {
            "type": "list",
            "data" : []
        }
        if data.get("next_action") is None:
            response_channel["data"].append({
                    "type" : "string",
                    "data": data.get("error")
            })
            return response_channel
        next_action = data["next_action"]
        while next_action != "action_listen":
            events = []
            ret = execute_next_action(next_action, data["slots"])
            if ret.get("type"): response_channel["data"].append(ret)
            if ret.get("events"): events = ret["events"]
            if ret.get("error"):
                return ["{}. The UDL team has been notified of the error.".format(ret["error"])]
            response = continue_connector.query_rasa(sender_id, next_action, events)
            _update_slot_and_next_action(data, response)
            next_action = data["next_action"]
        return response_channel

        
class RasaCoreConnector(object):

    port = "5005"
    base_url = "http://localhost:" + port + "/" 

    def __init__(self):
        self.response_data = {}

    def _post(self, url, query):
        try:
            request = urllib2.Request(url, data=json.dumps(query), headers={'Content-Type': 'application/json'})
            f = urllib2.urlopen(request)
            response = f.read()
            return json.loads(response)
        except urllib2.URLError as e:
            print("URLError: Failed to access Rasa Core server")
            return {"error": "URLError: Failed to access Rasa Core server"}


    def _get(self, url):
        try:
            f = urllib2.urlopen(url)
            response = f.read()
            return json.loads(response)
        except urllib2.URLError as e:
            print("URLError: Failed to access Rasa Core server")
            return {"error" : "URLError: Failed to access Rasa Core server"}

    def _set_response_data(self, response_data):
        self.response_data = response_data

    def query_rasa(self):
        raise NotImplementedError

class ParseConnector(RasaCoreConnector):

    def __init__(self):
        super(ParseConnector, self).__init__()
        self.endpoint = self.base_url + "conversations/{}/parse"

    def query_rasa(self, sender_id, message):
        """
        Query Rasa Core endpoint 'conversation/{sender_id}/parse'.
        """

        if not message:
            raise ValueError("No message passed into query rasa method of ParseConnector")
        elif not sender_id:
            raise ValueError("No sender id passed into query rasa method of ParseConnector")
        query = {
            "query" : message
        }
        url = self.endpoint.format(sender_id)
        response = self._post(url, query)
        self._set_response_data(response)
        return self.response_data

class ContinueConnector(RasaCoreConnector):

    def __init__(self):
        super(ContinueConnector, self).__init__()
        self.endpoint = self.base_url + "conversations/{}/continue"

    def query_rasa(self, sender_id, executed_action, events=None):
        if not executed_action:
            raise ValueError("No executed_action passed into query rasa method of ContinueConnector")
        elif not sender_id:
            raise ValueError("No sender id passed into query rasa method of ContinueConnector")
        if events == None:
            events = []
        query = {
            "executed_action": executed_action,
            "events" : events
        }
        url = self.endpoint.format(sender_id)
        response = self._post(url, query)
        self._set_response_data(response)
        return self.response_data
  
class VersionConnector(RasaCoreConnector):

    def __init__(self):
        super(VersionConnector, self).__init__()
        self.endpoint = self.base_url + "version"

    def query_rasa(self):
        response = self._get(self.endpoint)
        self._set_response_data(response)
        return self.response_data
    
