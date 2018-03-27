from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import urllib
import json
import time
import ckan.plugins.toolkit as toolkit
from rasa_core.agent                        import Agent
from rasa_core.interpreter                  import RasaNLUInterpreter
from rasa_core.tracker_store                import RedisTrackerStore    
from rasa_core.domain                       import TemplateDomain
from ckanext.rasa.data_bot.main.bot.utils   import ExtendedRedisTrackerStore
from ckan.common                            import config
from redis                                  import StrictRedis
from rq                                     import Queue

dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = os.path.join(dir_path, "models/dialogue")
INTEPRETER_PATH = os.path.join(dir_path, "models/nlu/default/current")
HOSTNAME = config.get('ckan.site_url')
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
agent, ipreter = None, None
redis_conn = StrictRedis(host=REDIS_HOST, port=PORT, db=DB)
q = Queue(QS, connection=redis_conn)
rasa_interpreter = RasaNLUInterpreter(INTEPRETER_PATH, lazy_init=True)

def run_initialize_interpreter_job():
    global ipreter
    # agent = q.enqueue(instantiate_agent)
    ipreter = q.enqueue(_initialize_interpreter)    

def _initialize_redis_tracker_store():
    # logger.info("Initializing Redis tracker store")
    domain = TemplateDomain.load(os.path.join(MODEL_PATH, "domain.yml"))
    redis_tracker_store = ExtendedRedisTrackerStore(domain, db=2, timeout=900)   
    # logger.info("Initialization of Redis tracker store complete")     
    return redis_tracker_store

def _initialize_interpreter():
    rasa_interpreter._load_interpreter()
    return 1

def instantiate_agent(interpreter):
    tracker_store = _initialize_redis_tracker_store()    
    agent = Agent.load(MODEL_PATH, interpreter=interpreter, tracker_store=tracker_store) 
    return agent

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
        action = "package_search?fq=tags:   {}&rows={}".format(tags, limit)
        data = api_get_data(HOSTNAME + action)
    except Exception as e:
        logger.exception("Handling error in api_get_package_by_tag(). tags: {}, limit: {}".format(tags, str(limit)))
        return "No datasets found"

    if not data["success"] or data["result"]["count"] == 0:
        return "Couldn't retrieve datasets."
    
    results = data["result"]["results"]
    message = _format_results_into_message(results)
    return message

def _format_results_into_message(results):
    message = ""
    titles = []
    for i in range(len(results)):
        message += str(i+1) + ". " + results[i]["title"] + "\n"
    message = message.rstrip()
    return message
