 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from unittest import TestCase, main, skipIf
from mock import Mock, patch
from ckanext.rasa.data_bot.main.main import UDLApiConnector
import ckan.plugins.toolkit as toolkit

class TestMainMethods(TestCase):

    def setUp(self):
        self.udl_api_connector = UDLApiConnector()
    
    def test_init(self):
        self.assertEqual(self.udl_api_connector.endpoints["package_search"], toolkit.get_action("package_search"))
    
    @patch("ckanext.rasa.data_bot.main.main.json.loads")                
    @patch("ckanext.rasa.data_bot.main.main.urllib2.urlopen")        
    def test__get(self, urlopen, loads):
        resource = "test1"
        self.udl_api_connector._get(resource)
        urlopen.assert_called_with("http://udltest1.cs.ucl.ac.uk/test1")
        
    
    # @patch("ckanext.rasa.data_bot.main.main.urllib2.urlopen")
    # def test_api_get_data(self, mock_urlopen):
    #     mock = Mock()
    #     mock.read.side_effect = ['{"field1":"success"}']
    #     mock_urlopen.return_value = mock
    #     url = "http://notpercentencodedurl.com?test1=a b&goodbye=['bye']"
    #     res = api_get_data(url)
    #     self.assertEqual(res, {"field1" : "success"})

    def test__filter_num_resources(self):
        results = [
           {"num_resources": 2},
           {"num_resources": 2},
           {"num_resources": 2},
           {"num_resources": 2},
           {"num_resources": 2},
           {"num_resources": 2},           
        ]
        limit = 4
        res = self.udl_api_connector._filter_num_resources(results, limit)
        self.assertEqual(len(res), 4)

    def test__strip_data(self):
        d = [{
            "title": "\t\ntest title",
            "num_resources": 100,
            "organization": {
                "title": "testOrg"
            }
        }]
        res = self.udl_api_connector._strip_data(d)
        self.assertEqual(res, [
            {
            unicode("title"): unicode("test title"),
            unicode("num_of_resources"): unicode("100"),
            unicode("org"): unicode("testOrg"),
            unicode("type"): unicode("source_data_object")
             }])





if __name__ == "__main__":
    main()