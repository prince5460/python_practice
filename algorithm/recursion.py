# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-17 下午5:10
@Desc :递归
'''


# 1加到100
def add(num):
    if num <= 0:
        return
    if num == 1:
        return num
    else:
        return num + add(num - 1)


print(add(10))


# 列表中元素的和
# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# 编写涉及数组的递归函数时,基线条件通常是数组为空或只包含一个元素

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


print(sum([1, 4, 6, 7, 8]))


# 计算列表包含的元素数
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


print(count([1, 3, 5, 7]))


# 找出列表中最大的数字
# def find_max(arr):
#     max = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#     return max


def find_max(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = find_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


print(find_max([1, 45, 7, 9, 2]))
