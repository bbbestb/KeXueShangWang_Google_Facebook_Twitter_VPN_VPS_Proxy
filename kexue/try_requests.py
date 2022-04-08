#!/usr/bin/python

'''
just try a lib for http request.
# pip install requests

To void an 'InsecurePlatformWarning':
You only need to install the security package extras.
$ pip install requests[security]
or, install them directly:
$ pip install pyopenssl ndg-httpsclient pyasn1
'''

import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
if request.ok:
    print(request.text) 
    
