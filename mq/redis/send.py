# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-7-3 上午11:26
@Desc :
'''

import redis
import names
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    time.sleep(3)
    name = names.get_full_name()
    x = r.publish('names', name)

    print(x, name)
