#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# User will be able to check the status of a sent/scheduled message

# Message ID (not group ID) is a mandatory parameter.
# numberinfo and page are optional parameters.

smsMessageRequest = SMSMessageRequest(id='')

smsMessageResponse = smsMessageRequest.sms_status()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_id())
print(smsMessageResponse.get_mobile())
print(smsMessageResponse.get_dlr_status())
print(smsMessageResponse.get_sent_time())
print(smsMessageResponse.get_delivery_time())
print(smsMessageResponse.get_customid())
print(smsMessageResponse.get_customid1())
print(smsMessageResponse.get_customid2())
print(smsMessageResponse.get_message())