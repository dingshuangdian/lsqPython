"""
Day57

约法三章：
	1. 课下不看视频
	2. 笔记梗概
	3. 课下整理上课内容

课程安排：
	MySQL
	Web框架：
		- Python
		- 前端
		- MySQL
	项目实战：
		- 简单CURD
		- 保障系统（博客+BBS+后台管理）
		- CMDB资产管理
		- CRM
		- 堡垒机
	爬虫:
		- Scrapy
	其他：
		...

MySQL

	单机程序（自己DB）

	单机程序（公用DB）

	MySQL：是用于管理文件的一个软件
		- 服务端软件
			- socket服务端
			- 本地文件操作
			- 解析指令【SQL语句】
		- 客户端软件（各种各样）
			- socket客户端
			- 发送指令
			- 解析指令【SQL语句】

		PS:
			- DBMS数据库管理系统
			- SQL语句

	技能：
		- 安装 服务端和客户端
		- 连接
		- 学习SQL语句规则；指示服务端做任意操作


	其他类似软件：
		关系型数据库：sqllite,db2,oracle,access,sql server MySQL
		非关系型数据库：MongoDB,redis


1. MySQL安装

	Windows:
		可执行文件
			点点点
		压缩包
			放置任意目录
			初始化
				服务端：E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin\mysqld --initialize-insecure
					    # 用户名 root 密码：空
			启动服务端：
				E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin\mysqld\mysqld

			客户端连接：
				E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin\mysqld\mysql -u root -p

				发送指令：
					show databases;
					create database db1;

			环境变量的配置：
				E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin
				mysqld

			windows服务：
				E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin\mysqld --install
				net start MySQL

				E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\bin\mysqld --remove

				net start MySQL
				net stop MySQL

2. 关于连接

	文件夹【数据库】
		文件【表】
			数据行【行】
			数据行
			数据行

	连接：

		默认：用户root


		show databases;

		use 数据库名称;

		show tables;

		select * from 表名;

		select name,age,id from 表名;

		mysql数据库user表
		use mysql;
		select user,host from user;


		创建用户：
			  create user 'alex'@'192.168.1.1' identified by '123123';
			  create user 'alex'@'192.168.1.%' identified by '123123';
			  create user 'alex'@'%' identified by '123123';
		授权：
			  权限  人

			  grant select,insert,update  on db1.t1 to 'alex'@'%';
			  grant all privileges  on db1.t1 to 'alex'@'%';

			  revoke all privileges on db1.t1 from 'alex'@'%';

		DBA: 用户名密码


3. 学习SQL语句规则

	操作文件夹
		create database db2;
		create database db2 default charset utf8; *****
		show databases;
		drop database db2;

	操作文件
		show tables;
		create table t1(id int,name char(10)) default charset=utf8;
		create table t1(id int,name char(10))engine=innodb default charset=utf8;
		create table t3(id int auto_increment,name char(10))engine=innodb default charset=utf8;  *****

		create table t1(
			列名 类型 null,
			列名 类型 not null,
			列名 类型 not null auto_increment primary key,
			id int,
			name char(10)
		)engine=innodb default charset=utf8;
			# innodb 支持事务，原子性操作
			# myisam myisam

			auto_increment 表示：自增
			primary key：  表示 约束(不能重复且不能为空); 加速查找
			not null: 是否为空
			数据类型：

				数字：
					tinyint
					int
					bigint

					FLOAT
						0.00000100000123000123001230123
					DOUBLE
						0.00000000000000000000100000123000123001230123
						0.00000100000123000000000000000
					decimal
						0.1

				字符串：
					char(10)      速度快()
						root
						root
					varchar(10)   节省空间
						root
					PS: 创建数据表定长列往前放

					text

					上传文件：
						文件存硬盘
						db存路径
				时间类型
					DATETIME

				enum
				set


			create table t1(
				id int signed not null auto_increment primary key,
				num decimal(10,5),
				name char(10)
			)engine=innodb default charset=utf8;

		清空表：
			delete from t1;
			truncate table t1;
		删除表：
			drop table t1;

	操作文件中内容
		插入数据：
			insert into t1(id,name) values(1,'alex');
		删除：
			delete from t1 where id<6
		修改：
			update t1 set age=18;
			update t1 set age=18 where age=17;
		查看数据：
			select * from t1;

	外键：

		create table userinfo(
			uid int auto_increment primary key,
			name varchar(32),
			department_id int,
			xx_id int,
			constraint fk_user_depar foreign key (department_id) references color(id)
		)engine=innodb default charset=utf8;

		create table department(
			id bigint auto_increment primary key,
			title char(15)
		)engine=innodb default charset=utf8;
innodb原子操作

今日内容参考博客：
	http://www.cnblogs.com/wupeiqi/articles/5713315.html
作业：
	http://images2015.cnblogs.com/blog/425762/201608/425762-20160803224643778-2071849037.png
	http://www.cnblogs.com/wupeiqi/articles/5729934.html


"""
