#!/usr/bin/env python

import datetime
import re
from dateutil.parser import parse

__author__ = "Likhit Jain and Yashita P Jain"
__copyright__ = "Copyright 2019, Kaleyra"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "support@kaleyra.com"
__status__ = "Production"

class Validate:

    """
    Validates a particular parameter entered by the user with the required correct format.
    If the parameter/parameters entered by the user is not validated,then the execution of API is restricted.
    """

    def __init__(self):
        pass


    @staticmethod
    def message(message):

        """
        Method to check whether the message parameter has some content or is null.

        :return: False and an alert message to the user if the message parameter is blank and exits the execution.
                Otherwise it returns True and continues with the execution of API.
        """

        try:
            if message is "":
                print("Enter a valid message.")
                exit(-1)
                return False
            return True
        except Exception as e:
            print(e)
            return False


    @staticmethod
    def number(to):

        """
        Method to check whether the number entered is in the correct format or not.

        :return: False and an alert message to the user if the number is not a valid number and exits the execution.
                Otherwise it returns True and continues with the execution of API.
        """

        try:
            num = int(to)
            if len(str(num)) != 12:
                print("Enter a valid number (Enter number with 2 digit ISD Code)")
                exit(-1)
                return False
            return True
        except Exception as e:
            print(e)
            return False


    @staticmethod
    def group_name(name):

        """
        Method to check whether the group_name has some content or is null.

        :return: False and an alert message to the user if the group_name is blank and exits the execution.
                Otherwise it returns True and continues with the execution of API.
        """

        try:
            if name is "":
                print("Enter a valid group name.")
                exit(-1)
                return False
            return True
        except Exception as e:
            print(e)
            return False


    @staticmethod
    def _24hr(v):

        """
        Method to parse the datetime entered by the user into date and time and convert the time which is in the 24 hour
        format to the standard format required by the API.

        :return:Date and time in the standard format.
        """

        try:
            v1 = v.string
            v2 = v1.rsplit(" ", 1)
            d = datetime.datetime.strptime(v2[1], "%H:%M")
            time = str(d.strftime("%I:%M %p"))
            return v2[0], time
        except Exception as e:
            print(e)


    @staticmethod
    def datething(date, month, year, time):

        """
        Method used to concatenate the standard date and time and compare it with the current datetime.
        Prints an alert statement to the user if the datetime difference is not sufficient.
        Otherwise the date and time is converted to the string format and concatenated to a single string variable.

        :return:False if the datetime difference between the the entered datetime and current time is not sufficient.
                Otherwise,a string format of standard datetime which is required by the API is returned.
        """

        global v5
        v3 = str(datetime.date(int(year), int(month), int(date)))
        v4 = parse(v3 + ' ' + time)
        curr_date = datetime.datetime.now()
        delta = v4 - curr_date
        delta1 = delta.total_seconds() / 60.0
        if delta1 < 5 or delta1 > 131400:
            print("Time difference should be greater than 5 minutes and less than 3 months from the current time.")
            exit(-1)
            return False
        else:
            time = str(v4.strftime("%I:%M %p"))
            date = str(v4.date())
            v5 = date+' '+time
            return v5


    @staticmethod
    def abbr_month(date_time):

        """
        Method to convert the datetime entered by the user in a format which has month entered in the abbreviated form
        to a standard format.
        Prints an alert statement to the user if the difference between the datetime entered by the user and the current
        datetime is not sufficient.
        Otherwise the date and time is converted to the string format and concatenated to a single string variable.

        :return:False if the time difference between the entered datetime and current time if not sufficient.
                Otherwise,a string format of standard datetime which is required by the API is returned.
        """

        try:
            dt = parse(date_time)
            d = str(dt.date())
            t = dt.time()
            time = t.strftime("%I:%M %p")
            val = parse(d+' '+time)
            curr_date = datetime.datetime.now()
            delta = val - curr_date
            delta1 = delta.total_seconds() / 60.0
            if delta1 < 5 or delta1 > 131400:
                print("Time difference should be greater than 5 minutes and less than 3 months from the current time.")
                exit(-1)
                return False
            else:
                time = str(val.strftime("%I:%M %p"))
                date = str(val.date())
                correct_val = date + ' ' + time
                return correct_val
        except Exception as e:
            print("Error:", e)


    @staticmethod
    def _12hrspace(v):

        """
        Method to parse the datetime entered by the user(format of time: HH:MM AM/PM) into date and time and convert
        time which is in the 12 hour format to a string.

        :return:Date and time in the standard format.
        """

        try:
            v1 = v.string
            v2 = v1.rsplit(" ", 2)
            va = v2[2].upper()
            vT = v2[1] + ' ' + va
            d = datetime.datetime.strptime(vT, "%I:%M %p")
            time = str(d.strftime("%I:%M %p"))
            return v2[0], time
        except Exception as e:
            print("Error:", e)


    @staticmethod
    def _12hrnospace(v):

        """
        Method to parse the datetime entered by the user(format of time:HH:MMAM/PM) into date and time and convert time
        which is in the 12 hour format to a string.

        :return:Date and time in the standard format.
        """

        try:
            v1 = v.string
            v2 = v1.rsplit(" ", 1)
            d = datetime.datetime.strptime(v2[1], "%I:%M%p")
            time = str(d.strftime("%I:%M %p"))
            return v2[0], time
        except Exception as e:
            print("ERROR:", e)


    @staticmethod
    def date_and_time_validation(date_time, format):

        """
        Method which receives parameters entered by the user and converts it to a standard datetime format required by
        the API by calling the respective functions that are defined above, depending on the type of datetime format
        entered by the user.
        If the format and datetime entered by the user is incorrect, then an alert message is displayed to the user.

        :return:Correct format of datetime obtained from datething() or abbr_month().
        """

        date_format = format.lower()

        # Regular expressions used to check whether the datetime and format entered by the user is valid or not.

        x = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](20)\d\d\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # dd-mm-yyyy HH:MM
        y = re.search(
            r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](20)\d\d\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # mm-dd-yyyy HH:MM
        z = re.search(
            r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # mm-dd-yy HH:MM
        a = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # dd-mm-yy HH:MM
        b = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # dd-mon-yy HH:MM
        c = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,](20)\d\d\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # dd-mon-yyyy HH:MM
        d = re.search(
            r"^((20)\d\d)[- /.,]([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # yyyy-mon-dd HH:MM
        e = re.search(
            r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # yyyy-dd-mon HH:MM
        f = re.search(
            r"^((20)\d\d)[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # yyyy-mm-dd HH:MM
        g = re.search(
            r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](0?[1-9]|1[012])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # yyyy-dd-mm HH:MM
        h = re.search(
            r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](20)\d\d)\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9]))$",
            date_time)  # mon-dd-yyyy HH:MM
        i = re.search(
            r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])))$",
            date_time)  # mon-dd-yy HH:MM
        xt = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](20)\d\d\s?((0?[1-9]|1[0-2])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # dd-mm-yyyy HH:MM AM/PM
        yt = re.search(
            r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](20)\d\d\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # mm-dd-yyyy HH:MM AM/PM
        zt = re.search(
            r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # mm-dd-yy HH:MM AM/PM
        at = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # dd-mm-yy HH:MM AM/PM
        bt = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # dd-mon-yy HH:MM AM/PM
        ct = re.search(
            r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,](20)\d\d\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # dd-mon-yyyy HH:MM AM/PM
        dt = re.search(
            r"^((20)\d\d)[- /.,]([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # yyyy-mon-dd HH:MM AM/PM
        et = re.search(
            r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # yyyy-dd-mon HH:MM AM/PM
        ft = re.search(
            r"^((20)\d\d)[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # yyyy-mm-dd HH:MM AM/PM
        gt = re.search(
            r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](0?[1-9]|1[012])\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # yyyy-dd-mm HH:MM AM/PM
        ht = re.search(
            r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](20)\d\d)\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM))$",
            date_time)  # mon-dd-yyyy HH:MM AM/PM
        it = re.search(
            r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([2-9][0-9]|(19))\s?((0?[0-9]|1[0-9]|2[0-4])[:](0?[0-9]|[1-5][0-9])\s?(AM|am|PM|pm|Am|aM|Pm|pM)))$",
            date_time)  # mon-dd-yy HH:MM AM/PM

        if True:
            if date_format == 'dd-mm-yyyy hh:mm' or date_format == 'dd.mm.yyyy hh:mm' or date_format == 'dd mm yyyy hh:mm' or date_format == 'dd/mm/yyyy hh:mm':
                if x:
                    var, date_time = Validate._24hr(x)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format

                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yyyy hh:mm' or date_format == 'mm.dd.yyyy hh:mm' or date_format == 'mm dd yyyy hh:mm' or date_format == 'mm/dd/yyyy hh:mm':
                if y:
                    var, date_time = Validate._24hr(y)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yy hh:mm' or date_format == 'mm.dd.yy hh:mm' or date_format == 'mm dd yy hh:mm' or date_format == 'mm/dd/yy hh:mm':
                if z:
                    var, date_time = Validate._24hr(z)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mm-yy hh:mm' or date_format == 'dd.mm.yy hh:mm' or date_format == 'dd mm yy hh:mm' or date_format == 'dd/mm/yy hh:mm':
                if a:
                    var, date_time = Validate._24hr(a)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mon-yy hh:mm' or date_format == 'dd.mon.yy hh:mm' or date_format == 'dd mon yy hh:mm' or date_format == 'dd/mon/yy hh:mm' or date_format == 'dd mon,yy hh:mm':
                if b:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mon-yyyy hh:mm' or date_format == 'dd.mon.yyyy hh:mm' or date_format == 'dd mon yyyy hh:mm' or date_format == 'dd/mon/yyyy hh:mm' or date_format == 'dd mon,yyyy hh:mm':
                if c:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-mon-dd hh:mm' or date_format == 'yyyy.mon.dd hh:mm' or date_format == 'yyyy mon dd hh:mm' or date_format == 'yyyy/mon/dd hh:mm' or date_format == 'yyyy,mon dd hh:mm':
                if d:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-dd-mon hh:mm' or date_format == 'yyyy.dd.mon hh:mm' or date_format == 'yyyy dd mon hh:mm' or date_format == 'yyyy/dd/mon hh:mm' or date_format == 'yyyy,dd mon hh:mm':
                if e:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-mm-dd hh:mm' or date_format == 'yyyy.mm.dd hh:mm' or date_format == 'yyyy mm dd hh:mm' or date_format == 'yyyy/mm/dd hh:mm':
                if f:
                    var, date_time = Validate._24hr(f)
                    year, month, date = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-dd-mm hh:mm' or date_format == 'yyyy.dd.mm hh:mm' or date_format == 'yyyy dd mm hh:mm' or date_format == 'yyyy/dd/mm hh:mm':
                if g:
                    var, date_time = Validate._24hr(g)
                    year, date, month = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mon-dd-yyyy hh:mm' or date_format == 'mon.dd.yyyy hh:mm' or date_format == 'mon dd yyyy hh:mm' or date_format == 'mon/dd/yyyy hh:mm' or date_format == 'mon dd,yyyy hh:mm':
                if h:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mon-dd-yy hh:mm' or date_format == 'mon.dd.yy hh:mm' or date_format == 'mon dd yy hh:mm' or date_format == 'mon/dd/yy hh:mm' or date_format == 'mon dd,yy hh:mm':
                if i:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mm-yyyy hh:mm am/pm' or date_format == 'dd.mm.yyyy hh:mm am/pm ' or date_format == 'dd mm yyyy hh:mm am/pm' or date_format == 'dd/mm/yyyy hh:mm am/pm':
                if xt:
                    var, date_time = Validate._12hrspace(xt)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mm-yyyy hh:mmam/pm' or date_format == 'dd.mm.yyyy hh:mmam/pm' or date_format == 'dd mm yyyy hh:mmam/pm' or date_format == 'dd/mm/yyyy hh:mmam/pm':
                if xt:
                    # withoutspace
                    var, date_time = Validate._12hrnospace(xt)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yyyy hh:mm am/pm' or date_format == 'mm.dd.yyyy hh:mm am/pm' or date_format == 'mm dd yyyy hh:mm am/pm' or date_format == 'mm/dd/yyyy hh:mm am/pm':
                if yt:
                    var, date_time = Validate._12hrspace(yt)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yyyy hh:mmam/pm' or date_format == 'mm.dd.yyyy hh:mmam/pm' or date_format == 'mm dd yyyy hh:mmam/pm' or date_format == 'mm/dd/yyyy hh:mmam/pm':
                if yt:
                    # withoutspace
                    var, date_time = Validate._12hrnospace(yt)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yy hh:mm am/pm' or date_format == 'mm.dd.yy hh:mm am/pm' or date_format == 'mm dd yy hh:mm am/pm' or date_format == 'mm/dd/yy hh:mm am/pm':
                if zt:
                    var, date_time = Validate._12hrspace(zt)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'mm-dd-yy hh:mmam/pm' or date_format == 'mm.dd.yy hh:mmam/pm' or date_format == 'mm dd yy hh:mmam/pm' or date_format == 'mm/dd/yy hh:mmam/pm':
                if zt:
                    # withoutspace
                    var, date_time = Validate._12hrnospace(zt)
                    month, date, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mm-yy hh:mm am/pm' or date_format == 'dd.mm.yy hh:mm am/pm' or date_format == 'dd mm yy hh:mm am/pm' or date_format == 'dd/mm/yy hh:mm am/pm':
                if at:
                    var, date_time = Validate._12hrspace(at)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'dd-mm-yy hh:mmam/pm' or date_format == 'dd.mm.yy hh:mmam/pm' or date_format == 'dd mm yy hh:mmam/pm' or date_format == 'dd/mm/yy hh:mmam/pm':
                if at:
                    # withoutspace
                    var, date_time = Validate._12hrnospace(at)
                    date, month, year = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, int(year) + 2000, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif (date_format == 'dd-mon-yy hh:mm am/pm' or date_format == 'dd.mon.yy hh:mm am/pm' or date_format == 'dd mon yy hh:mm am/pm' or date_format == 'dd/mon/yy hh:mm am/pm' or date_format == 'dd mon,yy hh:mm am/pm' or
                  date_format == 'dd-mon-yy hh:mmam/pm' or date_format == 'dd.mon.yy hh:mmam/pm' or date_format == 'dd mon yy hh:mmam/pm' or date_format == 'dd/mon/yy hh:mmam/pm' or date_format == 'dd mon,yy hh:mmam/pm'):
                if bt:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif(date_format == 'dd-mon-yyyy hh:mm am/pm' or date_format == 'dd.mon.yyyy hh:mm am/pm' or date_format == 'dd mon yyyy hh:mm am/pm' or date_format == 'dd/mon/yyyy hh:mm am/pm' or date_format == 'dd mon,yyyy hh:mm am/pm' or
                 date_format == 'dd-mon-yyyy hh:mmam/pm' or date_format == 'dd.mon.yyyy hh:mmam/pm' or date_format == 'dd mon yyyy hh:mmam/pm' or date_format == 'dd/mon/yyyy hh:mmam/pm'):
                if ct:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif(date_format == 'yyyy-mon-dd hh:mm am/pm' or date_format == 'yyyy.mon.dd hh:mm am/pm' or date_format == 'yyyy mon dd hh:mm am/pm' or date_format == 'yyyy/mon/dd hh:mm am/pm' or date_format == 'yyyy,mon dd hh:mm am/pm' or
                 date_format == 'yyyy-mon-dd hh:mmam/pm' or date_format == 'yyyy.mon.dd hh:mmam/pm' or date_format == 'yyyy mon dd hh:mmam/pm' or date_format == 'yyyy/mon/dd hh:mmam/pm' or date_format == 'yyyy,mon dd hh:mm am/pm'):
                if dt:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif(date_format == 'yyyy-dd-mon hh:mm am/pm' or date_format == 'yyyy.dd.mon hh:mm am/pm' or date_format == 'yyyy dd mon hh:mm am/pm' or date_format == 'yyyy/dd/mon hh:mm am/pm' or date_format == 'yyyy,dd mon hh:mm am/pm'
                 or date_format == 'yyyy-dd-mon hh:mmam/pm' or date_format == 'yyyy.dd.mon hh:mmam/pm' or date_format == 'yyyy dd mon hh:mmam/pm' or date_format == 'yyyy/dd/mon hh:mmam/pm' or date_format == 'yyyy,dd mon hh:mm am/pm'):
                if et:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-mm-dd hh:mm am/pm' or date_format == 'yyyy.mm.dd hh:mm am/pm' or date_format == 'yyyy mm dd hh:mm am/pm' or date_format == 'yyyy/mm/dd hh:mm am/pm':
                if ft:
                    var, date_time = Validate._12hrspace(ft)
                    year, month, date = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-mm-dd hh:mmam/pm' or date_format == 'yyyy.mm.dd hh:mmam/pm' or date_format == 'yyyy mm dd hh:mmam/pm' or date_format == 'yyyy/mm/dd hh:mmam/pm':
                if ft:
                    # withoutspace
                    var, date_time = Validate._12hrnospace(ft)
                    year, month, date = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-dd-mm hh:mm am/pm' or date_format == 'yyyy.dd.mm hh:mm am/pm' or date_format == 'yyyy dd mm hh:mm am/pm' or date_format == 'yyyy/dd/mm hh:mm am/pm':
                if gt:
                    var, date_time = Validate._12hrspace(gt)
                    year, date, month = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif date_format == 'yyyy-dd-mm hh:mmam/pm' or date_format == 'yyyy.dd.mm hh:mmam/pm' or date_format == 'yyyy dd mm hh:mmam/pm' or date_format == 'yyyy/dd/mm hh:mmam/pm':
                if gt:
                    # without space
                    var, date_time = Validate._12hrnospace(gt)
                    year, date, month = re.split(r"[\s -/.]", var)
                    curr_format = Validate.datething(date, month, year, date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif(date_format == 'mon-dd-yyyy hh:mm am/pm' or date_format == 'mon.dd.yyyy hh:mm am/pm' or date_format == 'mon dd yyyy hh:mm am/pm' or date_format == 'mon/dd/yyyy hh:mm am/pm' or date_format == 'mon dd,yyyy hh:mm am/pm'
                 or date_format == 'mon-dd-yyyy hh:mmam/pm' or date_format == 'mon.dd.yyyy hh:mmam/pm' or date_format == 'mon dd yyyy hh:mmam/pm' or date_format == 'mon/dd/yyyy hh:mmam/pm' or date_format == 'mon dd,yyyy hh:mmam/pm'):
                if ht:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            elif(date_format == 'mon-dd-yy hh:mm am/pm' or date_format == 'mon.dd.yy hh:mm am/pm' or date_format == 'mon dd yy hh:mm am/pm' or date_format == 'mon/dd/yy hh:mm am/pm' or date_format == 'mon dd,yy hh:mm am/pm'
                 or date_format == 'mon-dd-yy hh:mmam/pm' or date_format == 'mon.dd.yy hh:mmam/pm' or date_format == 'mon dd yy hh:mmam/pm' or date_format == 'mon/dd/yy hh:mmam/pm' or date_format == 'mon dd,yy hh:mmam/pm'):
                if it:
                    curr_format = Validate.abbr_month(date_time)
                    return curr_format
                else:
                    print("Format does not match with the entered date and time.")

            else:
                print("Enter a valid format")


    @staticmethod
    def date_validation(date, format):

        """
        Method which receives parameters entered by the user and converts it to a standard date format required by
        the API by calling the respective functions depending on the type of date format entered by the user.
        If the format and date entered is incorrect, then an alert message is displayed to the user.

        :return:Correct format of date that is required by the API.
        """

        date_format = format.lower()

        x = re.search(r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](20)\d\d$", date)  # dd-mm-yyyy
        y = re.search(r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](20)\d\d$", date)  # mm-dd-yyyy
        z = re.search(r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.]([2-9][0-9]|(19))$", date)  # mm-dd-yy
        a = re.search(r"^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.]([2-9][0-9]|(19))$", date)  # dd-mm-yy
        b = re.search(r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,]([2-9][0-9]|(19))$", date)  # dd-mon-yy
        c = re.search(r"^(0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)[- /.,](20)\d\d$", date)  # dd-mon-yyyy
        d = re.search(r"^((20)\d\d)[- /.,]([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])$", date)  # yyyy-mon-dd
        e = re.search(r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([A-Za-z]+)$", date)  # yyyy-dd-mon
        f = re.search(r"^((20)\d\d)[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$", date)  # yyyy-mm-dd
        g = re.search(r"^((20)\d\d)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](0?[1-9]|1[012])$", date)  # yyyy-dd-mm
        h = re.search(r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,](20)\d\d)$", date)  # mon-dd-yyyy
        i = re.search(r"^(([A-Za-z]+)[- /.,](0?[1-9]|[12][0-9]|3[01])[- /.,]([2-9][0-9]|(19)))$", date)  # mon-dd-yy

        if date_format == 'dd-mm-yyyy' or date_format == 'dd.mm.yyyy' or date_format == 'dd mm yyyy' or date_format == 'dd/mm/yyyy':
            if x:
                x1 = x.string
                date, month, year = re.split(r"[\s -/.]", x1)
                std_format = str(datetime.date(int(year), int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'mm-dd-yyyy' or date_format == 'mm.dd.yyyy' or date_format == 'mm dd yyyy' or date_format == 'mm/dd/yyyy':
            if y:
                y1 = y.string
                month, date, year = re.split(r"[\s -/.]", y1)
                std_format = str(datetime.date(int(year), int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'mm-dd-yy' or date_format == 'mm.dd.yy' or date_format == 'mm dd yy' or date_format == 'mm/dd/yy':
            if z:
                z1 = z.string
                month, date, year = re.split(r"[\s -/.]", z1)
                std_format = str(datetime.date(int(year)+2000, int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False


        elif date_format == 'dd-mm-yy' or date_format == 'dd.mm.yy' or date_format == 'dd mm yy' or date_format == 'dd/mm/yy':
            if a:
                a1 = a.string
                date, month, year = re.split(r"[\s -/.]", a1)
                std_format = str(datetime.date(int(year)+2000, int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'dd-mon-yy' or date_format == 'dd.mon.yy' or date_format == 'dd mon yy' or date_format == 'dd/mon/yy' or date_format == 'dd mon,yy':
            if b:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'dd-mon-yyyy' or date_format == 'dd.mon.yyyy' or date_format == 'dd mon yyyy' or date_format == 'dd/mon/yyyy' or date_format == 'dd mon,yyyy':
            if c:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'yyyy-mon-dd' or date_format == 'yyyy.mon.dd' or date_format == 'yyyy mon dd' or date_format == 'yyyy/mon/dd' or date_format == 'yyyy,mon dd':
            if d:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'yyyy-dd-mon' or date_format == 'yyyy.dd.mon' or date_format == 'yyyy dd mon' or date_format == 'yyyy/dd/mon' or date_format == 'yyyy,dd mon':
            if e:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'yyyy-mm-dd' or date_format == 'yyyy.mm.dd' or date_format == 'yyyy mm dd' or date_format == 'yyyy/mm/dd':
            if f:
                f1 = f.string
                year, month, date = re.split(r"[\s -/.]", f1)
                std_format = str(datetime.date(int(year), int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'yyyy-dd-mm' or date_format == 'yyyy.dd.mm' or date_format == 'yyyy dd mm' or date_format == 'yyyy/dd/mm':
            if g:
                g1 = g.string
                year, date, month = re.split(r"[\s -/.]", g1)
                std_format = str(datetime.date(int(year), int(month), int(date)))
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'mon-dd-yyyy' or date_format == 'mon.dd.yyyy' or date_format == 'mon dd yyyy' or date_format == 'mon/dd/yyyy' or date_format == 'mon dd,yyyy':
            if h:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False

        elif date_format == 'mon-dd-yy' or date_format == 'mon.dd.yy' or date_format == 'mon dd yy' or date_format == 'mon/dd/yy' or date_format == 'mon dd,yy':
            if i:
                dt = parse(date)
                std_format = str(dt.date())
                return std_format
            else:
                print("Format does not match with the entered date and time.")
                return False
