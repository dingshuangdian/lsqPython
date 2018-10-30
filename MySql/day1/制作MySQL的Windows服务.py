"""
windows服务

安装mysql服务:mysqld --install
卸载mysql服务:mysql --remove
启动服务:net start mysql

停止服务：net stop mysql



2、关于连接

文件夹【数据库】
    文件【表】
        数据行【行】
        数据行【行】
        数据行【行】

连接:
默认用户：root
创建：
create user 'alex'@'192.168.1.1' identified by '123123';
create user 'alex'@'192.168.1.%' identified by '123123';
create user 'alex'@'192.168.%' identified by '123123';
create user 'alex'@'%' identified by '123123';
授权：
    权限是什么  人是谁
    grant select,insert,update on db1.* to 'alex'@'%';
    grant all privileges on db1.t1 to 'alex'@'%';  #所有权限

    select *from 表名;
    select name,age,host from user;

"""
