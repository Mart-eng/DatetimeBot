# datetime_converter.py
# This program is meant to post multiple timezones with the input of one

import pytz, datetime

#print(pytz.common_timezones)
def timecall():
    print("Time in EST:")

    est = datetime.datetime.now(pytz.timezone('US/Eastern'))
    print(1,est.tzinfo)
    print(2,est)

    print('Time in PST')
    pst = datetime.datetime.now(pytz.timezone('US/Pacific'))
    print(3,pst.tzinfo)
    print(4,pst)

    print("Time in MST")
    mst = datetime.datetime.now(pytz.timezone("US/Arizona"))
    print(5,mst.tzinfo)
    print(6,mst)

    fmt = '%H:%M:%S'
    print("Time in CST")
    cst = datetime.datetime.now(pytz.timezone('US/Central'))
    cst.astimezone()
    print(7,cst.tzinfo)
    print(8,cst)


timecall()
