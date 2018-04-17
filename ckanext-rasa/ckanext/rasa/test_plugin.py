import ckanext.rasa.plugin as plugin
from unittest import TestCase, main
from mock import Mock, patch, call


class TestPlugin(TestCase):
    def setUp(self):
        self.rasa_plugin = plugin.RasaPlugin()

    @patch("ckan.plugins.toolkit.add_resource")
    @patch("ckan.plugins.toolkit.add_template_directory")
    def test_update_config(self, mock_add_res, mock_add_tempdir):
        mock = Mock()
        self.rasa_plugin.update_config(mock)
        mock_add_res.assert_called_with(mock, "templates")
        mock_add_tempdir.assert_called_with('fanstatic', 'rasa')
    
    def test_after_map(self):
        mock = Mock()
        self.rasa_plugin.after_map(mock)
        calls = [
            call.connect("databot_user_message", "/databot/user/message", controller="ckanext.rasa.controller:RasaPluginController", action="send_user_message"),
            call.connect("data_bot", "/databot",controller="ckanext.rasa.controller:RasaPluginController", action="databot_index")
            ]
        self.assertEqual(mock.mock_calls, calls)
    
    def test_before_map(self):
        mock = Mock()
        res = self.rasa_plugin.before_map(mock)
        self.assertEqual(res, mock)
    
if __name__ == "__main__":
    main()