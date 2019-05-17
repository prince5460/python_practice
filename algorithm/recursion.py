# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午5:10
@Desc :递归
'''


def recursion(num):
    if num == 1:
        return num
    else:
        return num + recursion(num - 1)


print(recursion(100))
