# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/9/6 下午11:07
@Desc :
'''
from multiprocessing import Pool

from pages_parsing import get_json_item_info

from pages_parsing import get_item_info
from channel_extract import channel_list

page = 1  # 页数


def get_all_links_from(url):
    for i in range(1, page + 1):
        get_item_info(url, i)


def get_data_from_links(url):
    for i in range(1, page+1):
        get_json_item_info(url, i)


if __name__ == '__main__':
    pool = Pool()
    # # pool = Pool(processes=6)
    pool.map(get_data_from_links, channel_list.split())
    pool.close()
    pool.join()