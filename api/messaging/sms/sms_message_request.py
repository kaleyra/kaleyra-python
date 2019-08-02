#!/usr/bin/env python

from configuration.config import BASEURL, SENDERID
from api.messaging.k_request import KRequest
from utility.validation import Validate
from api.messaging.sms.sms_message_response import SMSMessageResponse
from utility.klient import Klient

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


class SMSMessageRequest(KRequest):

    # constants for method parameter in url
    CREDITS = 'account.credits'
    SCHEDULE = 'sms.schedule'
    SMS = 'sms'
    STATUS = 'sms.status'
    USAGE = 'sms.usagecredit'

    # constants for task method in URL
    DELETE = 'delete'
    MODIFY = 'modify'


    def __init__(self, message=None, to=None, custom=None, datetime=None, dlr_url=None, flash=None, format=None,
                 from_date=None, group_id=None, id=None, port=None, to_date=None, unicode=None):

        """"
        Initialises the attributes of SMSMessageRequest and the derived attributes of parent class KRequest.
        All attributes are parameters in the URL.

        Note: The value of all attributes are initially considered as None.
        """

        KRequest.__init__(self, message, to)

        self.custom = custom
        self.datetime = datetime
        self.dlr_url = dlr_url
        self.flash = flash
        self.format = format
        self.from_date = from_date
        self.group_id = group_id
        self.id = id
        self.port = port
        self.to_date = to_date
        self.unicode = unicode


    def credit_status(self):

        """
        Method to check the available credits in the user's account.

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirement.
        """

        url = '{}&method={}'.format(BASEURL, SMSMessageRequest.CREDITS)
        response = Klient(url).response()
        sms_message_response = SMSMessageResponse(response=response)
        return sms_message_response


    def credit_usage(self):
        """
        Method to check credit usage of the user(API key) between two valid dates entered by the user.

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirement.
        """

        if Validate.date_validation(self.from_date, self.format) and \
                Validate.date_validation(self.to_date, self.format):
            from_date = Validate.date_validation(self.from_date, self.format)
            to_date = Validate.date_validation(self.to_date, self.format)
            url = '{}&method={}&from={}&to={}'.format(BASEURL, SMSMessageRequest.USAGE, from_date, to_date)
            response = Klient(url).response()
            sms_message_response = SMSMessageResponse(response=response)
            return sms_message_response


    def delete(self):

        """
        Method to delete a scheduled SMS campaign after a valid message-id is received from the user.

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirements.
        """

        url = '{}&groupid={}&task={}&method={}'.format(BASEURL, self.group_id, SMSMessageRequest.DELETE,
                                                       SMSMessageRequest.SCHEDULE)
        response = Klient(url).response()
        sms_message_response = SMSMessageResponse(response=response)
        return sms_message_response


    def edit(self):

        """
        Method to edit a scheduled SMS campaign after the mandatory parameters are validated and ID of the SMS campaign
        is entered correctly.

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirements.
        """

        if Validate.date_and_time_validation(self.datetime, self.format):
            correct_time = Validate.date_and_time_validation(self.datetime, self.format)
            url = '{}&groupid={}&time={}&task={}&method={}'.format(BASEURL, self.group_id, correct_time,
                                                                   SMSMessageRequest.MODIFY, SMSMessageRequest.SCHEDULE)
            response = Klient(url).response()
            sms_message_response = SMSMessageResponse(response=response)
            return sms_message_response


    def schedule(self):

        """
        Method to schedule a SMS campaign to a specified date and time after the required mandatory parameters received
        from the user are validated.
        dlr_url, custom, unicode and flash are optional parameters.

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirements.
        """

        if Validate.message(self.message) and Validate.number(self.to) and \
                Validate.date_and_time_validation(self.datetime, self.format):
            correct_time = Validate.date_and_time_validation(self.datetime, self.format)
            url = '{}&method={}&message={}&to={}&sender={}&time={}'.format(BASEURL, SMSMessageRequest.SMS, self.message,
                                                                           self.to, SENDERID, correct_time)
            if self.dlr_url:
                url += '&dlrurl={}'.format(self.dlr_url)
            if self.custom:
                url += '&custom={}'.format(self.custom)
            if self.unicode:
                url += '&unicode={}'.format(self.unicode)
            if self.flash:
                url += '&flash={}'.format(self.flash)
            response = Klient(url).response()
            sms_message_response = SMSMessageResponse(response=response)
            return sms_message_response


    def send(self):

        """
        Method to send a SMS campaign after the required mandatory parameters received from the user are validated.
        dlr_url, custom, unicode and flash are optional parameters.

        :return:object of smsMessageResponse which would be used to return a specific response as per the user's
        requirements.
        """

        if Validate.message(self.message) and Validate.number(self.to):
            url = '{}&method={}&message={}&to={}&sender={}'.format(BASEURL, SMSMessageRequest.SMS, self.message,
                                                                   self.to, SENDERID)
            if self.dlr_url:
                url += '&dlrurl={}'.format(self.dlr_url)
            if self.custom:
                url += '&custom={}'.format(self.custom)
            if self.unicode:
                url += '&unicode={}'.format(self.unicode)
            if self.flash:
                url += '&flash={}'.format(self.flash)
            response = Klient(url).response()
            sms_message_response = SMSMessageResponse(response=response)
            return sms_message_response


    def set_schedule(self, datetime, format):

        # TODO: Specify datetime format in main Kaleyra documentation.

        """
        Method to set the date and time when a SMS campaign is scheduled/edited.

        :return:None
        """

        self.datetime = datetime
        self.format = format


    def sms_status(self):

        """
        Method to check the status of any sent SMS campaign using it's message ID(not group ID).

        :return:object of SMSMessageResponse which would be used to return a specific response as per the user's
        requirement.
        """

        url = '{}&method={}&id={}'.format(BASEURL, SMSMessageRequest.STATUS, self.id)
        response = Klient(url).response()
        sms_message_response = SMSMessageResponse(response=response)
        return sms_message_response
