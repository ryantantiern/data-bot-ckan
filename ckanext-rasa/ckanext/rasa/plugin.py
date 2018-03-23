import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.base import BaseController
from data_bot.main.main import run_initialize_interpreter_job

class RasaPlugin(plugins.SingletonPlugin): # Inherits PLugin Singleton Class

    # Initilize the agent in the background
    run_initialize_interpreter_job()

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
            "databot_user_message", # name of path route
            "/databot/user/message", # url to map path to
            controller="ckanext.rasa.controller:RasaPluginController", # controller in rasa/controller.py
            action="send_user_message"
        )

        map.connect(
            "data_bot", # name of path route
            "/databot", # url to map path to
            controller="ckanext.rasa.controller:RasaPluginController", # controller in rasa/controller.py
            action="databot_index"
        )

        return map

    def before_map(self, map):
        return map
