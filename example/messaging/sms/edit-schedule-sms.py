#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Once an SMS has been scheduled, users will be able to edit  the schedule of the message.
# To edit a scheduled slot, there should a minimum gap of 5 minutes before its execution.

# datetime is a mandatory parameter.
# Format of the date must be specified.

smsMessageRequest = SMSMessageRequest(group_id='')
smsMessageRequest.set_schedule(datetime='', format='')

smsMessageResponse = smsMessageRequest.edit()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_status())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_message())
