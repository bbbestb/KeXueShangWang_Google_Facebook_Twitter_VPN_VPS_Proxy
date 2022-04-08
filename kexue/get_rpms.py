#!/usr/bin/python3
'''
Created on Dec 5, 2011

@author: Jay Ren
@note: to get and parse html from a url, then, to download all the RPMs listed in the html context
'''

import http.client
from html.parser import HTMLParser
import re
import os


def get_rpm_list(host, url, rpm_list):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", url)
    res = conn.getresponse()
    data = res.read()
    str = data.decode("utf-8")
    parser = my_html_parser(rpm_list)
    parser.feed(str)


class my_html_parser(HTMLParser):

    def __init__(self, rpm_list):
        HTMLParser.__init__(self)
        rpm_list = rpm_list

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == "href":
                    if re.search('\.rpm$', value):
                        rpm_list.append(value)


def download_rpms(rpm_list):
    path = base_dir + dir + '/'
    for rpm in rpm_list:
        rpm_url = url+rpm
        local_name = path + rpm
        if os.path.exists(local_name):
            os.remove(local_name)
        f = open(local_name, 'wb')
        conn = http.client.HTTPConnection(host)
        conn.request("GET", rpm_url)
        res = conn.getresponse()
        f.write(res.read())


def prepare_dir(base_dir, dir):
    path = base_dir + dir
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    host = 'XXX.XXX.com'
    url = "/pub/ISO/redhat/redhat-rhel6/RHEL-6.2-GA/Server/optional/x86_64/os/Packages/"
    rpm_list = []
    base_dir = '/home/master/Downloads/'
    dir = 'temp_packages'
    get_rpm_list(host, url, rpm_list)
    prepare_dir(base_dir, dir)
    download_rpms(rpm_list)
