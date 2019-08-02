#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can send an SMS to a number.

# to, message and are mandatory parameters.
# dlrurl, custom, unicode and flash are optional parameters.

smsMessageRequest = SMSMessageRequest(message='HELLO', to='917259819753')

smsMessageResponse = smsMessageRequest.send()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_id())
print(smsMessageResponse.get_customid())
print(smsMessageResponse.get_customid1())
print(smsMessageResponse.get_customid2())
print(smsMessageResponse.get_mobile())
print(smsMessageResponse.get_dlr_status())
print(smsMessageResponse.get_message())
print(smsMessageResponse.get_credits())
