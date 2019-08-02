#!/usr/bin/env python

import json
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
class SMSMessageResponse(KResponse):

    def __init__(self, data=None, message=None, status=None, status_code=None, response=None,
                 position=None):

        """
        Constructor parses the response received from the server and populates the attributes of the class. The
        attributes are then returned when a function call is made by the user.

        'response' parameter receives the HTTP response from the server.

        Note: The value of all attributes are initially considered as None.
        """

        KResponse.__init__(self, data, response, message, status, status_code)

        # inherited attributes
        self.data = data
        self.json_response = response
        self.message = message
        self.status = status
        self.status_code = status_code

        # GroupResponse attributes
        self.credits = None
        self.customid = None
        self.customid1 = None
        self.customid2 = None
        self.dlr_status = None
        self.dlr_time = None
        self.end_date = None
        self.id = None
        self.mobile = None
        self.sent_time = None
        self.start_date = None
        self.total_credits = None
        self.total_sms = None


        # If JSON response is not received, an error message is displayed.
        try:
            self.json_response = json.dumps(response)
        except Exception:
            print("JSON response not received.")

        # If a field is missing from the response, appropriate error message is returned.
        # If the field is blank, None is returned.

        try:
            self.credits = response['data']["credits"]
            if self.credits is "":
                self.credits = None
        except Exception:
            self.credits = "'credits' not found"


        try:
            self.data = response["data"]
            if self.data is "":
                self.data = None
        except Exception:
            self.data = "'data' not found"


        try:
            self.end_date = response["enddate"]
            if self.end_date is "":
                self.end_date = None
        except Exception:
            self.end_date = "'enddate' not found"


        try:
            self.message = response["message"]
            if self.message is "":
                self.message = None
        except Exception:
            self.message = "'message' not found"


        try:
            self.dlr_time = response['data'][0]["dlrtime"]
            if self.dlr_time is "":
                self.dlr_time = None
        except Exception:
            self.dlr_time = "'dlrtime' not found"


        try:
            self.sent_time = response['data'][0]["senttime"]
            if self.sent_time is "":
                self.sent_time = None
        except Exception:
            self.sent_time = "'senttime' not found"


        try:
            self.start_date = response["startdate"]
            if self.start_date is "":
                self.start_date = None
        except Exception:
            self.start_date = "'startdate' not found"


        try:
            self.status = response["status"]
            if self.status is "":
                self.status = None
        except Exception:
            self.status = "'status' not found"


        try:
            self.status_code = response["code"]
            if self.status_code is "":
                self.status_code = None
        except Exception:
            self.status_code = "'code' not found"


        try:
            self.total_credits = response["total_credit"]
            if self.total_credits is "":
                self.total_credits = None
        except Exception:
            self.total_credits = "'total_credit' not found"



        try:
            self.total_sms = response["total_sms"]
            if self.total_sms is "":
                self.total_sms = None
        except Exception:
            self.total_sms = "'total_sms' not found"


        # If position parameter is not None, it implies that the response is received from GroupResponse class
        # (the GroupResponse class is receiving the response from the server) and the attributes of SMSMessageResponse
        # are being populated as a part of GroupResponse.

        if position is not None:
            try:
                self.id = response['id']
                if self.id is "":
                    self.id = None
            except Exception:
                self.id = "'id' not found"

            try:
                self.customid = response['customid']
                if self.customid is "":
                    self.customid = None
            except:
                try:
                    self.customid = response['custom']
                    if self.customid is "":
                        self.customid = None
                except:
                    self.customid = "'customid' not found"

            try:
                self.customid1 = response['customid1']
                if self.customid1 is "":
                    self.customid1 = None
            except:
                try:
                    self.customid1 = response['custom1']
                    if self.customid1 is "":
                        self.customid1 = None
                except:
                    self.customid1 = "'customid1' not found"

            try:
                self.customid2 = response['customid2']
                if self.customid2 is "":
                    self.customid2 = None
            except:
                try:
                    self.customid2 = response['custom2']
                    if self.customid2 is "":
                        self.customid2 = None
                except:
                    self.customid = "'customid' not found"

            try:
                self.mobile = response['mobile']
                if self.mobile is "":
                    self.mobile = None
            except Exception:
                self.mobile = "'mobile' not found"

            try:
                self.dlr_status = response['status']
                if self.dlr_status is "":
                    self.dlr_status = None
            except Exception:
                self.dlr_status = "'status' not found"

        # If position is None, the response is received directly from the server and the attributes of
        # SMSMessageResponse are populated for the SMSMessageResponse class itself.

        else:
            try:
                self.id = response['data'][0]['id']
                if self.id is "":
                    self.id = None
            except Exception:
                self.id = "'id' not found"

            try:
                self.customid = response['data'][0]['customid']
                if self.customid is "":
                    self.customid = None
            except:
                try:
                    self.customid = response['data'][0]['custom']
                    if self.customid is "":
                        self.customid = None
                except:
                    self.customid = "'customid' not found"

            try:
                self.customid1 = response['data'][0]['customid1']
                if self.customid1 is "":
                    self.customid1 = None
            except:
                try:
                    self.customid1 = response['data'][0]['custom1']
                    if self.customid1 is "":
                        self.customid1 = None
                except:
                    self.customid1 = "'customid1' not found"

            try:
                self.customid2 = response['data'][0]['customid2']
                if self.customid2 is "":
                    self.customid2 = None
            except:
                try:
                    self.customid2 = response['data'][0]['custom2']
                    if self.customid2 is "":
                        self.customid2 = None
                except:
                    self.customid = "'customid' not found"

            try:
                self.mobile = response['data'][0]['mobile']
                if self.mobile is "":
                    self.mobile = None
            except Exception:
                self.mobile = "'mobile' not found"

            try:
                self.dlr_status = response['data'][0]['status']
                if self.dlr_status is "":
                    self.dlr_status = None
            except Exception:
                self.dlr_status = "'status' not found"


    # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
    # as per the user's requirements.


    def get_data(self):

        """

        :return:data
        """

        return self.data

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

    def get_status_code(self):

        """

        :return:status_code
        """

        return self.status_code

    def get_credits(self):

        """

        :return:credits
        """

        return self.credits

    def get_customid(self):

        """

        :return:customid
        """

        return self.customid

    def get_customid1(self):

        """

        :return:customid1
        """

        return self.customid1

    def get_customid2(self):

        """

        :return:customid2
        """

        return self.customid2

    def get_dlr_status(self):

        """

        :return:delivery_status
        """

        return self.dlr_status

    def get_delivery_time(self):

        """

        :return:delivery_time
        """

        return self.dlr_time

    def get_end_date(self):

        """

        :return:end_date
        """

        return self.end_date

    def get_id(self):

        """

        :return:id
        """

        return self.id

    def get_mobile(self):

        """

        :return:mobile
        """

        return self.mobile

    def get_sent_time(self):

        """

        :return:sent_time
        """

        return self.sent_time

    def get_start_date(self):

        """

        :return:start_date
        """

        return self.start_date

    def get_total_credits(self):

        """

        :return:total_credits
        """

        return self.total_credits

    def get_total_sms(self):

        """

        :return:total_sms
        """

        return self.total_sms
