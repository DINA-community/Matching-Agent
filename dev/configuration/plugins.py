"""Necessary Plugins for the application in NetBox"""

PLUGINS = ["csaf", "d3c"]

# Configuration for local use of synchronisers and isduba'
# PLUGINS_CONFIG = {
#   "d3c": {
#     'top_level_menu': True
#   },
#   'csaf': {
#     'isduba': {
#       'keycloak_url': 'http://keycloak.localhost/',
#       'keycloak_verify_ssl': False,
#       'username': 'user',
#       'password': 'user'
#     },
#     'synchronisers': {
#         'username': 'admin',
#         'password': 'admin2',
#         'verify_ssl': False,
#         'urls': [
#             {
#                 'name': 'ISDuBA Sync',
#                 'url': 'http://localhost:8991/',
#             },
#             {
#                 'name': 'Netbox Sync',
#                 'url': 'http://localhost:8992/',
#             },
#             {
#                 'name': 'CSAF Matcher',
#                 'url': 'http://localhost:8998/',
#             }
#         ]
#     }
#   }
# }
