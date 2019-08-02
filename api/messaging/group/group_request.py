#!/usr/bin/env python

from configuration.config import BASEURL, SENDERID
from api.messaging.k_request import KRequest
from api.messaging.group.group_response import GroupResponse
from utility.klient import Klient
from utility.validation import Validate

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


class GroupRequest(KRequest):

    # constant for action parameter in url
    ADD = 'add'

    # constants for method parameter in url
    GROUPS = 'groups'
    GROUPS_ADD = 'groups.add'
    GROUPS_REGISTER = 'groups.register'
    OPTIN = 'optin'

    # constant for task parameter in url
    SAVE = 'save'

    def __init__(self, message=None, to=None, email_id=None, full_name=None, group_name=None):

        """"
        Initialises the attributes of GroupRequest and the derived attributes of parent class KRequest.
        All attributes are parameters in the URL.

        Note: The value of all attributes are initially considered as None.
        """

        KRequest.__init__(self, message, to)
        self.email_id = email_id
        self.full_name = full_name
        self.group_name = group_name


    def add(self):

        """
        Method to add contacts to an SMS group that already exists.
        full_name and email_id are optional parameters.

        :return:groupResponse object which would be used to return a specific response as per user's requirements.
        """

        if Validate.group_name(self.group_name) and Validate.number(self.to):
            url = '{}&method={}&number={}&name={}&action={}'.format(BASEURL, GroupRequest.GROUPS_REGISTER, self.to,
                                                                    self.group_name, GroupRequest.ADD)
            if self.full_name:
                url += '&fullname={}'.format(self.full_name)
            if self.email_id:
                url += '&email={}'.format(self.email_id)
            response = Klient(url).response()
            group_response = GroupResponse(response=response)
            return group_response


    def create(self):

        """
        Method to create a group of contacts having a unique name so that you can simply type the group name to send an
        SMS campaign.

        :return:groupResponse object which would be used to return a specific response as per user's requirements.
        """

        if Validate.group_name(self.group_name):

            url = '{}&method={}&task={}&app=1&data[name]={}'.format(BASEURL, GroupRequest.GROUPS_ADD,
                                                                    GroupRequest.SAVE, self.group_name)
            response = Klient(url).response()
            group_response = GroupResponse(response=response)
            return group_response



    def send(self):

        """
        Method to send an SMS to a group of contacts.

        :return:groupResponse object which would be used to return a specific response as per user's requirements.
        """

        if Validate.group_name(self.group_name) and Validate.message(self.to):

            url = '{}&method={}&name={}&sender={}&message={}'.format(BASEURL, GroupRequest.GROUPS, self.group_name,
                                                                     SENDERID, self.message)
            response = Klient(url).response()
            group_response = GroupResponse(response=response)
            return group_response

    def send_optin(self):

        """
        Method to send an SMS to an optin group of contacts.

        :return:groupResponse object which would be used to return a specific response as per user's requirements.
        """

        if Validate.group_name(self.group_name) and Validate.message(self.to):

            url = '{}&method={}&sender={}&message={}&name={}'.format(BASEURL, GroupRequest.OPTIN, SENDERID,
                                                                     self.message, self.group_name)
            response = Klient(url).response()
            group_response = GroupResponse(response=response)
            return group_response
