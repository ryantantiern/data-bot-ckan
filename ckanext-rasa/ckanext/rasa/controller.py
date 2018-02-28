import ckan.plugins as p
from ckan.lib.base import BaseController
from ckan.common import request, response

class RasaPluginController(BaseController):
    def send_user_message(self):
        response.body = "all ok!"
        return
