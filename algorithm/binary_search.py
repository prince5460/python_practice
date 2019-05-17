# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午3:15
@Desc :二分查找(只能用于有序元素列表)
'''


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    # 只要范围没有缩小到只包含一个元素,每次都检查中间的元素
    while low <= high:
        # 如果(low + high)不是偶数,自动将mid向下圆整
        mid = (low + high) // 2
        guess = list[mid]
        # 找到了元素
        if guess == item:
            return mid
        # 猜的数字大了
        if guess > item:
            high = mid - 1
        # 猜的数字小了
        else:
            low = mid + 1
    # 没有指定的元素
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))

print(binary_search(my_list, -1))
