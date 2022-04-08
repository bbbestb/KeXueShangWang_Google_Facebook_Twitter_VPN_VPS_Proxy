#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 2011-8-15

@author: Jay Ren  笑遍世界
'''

import re
import urllib.request


def get_reponse_from_url(url):
    req = urllib.request.Request(url)
    encoding = 'gbk'
    try:
        doc = urllib.request.urlopen(req).read()
        # print(doc.decode(encoding))
        return doc.decode(encoding)
    except Exception as e:
        print("urlopen Exception : %s" % e)


def get_ip_and_location():
    url_ip_qq = "http://fw.qq.com/ipaddress"
    url_location_youdao = "http://www.youdao.com/smartresult-xml/search.s?type=ip&q="
    re_ip = "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))"
    str_ip = get_reponse_from_url(url_ip_qq)
    ip = re.search(re_ip, str_ip).group(1)
    # print("ip="+ip.group(1))
    print("your ip is:"+ip)
    url_location_youdao += ip
    str_location = get_reponse_from_url(url_location_youdao)
    re_location = '<location>(.*)</location>'
    location = re.search(re_location, str_location).group(1)
    print("you are here:"+location)

if __name__ == '__main__':
    get_ip_and_location()
