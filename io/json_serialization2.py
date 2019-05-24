# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-24 上午11:20
@Desc :
'''

import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
