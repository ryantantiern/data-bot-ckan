 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import urllib2
import json
import re
import unicodedata
import ckan.plugins.toolkit as toolkit

dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = os.path.join(dir_path, "models/dialogue")
INTEPRETER_PATH = os.path.join(dir_path, "models/nlu/default/newest")
HOSTNAME = "http://udltest1.cs.ucl.ac.uk/" # config.get('ckan.site_url')
REDIS_HOST = "localhost"
PORT = 6379
DB = 2
QS = "databot"

logger = logging.getLogger(__name__)
all_chars = (unichr(i) for i in xrange(0x110000))
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
control_chars = ''.join(map(unichr, range(0, 32) + range(127, 160)))
control_char_re = re.compile('[%s]'% re.escape(control_chars))

class UDLApiConnector(object):
    
    hostname = "http://udltest1.cs.ucl.ac.uk/"
    prod = True
    def __init__(self):
        if not self.prod:
            self.endpoints = {
                "package_search": 'api/action/package_search?q={}&rows={}'
            }
        else:
            self.endpoints = {
                 "package_search": toolkit.get_action("package_search")
            }
    def _get(self, resource, safe_chars=":/?=&"):
        try:
            url = self.hostname + resource
            url = urllib2.quote(url, safe=safe_chars) if safe_chars else url
            f = urllib2.urlopen(url)
            response = f.read()
            return json.loads(response)
        except urllib2.URLError as e:
            raise urllib2.URLError

    def search_packages(self, tags, limit=5):
        """
        tags: List[String]
        limit: Int
        return: List[Dict]
        """
        if not tags:
            data = [{
                "type": "string",
                "data": "No search tags were detected"
            }]
            return data
        resp = []        
        search_limit = limit + 10
        try:
            if not self.prod:
                resource = self.endpoints["package_search"].format(tags, search_limit)
                response = self._get(resource)
                results = response["result"]["results"]
            else:
                response = self.endpoints["package_search"](
                    data_dict = {
                        "q": tags,
                        "rows": search_limit
                    }
                )
                results = response["results"]
            results = self._filter_num_resources(results, limit)
            results = self._strip_data(results)
            if len(results) == 0:
                results.append({
                        "type": "string",
                        "data": "No results found. You can't access UDL CKAN Server without being on UCL's network."
                    })
            return results
        except urllib2.URLError as e:
            return[{
                "type":"string",
                "data": "URLError: Failed to access UDL CKAN server"
                }]


    def _filter_num_resources(self, results, limit):
        # Filter results that have no resource
        res = []
        for i in range(len(results)):
            if results[i]["num_resources"] > 0:
                res.append(results[i])
                limit -= 1
            if limit == 0: return res
        return res
    
    def _strip_data(self, results):
        def _remove_control_chars(s):
            return control_char_re.sub('', s)
        res = []
        for r in results:
            d = {}
            d["type"] = "source_data_object"
            d["title"] =  _remove_control_chars(r["title"])
            d["num_of_resources"]=  str(r["num_resources"])
            d["org"] =  _remove_control_chars(r["organization"]["title"])
            res.append(d)
        return res

