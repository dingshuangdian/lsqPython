"""
今日内容:
0、唯一索引（加速查找）
create table t1(
id int,
num int,#身份证号
xx int,
unique qu1(num,xx)  #身份证不能重复，num是唯一的  (两个联合唯一)
)

1 1 1
2 1 2 num xx不能完全一样
唯一:约束不能重复，可以为空
主键:主键不能重复，不能为空

加速查找

1、外键的变种

a、用户表和部门表
用户:1 alex      1
    2、root      1
    3、egon      2
    4、laoyao    3

部门:
    1、服务
    2、保安
    3、公关


"""
