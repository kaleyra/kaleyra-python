#!/usr/bin/env python

from api.messaging.sms.sms_message_request import SMSMessageRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can schedule an sms to a specific time.
# SMS cannot be scheduled before 5 minutes and after 3 months from the date of scheduling the SMS.

# to, message and datetime are mandatory parameters.
# Format of the datetime must be specified.
# dlrurl, custom, unicode and flash are optional parameters.

smsMessageRequest = SMSMessageRequest(to='', message='')
smsMessageRequest.set_schedule(datetime='', format='')

smsMessageResponse = smsMessageRequest.schedule()

print(smsMessageResponse.to_json())
print(smsMessageResponse.get_data())
print(smsMessageResponse.get_id())
print(smsMessageResponse.get_customid())
print(smsMessageResponse.get_customid1())
print(smsMessageResponse.get_customid2())
print(smsMessageResponse.get_mobile())
print(smsMessageResponse.get_dlr_status())
print(smsMessageResponse.get_message())
