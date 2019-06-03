-- 新建数据库
CREATE DATABASE `school` CHARSET `utf8`;

-- 使用数据库
USE `school`;
-- 创建数据库表
CREATE TABLE `students`(
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name` VARCHAR(20) NOT NULL,
  `nickname` varchar(20) NULL,
  `sex` CHAR(1) NULL,
  `in_time` DATETIME NULL
);

-- 插入数据
INSERT INTO `students` VALUE (1,'小强','强哥','男',now());

INSERT INTO `students`(`name`,`nickname`,`sex`,`in_time`) VALUE ('小强','强哥','男',now());

INSERT INTO `students`(`name`,`nickname`) VALUES
  ('小强1','强哥1'),
  ('小强2','强哥2'),
  ('小强3','强哥3'),
  ('小强4','强哥4');

-- 查询数据
SELECT `id`,`name`,`nickname` FROM `students` WHERE `sex`='男' ORDER BY `id` ASC LIMIT 0,2;

-- 修改数据
update `students` set `sex`='女' where `sex` = '男';
update `students` set `sex`='女',`nickname`='没有';
update `students` set `sex`='男' where `id` > 3;

-- 删除数据
delete from `students` where `sex` = '男';