# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-5-31 上午11:21
@Desc :mongoengine
'''

from mongoengine import connect, Document, EmbeddedDocument, DynamicDocument, \
    StringField, IntField, FloatField, DateTimeField, ListField, EmbeddedDocumentField
from datetime import datetime

connect('students', host='mongodb://localhost/students')


class Grade(EmbeddedDocument):
    '''学生的成绩'''
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICE = (
    ('male', '男'),
    ('female', '女')
)


class Student(DynamicDocument):
    '''学生模型'''
    name = StringField(max=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICE, required=True)
    grade = FloatField()
    created_at = DateTimeField(default=datetime.now())
    grades = ListField(EmbeddedDocumentField(Grade))
    address = StringField()
    school = StringField()

    meta = {
        'collection': 'students',
        'ordering': ['-age']
    }


class TestMongoEngine():
    def add_one(self):
        '''添加一条数据到数据库'''
        yuwen = Grade(
            name='语文',
            score=90
        )
        shuxue = Grade(
            name='数学',
            score=100
        )
        stu_obj = Student(
            name='张三3',
            age=15,
            sex='male',
            grades=[yuwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        ''' 查询一条数据 '''
        return Student.objects.first()

    def get_more(self):
        ''' 查询多条数据 '''
        return Student.objects.all()

    def get_one_from_oid(self, oid):
        ''' 查询指定ID的数据 '''
        return Student.objects.filter(id=oid).first()

    def update(self):
        '''修改数据'''
        # 修改所有男生年龄，增加10岁
        # return Student.objects.filter(sex='male').update(inc__age=10)

        # 修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)

    def delete(self):
        '''删除数据'''
        # 删除一条数据
        # return Student.objects.filter(sex='male').first().delete()

        # 删除多条数据
        return Student.objects.filter(sex='female').delete()


def main():
    obj = TestMongoEngine()

    rest = obj.add_one()
    print(rest.id)

    # rest = obj.get_one()
    # print(rest.id)

    # rest = obj.get_more()
    # print(type(rest))
    # for item in rest:
    #     print(item.age)

    # rest = obj.get_one_from_oid('5cefa5a6646e144bdfc3a9c6')
    # print(rest.name)

    # rest = obj.update()
    # print(rest)

    # rest = obj.delete()
    # print(rest)


if __name__ == '__main__':
    main()
