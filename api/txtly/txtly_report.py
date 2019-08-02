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
class TxtlyReport:
    """

    """

    def __init__(self, response):

        """
        Constructor parses the response received from the server and populates the attributes of the class. The
        attributes are then returned when a function call is made by the user.

        'response' parameter receives the HTTP response from the server.

        Note: The value of all attributes are initially considered as None.
        """

        self.data = None
        self.json_response = None
        self.message = None
        self.pagination = None
        self.pagination_obj = None
        self.status = None
        self.txtly_responses = None
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
            self.message = response["message"]
            if self.message is "":
                self.message = None
        except Exception:
            self.message = "'message' not found"


        try:
            self.pagination = response['data']['pagination']
            if self.pagination is "":
                self.pagination = None
        except Exception:
            self.pagination = "'pagination' not found"


        try:
            self.status = response["status"]
            if self.status is "":
                self.status = None
        except Exception:
            self.status = "'status' not found"


        try:
            self.txtlys = response['data']['txtlys']
            if self.txtlys is "":
                self.txtlys = None
        except Exception:
            self.txtlys = "'txtlys' not found"


        try:
            self.pagination_obj = self.Pagination(self.pagination)
        except Exception:
            self.pagination_obj = 'Pagination not found.'


        self.txtly_responses = []
        for i in range(len(self.txtlys)):
            txtly_response = TxtlyReport.Txtlys(response=self.txtlys[i])
            self.txtly_responses.append(txtly_response)

    # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
    # as per the user's requirements.

    def get_data(self):

        """

        :return:data
        """
        return self.data

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

    def get_pagination(self):

        """

        :return:pagination
        """
        return self.pagination

    def get_status(self):

        """

        :return:status
        """
        return self.status

    def get_txtlys_responses(self):

        """

        :return:txtly_responses
        """
        return self.txtly_responses

    def get_txtlys(self):

        """

        :return:txtlys
        """
        return self.txtlys

    def get_pagination_responses(self):

        """

        :return:pagination_obj
        """
        if self.pagination_obj == "":
            return None
        else:
            return self.pagination_obj

    # noinspection PyBroadException
    class Txtlys:

        """
        Txtlys is a nested class within TxtlyReport
        """

        def __init__(self, response):

            """
            Constructor parses the response received from the outer TxtlyReport class and populates the attributes of
            the class. The attributes are then returned when a function call is made by the user.

            'response' parameter receives the entire 'txtlys' response from a function in TxtlyReport class.

            Note: The value of all attributes are initially considered as None.
            """

            self.advanced = None
            self.callback = None
            self.created = None
            self.json_response = None
            self.last_viewed = None
            self.link_id = None
            self.link_type = None
            self.long_url = None
            self.meta_value = None
            self.serial = None
            self.short_url = None
            self.status = None
            self.title = None
            self.token = None
            self.views = None
            self.uw = None


            # If JSON response is not received, an error message is displayed.

            try:
                self.json_response = json.dumps(response)
            except Exception:
                self.json_response = "JSON response not received."


            # If a field is missing from the response, appropriate error message is returned.
            # If the field is blank, None is returned.

            try:
                self.advanced = response['advanced']
                if self.advanced is "":
                    self.advanced = None
            except Exception:
                self.advanced = "'advanced' not found"

            try:
                self.callback = response['callback']
                if self.callback is "":
                    self.callback = None
            except Exception:
                self.callback = "'callback' not found"


            try:
                self.created = response['created']
                if self.created is "":
                    self.created = None
            except Exception:
                self.created = "'created' not found"


            try:
                self.last_viewed = response['last_viewed']
                if self.last_viewed is "":
                    self.last_viewed = None
            except Exception:
                self.last_viewed = "'last_viewed' not found"


            try:
                self.link_id = response['link_id']
                if self.link_id is "":
                    self.link_id = None
            except Exception:
                self.link_id = "'link_id' not found"


            try:
                self.link_type = response['link_type']
                if self.link_type is "":
                    self.link_type = None
            except Exception:
                self.link_type = "'link_type' not found"


            try:
                self.long_url = response['long_url']
                if self.long_url is "":
                    self.long_url = None
            except Exception:
                self.long_url = "'long_url' not found"


            try:
                self.meta_value = response['meta_value']
                if self.meta_value is "":
                    self.meta_value = None
            except Exception:
                self.meta_value = "'meta_value' not found"


            try:
                self.serial = response['serial']
                if self.serial is "":
                    self.serial = None
            except Exception:
                self.serial = "'serial' not found"


            try:
                self.short_url = response['short_url']
                if self.short_url is "":
                    self.short_url = None
            except Exception:
                self.short_url = "'short_url' not found"


            try:
                self.status = response['status']
                if self.status is "":
                    self.status = None
            except Exception:
                self.status = "'status' not found"


            try:
                self.title = response['title']
                if self.title is "":
                    self.title = None
            except Exception:
                self.title = "'title' not found"


            try:
                self.token = response['token']
                if self.token is "":
                    self.token = None
            except Exception:
                self.token = "'token' not found"


            try:
                self.uw = response['uw']
                if self.uw is "":
                    self.uw = None
            except Exception:
                self.uw = "'uw' not found"


            try:
                self.views = response['views']
                if self.views is "":
                    self.views = None
            except Exception:
                self.views = "'views' not found"


        def get_advanced(self):

            """

            :return:advanced
            """
            return self.advanced

        def get_callback(self):

            """

            :return:callback
            """
            return self.callback

        def get_created(self):

            """

            :return:created
            """
            return self.created

        def to_json(self):

            """

            :return:json_response
            """
            return self.json_response

        def get_last_viewed(self):

            """

            :return:last_viewed
            """
            return self.last_viewed

        def get_link_id(self):

            """

            :return:link_id
            """
            return self.link_id

        def get_link_type(self):

            """

            :return:link_type
            """
            return self.link_type

        def get_long_url(self):

            """

            :return:long_url
            """
            return self.long_url

        def get_meta_value(self):

            """

            :return:meta_value
            """
            return self.meta_value

        def get_serial(self):

            """

            :return:serial
            """
            return self.serial

        def get_short_url(self):

            """

            :return:short_url
            """
            return self.short_url

        def get_status(self):


            """

            :return:status
            """
            return self.status

        def get_title(self):

            """

            :return:title
            """
            return self.title

        def get_token(self):

            """

            :return:token
            """
            return self.token

        def get_uw(self):

            """

            :return:uw
            """
            return self.uw

        def get_views(self):

            """

            :return:views
            """
            return self.views

    # noinspection PyBroadException
    class Pagination:

        """
        Pagination is a nested class within TxtlyReport
        """

        def __init__(self, response):

            """
            Constructor parses the response received from the outer TxtlyReport class and populates the attributes of the
            class. The attributes are then returned when a function call is made by the user.

            'response' parameter receives the entire 'pagination' response from a function in TxtlyReport class.

            Note: The value of all attributes are initially considered as None.
            """

            self.extra = None
            self.json_response = None
            self.limit = None
            self.limitstart = None
            self.next = None
            self.now = None
            self.page = None
            self.total = None


            # If JSON response is not received, an error message is displayed.

            try:
                self.json_response = json.dumps(response)
            except Exception:
                self.json_response = "JSON response not received."


            # If a field is missing from the response, appropriate error message is returned.
            # If the field is blank, None is returned.

            try:
                self.extra = response['extra']
                if self.extra is "":
                    self.extra = None
            except Exception:
                self.extra = "'extra' not found"


            try:
                self.limit = response['limit']
                if self.limit is "":
                    self.limit = None
            except Exception:
                self.limit = "'limit' not found"


            try:
                self.limitstart = response['limitstart']
                if self.limitstart is "":
                    self.limitstart = None
            except Exception:
                self.limitstart = "'limitstart' not found"


            try:
                self.next = response['next']
                if self.next is "":
                    self.next = None
            except Exception:
                self.next = "'next' not found"


            try:
                self.now = response['now']
                if self.now is "":
                    self.now = None
            except Exception:
                self.now = "'now' not found"


            try:
                self.page = response['page']
                if self.page is "":
                    self.page = None
            except Exception:
                self.page = "'page' not found"


            try:
                self.total = response['total']
                if self.total is "":
                    self.total = None
            except Exception:
                self.total = "'total' not found"


        # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
        # as per the user's requirements.


        def get_extra(self):

            """

            :return:extra
            """
            return self.extra

        def get_limit(self):

            """

            :return:limit
            """
            return self.limit

        def get_limitstart(self):

            """

            :return:limitstart
            """
            return self.limitstart

        def get_next(self):

            """

            :return:next
            """
            return self.next

        def get_now(self):

            """

            :return:now
            """
            return self.now

        def get_page(self):

            """

            :return:page
            """
            return self.page

        def get_total(self):

            """

            :return:total
            """
            return self.total
