#!/usr/bin/env python

from api.messaging.group.group_request import GroupRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can add contacts to a sms group that has been created.

# number and groupname are mandatory parameters.
# fullname and email-id are optional parameters.

groupRequest_add = GroupRequest(to='917259819753', group_name='test')
groupResponse_add = groupRequest_add.add()

print(groupResponse_add.to_json())
print(groupResponse_add.get_status())
print(groupResponse_add.get_status_code())
# print(groupResponse_add.get_code())
print(groupResponse_add.get_message())
