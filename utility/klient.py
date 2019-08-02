#!/usr/bin/env python

import requests

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


class Klient:
    """

    """

    def __init__(self, url):

        """
        Initialises the attributes of Klient class.
        """

        self.url = url

    def response(self):

        """
        Makes a HTTP GET request to the server.

        :return:response in JSON format
        """

        try:
            response = requests.get(self.url)
            response_json = response.json()
            return response_json
        except Exception as e:
            print(e)
