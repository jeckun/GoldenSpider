import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_PATH, 'data', 'foo.db')

URL = 'https://www.sge.com.cn/sjzx/mrhqsj'

sge_script = ['load', 'get_catalog_list', 'get_table', 'save_to_db']

sge_xpath = {
    'catalog_list': ".articleList ul li a",
    # 'catalog_list': '''//div[@class="articleList border_ea mt30 mb30"]/ul/li/a |
    #            //div[@class="articleList border_ea mt30 mb30"]/ul/li/a/span[2]
    #             ''',
    'tbody': '//table[@class="ke-zeroborder"]/tbody',
    'col': '//table[@class="ke-zeroborder"]/tbody/tr/td[1]',
    'row': '//table[@class="ke-zeroborder"]/tbody/tr[%d]/td',
}
