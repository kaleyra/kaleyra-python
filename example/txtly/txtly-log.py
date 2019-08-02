#!/usr/bin/env python

from api.txtly.txtly_request import TxtlyRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# The user will be able to pull out event logs for particular txtly URL.
# A Txtly campaign must be created and executed to track its logs.

# id (Txtly ID) is a mandatory parameter.


logRequest = TxtlyRequest(id='778975090')
logResponse = logRequest.log()
txtlys = logResponse.get_txtlys_responses()
pagination = logResponse.get_pagination_responses()

print(logResponse.get_message())
print(logResponse.get_txtlys())
print(logResponse.to_json())
print(txtlys[1].get_log_id())
print(txtlys[3].get_log_id())
print(txtlys[0].get_fk_link_id())
print(txtlys[3].get_browser_version())
print(pagination.get_now())
print(pagination.get_limit())
print(pagination.get_limitstart())
