from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from pprint import pprint

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted, AllSlotsReset
from ckanext.rasa.data_bot.main.main import api_get_package_by_tag

FUNCTIONS = [
    "source data"
]

class Greet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class GoodBye(Action):
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
        print(tracker.current_state())
        tags = tracker.get_slot('tags')
        limit = tracker.get_slot('limit')
        message = "Currently I can only support sourcing from 1 tag. Datasets that have tag(s) {}:\n".format(tags)
        if limit is None:
            limit = 5
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