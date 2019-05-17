# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午5:09
@Desc :快速排序
'''


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


my_list = [9, 1, 21, 4, 7]
print(quick_sort(my_list))
