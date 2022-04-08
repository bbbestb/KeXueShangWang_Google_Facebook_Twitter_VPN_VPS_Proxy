#!/usr/bin/python

'''
Beautiful Soup sits atop an HTML or XML parser, providing Pythonic idioms
for iterating, searching, and modifying the parse tree.
# pip install beautifulsoup4
# pip install requests
'''

import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
if request.ok:
    soup = BeautifulSoup(request.text, 'html.parser')
    print soup.title.string
