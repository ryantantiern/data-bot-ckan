from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from pprint import pprint

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted, AllSlotsReset
from ckanext.rasa.data_bot.main.main import api_get_package_by_tag

DEV = True

FUNCTIONS = [
    "source data"
]



class Greet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class Farewell(Action):
    def name(self):
        return 'action_farewell'


    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class OfferHelp(Action):
    def name(self):
        return 'action_offer_help'


    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class SourceData(Action):
    def name(self):
        return 'action_source_data'


    def run(self, dispatcher, tracker, domain):
        """
        Find data sources that match tags
        """
        tags = tracker.get_slot('tags')
        limit = tracker.get_slot('limit')
        if limit is None:
            limit = 5

        formatted_tags = ' '.join(tags)
        plural = "s" if len(tags) > 1 else ""
        message = "Searching for datasets that have tag{} {} limited to top {} results:\n".format(plural ,formatted_tags, limit)
        if DEV:
            results = "1. This is currently in development!"
            
        else:
            results = api_get_package_by_tag(formatted_tags, limit)
        message += results
        dispatcher.utter_message(message)
        return []

class Help(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):

        functions = ",".join(FUNCTIONS)
        message = "Currently I can {}.".format(functions)
        dispatcher.utter_message(message)
        return

class ClarifyUnderstanding(Action):
    def name(self):
        return 'action_clarify_understanding'

    def run(self, dispatcher, tracker, domain):
        # get latest user message parse data
        print(tracker.latest_message.parse_data)
        name = tracker.latest_message.parse_data["intent"]["name"]
        response = "I couldn't clarify your message. Please report this issue to my maintainers. Type '/reset' and start again.\n[For the maintainers of DataBot] Cannot clarify understanding for intent {} because the appropriate response has not yet been defined. Implement appropriate response in action ClarifyUnderstanding.".format(name)

        # Respond differently for each intent, must be binary question
        if name == "greet":
            response = "Did you mean to greet me?"
            pass
        elif name == "farewell":
            response = "Are you bidding farewell?"
        elif name == "affirm":
            response = "Do you mean yes'?"
        elif name == "deny":
            response = "Do you mean 'no'?"
        elif name == "random":
            response = ""
        elif name == "requestHelp":
            response = "Should I tell you what I can do?"
        elif name == "sourceData":
            tags = ltracker.get_slot('tags')
            limit = tracker.get_slot('limit')
            additions = ""
            if tags is not None and len(tags) > 0:
                additions = " with tags {}".format(', '.join(tags).rstrip(", "))
                if limit is not None:
                    additions += " limited to {} results".format(limit)
                response = "Are you requesting to source data{}?".format(additions)
        elif name == "sourceDataProvideTags":
            tags = list(tracker.get_latest_entity_values('tags'))
            if tags is not None or len(tags) > 0:
                additions = ", ".join(tags).rstrip(" ,")
            else:
                additions = "-- sorry, I couldn't detect any tags. Please enter different tags."
            response = "Are the search tags {}?".format(additions)
        dispatcher.utter_message(response)
        return []

class GiveUp(Action):
    def name(self):
        return 'action_give_up'

    def run(self, dispatcher, tracker, domain):
        print(tracker.latest_message.parse_data)
        message = "I'm still trying to understanding humans - try structuring your message in a different way. "

        # Do not add GiveUp to tracker, and remove all events until last action listen <- so bot will listen after this

        dispatcher.utter_message(message)
        return []

class ReofferHelp(Action):
    def name(self):
        return 'action_reoffer_help'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class SourceDataPromptTags(Action):
    def name(self):
        return 'action_source_data_prompt_tags'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class ResetSlots(object):
    def name(self):
        return 'action_reset_slots'

    def run(self, dispatcher, tracker, domain):
        return [(AllSlotsReset())]
