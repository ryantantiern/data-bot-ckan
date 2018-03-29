 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import urllib
import json
import re
import unicodedata
import ckan.plugins.toolkit as toolkit
from rasa_core.interpreter                  import RasaNLUInterpreter
from rasa_core.tracker_store                import RedisTrackerStore    
from rasa_core.domain                       import TemplateDomain
from ckanext.rasa.data_bot.main.extended    import ExtendedRedisTrackerStore, ExtendedAgent
from ckan.common                            import config
from redis                                  import StrictRedis
from rq                                     import Queue

dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = os.path.join(dir_path, "models/dialogue")
INTEPRETER_PATH = os.path.join(dir_path, "models/nlu/default/current")
HOSTNAME = "http://udltest1.cs.ucl.ac.uk/" # config.get('ckan.site_url')
REDIS_HOST = "localhost"
PORT = 6379
DB = 2
QS = "databot"

"""
REDIS_HOST = config.get('ckan.rasa.redis.host')
PORT = toolkit.asint(config.get('ckan.rasa.redis.port'))
DB = toolkit.asint(config.get('ckan.rasa.redis.db'))
QS = config.get('ckan.rasa.rq.qs')
"""

logger = logging.getLogger(__name__)
redis_conn = StrictRedis(host=REDIS_HOST, port=PORT, db=DB)
all_chars = (unichr(i) for i in xrange(0x110000))
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
control_chars = ''.join(map(unichr, range(0, 32) + range(127, 160)))
control_char_re = re.compile('[%s]'% re.escape(control_chars))
agent = None

def _initialize_redis_tracker_store(mock):
    domain = TemplateDomain.load(os.path.join(MODEL_PATH, "domain.yml"))
    redis_tracker_store = ExtendedRedisTrackerStore(domain, db=2, timeout=900, mock=mock)   
    return redis_tracker_store

def instantiate_agent(mock=False):
    global agent
    tracker_store = _initialize_redis_tracker_store(mock)
    rasa_interpreter = RasaNLUInterpreter(INTEPRETER_PATH, lazy_init=True)        
    agent = ExtendedAgent.load(MODEL_PATH, interpreter=rasa_interpreter)
    agent.tracker_store = tracker_store
    return agent

def api_get_data(url):
    url = urllib.quote(url, safe=":/?=&")
    read = urllib.urlopen(url).read()
    return json.loads(read)

def api_get_package_by_tag(tags, limit=5):
    # Tags should be a string of tags, space seperated
    search_limit = int(limit) + 10
    if not tags:
        return "No datasets found"
    try:
        action = 'api/action/package_search?q={}&rows={}'.format(tags, search_limit)
        data = api_get_data(HOSTNAME + action)
    except IOError as e:
        logger.exception("Handling IOerror in api_get_package_by_tag(). tags: {}, limit: {}".format(tags, limit))
        return "Your request timed out while connecting to UDL's database. This means their server is down. Please report this to system administrators."
    except Exception as e:
        logger.exception("Handling error in api_get_package_by_tag(). tags: {}, limit: {}".format(tags, limit))
        return "An error had occured while processing your request. Please report the following to system administrators:/n {}: {}".format(e.errno, e.strerror)

    if not data["success"] or data["result"]["count"] == 0:
        return "No matching packages found"
    
    results = data["result"]["results"]
    results = _filter_num_resources(results, int(limit))

    # results is dict. need to be converted into list
    message = _format_results_into_message(results)
    return message

def _filter_num_resources(results, limit):
    # Filter results that have no resource
    res = []
    for i in range(len(results)):
        if results[i]["num_resources"] > 0:
            res.append(results[i])
            limit -= 1
        if limit == 0: return res
    return res


def _strip_data(results):
    res = []
    for r in results:
        d = {}
        d["t"] = "Title: " + _remove_control_chars(r["title"])
        d["nr"]= "Num of resources: " + str(r["num_resources"])
        d["o"] = "Organization: " + _remove_control_chars(r["organization"]["title"])
        res.append(d)
    return res

def _format_results_into_message(results):
    data = _strip_data(results)
    message = ""
    for i, d in enumerate(data):
        sent = "\n".join([d["t"], d["o"]])
        message += "\n" + str(i + 1) + ". " + sent +"\n"
    return message

def _remove_control_chars(s):
    return control_char_re.sub('', s)

instantiate_agent()