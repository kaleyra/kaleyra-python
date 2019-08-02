#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# User will be able to check account usage for a given period.

# from_date, to_date are mandatory parameters.
# Format of the date has to be specified.

smsMessageRequest = SMSMessageRequest(from_date='', to_date='', format='')

smsMessageResponse = smsMessageRequest.credit_usage()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_status())
print(smsMessageResponse.get_total_credits())
print(smsMessageResponse.get_total_sms())
print(smsMessageResponse.get_start_date())
print(smsMessageResponse.get_end_date())
