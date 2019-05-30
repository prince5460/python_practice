# redis

###1.字符串（String）相关操作
```
set -- 设置值
get -- 获取值
mset -- 设置多个键值对
mget -- 获取多个键值对
append -- 添加字符串
del -- 删除
incr/decr -- 增加/减少1

redis-cli
127.0.0.1:6379> set animal 'cat'
OK
127.0.0.1:6379> get animal
"cat"
127.0.0.1:6379> set animal 'Dog'
OK
127.0.0.1:6379> get animal
"Dog"
127.0.0.1:6379> append animal ' Cat'
(integer) 7
127.0.0.1:6379> get animal
"Dog Cat"
127.0.0.1:6379> mset user1 'Tom' user2 'Jhon'
OK
127.0.0.1:6379> get user1
"Tom"
127.0.0.1:6379> get user2
"Jhon"
127.0.0.1:6379> mget user1 user2 animal
1) "Tom"
2) "Jhon"
3) "Dog Cat"
127.0.0.1:6379> del user2
(integer) 1
127.0.0.1:6379> del user2
(integer) 0
127.0.0.1:6379> get user2
(nil)
127.0.0.1:6379> set num 10
OK
127.0.0.1:6379> decr num
(integer) 9
127.0.0.1:6379> get num
"9"
127.0.0.1:6379> decr num
(integer) 8
127.0.0.1:6379> get num
"8"
127.0.0.1:6379> incr num
(integer) 9
127.0.0.1:6379> get num
"9"
127.0.0.1:6379> del animal
(integer) 1
127.0.0.1:6379> get animal
(nil)
127.0.0.1:6379> set animal "Cat" EX 5 // 暂存5秒
OK
127.0.0.1:6379> get animal
"Cat"
127.0.0.1:6379> get animal
(nil)
127.0.0.1:6379> set user:Lucy "Hello World"
OK
127.0.0.1:6379> get user:Lucy
"Hello World"
127.0.0.1:6379> 

```

###2.列表（List）相关操作
```
lpush/rpush -- 从左/右插入数据
llen -- 返回列表的长度
lrange -- 获取指定长度的数据
ltrim -- 截取一定长度的数据
lpop/rpop -- 移除最左/右的元素并返回
lpushx/rpushx -- key存在的时候才插入数据，不存在时不做任何处理

127.0.0.1:6379> lpush q1 "John" "Cat" "Tom"
(integer) 3
127.0.0.1:6379> llen q1
(integer) 3
127.0.0.1:6379> lrange q1 0 1
1) "Tom"
2) "Cat"
127.0.0.1:6379> lrange q1 0 -1
1) "Tom"
2) "Cat"
3) "John"
127.0.0.1:6379> rpush q1 "Bob"
(integer) 4
127.0.0.1:6379> lrange q1 0 999
1) "Tom"
2) "Cat"
3) "John"
4) "Bob"
127.0.0.1:6379> lpushx q1 "Lily"
(integer) 5
127.0.0.1:6379> lrange q1 0 -1
1) "Lily"
2) "Tom"
3) "Cat"
4) "John"
5) "Bob"
127.0.0.1:6379> lpushx q2 "Lily"
(integer) 0
127.0.0.1:6379> ltrim q1 0 2
OK
127.0.0.1:6379> lrange q1 0 -1
1) "Lily"
2) "Tom"
3) "Cat"
127.0.0.1:6379> lpop q1
"Lily"
127.0.0.1:6379> lrange q1 0 -1
1) "Tom"
2) "Cat"
127.0.0.1:6379> rpop q1
"Cat"
127.0.0.1:6379> lrange q1 0 -1
1) "Tom"
127.0.0.1:6379> 

```

###3.集合（set）相关操作
```
sadd/srem -- 添加/删除元素
sismember -- 判断是否为set的一个元素
smembers -- 返回该集合的所有成员
sdiff -- 返回一个集合与其他集合的差异
sinter -- 返回几个集合的交集
sunion -- 返回几个集合的并集

127.0.0.1:6379> sadd zoo Cat Dog
(integer) 2
127.0.0.1:6379> smembers zoo
1) "Dog"
2) "Cat"
127.0.0.1:6379> srem zoo Cat
(integer) 1
127.0.0.1:6379> srem zoo Cat
(integer) 0
127.0.0.1:6379> sismember zoo Cat
(integer) 0
127.0.0.1:6379> sismember zoo Dog
(integer) 1
127.0.0.1:6379> smembers zoo
1) "Dog"
127.0.0.1:6379> sadd zoo Cat
(integer) 1
127.0.0.1:6379> smembers zoo
1) "Dog"
2) "Cat"
127.0.0.1:6379> sadd zoo1 Cat Cow
(integer) 2
127.0.0.1:6379> smembers zoo1
1) "Cow"
2) "Cat"
127.0.0.1:6379> sdiff zoo zoo1
1) "Dog"
127.0.0.1:6379> sdiff zoo1 zoo
1) "Cow"
127.0.0.1:6379> sinter zoo zoo1
1) "Cat"
127.0.0.1:6379> sunion zoo zoo1
1) "Dog"
2) "Cow"
3) "Cat"
127.0.0.1:6379> 
```

### 散列（Hash）相关操作
```
hset/hget -- 设置/获取散列值
hmset/hmget -- 设置/获取多对散列值
hsetnx -- 如果散列已经存在，则不设置
hkeys/hvals -- 返回所有keys/values
hlen -- 返回散列包含域（field）的数量
hdel -- 删除散列指定的域（field）
hexists -- 判断是否存在

127.0.0.1:6379> hset news:1 title "Title1"
(integer) 1
127.0.0.1:6379> hset news:1 content "Content1"
(integer) 1
127.0.0.1:6379> hget news:1 title
"Title1"
127.0.0.1:6379> hget news:1 content
"Content1"
127.0.0.1:6379> hmget news:1 title content
1) "Title1"
2) "Content1"
127.0.0.1:6379> hmset news:2 title "Title2" content "Content2" is_valid 1
OK
127.0.0.1:6379> hmget news:2 title content is_valid
1) "Title2"
2) "Content2"
3) "1"
127.0.0.1:6379> hkeys news:1
1) "title"
2) "content"
127.0.0.1:6379> hkeys news:2
1) "title"
2) "content"
3) "is_valid"
127.0.0.1:6379> hvals news:1
1) "Title1"
2) "Content1"
127.0.0.1:6379> hvals news:2
1) "Title2"
2) "Content2"
3) "1"
127.0.0.1:6379> hlen news:1
(integer) 2
127.0.0.1:6379> hlen news:3
(integer) 0
127.0.0.1:6379> hlen news:2
(integer) 3
127.0.0.1:6379> hdel news:1 is_valid
(integer) 0
127.0.0.1:6379> hdel news:2 is_valid
(integer) 1
127.0.0.1:6379> hlen news:2
(integer) 2
127.0.0.1:6379> hexists news:2 is_valid
(integer) 0
127.0.0.1:6379> hset news:2 isvalid 1
(integer) 1
127.0.0.1:6379> hexists news:2 is_valid
(integer) 0
127.0.0.1:6379> hset news:2 is_valid 1
(integer) 1
127.0.0.1:6379> hexists news:2 is_valid
(integer) 1
127.0.0.1:6379> 

```