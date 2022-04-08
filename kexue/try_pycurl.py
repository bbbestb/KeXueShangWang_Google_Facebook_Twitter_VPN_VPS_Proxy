#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 15, 2013

@author: Jay
'''

import sys
import pycurl
import time

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf

sys.stderr.write("Testing %s\n" % pycurl.version)

start_time = time.time()

url = 'http://www.dianping.com/shanghai'
t = Test()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
end_time = time.time()
duration = end_time - start_time
print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
c.close()

print 'pycurl takes %s seconds to get %s ' % (duration, url)

print 'lenth of the content is %d' % len(t.contents)
#print(t.contents)
