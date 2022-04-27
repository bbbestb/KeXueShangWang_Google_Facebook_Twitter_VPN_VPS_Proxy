

import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
if request.ok:
    soup = BeautifulSoup(request.text, 'html.parser')
    print soup.title.string
