# datetime_converter.py
# This program is meant to post multiple timezones with the input of one

import pytz, datetime


def timecall():
    print("Time in EST:")

    est = datetime.datetime.now(pytz.timezone('US/Eastern'))
    print(1,est.tzinfo)
    print(2,est)

    
    


timecall()
