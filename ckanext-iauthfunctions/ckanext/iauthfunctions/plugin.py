import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def group_create(context, data_dict=None):
    print("In group create: ")
    print(data_dict)
    # Get the username of logged in user
    user_name = context['user']

    # Get a list of members of the 'test-curators' group
    try:
        members = toolkit.get_action("member_list")(
            data_dict={"id": "test-curators", "object_type": "user"}
        )
    except toolkit.ObjectNotFound:
        # test-curators group does not exist
        return {'success': False,
                'msg': "The test-curators groups doesn't exist, so only sysadmins are authorized to create groups."
                }

    # Members is a list of (user_id, object_type, capacity)
    # We're only interested in the user_id
    members_id = [member[0] for member in members]

    # Get the logged in user's id
    convert_user_name_or_id_to_id = toolkit.get_converter("convert_user_name_or_id_to_id")
    try:
        user_id = convert_user_name_or_id_to_id(user_name, context)
    except toolkit.Invalid:
        return {
        'success': False,
        'msg': 'You must be logged-in as a member of the curators group to create new groups.'
        }
    print("Out of group create")
    # Test whether the member is of the curators group
    if user_id in members_id:
        return {"success": True}
    else:
        return {
        "success": False,
        "msg": "Only test-curators are allowed to create groups"
        }

class ExampleIauthfunctionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)

    def get_auth_functions(self):
        return {"group_create": group_create}
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'iauthfunctions')
