"""
数据类型

数字:
int
tinyint
bigint
float
double
decimal   0.1 (精确的小数)


字符串(最高255)
char(10)  不管够不够都占10个 速度快
varchar(10) 实际存储多少就多少 节省空间

65535
text

数据表优化：定长列往前放，变长列往后放


上传文件：
文件存硬盘  数据库存路径


时间格式：
datatime(常用)


枚举
create table shirts(
name Varchar(40),
size enum('x-small','small','medium','large','x-larhe')
);
insert into shirts(name,size) values('123','large')

"""

"""
操作文件中的内容
1、插入数据
insert into t1(id,name)values(1,'alex');
2、删除
delete from t1 where id <6
3、修改
update t1 set age =18;
update t1 set age=18 where age=17;

查看数据:
select *from t1



外键：节省空间 约束保证数据一致性
create table userinfo(
uid int auto_increment primary key,
name varchar(32),
department_id int,
constraint fk_user_depar foreign key('department_id',) references department('id')
)engine=innodb default charset=utf8;

create table department(
id bigint auto_increment primary key,
title char(15)
)engine=innodb default charset=utf8;
"""
