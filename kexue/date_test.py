#!/usr/bin/python

'''
Created on Sep 20, 2013
@summary: some of the methods to handle date calculation
@author: Jay <smilejay.com>
'''

import datetime
import calendar


def get_a_month_val(year, month, day=1):
    day = datetime.datetime(year, month, day)
    print day
    last_day_previous_month = day.replace(day=1) - datetime.timedelta(days=1)
    first_day_this_month = day.replace(day=1)
    last_day_this_month = day.replace(day=calendar.monthrange(year, month)[1])
    last_day_this_month_1 = day.replace(day=calendar.mdays[day.month])
    print last_day_previous_month
    print first_day_this_month
    print last_day_this_month
    print last_day_this_month_1

if __name__ == '__main__':
    get_a_month_val(2013, 10, 20)
