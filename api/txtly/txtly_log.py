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
class TxtlyLog:
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
            txtly_response = TxtlyLog.Txtlys(response=self.txtlys[i])
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

    def get_status(self):
        
        """
        
        :return:status 
        """

        return self.status

    def get_txtlys(self):
        
        """
        
        :return:txtlys 
        """

        return self.txtlys

    def get_txtlys_responses(self):
        
        """
        
        :return:txtly_responses 
        """

        return self.txtly_responses

    def get_pagination(self):
        
        """
        
        :return:pagination 
        """

        if self.pagination == "":
            return None
        else:
            return self.pagination

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
        Txtlys is a nested class within TxtlyLog
        """

        def __init__(self, response):

            """
            Constructor parses the response received from the outer TxtlyLog class and populates the attributes of
            the class. The attributes are then returned when a function call is made by the user.

            'response' parameter receives the entire 'txtlys' response from a function in TxtlyLog class.

            Note: The value of all attributes are initially considered as None.
            """

            self.json_response = None
            self.log_id = None
            self.fkuserid = None
            self.fk_link_id = None
            self.client_ip = None
            self.scheme = None
            self.host = None
            self.query_string = None
            self.user_agent = None
            self.browser = None
            self.browser_version = None
            self.browser_engine = None
            self.browser_lang = None
            self.resolution = None
            self.platform = None
            self.platform_version = None
            self.device_type = None
            self.device_version = None
            self.device_model = None
            self.touch_enabled = None
            self.latitude = None
            self.longitude = None
            self.country = None
            self.city = None
            self.status = None
            self.created = None
            self.mobile = None
            self.serial = None

            # If JSON response is not received, an error message is displayed.

            try:
                self.json_response = json.dumps(response)
            except Exception:
                self.json_response = "JSON response not received."


            # If a field is missing from the response, appropriate error message is returned.
            # If the field is blank, None is returned.

            try:
                self.log_id = response['log_id']
                if self.log_id is "":
                    self.log_id = None
            except Exception:
                self.log_id = "'log_id' not found"


            try:
                self.fkuserid = response['fkuserid']
                if self.fkuserid is "":
                    self.fkuserid = None
            except Exception:
                self.fkuserid = "'fkuserid' not found"


            try:
                self.fk_link_id = response['fk_link_id']
                if self.fk_link_id is "":
                    self.fk_link_id = None
            except Exception:
                self.fk_link_id = "'fk_link_id' not found"


            try:
                self.client_ip = response['client_ip']
                if self.client_ip is "":
                    self.client_ip = None
            except Exception:
                self.client_ip = "'client_ip' not found"


            try:
                self.scheme = response['scheme']
                if self.scheme is "":
                    self.scheme = None
            except Exception:
                self.scheme = "'scheme' not found"


            try:
                self.host = response['host']
                if self.host is "":
                    self.host = None
            except Exception:
                self.host = "'host' not found"


            try:
                self.query_string = response['query_string']
                if self.query_string is "":
                    self.query_string = None
            except Exception:
                self.query_string = "'query_string' not found"


            try:
                self.user_agent = response['user_agent']
                if self.user_agent is "":
                    self.user_agent = None
            except Exception:
                self.user_agent = "'user_agent' not found"


            try:
                self.browser = response['browser']
                if self.browser is "":
                    self.browser = None
            except Exception:
                self.browser = "'browser' not found"


            try:
                self.browser_version = response['browser_version']
                if self.browser_version is "":
                    self.browser_version = None
            except Exception:
                self.browser_version = "'browser_version' not found"


            try:
                self.browser_lang = response['browser_lang']
                if self.browser_lang is "":
                    self.browser_lang = None
            except Exception:
                self.browser_lang = "'browser_lang' not found"


            try:
                self.browser_engine = response['browser_engine']
                if self.browser_engine is "":
                    self.browser_engine = None
            except Exception:
                self.browser_engine = "'browser_engine' not found"


            try:
                self.resolution = response['resolution']
                if self.resolution is "":
                    self.resolution = None
            except Exception:
                self.resolution = "'resolution' not found"


            try:
                self.platform = response['platform']
                if self.platform is "":
                    self.platform = None
            except Exception:
                self.platform = "'platform' not found"


            try:
                self.platform_version = response['platform_version']
                if self.platform_version is "":
                    self.platform_version = None
            except Exception:
                self.platform_version = "'platform_version' not found"


            try:
                self.device_type = response['device_type']
                if self.device_type is "":
                    self.device_type = None
            except Exception:
                self.device_type = "'device_type' not found"


            try:
                self.device_brand = response['device_brand']
                if self.device_brand is "":
                    self.device_brand = None
            except Exception:
                self.device_brand = "'device_brand' not found"


            try:
                self.device_version = response['device_version']
                if self.device_version is "":
                    self.device_version = None
            except Exception:
                self.device_version = "'device_version' not found"


            try:
                self.device_model = response['device_model']
                if self.device_model is "":
                    self.device_model = None
            except Exception:
                self.device_model = "'device_model' not found"


            try:
                self.touch_enabled = response['touch_enabled']
                if self.touch_enabled is "":
                    self.touch_enabled = None
            except Exception:
                self.touch_enabled = "'touch_enabled' not found"


            try:
                self.latitude = response['latitude']
                if self.latitude is "":
                    self.latitude = None
            except Exception:
                self.latitude = "'latitude' not found"


            try:
                self.longitude = response['longitude']
                if self.longitude is "":
                    self.longitude = None
            except Exception:
                self.longitude = "'longitude' not found"


            try:
                self.country = response['country']
                if self.country is "":
                    self.country = None
            except Exception:
                self.country = "'country' not found"


            try:
                self.region = response['region']
                if self.region is "":
                    self.region = None
            except Exception:
                self.region = "'region' not found"


            try:
                self.city = response['city']
                if self.city is "":
                    self.city = None
            except Exception:
                self.city = "'city' not found"


            try:
                self.status = response['status']
                if self.status is "":
                    self.status = None
            except Exception:
                self.status = "'status' not found"


            try:
                self.created = response['created']
                if self.created is "":
                    self.created = None
            except Exception:
                self.created = "'created' not found"


            try:
                self.mobile = response['mobile']
                if self.mobile is "":
                    self.mobile = None
            except Exception:
                self.mobile = "'mobile' not found"


            try:
                self.serial = response['serial']
                if self.serial is "":
                    self.serial = None
            except Exception:
                self.serial = "'serial' not found"


        # When the user calls the methods defined below, the above attributes are simply returned in the functions below,
        # as per the user's requirements.


        def to_json(self):
            
            """
            
            :return:json_response 
            """

            return self.json_response

        def get_log_id(self):
            
            """
            
            :return:log_id 
            """

            return self.log_id

        def get_fkuserid(self):
            
            """
            
            :return:fkuserid 
            """

            return self.fkuserid

        def get_fk_link_id(self):
            
            """
            
            :return:fk_link_id 
            """

            return self.fk_link_id

        def get_client_ip(self):
            
            """
            
            :return:client_ip 
            """

            return self.client_ip

        def get_scheme(self):
            
            """
            
            :return:scheme 
            """

            return self.scheme

        def get_host(self):
            
            """
            
            :return:host 
            """

            return self.host

        def get_query_string(self):
            
            """
            
            :return:query_string 
            """

            return self.query_string

        def get_user_agent(self):
            
            """
            
            :return:user_agent 
            """

            return self.user_agent

        def get_browser(self):
            
            """
            
            :return:browser 
            """

            return self.browser

        def get_browser_version(self):
            
            """
            
            :return:browser_version 
            """

            if self.browser_version is "":
                return None
            else:
                return self.browser_version

        def get_browser_lang(self):
            
            """
            
            :return:browser_lang 
            """

            if self.browser_lang is "":
                return None
            else:
                return self.browser_lang

        def get_browser_engine(self):
            
            """
            
            :return:browser_engine 
            """

            return self.browser_engine

        def get_resolution(self):
            
            """
            
            :return:resolution 
            """

            return self.resolution

        def get_platform(self):
            
            """
            
            :return:platform 
            """

            return self.platform

        def get_platform_version(self):
            
            """
            
            :return:platform_version 
            """

            return self.platform_version

        def get_device_type(self):
            
            """
            
            :return:device_type 
            """

            return self.device_type

        def get_device_brand(self):
            
            """
            
            :return:device_brand
            """
            
            return self.device_brand

        def get_device_version(self):
            
            """
            
            :return:device_version 
            """

            return self.device_version

        def get_device_model(self):
            
            """
            
            :return:device_model 
            """

            return self.device_model

        def get_touch_enabled(self):
            
            """
            
            :return:touch_enabled 
            """

            return self.touch_enabled

        def get_latitude(self):
            
            """
            
            :return:latitude 
            """

            return self.latitude

        def get_longitude(self):
            
            """
            
            :return:longitude 
            """

            return self.longitude

        def get_country(self):
            
            """
            
            :return:country 
            """

            return self.country

        def get_region(self):
            
            """
            
            :return:region 
            """

            return self.region

        def get_city(self):
            
            """
            
            :return:city 
            """

            return self.city

        def get_status(self):
            
            """
            
            :return:status 
            """

            return self.status

        def get_created(self):
            
            """
            
            :return:created 
            """

            return self.created

        def get_mobile(self):
            
            """
            
            :return:mobile 
            """

            return self.mobile

        def get_serial(self):
            
            """
            
            :return:serial 
            """

            return self.serial


    # noinspection PyBroadException


    class Pagination:

        """
        Pagination is a nested class within TxtlyLog
        """

        def __init__(self, response):

            """
            Constructor parses the response received from the outer TxtlyLog class and populates the attributes of the
            class. The attributes are then returned when a function call is made by the user.

            'response' parameter receives the entire 'pagination' response from a function in TxtlyLog class.

            Note: The value of all attributes are initially considered as None.
            """

            self.extra = None
            self.limit = None
            self.limitstart = None
            self.next = None
            self.now = None
            self.page = None
            self.total = None

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
