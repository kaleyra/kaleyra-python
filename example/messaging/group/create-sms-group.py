#!/usr/bin/env python

from api.messaging.group.group_request import GroupRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# User's can create a group of contacts so that you can simply use the group name to send SMS instead of
# adding multiple numbers manually.

# groupname is a mandatory parameter.

groupRequest_create = GroupRequest(group_name='test')

groupResponse_create = groupRequest_create.create()

print(groupResponse_create.to_json())
print(groupResponse_create.get_status())
print(groupResponse_create.get_message())
print(groupResponse_create.get_status())
