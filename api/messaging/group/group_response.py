#!/usr/bin/env python

import json
from api.messaging.sms.sms_message_response import SMSMessageResponse
from api.messaging.k_response import KResponse
from configuration.config import APIKEY

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(APIKEY)}


# noinspection PyBroadException
class GroupResponse(KResponse):
    def __init__(self, data=None, json_response=None, message=None, status=None, status_code=None, response=None):

        """
        Constructor parses the response received from the server and populates the attributes of the class. The
        attributes are then returned when a function call is made by the user.

        'response' parameter receives the HTTP response from the server.

        Note: The value of all attributes are initially considered as None.
        """

        KResponse.__init__(self, data, json_response, message, status, status_code)

        # If JSON response is not received, error message is displayed.
        try:
            self.json_response = json.dumps(response)
        except Exception:
            self.json_response = "Response not received."

        # If a field is missing from the response, appropriate error message is returned.
        # If the field is blank, None is returned.

        try:
            self.data = response["data"]
            if self.data is "":
                self.data = None
        except Exception:
            self.data = "'data' not found"


        try:
            self.message = response["message"]
            if self.message is "":
                self.message = None
        except Exception:
            self.message = "'message' not found"


        try:
            self.status = response["status"]
            if self.status is "":
                self.status = None
        except Exception:
            self.message = "'status' not found"


        try:
            self.status_code = response["code"]
            if self.status_code is "":
                self.status_code = None
        except Exception:
            self.status_code = "'code' not found"


        self.group_id = None

        # SMSMessageResponse objects are created and appended to a list and the list is returned to the user.

        self.smsMessageResponses = []
        dataFlag = False
        for k, v in response.items():
            if k == 'data':
                dataFlag = True
        if dataFlag:
            if isinstance(response['data'], list):
                pass
            else:
                for k, v in response['data'].items():
                    if k == 'group_id':
                        self.group_id = response['data']['group_id']
                    else:
                        smsMessageResponse = SMSMessageResponse(response=v, position=k)
                        self.smsMessageResponses.append(smsMessageResponse)

    # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
    # as per the user's requirements.

    def get_data(self):
        """

        :return:data
        """

        return self.data

    def get_group_id(self):

        """

        :return:group_id
        """

        return self.group_id

    def to_json(self):

        """

        :return:json_response
        """

        return self.json_response

    def get_message(self):

        """

        :return:message
        """

        return self.message

    def get_sms_message_responses(self):

        """

        :return:smsMessageResponse
        """

        return self.smsMessageResponses

    def get_status(self):

        """

        :return:status
        """

        return self.status

    def get_status_code(self):

        """

        :return:status_code
        """

        return self.status_code
