#!/usr/bin/env python

import unittest
from utility.validation import Validate
from ddt import ddt, data, unpack

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"


@ddt
class TestValidation(unittest.TestCase, Validate):

    @data(("01-09-2019 16:00", "dd-mm-yyyy hh:mm"),
          ("09-01-2019 16:00", "mm-dd-yyyy hh:mm"),
          ("09-01-19 16:00", "mm-dd-yy hh:mm"),
          ("01-09-19 16:00", "dd-mm-yy hh:mm"),
          ("01-Sep-19 16:00", "dd-mon-yy hh:mm"),
          ("01-Sep-2019 16:00", "dd-mon-yyyy hh:mm"),
          ("2019-Sep-01 16:00", "yyyy-mon-dd hh:mm"),
          ("2019-01-Sep 16:00", "yyyy-dd-mon hh:mm"),
          ("2019-09-01 16:00", "yyyy-mm-dd hh:mm"),
          ("2019-01-09 16:00", "yyyy-dd-mm hh:mm"),
          ("Sep-01-2019 16:00", "mon-dd-yyyy hh:mm"),
          ("Sep-01-19 16:00", "mon-dd-yy hh:mm"),
          ("01-09-2019 04:00 PM", "dd-mm-yyyy hh:mm am/pm"),
          ("09-01-2019 04:00 PM", "mm-dd-yyyy hh:mm am/pm"),
          ("09-01-19 04:00 PM", "mm-dd-yy hh:mm am/pm"),
          ("01-09-19 04:00 PM", "dd-mm-yy hh:mm am/pm"),
          ("01-Sep-19 04:00 PM", "dd-mon-yy hh:mm am/pm"),
          ("01-Sep-2019 04:00 PM", "dd-mon-yyyy hh:mm am/pm"),
          ("2019-Sep-01 04:00 PM", "yyyy-mon-dd hh:mm am/pm"),
          ("2019-01-Sep 04:00 PM", "yyyy-dd-mon hh:mm am/pm"),
          ("2019-09-01 04:00 PM", "yyyy-mm-dd hh:mm am/pm"),
          ("2019-01-09 04:00 PM", "yyyy-dd-mm hh:mm am/pm"),
          ("Sep-01-2019 04:00 PM", "mon-dd-yyyy hh:mm am/pm"),
          ("Sep-01-19 04:00 PM", "mon-dd-yy hh:mm am/pm"),
          ("01-09-2019 04:00PM", "dd-mm-yyyy hh:mmam/pm"),
          ("09-01-2019 04:00PM", "mm-dd-yyyy hh:mmam/pm"),
          ("09-01-19 04:00PM", "mm-dd-yy hh:mmam/pm"),
          ("01-09-19 04:00PM", "dd-mm-yy hh:mmam/pm"),
          ("2019-09-01 04:00PM", "yyyy-mm-dd hh:mmam/pm"),
          ("2019-01-09 04:00PM", "yyyy-dd-mm hh:mmam/pm"))
    @unpack
    def test_date_and_time_validation(self, v1, v2):
        date_time, format = v1, v2
        expected_format = self.date_and_time_validation(date_time=date_time, format=format)
        self.assertEqual(expected_format, '2019-09-01 04:00 PM')


if __name__ == '__main':
    unittest.main()
