# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Spider:
    module = None
    bs_soup = None

    def __init__(self, module):
        self.module = module

    def load(self, url):
        return self.load_by_params(url, None)

    def load_by_params(self, url, params):
        try:
            self.module.url = url
            if params:
                response = requests.get(url, params=params)
            else:
                response = requests.get(url)
            response.encode = 'utf-8'
            html_doc = response.text
            self.soup = BeautifulSoup(html_doc, 'lxml')
        except Exception as e:
            print('Error: %s' % e)
