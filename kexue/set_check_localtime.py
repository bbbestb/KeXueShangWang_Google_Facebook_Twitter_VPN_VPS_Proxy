# -*- coding: utf-8

import sys
import time
import subprocess
import argparse
import urllib2


def set_beijing_time_from_web(url):
    ''' set os and hardware clock as beijing time from internet '''
    # use urllib2 in python2; not use requests which need installation
    response = urllib2.urlopen(url)
    #print response.read()
    # 获取http头date部分
    ts = response.headers['date']
    # 将日期时间字符转化为time
    gmt_time = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 将GMT时间转换成北京时间
    local_time = time.localtime(time.mktime(gmt_time) + 8*3600)
    str1 = "%u-%02u-%02u" % (local_time.tm_year,
                             local_time.tm_mon, local_time.tm_mday)
    str2 = "%02u:%02u:%02u" % (
        local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
    cmd = 'date -s "%s %s"' % (str1, str2)
    #print cmd
    subprocess.check_call(cmd, shell=True)
    hw_cmd = 'hwclock -w'
    #print hw_cmd
    subprocess.check_call(hw_cmd, shell=True)
    print 'OK. set time: %s' % ' '.join([str1, str2])


def check_localtime_with_internet(url):
    ''' check local time with internet '''
    threshold = 2
    # use urllib2 in python2; not use requests which need installation
    response = urllib2.urlopen(url)
    #print response.read()
    # 获取http头date部分
    ts = response.headers['date']
    # 将日期时间字符转化为time
    gmt_time = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 将GMT时间转换成北京时间
    internet_ts = time.mktime(gmt_time)
    local_ts = time.mktime(time.gmtime())
    if abs(local_ts - internet_ts) <= threshold:
        print 'OK. check localtime.'
    else:
        print 'ERROR! local_ts: %s  internet_ts:%s' % (local_ts, internet_ts)
        sys.exit(1)


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    parser = argparse.ArgumentParser()
    parser.description = 'set/check localtime (i.e. CST) with internet'
    parser.add_argument('-c', '--check', action='store_true',
                        help='only check local time')
    parser.add_argument('-s', '--set', action='store_true',
                        help='only set local time')
    parser.add_argument('-u', '--url', default=url,
                        help='the url to sync time')
    args = parser.parse_args()
    if args.set:
        set_beijing_time_from_web(args.url)
    else:
        check_localtime_with_internet(args.url)
