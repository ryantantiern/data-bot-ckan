from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import urllib
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = os.path.join(dir_path, "models/dialogue")
INTEPRETER_PATH = os.path.join(dir_path, "models/nlu/default/13_3_2018")
AGENT_PKL_PATH = os.path.join(dir_path, "agent.pkl")
HOSTNAME = "http://udltest1.cs.ucl.ac.uk/api/3/action/"

logger = logging.getLogger(__name__)


"""
There are 2 problems.
(1) during dev, data is queries using rest api whilst in prod, data is queried using 
ckan api
(2) when shifting from dev to prod, need to change data pipeline

solution:
(1) split the pipeline into 2 parts. The first retrieves raw data and returns dict. 
(2) the second takes the dict and does manipultation. 

that way, I only define (2) once, and add 2 new data pipelines (1 for dev, 1 for prod)
for each feature. 
"""

def api_get_data(url):
    url = urllib.quote(url, safe=":/?=&")
    print(url)
    read = urllib.urlopen(url).read()
    return json.loads(read)

def api_get_package_by_tag(tags, limit=5):
    # Tags should be a string of tags, space seperated
    if not tags:
        return "No datasets found"
    try:
        action = "package_search?fq=tags:{}&rows={}".format(tags, limit)
        data = api_get_data(HOSTNAME + action)
    except Exception as e:
        logger.exception("Handling error in api_get_package_by_tag(). tags: {}, limit: {}".format(tags, str(limit)))
        return "No datasets found"

    if not data["success"] or data["result"]["count"] == 0:
        return "Couldn't retrieve datasets."
    
    results = data["result"]["results"]
    message = ""
    titles = []
    for i in range(len(results)):
        message += str(i+1) + ". " + results[i]["title"] + "\n"
    message = message.rstrip()
    return message
    
