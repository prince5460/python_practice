# mongodb

### 使用命令操作mongodb
```
> use students
switched to db students
> stu = {}
{ }
> stu = {
... name:"tom",
... age:18}
{ "name" : "tom", "age" : 18 }
> db.students.insert(stu)
WriteResult({ "nInserted" : 1 })
> db.students.find()
{ "_id" : ObjectId("5cefa1bb85d4f5e384a1d1b0"), "name" : "tom", "age" : 18 }
> db.students.insert({name:"amy"})
WriteResult({ "nInserted" : 1 })
> db.students.findOne()
{ "_id" : ObjectId("5cefa1bb85d4f5e384a1d1b0"), "name" : "tom", "age" : 18 }
> db.students.find()
{ "_id" : ObjectId("5cefa1bb85d4f5e384a1d1b0"), "name" : "tom", "age" : 18 }
{ "_id" : ObjectId("5cefa2c485d4f5e384a1d1b1"), "name" : "amy" }
> db.students.update({name:"tom"},{name:"toms"})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.students.find()
{ "_id" : ObjectId("5cefa1bb85d4f5e384a1d1b0"), "name" : "toms" }
{ "_id" : ObjectId("5cefa2c485d4f5e384a1d1b1"), "name" : "amy" }
> db.students.remove({name:"amy"})
WriteResult({ "nRemoved" : 1 })
> db.students.find()
{ "_id" : ObjectId("5cefa1bb85d4f5e384a1d1b0"), "name" : "toms" }
> db.students.remove({})
WriteResult({ "nRemoved" : 1 })
> db.students.find()
> 

```

### 练习
```
db.students.insertMany(
   [
     { name: "bob", age: 16, sex: "male", grade: 95},
     { name: "ahn", age: 18, sex: "female", grade: 45},
     { name: "xi", age: 15, sex: "male", grade: 75},
     { name: "bob1", age: 16, sex: "male", grade: 95},
     { name: "ahn1", age: 18, sex: "male", grade: 45},
     { name: "xi1", age: 15, sex: "female", grade: 55},
     { name: "bob2", age: 16, sex: "female", grade: 95},
     { name: "ahn2", age: 18, sex: "male", grade: 60},
     { name: "xi2", age: 15, sex: "male", grade: 75},
     { name: "bob3", age: 16, sex: "male", grade: 95},
     { name: "ahn3", age: 18, sex: "female", grade: 45},
     { name: "xi3", age: 15, sex: "male", grade: 85},
     { name: "bob4", age: 16, sex: "female", grade: 95},
     { name: "ahn4", age: 18, sex: "male", grade: 45},
     { name: "xi4", age: 15, sex: "male", grade: 75}
   ]
)


创建一个学生信息表（至少包含：姓名，性别，成绩，年龄）
写入十五条不同的数据
查询所有的男生数据（只需要学生的姓名和年龄）
db.students.find({sex: 'male'}, {name: 1, age: true, _id: 0})
查询成绩及格的学生信息（学生成绩大于或等于60分）
db.students.find({grade: {'$gte': 60}})
查询所有18岁的男生和16岁的女生的数据
db.students.find({'$or': [{sex: 'male', age: 18}, {sex: 'female', age: 16}]})
按照学生的年龄进行排序
db.students.find().sort({age: 1})
将所有的女学生年龄增加一岁
db.students.update({sex: 'female'}, {'$inc': {age: 1}}, {multi: true})
```