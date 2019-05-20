# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-20 上午11:03
@Desc :选择排序
'''


# 找出数组中最小元素
def find_smallest(arr):
    smallest = arr[0]  # 存储最小的值
    smallest_index = 0  # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 选择排序
def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # 找出数组中最小的元素,
        new_arr.append(arr.pop(smallest))  # 将其加入到新数组中
    return new_arr


print(select_sort([5, 1, 4, 8, 0, 7, 9]))
