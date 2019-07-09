# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-7-3 上午11:27
@Desc :
'''

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

ps = r.pubsub()
ps.subscribe('names')

for item in ps.listen():
    print(item)
