#!/usr/bin/env python

import json
from configuration.config import APIKEY

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(APIKEY)}


# noinspection PyBroadException
class TxtlyResponse:

    """
    Constructor parses the response received from the server and populates the attributes of the class. The
    attributes are then returned when a function call is made by the user.

    'response' parameter receives the HTTP response from the server.

    Note: The value of all attributes are initially considered as None.
    """

    def __init__(self, response):
        self.data = None
        self.id = None
        self.json_response = None
        self.message = None
        self.status = None
        self.token = None
        self.txtly = None
        self.txtlys = None

        # If JSON response is not received, an error message is displayed.

        try:
            self.json_response = json.dumps(response)
        except Exception:
            self.json_response = "JSON response not received."

        # If a field is missing from the response, appropriate error message is returned.
        # If the field is blank, None is returned.

        try:
            self.data = response["data"]
            if self.data is "":
                self.data = None
        except Exception:
            self.data = "'data' not found"

        try:
            self.id = response["id"]
            if self.id is "":
                self.id = None
        except Exception:
            self.id = "'id' not found"


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
            self.status = "'status' not found"


        try:
            self.token = response["token"]
            if self.token is "":
                self.token = None
        except Exception:
            self.token = "'token' not found"


        try:
            self.txtly = response["txtly"]
            if self.txtly is "":
                self.txtly = None
        except Exception:
            self.token = "'token' not found"


    # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
    # as per the user's requirements.


    def get_data(self):

        """

        :return:data
        """

        return self.data

    def get_id(self):

        """

        :return:id
        """

        return self.id

    def to_json(self):

        """

        :return:json
        """

        return self.json_response

    def get_message(self):

        """

        :return:message
        """

        return self.message

    def get_status(self):

        """

        :return:status
        """

        return self.status

    def get_token(self):

        """

        :return:token
        """

        return self.token

    def get_txtly_link(self):

        """

        :return:txtly
        """

        return self.txtly
