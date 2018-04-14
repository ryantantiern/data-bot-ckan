 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from pprint import pprint

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted, AllSlotsReset

DEV = True

FUNCTIONS = [
    "(1) Source data - Return datasets that are related to a given search term. An optional limit can be provided to constraint that number of results returned, defaults to 5. e.g.'Find data relating to population and pollution 2016', 'get child health care policy datasets limited to 20 results.'"
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
        return []


class Help(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):

        functions = ",".join(FUNCTIONS)
        message = "Currently I can: \n{}.".format(functions)
        dispatcher.utter_message(message)
        return

class ClarifyUnderstanding(Action):
    def name(self):
        return 'action_clarify_understanding'

    def run(self, dispatcher, tracker, domain):
        # get latest user message parse data
        print(tracker.latest_message.parse_data)
        name = tracker.latest_message.parse_data["intent"]["name"]
        response = "I couldn't clarify your message. Please report this issue to my maintainers. Type '/stop' and start again.\n[For the maintainers of DataBot] Cannot clarify understanding for intent {} because the appropriate response has not yet been defined. Implement appropriate response in action ClarifyUnderstanding.".format(name)

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
        print("Slots reset")
        return [(AllSlotsReset())]
