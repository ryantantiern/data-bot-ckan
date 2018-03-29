 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from unittest import TestCase, main, skipIf
from mock import Mock, patch
from ckanext.rasa.data_bot.main.main import instantiate_agent, api_get_data, _filter_num_resources, _strip_data, _remove_control_chars
from ckanext.rasa.data_bot.main.extended import ExtendedAgent

class TestMainMethods(TestCase):

    def test__initialize_redis_tracker_store(self):
        pass
    
    def test_instantiate_agent(self):
        mock_agent = instantiate_agent(True)
        self.assertIsInstance(mock_agent, ExtendedAgent)
    
    @patch("ckanext.rasa.data_bot.main.main.urllib.urlopen")
    def test_api_get_data(self, mock_urlopen):
        mock = Mock()
        mock.read.side_effect = ['{"field1":"success"}']
        mock_urlopen.return_value = mock
        url = "http://notpercentencodedurl.com?test1=a b&goodbye=['bye']"
        res = api_get_data(url)
        self.assertEqual(res, {"field1" : "success"})
    
    def test_api_get_package_by_tag(self):
        pass

    def test__filter_num_resources(self):
        results = [
            {"data" : 1, "num_resources" : 0},
            {"data" : 2, "num_resources" : -1},
            {"data" : 3, "num_resources" : 5},
            {"data" : 4, "num_resources" : 1}   
        ]
        limit = 4
        res = _filter_num_resources(results, limit)
        self.assertEqual(len(res), 2)
        self.assertIn({"data": 3, "num_resources": 5}, res)
        self.assertIn({"data" : 4, "num_resources" : 1} , res)
        
    def test__filter_num_resources_limitedByLimit(self):
        results = [
            {"data" : 1, "num_resources" : 0},
            {"data" : 2, "num_resources" : -1},
            {"data" : 3, "num_resources" : 5},
            {"data" : 4, "num_resources" : 1},
            {"data" : 5, "num_resources" : 55},
            {"data" : 6, "num_resources" : 12},
            {"data" : 7, "num_resources" : 50},
            {"data" : 8, "num_resources" : 10}         
        ]
        limit = 4
        res = _filter_num_resources(results, limit)
        self.assertEqual(len(res), 4)

    def test_remove_control_chars(self):
        test_string = ("\n\tTEst")
        res = _remove_control_chars(test_string)
        self.assertEqual(res, "TEst")

    def test__strip_data(self):
        d = [{
            "title": "\t\ntest title",
            "num_resources": 100,
            "organization": {
                "title": "testOrg"
            }
        }]
        res = _strip_data(d)
        self.assertEqual(res, [{unicode("t"):unicode("Title: test title"), unicode("nr") : unicode("Num of resources: 100"), unicode("o"): unicode("Organization: testOrg") }])

    def test__format_results_into_message(self):
        # This method was never used
        pass



if __name__ == "__main__":
    main()