#!/usr/bin/env python

import unittest
from api.messaging.group.group_request import GroupRequest
import tests.messaging.group.config_test_group as test

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

class TestGroupRequest(unittest.TestCase, GroupRequest):

    """Tests of the GroupRequest class"""


    def test_add_contacts(self):

        """test_add_contacts() will raise an AssertionError if number is not successfully added to the created group."""

        groupRequest = GroupRequest(group_name=test.a_group_name)
        groupRequest.create()
        groupRequest = GroupRequest(to=test.a_number, group_name=test.a_group_name)
        groupResponse = groupRequest.add()
        resp_message = groupResponse.get_message()
        resp_code = groupResponse.get_code()
        self.assertEqual(resp_message, 'Number has been added Successfully')
        self.assertEqual(resp_code, 200)


    def test_create_group(self):

        """test_create_group() will raise an AssertionError if group is not added successfully."""

        groupRequest = GroupRequest(group_name=test.c_group_name)
        groupResponse = groupRequest.create()
        resp_message = groupResponse.get_message()
        self.assertEqual(resp_message, 'Group added Successfully')


    def test_send_sms(self):

        """test_send_sms() will raise an AssertionError if message is not sent successfully to the created group."""

        groupRequest = GroupRequest(group_name=test.s_group_name)
        groupRequest.create()
        groupRequest = GroupRequest(to=test.s_number1, group_name=test.s_group_name)
        groupRequest.add()
        groupRequest = GroupRequest(group_name=test.s_group_name)
        groupRequest.create()
        groupRequest = GroupRequest(to=test.s_number2, group_name=test.s_group_name)
        groupRequest.add()
        groupRequest = GroupRequest(group_name=test.s_group_name, message=test.s_message)
        groupResponse = groupRequest.send()
        resp_message = groupResponse.get_message()
        self.assertEqual(resp_message, 'Submitted successfully')
        resp_status = groupResponse.get_status()
        self.assertEqual(resp_status, 'OK')
