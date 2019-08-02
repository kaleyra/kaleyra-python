#!/usr/bin/env python

from api.messaging.group.group_request import GroupRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# In this example, users can create a group, add contacts to that group and send a message to the same group,
# all in one

# Enter the new group name, contact numbers and the message to be sent below

GROUP_NAME = 'test'
NUMBER_1 = '918970736699'
NUMBER_2 = '918970736690'
# NUMBER_3 = ''
MESSAGE = 'hello'

groupRequest_create = GroupRequest(group_name=GROUP_NAME)
groupResponse_create = groupRequest_create.create()
print(groupResponse_create.to_json())

groupRequest_add = GroupRequest(to=NUMBER_1, group_name=GROUP_NAME)
groupResponse_add1 = groupRequest_add.add()
# groupRequest_add = GroupRequest(to=NUMBER_2, group_name=GROUP_NAME)
# groupResponse_add2 = groupRequest_add.add()
print(groupResponse_add1.to_json())
# print(groupResponse_add2.to_json())

groupRequest_send = GroupRequest(message=MESSAGE, group_name=GROUP_NAME,)
groupResponse_send = groupRequest_send.send()
smsMessageResponse = groupResponse_send.get_sms_message_responses()
print(groupResponse_send.to_json())
print(smsMessageResponse[0].get_id())
print(smsMessageResponse[0].get_mobile())
print(smsMessageResponse[1].get_mobile())
print(smsMessageResponse[0].get_status())
print(smsMessageResponse[1].get_status())
print(smsMessageResponse[0].get_mobile())
print(smsMessageResponse[1].get_mobile())
print(groupResponse_send.get_group_id())
