# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午5:09
@Desc :快速排序
'''


def quick_sort(arr):
    if len(arr) < 2:
        return arr  # 基线条件:为空或只包含一个元素的数组是“有序”的
    else:
        pivot = arr[0]  # 递归条件
        less = [i for i in arr[1:] if i <= pivot]  # 由所有小于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组
        return quick_sort(less) + [pivot] + quick_sort(greater)


my_list = [9, 1, 21, 4, 7]
print(quick_sort(my_list))
