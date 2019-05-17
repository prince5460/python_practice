# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午4:53
@Desc :冒泡排序
'''


def bubble_sort(arr):
    # 外部循环控制所有的回合
    for i in range(len(arr) - 1):
        # 内部循环实现每一轮的冒泡处理，先进行元素比较，再进行元素交换
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


my_list = [9, 23, 1, 3, 6, 8]
print(bubble_sort(my_list))
