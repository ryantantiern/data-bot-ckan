import ckanext.rasa.plugin as plugin
from unittest import TestCase, main, skip
from mock import Mock, patch, call
from ckanext.rasa.controller import _update_slot_and_next_action, RasaPluginController, RasaCoreConnector, ParseConnector, ContinueConnector, VersionConnector
import ckan.plugins

class TestController(TestCase):
    def setUp(self):
        pass

    def test__update_slot_and_next_action_withSlot(self):
        data = {}
        response = {
            "next_action": "action_1",
            "tracker": {
                "slots": {
                    "slot1" : True
                }
            }
        }
        _update_slot_and_next_action(data, response)
        self.assertEqual(data, {
            "next_action": "action_1",
            "slots": {
                "slot1" : True
            }
        })
    

    def test__update_slot_and_next_action_withoutSlot(self):
        data = {}
        response = {
            "next_action": "action_1",
            "tracker": {
            }
        }
        _update_slot_and_next_action(data, response)
        self.assertEqual(data, {
            "next_action": "action_1",
            "slots": {}
        })    

    def test__update_slot_and_next_action_withError(self):
        data = {}
        response = {
            "error" : "err_message"
        }
        _update_slot_and_next_action(data, response)
        self.assertEqual(data, {
            "error": "err_message",
            "next_action": None,
            "slots": {}
        })
    

class TestRasaPluginController(TestCase):

    def setUp(self):
        self.rasa_controller = RasaPluginController()


    @patch("ckanext.rasa.controller.response")
    @patch("ckanext.rasa.controller.request")
    @patch("ckanext.rasa.controller.session")
    @patch("ckanext.rasa.controller.render")
    def test_databot_index(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
        ret_val = self.rasa_controller.databot_index()
        self.assertIsInstance(ret_val, Mock)
    

    
    @patch("ckanext.rasa.controller.response")
    @patch("ckanext.rasa.controller.request")
    @patch("ckanext.rasa.controller.session")
    @patch("ckanext.rasa.controller.render")
    def test_send_user_message(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
        mock_request.body = {
            "text" : "test_text"
        }
        self.rasa_controller.send_user_message()
        assert hasattr(mock_response, "bot")

    @patch("ckanext.rasa.controller.response")
    @patch("ckanext.rasa.controller.request")
    @patch("ckanext.rasa.controller.session")
    @patch("ckanext.rasa.controller.render")
    def test_send_user_message_error(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
        mock_request.body = []
        self.rasa_controller.send_user_message()
        assert hasattr(mock_response, "error")
        assert hasattr(mock_response, "bot")        
    

    @patch("ckanext.rasa.controller.response")
    @patch("ckanext.rasa.controller.request")
    @patch("ckanext.rasa.controller.session")
    @patch("ckanext.rasa.controller.render")
    def test_rasa_handle_message(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
    
        message = "test message"
        sender_id = 1
        resp = self.rasa_controller.rasa_handle_message(message, sender_id)
        self.assertEqual(type(resp), dict)
        self.assertEqual(resp.get("type"), "list")
    
class TestRasaCoreConnector(TestCase):

    def setUp(self):
        self.rasa_core_connector = RasaCoreConnector()

    @patch("ckanext.rasa.controller.urllib2.Request")
    @patch("ckanext.rasa.controller.urllib2.urlopen")
    def test__post(self, mock_Request, mock_urlopen):
        rcc = self.rasa_core_connector
        rcc._post = Mock()
        resp = rcc._post("test_url", "test_query")
        rcc._post.assert_called_with("test_url", "test_query")
        self.assertIsInstance(resp, Mock)
    
    @patch("ckanext.rasa.controller.urllib2.Request")
    @patch("ckanext.rasa.controller.urllib2.urlopen")
    def test__get(self, mock_Request, mock_urlopen):
        rcc = self.rasa_core_connector
        rcc._get = Mock()
        resp = rcc._get("test_url")
        rcc._get.assert_called_with("test_url")
        self.assertIsInstance(resp, Mock)
     
    def test_set_response_data(self):
        response_data = "abc"
        self.rasa_core_connector._set_response_data(response_data)
        self.assertEqual(self.rasa_core_connector.response_data, response_data)
    

class TestParseConnector(TestCase):
    def setUp(self):
        self.parse_connector = ParseConnector()
    
    def test_endpoint(self):
        self.assertEqual(self.parse_connector.endpoint,  "http://localhost:5005/conversations/{}/parse")
    
    @patch("ckanext.rasa.controller.ParseConnector._set_response_data")    
    @patch("ckanext.rasa.controller.ParseConnector._post")
    def test_query_rasa(self, mock_post, mock_set_response_data):
        message = "test_message"
        sender_id = "test_sender_id"
        resp = self.parse_connector.query_rasa(sender_id, message)
        self.assertEqual(type(resp), dict)

class TestContinueConnector(TestCase):
    def setUp(self):
        self.continue_connector = ContinueConnector()
    
    @patch("ckanext.rasa.controller.ContinueConnector._set_response_data")    
    @patch("ckanext.rasa.controller.ContinueConnector._post")
    def test_query_rasa(self, mock_post, mock_set_response_data):
        sender_id = "test_sender_id"
        action_executed = "test_action"
        resp = self.continue_connector.query_rasa(sender_id, action_executed)
        self.assertEqual(type(resp), dict)

class TestVersionConnector(TestCase):
    def setUp(self):
        self.version_connector = VersionConnector()

    @patch("ckanext.rasa.controller.VersionConnector")
    def test_query_rasa(self, mock_version_controller):
        mock_version_controller.query_rasa()
        
if __name__ == "__main__":
    main()