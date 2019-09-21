# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/9/6 下午10:40
@Desc :解析页面内容
'''
import time
import asyncio
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import pymongo

client = pymongo.MongoClient('localhost', 27017)
topshop = client['topshop']
clothing = topshop['clothing']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Connection': 'keep-alive',
    'brand-code': 'tsuk',
}


# 方式一：解析页面元素
def get_item_info(url, page):
    web_data = requests.get(url.format(str(page)), headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')

    titles = soup.select("div.Product-meta > div > header > a")
    prices = soup.select("div.Product-meta > div > span > span.Price.notranslate")
    images = soup.select("picture > img")

    for title, price, image in zip(titles, prices, images):
        data = {
            "title": title.get_text(),
            "price": price.get_text(),
            "image": "https:" + image.get('src').split('?')[0]
        }
        time.sleep(3)

        # 异步处理
        loop = asyncio.get_event_loop()  # 创建一个默认的事件循环事件
        dl_img = download_images(data["image"], data["title"])
        loop.run_until_complete(dl_img)  # 通过调用事件循环的 run_until_complete() 启动协程
        print("图片下载完成")

        print(data)
        clothing.insert_one(data)


# 方式二：解析json数据
def get_json_item_info(url, page):
    time.sleep(2)
    web_data = requests.get(url.format(str(page)), headers=headers).json()
    products = web_data["products"]
    for product in products:
        product_data = {}
        product_data['name'] = product['name']
        product_data['unitPrice'] = product['unitPrice']
        product_data['seoUrl'] = product['seoUrl']
        product_data['productBaseImageUrl'] = product['productBaseImageUrl'] + '.jpg'
        product_data['outfitBaseImageUrl'] = product['outfitBaseImageUrl'] + '.jpg'
        product_data['created_at'] = datetime.now()

        print(product_data)
        clothing.insert_one(product_data)

        # 异步处理图片下载
        loop = asyncio.get_event_loop()  # 创建一个默认的事件循环事件
        dl_img = download_images(product['productBaseImageUrl'] + '.jpg', product['name'])
        loop.run_until_complete(dl_img)  # 通过调用事件循环的 run_until_complete() 启动协程
        print("图片下载完成")


# 下载图片
async def download_images(img_url, name):
    await asyncio.sleep(1)
    response = requests.get(img_url)
    with open("images/" + name + ".jpg", 'wb') as f:
        f.write(response.content)
        f.close()
