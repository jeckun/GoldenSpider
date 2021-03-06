# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Module:
    __hostname__ = ''
    url = ''
    catalog_list = []

    def __init__(self, url=None):
        self.url = url

    @property
    def hostname(self):
        return self.__hostname__


class Spider:
    module = Module()
    parser = None

    def __init__(self, module):
        self.module = module

    def load(self, url=None, headers=None, cookies=None):
        if url:
            return self.load_by_params(url=url, params=None, headers=headers, cookies=cookies)
        else:
            return self.load_by_params(url=self.module.url, params=None, headers=headers, cookies=cookies)

    def load_by_params(self, url, params, headers=None, cookies=None):
        try:
            self.module.url = url
            if params:
                response = requests.get(
                    url, params=params, headers=headers, cookies=cookies)
            else:
                response = requests.get(url, headers=headers, cookies=cookies)
            response.encode = 'utf-8'
            html_doc = response.text
            self.parser = BeautifulSoup(html_doc, 'lxml')
            print('网页：%s 加载成功.' % self.module.hostname)
        except Exception as e:
            print('Error: %s' % e)

    def get_catalog_list(self, catalog_list_xpath):
        pass
