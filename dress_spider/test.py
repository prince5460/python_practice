# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/9/7 下午12:18
@Desc :
'''

import requests
from bs4 import BeautifulSoup

'''
裙子
https://www.topshop.com/en/tsuk/category/clothing-427/dresses-442
https://www.topshop.com/api/products?currentPage=2&pageSize=24&category=203984,208523


所有衣服
https://www.topshop.com/en/tsuk/category/clothing-427
https://www.topshop.com/api/products?currentPage=2&pageSize=24&category=203984
https://www.topshop.com/api/products?currentPage=3&pageSize=24&category=203984
https://www.topshop.com/api/products?currentPage=4&pageSize=24&category=203984



牛仔裤
https://www.topshop.com/en/tsuk/category/jeans-6877054/
https://www.topshop.com/api/products?currentPage=2&pageSize=24&category=3493110



鞋子
https://www.topshop.com/en/tsuk/category/shoes-430
https://www.topshop.com/api/products?currentPage=2&pageSize=24&category=208492
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Connection': 'keep-alive',
    'brand-code': 'tsuk',
}

web_data = requests.get("https://www.topshop.com/api/products?currentPage=2&pageSize=24&category=203984,208523",headers=headers).json()
# products_data = web_data["products"]
# for product in products_data:
#     print(product['name'])
print(web_data)