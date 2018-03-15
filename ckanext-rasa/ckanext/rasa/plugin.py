import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.base import BaseController

import time
import logging
import cPickle as pkl
from data_bot.main.main import MODEL_PATH, INTEPRETER_PATH, AGENT_PKL_PATH
from rasa_core.agent            import Agent
from rasa_core.interpreter      import RasaNLUInterpreter

logger = logging.getLogger(__name__)


class RasaPlugin(plugins.SingletonPlugin): # Inherits PLugin Singleton Class

    # initialize agent
    logger.info("Instantiating Rasa Agent")
    start = time.time()
    global agent
    agent = Agent.load(MODEL_PATH, interpreter=RasaNLUInterpreter(INTEPRETER_PATH))    
    end = time.time()
    logger.info("Instantiatiation took {} seconds".format(end-start))

    
    plugins.implements(plugins.IConfigurer)
    def update_config(self, config_):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is
        toolkit.add_template_directory(config_, 'templates')

        # Register this plugin's fanstatic directory with CKAN.
        # Here, 'fanstatic' is the path to the fanstatic directory
        # (relative to this plugin.py file), and 'example_theme' is the name
        # that we'll use to refer to this fanstatic directory from CKAN
        # templates.
        toolkit.add_resource('fanstatic', 'rasa')

    plugins.implements(plugins.IRoutes)
    def after_map(self, map):
        map.connect(
            "rasa_user_message", # name of path route
            "/rasa/user/message", # url to map path to
            controller="ckanext.rasa.controller:RasaPluginController", # controller in rasa/controller.py
            action="send_user_message"
        )
        return map

    def before_map(self, map):
        return map
