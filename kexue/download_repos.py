'''
package installation command:
    pip install beautifulsoup4 requests
(bs4 doesn't work with python 2.6, so this only work on python 2.7)
'''

import requests
from bs4 import BeautifulSoup
import os
from urllib import unquote


class repos(object):

    """download linux repos from mirrors' site."""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/42.0'}
    urls_dict = {}

    def __init__(self, base_url, base_dir):
        super(repos, self).__init__()
        self.base_url = base_url
        self.base_dir = base_dir

    def download(self):
        for i in self.urls_dict:
            for j in self.urls_dict[i]['files']:
                url = self.base_url + i + j
                print url
                request = requests.get(url, headers=self.headers)
                if request.ok:
                    file_location = self.base_dir + i + j
                    print file_location
                    if not os.path.exists(self.base_dir + i):
                        os.makedirs(self.base_dir + i)
                    with open(file_location, "wb") as the_file:
                        the_file.write(request.content)

    def get_urls_dict(self, path='/', parent=None):
        if path not in self.urls_dict:
            self.urls_dict[path] = {
                'parent': parent, 'sub_dirs': [], 'files': []}
            url = self.base_url + path
            request = requests.get(url, headers=self.headers)
            if request.ok:
                soup = BeautifulSoup(request.text, 'html.parser')
                for url in soup.find_all('a'):
                    url_text = unquote(url.get('href'))
                    if url_text.endswith('/') and url_text != '/' and url_text != '../':
                        self.urls_dict[path]['sub_dirs'].append(url_text)
                    elif not url_text.endswith('/') and not url_text.startswith('?'):
                        self.urls_dict[path]['files'].append(url_text)
        if self.urls_dict[path]['parent'] == None and len(self.urls_dict[path]['sub_dirs']) == 0:
            pass
        elif len(self.urls_dict[path]['sub_dirs']) != 0:
            for i in self.urls_dict[path]['sub_dirs']:
                return self.get_urls_dict(path=path + i, parent=path)
        elif self.urls_dict[path]['parent'] != None and len(self.urls_dict[path]['sub_dirs']) == 0:
            self.urls_dict[self.urls_dict[path]['parent']][
                'sub_dirs'].remove(path.split('/')[-2] + '/')
            return self.get_urls_dict(path=self.urls_dict[path]['parent'],
                                      parent=self.urls_dict[self.urls_dict[path]['parent']]['parent'])


if __name__ == '__main__':
    url = 'http://mirrors.163.com/centos/6.7/os/x86_64'
    the_dir = '/tmp/centos6u7'
    repo = repos(url, the_dir)
    repo.get_urls_dict()
    # print repo.urls_dict
    repo.download()
