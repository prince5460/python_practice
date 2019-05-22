# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-22 上午9:38
@Desc :广度优先搜索
'''

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []


def seller(name):
    return name[-1] == 'y'  # 判断一个人是不是销售商,检查人的姓名是否以y结尾:如果是,他就是销售商


def search(name):
    search_deque = deque()  # 创建一个双端队列
    search_deque += graph[name]  # 将你的邻居都加入到这个搜索队列中
    searched = []  # 这个数组用于记录检查过的人
    while search_deque:  # 只要队列不为空
        person = search_deque.popleft()  # 取出其中的第一个人,检查这个人是否是销售商
        if person not in searched:  # 仅当这个人没检查过时才检查
            if seller(person):
                print(person + ' is seller!')
                return True
            else:
                search_deque += graph[person]  # 如果不是销售商,将这个人的朋友都加入搜索队列
                searched.append(person)  # 将这个人标记为检查过
    return False  # 如果到达了这里,就说明队列中没人是销售商


search("you")
