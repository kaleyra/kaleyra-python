#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest


__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# The user will be able to check available credits in his/her account.

# No parameters are required.

smsMessageRequest = SMSMessageRequest()

smsMessageResponse = smsMessageRequest.credit_status()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_status())

print(smsMessageResponse.get_status_code())
print(smsMessageResponse.get_message())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_credits())


