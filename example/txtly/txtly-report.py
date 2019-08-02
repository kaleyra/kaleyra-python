#!/usr/bin/env python

from api.txtly.txtly_request import TxtlyRequest

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

# Users can extract the reports of all the Txtly links that have been shortened in their account.
# At once, user may pull maximum 25 Txtly reports.

# No parameters are required.
# page is an optional parameter.

reportRequest = TxtlyRequest()
reportResponse = reportRequest.report()

pagination = reportResponse.get_pagination_responses()
txtlys = reportResponse.get_txtlys_responses()

print(reportResponse.to_json())
print(reportResponse.get_txtlys())
print(reportResponse.get_pagination())
print(pagination.get_now())
print(pagination.get_limit())
print(txtlys[0].get_link_id())
print((txtlys[0].get_short_url()))
print(txtlys[0].get_title())
print(txtlys[0].get_created())
print(txtlys[0].get_serial())
print(txtlys[0].get_uw())
