#!/usr/bin/env python

from configuration.config import BASEURL
from api.txtly.txtly_response import TxtlyResponse
from api.txtly.txtly_report import TxtlyReport
from api.txtly.txtly_log import TxtlyLog
from utility.klient import Klient

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


class TxtlyRequest:

    """
    TxtlyRequest
    """

    # constants for method parameter in url
    CREATE = 'txtly.create'
    LOG = 'txtly.logs'
    TXTLY = 'txtly'

    # constant for task parameter in url
    DELETE = 'delete'

    def __init__(self, advanced=None, id=None, name=None, page=None, title=None, token=None, track=None, url=None):

        """"
        Initialises the attributes of TxtlyRequest. All attributes are parameters in the URL.

        Note: The value of all attributes are initially considered as None.
        """

        self.advanced = advanced
        self.id = id
        self.name = name
        self.page = page
        self.title = title
        self.token = token
        self.track = track
        self.url = url

    def create(self):

        """
        Method to create a txtly URL to be sent as a message.

        Txtly is basically a shortened URL which can be used within text messages so that SMS would not exceed
        the specified characters.

        :return: txtlyResponse object which is used to return a specific response as per user's requirements
        """

        url = '{}&method={}&url={}&token={}&title={}'.format(BASEURL, TxtlyRequest.CREATE, self.url, self.token,
                                                             self.title)
        if self.advanced:
            url += '&advanced={}'.format(self.advanced)
        if self.track:
            url += '&track={}'.format(self.track)
        response = Klient(url).response()
        txtly_response = TxtlyResponse(response)
        return txtly_response

    def delete(self):

        """
        Method to delete an existing Txtly web link.

        :return: txtlyResponse object which is used to return a specific response as per user's requirements
        """

        TASK = 'delete'
        url = '{}&method={}&task={}&id={}&app=1'.format(BASEURL, TxtlyRequest.TXTLY, TASK, self.id)
        response = Klient(url).response()
        txtly_response = TxtlyResponse(response)
        return txtly_response

    def log(self):

        """
        Method to extract the logs of all the Txtly link that have been shortened in the user's account.
        page is an optional parameter.

        :return: txtlyResponse object which is used to return a specific response as per user's requirements
        """

        url = '{}&method={}&id={}&app=1'.format(BASEURL, TxtlyRequest.LOG, self.id)
        response = Klient(url).response()
        txtly_log_response = TxtlyLog(response)
        return txtly_log_response

    def report(self):

        """
        Method to extract the reports of all the Txtly links that have been shortened in the user's account
        page is an optional parameter.

        :return: txtlyResponse object which is used to return a specific response as per user's requirements
        """

        url = '{}&method={}&app=1'.format(BASEURL, TxtlyRequest.TXTLY)
        if self.page:
            url += '&page={}'.format(self.page)
        response = Klient(url).response()
        txtly_report_response = TxtlyReport(response)
        return txtly_report_response
