#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Create on 2015-05-05
'''
import os
import unittest
from selenium import webdriver
import time

# Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class DpAppTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['autoLaunch'] = 'true'
  #      desired_caps['automationName'] = "selendroid"
        desired_caps['app'] = PATH(
            'apps/Nova_7.2.0_debug.apk'
        )
        desired_caps['appPackage'] = 'com.dianping.v1'
        desired_caps[
            'appActivity'] = 'com.dianping.main.guide.SplashScreenActivity'

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_dpApp(self):
        time.sleep(10)
        el = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'美食')]")
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
