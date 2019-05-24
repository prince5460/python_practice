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

params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

original_params = json.loads(params_str)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
