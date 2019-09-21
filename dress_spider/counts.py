# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/9/6 下午11:17
@Desc :打印item数据量
'''

import time
from pages_parsing import clothing

while True:
    print(clothing.find().count())
    time.sleep(5)


