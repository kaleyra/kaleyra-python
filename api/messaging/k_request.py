#!/usr/bin/env python

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


class KRequest:

    """
    Abstract class.

    Note: KRequest is inherited by SMSMessageRequest and GroupRequest.
    """

    def __init__(self, message, to):

        """
        Initialises the attributes of KRequest class. All attributes are parameters in the URL.

        :return:None
        """

        self.message = message
        self.to = to
