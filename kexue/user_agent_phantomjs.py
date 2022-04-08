'''
Created on Dec 6, 2013

@author: Jay <smile665@gmail.com>
@summary: Set user-agent before using PhantomJS to get a web page.
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)

driver = webdriver.PhantomJS(executable_path='./phantomjs', desired_capabilities=dcap)
driver.get("http://dianping.com/")
cap_dict = driver.desired_capabilities
for key in cap_dict:
    print '%s: %s' % (key, cap_dict[key])
print driver.current_url
driver.quit
