#!/usr/bin/env python

from api.messaging.group.group_request import GroupRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can send an sms to a group.

# groupname and message are mandatory parameters.

groupRequest_send = GroupRequest(group_name='test', message="hello")

groupResponse_send = groupRequest_send.send()
smsMessageResponses = groupResponse_send.get_sms_message_responses()

print(groupResponse_send.to_json())
print(smsMessageResponses[0].get_id())
