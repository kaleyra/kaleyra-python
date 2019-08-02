#!/usr/bin/env python

from api.txtly.txtly_request import TxtlyRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Txtly is basically a shortened URL which can be used within text messages so that SMS would not exceed
# the specified characters.

# The user will be able to create txtly links.

# url, token and title are mandatory parameters.
# advanced and track are optional parameters.

txtlyRequest = TxtlyRequest(url='https://github.com/thelikhit/kaleyra-python', token='git', title='Git')

txtlyResponse = txtlyRequest.create()

print(txtlyResponse.to_json())
print(txtlyResponse.get_status())
print(txtlyResponse.get_message())
print(txtlyResponse.get_token())
print(txtlyResponse.get_id())
print(txtlyResponse.get_txtly_link())
