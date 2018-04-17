import ckanext.rasa.plugin as plugin
import ckan.plugins
from unittest import TestCase, main
from mock import Mock, patch, call
from ckanext.rasa.action_manager import greet, farewell, offer_help, source_data, provide_help, reoffer_help, prompt_tags, reset_slots, restart, execute_next_action

class TestActionManager(TestCase):

    def test_greet(self):
        resp = greet()
        self.assertEqual(type(resp), dict)


    def test_farewell(self):
        resp = farewell()
        self.assertEqual(type(resp), dict)
        
        
    def test_offer_help(self):
        resp = offer_help()
        self.assertEqual(type(resp), dict)
    
    @patch("ckanext.rasa.action_manager.UDLApiConnector")
    def test_source_data(self, mock_connector):
        tags = Mock()
        limit = Mock()
        data = {
            "tags": ["test_tag"],
            "limit" : 1
        }
        resp = source_data( ** data)
        mock_connector.search_packages = Mock()
        self.assertEqual(type(resp), dict)
        
    def test_provide_help(self):
        resp = provide_help()
        self.assertEqual(type(resp), dict)
        
    def test_reoffer_help(self):
        resp = reoffer_help()
        self.assertEqual(type(resp), dict)
        
    def test_promp_tags(self):
        resp = prompt_tags()
        self.assertEqual(type(resp), dict)
        
    def test_reset_slots(self):
        resp = reset_slots()
        self.assertEqual(type(resp), dict)
        self.assertEqual(resp.get("events"),  [{'event': 'reset_slots'}])
        
    def test_restart(self):
        resp = restart()
        self.assertEqual(type(resp), dict)
        self.assertEqual(resp.get("events"), [{'event': 'restart'}])

    def test_execute_next_action(self):
        action_name = "test"
        resp = execute_next_action(action_name, {})
        self.assertEqual(type(resp), dict)
        
if __name__ == "__main__":
    main()