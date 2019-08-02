#!/usr/bin/env python

from api.messaging.group.group_request import GroupRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can send an sms to an optin group.

# groupname and message are mandatory parameters.

groupRequest_send_optin = GroupRequest(group_name='', to='')

groupResponse_send_optin = groupRequest_send_optin.send_optin()

groupResponse_send_optin.to_json()
groupResponse_send_optin.get_message()
groupResponse_send_optin.get_data()
groupResponse_send_optin.get_id()
groupResponse_send_optin.get_customid()
groupResponse_send_optin.get_customid1()
groupResponse_send_optin.get_customid2()
groupResponse_send_optin.get_mobile()
groupResponse_send_optin.get_dlr_status()
groupResponse_send_optin.get_group_id()
