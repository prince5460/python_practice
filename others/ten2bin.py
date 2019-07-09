# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-28 下午5:18
@Desc :
'''


def mybin(num):
    if num == 0:
        return 0

    res = []
    while num:
        num, rem = divmod(num, 2)
        res.append(str(rem))
    return ''.join(reversed(res))


CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def encode(num):
    if num == 0:
        return CHARS[0]
    res = []
    while num:
        num, rem = divmod(num, len(CHARS))
        res.append(CHARS[rem])
    return ''.join(reversed(res))


if __name__ == '__main__':
    print(mybin(12))
    print(len(CHARS))
