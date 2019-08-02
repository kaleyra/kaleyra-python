#!/usr/bin/env python

import unittest
from api.txtly.txtly_request import TxtlyRequest
import tests.txtly.config_test_txtly as test

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

class TestTxtlyRequest(unittest.TestCase, TxtlyRequest):

    """Tests of the TxtlyRequest class"""

    def test_create(self):

        """test_create() will raise an AssertionError if txtly link is not created successfully."""

        txtlyRequest = TxtlyRequest(url=test.c_url, token=test.c_token,
                                    title=test.c_title)
        txtlyResponse = txtlyRequest.create()
        resp_status = txtlyResponse.get_status()
        resp_message = txtlyResponse.get_message()
        self.assertEqual(resp_status, 'OK')
        self.assertEqual(resp_message, 'Details saved Successfully')

    def test_delete(self):

        """test_delete() will raise an AssertionError if created txtly link is not deleted successfully."""

        txtlyRequest = TxtlyRequest(url=test.d_url, token=test.d_token,
                                    title=test.d_title)
        txtlyResponse = txtlyRequest.create()
        resp_id = txtlyResponse.get_id()
        txtlyRequest = TxtlyRequest(id=resp_id)
        txtlyResponse = txtlyRequest.delete()
        resp_status = txtlyResponse.get_status()
        resp_message = txtlyResponse.get_message()
        self.assertEqual(resp_status, 'OK')
        self.assertEqual(resp_message, 'Deleted successfully..')

    def test_get_log(self):
        txtlyRequest = TxtlyRequest(id=test.l_id)
        txtlyResponse = txtlyRequest.log()
        resp_status = txtlyResponse.get_status()
        resp_message = txtlyResponse.get_message()
        self.assertEqual(resp_status, 'OK')
        self.assertEqual(resp_message, 'OK')


    def test_get_report(self):
        """test_get_report() will raise an AssertionError if report is not generated."""

        txtlyRequest = TxtlyRequest()
        txtlyResponse = txtlyRequest.report()
        resp_status = txtlyResponse.get_status()
        resp_message = txtlyResponse.get_message()
        self.assertEqual(resp_status, 'OK')
        self.assertEqual(resp_message, 'OK')
