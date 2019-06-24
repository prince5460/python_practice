# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-24 下午3:13
@Desc :
'''
from app import celery


@celery.task
def add(x, y):
    return x + y


print(add(1, 4))
