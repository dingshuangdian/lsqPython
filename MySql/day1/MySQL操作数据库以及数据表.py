"""
学习sql语句规则

操作文件夹
create database db2 default charset utf8;
show databases;
drop database db2; #删除库

操作文件
show tables;
create table t1(id int,name char(10)) default charset=utf8;


create table t1(
#列名 类型 null(是否可以为空);
#列名 类型 not null(是否可以为空);
#列名 类型 null(是否可以为空) default 1;
#列名 类型 null(是否可以为空) auto_increment(自增)primary key;
id int,
name char(10)
) engine=innodb default charset=utf8; #引擎
innodb 支持事务，原子性操作
select *from t1;

auto_increment:表示自增
primary key：表示约束（不能重复且不能为空）；加速查找

#正确创建表的方式

create table t1(
#列名 类型 null(是否可以为空);
#列名 类型 not null(是否可以为空);
#列名 类型 null(是否可以为空) default 1;
#列名 类型 null(是否可以为空) auto_increment(自增)primary key;
id int not null  auto_increment primary key,  #自增列
name char(10)
) engine=innodb default charset=utf8;

#清空表
delete from t1;
truncate table t1; 效率高

删除表：
drop table t1;

操作文件中的内容
插入数据
insert into t1(id ,name) values(1,'alex');
查看数据
select *from t1;
"""
