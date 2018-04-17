from random import randint
from ckanext.rasa.data_bot.main.main import UDLApiConnector
def greet(**kwargs):

    possible_responses = [
        "Hi, I'm DataBot! Currently, I can source data. Ask me what I can do for a detailed explanation!\nPlease keep messages as unambiguous as possible - I'm still under development by very smart geeks.",
        "Hello there, I'm DataBot! Currently, I can source data. Ask me what I can do for a detailed explanation!\nPlease keep messages as unambiguous as possible - I'm still under development by very smart geeks.",
        "I'm DataBot. Nice to make your acquaintance. Currently, I can source data. Ask me what I can do for a detailed explanation!\nPlease keep messages as unambiguous as possible - I'm still under development by very smart geeks."
    ]
    response = {
        "type": "string",
        "data": possible_responses[randint(0, len(possible_responses) - 1)]
    }
    return response

def farewell(**kwargs):
    
    possible_responses = [
        "Thanks for using DataBot. Goodbye!",
        "Thanks for using DataBot. See you soon."
    ]
    response = {
        "type": "string",
        "data": possible_responses[randint(0, len(possible_responses) - 1)]
    }
    return response

def offer_help(**kwargs):
    possible_responses = [
        "What can I do for you?",
        "How can I be of assistance?",
        "What would you like me to do?",
        "What shall we do today?"
    ]
    response = {
        "type": "string",
        "data": possible_responses[randint(0, len(possible_responses) - 1)]
    }
    return response

def source_data( ** kwargs):
    tags = kwargs.get("tags")
    limit = int(kwargs.get("limit")) if kwargs.get("limit") else 5
    udl_api_connector = UDLApiConnector()
    results = udl_api_connector.search_packages(tags, limit)
    response = {
        "type": "list",
        "data": [{
            "type": "string",
            "data": "Searching for datasets that relate to {}, limiting search to {} results".format(" ".join(tags), limit)
        }]
    }
    response["data"] = response["data"] + results
    return response

def provide_help( ** kwargs):
    function_list = [
        "(1) Source data - Return datasets that are related to a given search term. An optional limit can be provided to constraint that number of results returned, defaults to 5. e.g.'Find data relating to population and pollution 2016', 'get child health care policy datasets limited to 20 results.'"
    ]
    f = ",".join(function_list)
    message = "Currently I can: \n{}.".format(f)
    response = {
        "type": "string",
        "data": message
    }
    return response


def reoffer_help(**kwargs):
    possible_responses = [
        "Is there anything else I can do for you?",
        "Do you need further assistance?"
    ]
    response = {
       "type": "string",
       "data": possible_responses[randint(0, len(possible_responses) - 1)]
    }
    return response

def prompt_tags(**kwargs):
    possible_responses = [
        "Great! What data would you like?",
        "Excellent! What data are you searching for?",
        "Wonderful! What kind of data are you looking for?",
        "Sure, what are the search terms?"
    ]
    response = {
        "type": "string",
        "data": possible_responses[randint(0, len(possible_responses) - 1)]
    }
    return response

def reset_slots(**kwargs):
    response = {
        "events": [{"event":"reset_slots"}]
    }
    return response

def restart( ** kwargs):
    response = {
        "events": [{"event":"restart"}]
    }
    return response

action_map = {
    "action_greet": greet,
    "action_farewell": farewell,
    "action_offer_help": offer_help,
    "action_source_data": source_data,
    "action_help": provide_help,
    "action_reoffer_help": reoffer_help,
    "action_source_data_prompt_tags": prompt_tags,
    "action_reset_slots": reset_slots,
    "action_restart" : restart
}

def execute_next_action(next_action, data):
    """
    Process to execute the next action
    next_action: String
    response_channel: List
    data: Dict
    """
    
    action = action_map.get(next_action)
    if action is None:
        return {"not_found": next_action}
    ret_val = action(**data) #Each action shoud return dict with optional keys {message, events}
    return ret_val
     
        