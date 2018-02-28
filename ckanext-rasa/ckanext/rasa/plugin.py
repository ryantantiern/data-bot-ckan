import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class RasaPlugin(plugins.SingletonPlugin): # Inherits PLugin Singleton Class
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)
    # IConfigurer

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
    # 
    # def after_map(map):
    #     map.connect("rasa/message/send")
