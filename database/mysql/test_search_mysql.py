# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-4 上午9:25
@Desc :操作mysql
'''
import MySQLdb


class MysqlSearch():

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        '''获取连接'''
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='zhou123',
                db='school',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error:{}'.format(e))

    def close_conn(self):
        '''关闭连接'''
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error:{}'.format(e))

    def get_one(self):
        """获取一条数据"""
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家',))
        # print(dir(cursor))
        # print(cursor.description)
        # for k in cursor.description:
        #     print(k[0])
        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self):
        """获取多条数据"""
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家',))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more_by_page(self, page, page_size):
        ''' 分页查询数据 '''
        offset = (page - 1) * page_size
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s, %s;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', offset, page_size))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        ''' 插入数据 '''
        # 受影响的行数
        row_count = 0
        try:
            # 准备SQL
            sql = (
                "INSERT INTO `news`(`title`,`image`, `content`, `types`, `is_valid`) VALUE"
                "(%s, %s, %s, %s, %s);"
            )
            # 获取链接和cursor
            cursor = self.conn.cursor()
            # 执行sql
            # 提交数据到数据库
            cursor.execute(sql, ('标题1', '/static/img/news/01.png', '新闻内容1', '推荐', 1))
            # cursor.execute(sql, ('标题2', '/static/img/news/01.png', '新闻内容2', '推荐', 1, 1))
            # 提交事务
            self.conn.commit()
            # 执行最后一条SQL影响的行数
            row_count = cursor.rowcount
            # 关闭cursor
            cursor.close()
        except:
            print('Translation Error Rollback')
            # 回滚事务
            self.conn.rollback()

        # 关闭连接
        self.close_conn()
        return row_count


def main():
    obj = MysqlSearch()

    # rest = obj.get_one()
    # print(rest['title'])

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)
    #     print('------')
    # print('*' * 20)

    # rest = obj.get_more_by_page(1, 3)
    # for item in rest:
    #     print(item)
    #     print('-------------------')

    rest = obj.add_one()
    print(rest)


if __name__ == '__main__':
    main()
