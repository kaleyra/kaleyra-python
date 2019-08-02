#!/usr/bin/env python

from configuration.config import APIKEY

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(APIKEY)}


class KResponse:

    """
    Abstract class.

    Note: KResponse is inherited by SMSMessageResponse and GroupResponse.
    """

    def __init__(self, data, response, message, status, status_code):

        """
        Constructor to initialize the attributes of KResponse. All attributes are parameters in the URL.
        """

        self.data = data
        self.json_response = response
        self.message = message
        self.status = status
        self.status_code = status_code

    def to_json(self):

        """
        Overridden abstract method.
        """

        pass

    def get_message(self):

        """
        Overridden abstract method.
        """

        pass


    def get_status(self):

        """
        Overridden abstract method.
        """

        pass

    def get_data(self):

        """
        Overridden abstract method.
        """

        pass

    def get_status_code(self):

        """
        Overridden abstract method.
        """

        pass
