#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# User will be able to delete a scheduled message.
# To delete a message, there should be a minimum gap of 5 minutes before its execution.

# groupid is a mandatory parameter.

smsMessageRequest = SMSMessageRequest(group_id='')


smsMessageResponse = smsMessageRequest.delete()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_status())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_message())

