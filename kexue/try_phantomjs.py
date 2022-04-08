#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Dec 6, 2013

@author: Jay <smile665@gmail.com>
@description: use PhantomJS to parse a web page to get the geo info of an IP
              For PhantomJS, please visit: http://phantomjs.org/
'''

from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS(executable_path='./phantomjs')
driver.get("http://www.ip.cn/125.95.26.81")
#print driver.current_url
#print driver.page_source
print driver.find_element_by_id('result').text.split('\n')[0].split('来自：')[1]
#text =  driver.find_element_by_xpath('//div[@id="result"]/div/p').text
#result = text.split('来自：')[1]
#print result
driver.quit
