#!/usr/bin/env python

import unittest
from api.messaging.sms.sms_message_request import SMSMessageRequest
import tests.messaging.sms.config_test_sms as test

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

class TestSMSMessageRequest(unittest.TestCase, SMSMessageRequest):

    """Tests of the SMSMessageRequest class"""

    def test_sms_status(self):

        """test_sms_status() will raise an AssertionError if sms status response is not processed successfully"""

        smsMessageRequest = SMSMessageRequest(to=test.s_to, message=test.s_message)
        smsMessageResponse = smsMessageRequest.send()
        resp_id = smsMessageResponse.get_id()
        smsMessageRequest = SMSMessageRequest(id=resp_id)
        smsMessageResponse = smsMessageRequest.sms_status()
        resp_message = smsMessageResponse.get_message()
        self.assertEqual(resp_message, 'Processed Successfully')


    def test_credit_status(self):

        """test_credit_status() will raise an AssertionError if credit status response is not obtained"""

        smsMessageRequest = SMSMessageRequest()
        smsMessageResponse = smsMessageRequest.credit_status()
        resp_code = smsMessageResponse.get_status_code()
        self.assertEqual(resp_code, '200')


    def test_check_credit_usage(self):

        """test_check_credit_usage() will raise an AssertionError if sms status response is not processed successfully"""

        smsMessageRequest = SMSMessageRequest(from_date=test.u_from_date, to_date=test.u_to_date,
                                              format=test.u_format)
        smsMessageResponse = smsMessageRequest.credit_usage()
        resp_status = smsMessageResponse.get_status()
        self.assertEqual(resp_status, 'OK')


    def test_delete(self):

        """test_delete() will raise an AssertionError if message is not scheduled and then deleted successfully"""

        smsMessageRequest = SMSMessageRequest(to=test.sch_to, message=test.sch_message)
        smsMessageRequest.set_schedule(datetime=test.sch_datetime, format=test.sch_format)
        smsMessageResponse = smsMessageRequest.schedule()
        resp_id = str(smsMessageResponse.get_id())
        print(resp_id)
        smsMessageRequest = SMSMessageRequest(group_id=resp_id)
        smsMessageResponse = smsMessageRequest.delete()
        resp_message = smsMessageResponse.get_message()
        self.assertEqual(resp_message, 'Campaign canceled successfully and credits are refunded.')


    def test_edit(self):

        """test_edit() will raise an AssertionError if message is not scheduled and then edited successfully"""

        smsMessageRequest = SMSMessageRequest(to=test.sch_to, message=test.sch_message)
        smsMessageRequest.set_schedule(datetime=test.sch_datetime, format=test.sch_format)
        smsMessageResponse = smsMessageRequest.schedule()
        resp_id = smsMessageResponse.get_id()
        smsMessageRequest = SMSMessageRequest(group_id=resp_id, datetime=test.e_datetime,
                                              format=test.e_format)
        smsMessageResponse = smsMessageRequest.edit()
        resp_message = smsMessageResponse.get_message()
        self.assertEqual(resp_message, 'Campaign updated successfully')


    def test_schedule(self):

        """test_schedule() will raise an AssertionError if message is not scheduled successfully"""

        smsMessageRequest = SMSMessageRequest(to=test.sch_to, message=test.sch_message)
        smsMessageRequest.set_schedule(datetime=test.sch_datetime, format=test.sch_format)
        smsMessageResponse = smsMessageRequest.schedule()
        resp_message = smsMessageResponse.get_message()
        self.assertEqual(resp_message, 'Campaign of 1 numbers Scheduled successfully.')
        resp_status = smsMessageResponse.get_dlr_status()
        self.assertEqual(resp_status, 'AWAITED-DLR')


    def test_send(self):

        """test_send() will raise an AssertionError if message is not sent successfully"""

        smsMessageRequest = SMSMessageRequest(to=test.s_to, message=test.s_message)
        smsMessageResponse = smsMessageRequest.send()
        resp_message = smsMessageResponse.get_message()
        self.assertEqual(resp_message, 'Campaign of 1 numbers Submitted successfully.')
        resp_status = smsMessageResponse.get_dlr_status()
        self.assertEqual(resp_status, 'AWAITED-DLR')


if __name__ == '__main':
    unittest.main()
