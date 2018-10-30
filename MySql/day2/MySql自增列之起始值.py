"""
对于自增

desc t10;
show create table t10;  #查看表怎么创建
show create table t10 \G; #格式化

alter table t10 AUTO_INCREMENT=20;#修改自增的值

MySql:自增步长
基于会话级别
show session variables like 'auto_inc%'; 查看全局变量
set session auto_increment_increment=2; #设置会话的步长
set session auto_increment_offset=2;#设置起始值


基于全局级别
show globle variables like 'auto_inc%';
set globle auto_increment_increment=2;
set globle auto_increment_offset=2;

sqlServer:自增步长
基于表级别
"""
