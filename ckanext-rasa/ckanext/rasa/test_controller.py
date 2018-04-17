import ckanext.rasa.plugin as plugin
from unittest import TestCase, main
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

    @classmethod
    def setUpClass(cls):
        ckan.plugins.load('rasa')
        self.rasa_controller = RasaPluginController()
    
    @classmethod
    def tearDownClass(cls):
        ckan.plugins.unload('rasa')

    def test_send_user_message(self):
        pass

    @patch("ckan.common.response")
    @patch("ckan.common.request")
    @patch("ckan.common.session")
    @patch("ckan.lib.base.render")
    def test_databot_index(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
        mock = Mock()
        ret_val = self.rasa_controller.databot_index()
        self.assertEqual(ret_val, mock_render)
    
    @patch("ckan.common.response")
    @patch("ckan.common.request")
    @patch("ckan.common.session")
    @patch("ckan.lib.base.render")
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
        self.rasa_controller.test_send_user_message()
        assert hasattr(mock_response, "bot")

    
    @patch("ckan.common.response")
    @patch("ckan.common.request")
    @patch("ckan.common.session")
    @patch("ckan.lib.base.render")
    def test_send_user_message_error(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
        mock_request.body = []
        self.rasa_controller.test_send_user_message()
        assert hasattr(mock_response, "error")
        assert hasattr(mock_response, "bot")        
    
    @patch("ckan.common.response")
    @patch("ckan.common.request")
    @patch("ckan.common.session")
    @patch("ckan.lib.base.render")
    def test_rasa_handle_message(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
    
        message = "test message"
        sender_id = 1
        resp = self.rasa_controller.rasa_handler_message(message, sender_id)
        self.assertEqual(type(resp), list)
        self.assertEqual(resp[0].get("type"), "string")

    @patch("ckan.common.response")
    @patch("ckan.common.request")
    @patch("ckan.common.session")
    @patch("ckan.lib.base.render")
    def test_rasa_handle_message(
        self,
        mock_render,
        mock_session,
        mock_request,
        mock_response
    ):
    
        message = "test message"
        sender_id = 1
        resp = self.rasa_controller.rasa_handler_message(message, sender_id)
        self.assertEqual(type(resp), list)

class TestRasaCoreConnector(TestCase):

    def setUp(self):
        self.rasa_core_connector = RasaCoreConnector()

    @patch("urllib2.Request")
    @patch("urllib2.urlopen")
    def test__post(self, mock_Request, mock_urlopen):
        rcc = self.rasa_core_connector()
        rcc._post = Mock()
        resp = rcc._post("test_url", "test_query")
        rcc._post.assert_called_with("test_url", "test_query")
        self.assertEqual(type(resp), dict)

    @patch("urllib2.urlopen")
    def test__get(self, mock_Request, mock_urlopen):
        rcc = self.rasa_core_connector()
        rcc._get = Mock()
        resp = rcc._get("test_url", "test_query")
        rcc._get.assert_called_with("test_url", "test_query")
        self.assertEqual(type(resp), dict)
     
    def test_set_response_data(self):
        response_data = "abc"
        self.rasa_core_connector._set_response_data(response_data)
        self.assertEqual(self.rasa_core_connector.response_data, response_data)
    

class TestParseConnector(TestCase):
    def setUp(self):
        self.parse_connector = ParseConnector()
    
    def test_endpoint(self):
        self.assertEqual(self.parse_connector.endpoint,  "http://localhost:5005/conversations/{}/parse")

    @patch("ckanext.rasa.controller.RasaCoreConnector")
    def test_query_rasa(self):
        message = "test_message"
        sender_id = "test_sender_id"
        rpc = self.parse_connector
        rpc._set_response_data = Mock()
        rpc._post = Mock()
        resp = rpc.query_rasa(sender_id, message)
        rpc._post.assert_any_call()
        rpc._set_response_data.assert_any_call()
        self.assertEqual(type(resp), dict)

class TestContinueConnector(TestCase):
    def setUp(self):
        self.continue_connector = ContinueConnector()
    
    def test_query_rasa(self):
        sender_id = "test_sender_id"
        action_executed = "test_action"
        cc = self.continue_connector
        cc._post = Mock()
        cc._set_response_data = Mock()
        resp = rpc.query_rasa(sender_id, action_executed)
        cc._post.assert_any_call()
        cc._set_response_data.assert_any_call()
        self.assertEqual(type(resp), dict)

class TestVersionConnector(TestCase):
    def setUp(self):
        self.version_connector = VersionConnector()

    def test_query_rasa(self):
        vc = self.version_connector()
        vc._get = Mock()
        vc._set_response_data = Mock()
        vc.query_rasa()
        vc._get.assert_any_call()
        vc._set_response_data.assert_any_call()
        
if __name__ == "__main__":
    main()