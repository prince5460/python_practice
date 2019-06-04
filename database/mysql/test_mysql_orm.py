# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-4 下午2:07
@Desc :SQLAlchemy
'''
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:zhou123@localhost:3306/news?charset=utf8')
Base = declarative_base()

Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(200), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


class OrmTest():
    def __init__(self):
        self.session = Session()

    def add_one(self):
        ''' 添加数据 '''
        new_obj = News(
            title='标题1',
            content='内容1',
            types="百家"
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据'''
        return self.session.query(News).get(1)

    def get_more(self):
        '''查询多条数据'''
        return self.session.query(News).filter_by(is_valid=True)

    def update_data(self, pk):
        '''修改数据'''

        # 修改单条数据
        # new_obj = self.session.query(News).get(pk)
        # if new_obj:
        #     new_obj.is_valid = 0
        #     self.session.add(new_obj)
        #     self.session.commit()
        #     return True
        # return False

        # 修改多条数据
        data_list = self.session.query(News).filter_by(is_valid=True)
        for item in data_list:
            item.is_valid = 0
            self.session.add(item)
        self.session.commit()

    def delete_data(self, pk):
        '''删除数据'''
        # 获取要删除的数据
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()


def main():
    obj = OrmTest()

    # rest = obj.add_one()
    # print(rest.id)

    # rest = obj.get_one()
    # if rest:
    #     print(rest.title)
    # else:
    #     print('Not exist.')

    # rest = obj.get_more()
    # print(rest.count())

    # print(obj.update_data(1))

    obj.delete_data(1)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    main()
