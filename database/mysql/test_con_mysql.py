# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-4 上午9:10
@Desc :连接数据库
'''

import MySQLdb

# 获取连接
try:
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='zhou123',
        db='school',
        port=3306,
        charset='utf8'
    )

    # 获取数据
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `news` ORDER BY `created_at` DESC;')
    rest = cursor.fetchone()
    print(rest)

    # 关闭连接
    conn.close()

except MySQLdb.Error as e:
    print('Error:{}'.format(e))
