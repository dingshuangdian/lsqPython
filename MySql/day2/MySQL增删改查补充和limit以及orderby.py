# MySQL增删改查补充和limit以及order by

"""
SQL语句数据行的操作补充



增
insert into tb(name,age) values('alex',12);
insert into tb(name,age) values('alex',12),('root',18);

表二插入表一数据
insert into tb12(name,age) select name,age from tb11;

删

delete from tb12;
delete from tb12 where id =2


改
update tb12 set name='alex',age=19 where id>12 and name='xx';


查
select *from tb12;
select id ,name from tb12;
select id ,name as cname from tb12; #as 代表取别名

select id ,name,from tb12 where id >10 or name='alex';

select name,age,11 from tb12;

条件 where:
不等于:!= <>

select *from tb12 where id in(1,5,12);#查询1，5，12的id
select *from tb12 where id not in(1,5,12);#不查询1，5，12的id
select *from tb12 where id between 5 and 12;#查询5，12


select *from tb12 where id in(select id from tb11);

#通配符
以a开头:
a% :a后边有任意多个字符
a_:a后面只能有一个位置
%a%

select *from tb12 where name like "a%";
select *from tb12 where name like "a_";

#分页
select *from tb12 limit 2;
select *from tb12 limit 1,2;  #从1开始往后取2条

排序：
select *from tb12 order by id desc;#根据id从大到小排序
select *from tb12 order by id asc;#根据id从小到大排序

select *from tb12 order by id desc limit 10;

"""
