import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
from ckan.lib.base import BaseController
from data_bot.main.main import dir_path
import os.path as path

# Setup all logging

# log = logging.getLogger("rasa logs")
# log.setLevel(logging.DEBUG)
# fh = logging.FileHandler(path.join(dir_path, "bot/logs/rasa_core.log"))
# fh.setLevel(logging.DEBUG)
# fh2 = logging.FileHandler(path.join(dir_path, "bot/logs/rasa_core.log"))
# fh2.setLevel(logging.INFO)
# log.addHandler(fh)
# log.addHandler(fh2)

# warning_logger = logging.getLogger("py.warning")
# warning_fh = logging.FileHandler(path.join(dir_path, "bot/logs/warnings.log"))
# warning_fh.setLevel(logging.WARNING)    
# warning_logger.addHandler(warning_fh)


class RasaPlugin(plugins.SingletonPlugin): # Inherits PLugin Singleton Class

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
