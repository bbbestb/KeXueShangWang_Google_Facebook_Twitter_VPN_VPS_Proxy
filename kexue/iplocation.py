#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Oct 20, 2013
@summary: geography info about an IP address
@author: Jay <smile665@gmail.com>     http://smilejay.com/
'''

import json
import urllib2
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class location_freegeoip():
    '''
    build the mapping of the ip address and its location.
    the geo info is from <freegeoip.net>
    '''

    def __init__(self, ip):
        '''
        Constructor of location_freegeoip class
        '''
        self.ip = ip
        self.api_format = 'json'
        self.api_url = 'http://freegeoip.net/%s/%s' % (self.api_format, self.ip)

    def get_geoinfo(self):
        """ get the geo info from the remote API.

            return a dict about the location.
        """
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
#        print datadict
        return datadict

    def get_country(self):
        key = 'country_name'
        datadict = self.get_geoinfo()
        return datadict[key]

    def get_region(self):
        key = 'region_name'
        datadict = self.get_geoinfo()
        return datadict[key]

    def get_city(self):
        key = 'city'
        datadict = self.get_geoinfo()
        return datadict[key]


class location_taobao():
    '''
    build the mapping of the ip address and its location
    the geo info is from Taobao
    e.g. http://ip.taobao.com/service/getIpInfo.php?ip=112.111.184.63
    The getIpInfo API from Taobao returns a JSON object.
    '''

    def __init__(self, ip):
        self.ip = ip
        self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % self.ip

    def get_geoinfo(self):
        """ get the geo info from the remote API.

            return a dict about the location.
        """
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
#        print datadict
        return datadict['data']

    def get_country(self):
        key = u'country'
        datadict = self.get_geoinfo()
        return datadict[key]

    def get_region(self):
        key = 'region'
        datadict = self.get_geoinfo()
        return datadict[key]

    def get_city(self):
        key = 'city'
        datadict = self.get_geoinfo()
        return datadict[key]

    def get_isp(self):
        key = 'isp'
        datadict = self.get_geoinfo()
        return datadict[key]


class location_qq():
    '''
    build the mapping of the ip address and its location.
    the geo info is from Tencent.
    Note: the content of the Tencent's API return page is encoded by 'gb2312'.
    e.g. http://ip.qq.com/cgi-bin/searchip?searchip1=112.111.184.64
    '''

    def __init__(self, ip):
        '''
        Construction of location_ipdotcn class.
        '''
        self.ip = ip
        self.api_url = 'http://ip.qq.com/cgi-bin/searchip?searchip1=%s' % ip

    def get_geoinfo(self):
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read().decode('gb2312').encode('utf8')
        pattern = re.compile(r'该IP所在地为：<span>(.+)</span>')
        m = re.search(pattern, data)
        if m is not None:
            return m.group(1).split('&nbsp;')
        else:
            return None

    def get_region(self):
        return self.get_geoinfo()[0]

    def get_isp(self):
        return self.get_geoinfo()[1]


class location_ipdotcn():
    '''
    build the mapping of the ip address and its location.
    the geo info is from www.ip.cn
    need to use PhantomJS to open the URL to render its JS
    '''

    def __init__(self, ip):
        '''
        Construction of location_ipdotcn class.
        '''
        self.ip = ip
        self.api_url = 'http://www.ip.cn/%s' % ip

    def get_geoinfo(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/29.0 ")
        driver = webdriver.PhantomJS(
            executable_path='/usr/local/bin/phantomjs',
            desired_capabilities=dcap)
        driver.get(self.api_url)
        text = driver.find_element_by_xpath('//div[@id="result"]/div/p').text
        res = text.split('来自：')[1].split(' ')
        driver.quit()
        return res

    def get_region(self):
        return self.get_geoinfo()[0]

    def get_isp(self):
        return self.get_geoinfo()[1]


if __name__ == '__main__':
    ip = '110.84.0.129'
#    iploc = location_taobao(ip)
#    print iploc.get_geoinfo()
#    print iploc.get_country()
#    print iploc.get_region()
#    print iploc.get_city()
#    print iploc.get_isp()
#    iploc = location_qq(ip)
    iploc = location_ipdotcn(ip)
#    iploc.get_geoinfo()
    print iploc.get_region()
    print iploc.get_isp()
