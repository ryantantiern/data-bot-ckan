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
        return 'action_goodbye'


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

        plural = "s" if tags > 1 else ""
        message = "Searching for datasets that have tag{} {} limited to top {} results:\n".format(plural ,tags, limit)
        if DEV:
            results = "1. This is currently in development!"
            
        else:
            results = api_get_package_by_tag(tags, limit)
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

class CheckUnderstanding(Action):
    def name(self):
        return 'action_check_understanding'

    def run(self, dispatcher, tracker, domain):
        pass

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
