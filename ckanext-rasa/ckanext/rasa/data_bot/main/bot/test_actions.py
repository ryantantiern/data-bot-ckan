from unittest import TestCase, main
from mock import Mock, patch
import os.path as path
from rasa_core.domain import TemplateDomain
from rasa_core.trackers import DialogueStateTracker
from ckanext.rasa.data_bot.main.main import MODEL_PATH
from ckanext.rasa.data_bot.main.bot.actions import Greet, Farewell, OfferHelp, SourceData, Help, GiveUp, FUNCTIONS, ReofferHelp, SourceDataPromptTags, ResetSlots


DOMAIN_PATH = path.join(MODEL_PATH, "domain.yml")

class TestActions(TestCase):
    
    def setUp(self):
        self.actions = TemplateDomain.load(DOMAIN_PATH).action_for_name

    def test_Greet_name(self):
        obj = self.actions("action_greet")
        self.assertIsInstance(obj, Greet)
    
    def test_Greet_run(self):
        obj = self.actions("action_greet")
        dis, trac, dom = Mock(), Mock(), Mock()
        obj.run(dis, trac, dom)
        dis.utter_template.assert_called_with("action_greet")
    
    def test_Farewell_name(self):
        obj = self.actions("action_farewell")
        self.assertIsInstance(obj, Farewell)
    
    def test_Farewell__run(self):
        obj = self.actions("action_farewell")
        dis, trac, dom = Mock(), Mock(), Mock()
        obj.run(dis, trac, dom)
        dis.utter_template.assert_called_with("action_farewell")

    def test_OfferHelp_name(self):
        obj = self.actions("action_offer_help")
        self.assertIsInstance(obj, OfferHelp)
    
    def test_OfferHelp_run(self):
        obj = self.actions("action_offer_help")
        dis, trac, dom = Mock(), Mock(), Mock()
        obj.run(dis, trac, dom)
        dis.utter_template.assert_called_with("action_offer_help")

    def test_SourceData_name(self):
        obj = self.actions("action_source_data")
        self.assertIsInstance(obj, SourceData)
    
    @patch('ckanext.rasa.data_bot.main.bot.actions.SourceData._my_func')
    def test_SourceData_run(self, mock__my_func):
        greet = self.actions("action_source_data")
        dis, trac, dom = Mock(), Mock(), Mock()
        greet.run(dis, trac, dom)
        dis.utter_message.assert_called()

    def test_Help_name(self):
        obj = self.actions("action_help")
        self.assertIsInstance(obj, Help)
    
    def test_Help_run(self):
        obj = self.actions("action_help")
        dis, trac, dom = Mock(), Mock(), Mock()
        functions = ",".join(FUNCTIONS)
        message = "Currently I can: \n{}.".format(functions)
        obj.run(dis, trac, dom)
        dis.utter_message.assert_called_with(message)
    
    def test_GiveUp_name(self):
        obj = self.actions("action_give_up")
        self.assertIsInstance(obj, GiveUp)
    
    def test_GiveUp_run(self):
        obj = self.actions("action_give_up")
        dis, trac, dom = Mock(), Mock(), Mock()
        message = "I'm still trying to understanding humans - try structuring your message in a different way. "
        obj.run(dis, trac, dom)
        dis.utter_message.assert_called_with(message)
    
    def test_ReofferHelp_name(self):
        obj = self.actions("action_reoffer_help")
        self.assertIsInstance(obj, ReofferHelp)
    
    def test_ReoffeHelp_run(self):
        obj = self.actions("action_reoffer_help")
        dis, trac, dom = Mock(), Mock(), Mock()
        obj.run(dis, trac, dom)
        dis.utter_template.assert_called_with("action_reoffer_help")

    def test_SourceDataPromptTags_name(self):
        obj = self.actions("action_source_data_prompt_tags")
        self.assertIsInstance(obj, SourceDataPromptTags)
    
    def test_SourceDataPromptTags_run(self):
        obj = self.actions("action_source_data_prompt_tags")
        dis, trac, dom = Mock(), Mock(), Mock()
        obj.run(dis, trac, dom)
        dis.utter_template.assert_called_with("action_source_data_prompt_tags")

    def test_ResetSlots_name(self):
        obj = self.actions("action_reset_slots")
        self.assertIsInstance(obj, ResetSlots)

    def test_ResetSlots_run(self):
        obj = self.actions("action_reset_slots")
        dis, trac, dom = Mock(), Mock(), Mock()
        res = obj.run(dis, trac, dom)
        from rasa_core.events import AllSlotsReset
        self.assertEqual(res, [AllSlotsReset()])

if __name__ == "__main__":
	main()