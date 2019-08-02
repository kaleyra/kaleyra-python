#!/usr/bin/env python

from api.txtly.txtly_request import TxtlyRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# The user can delete the created txtly links.
# If Txtly URL got deleted, then user won't be able to use it and redirect anywhere.

# id (Txtly ID) is a mandatory parameter.

txtlyRequest = TxtlyRequest(id='')

txtlyResponse = txtlyRequest.delete()

print(txtlyResponse.to_json())
print(txtlyResponse.get_status())
print(txtlyResponse.get_message())
print(txtlyResponse.get_data())
