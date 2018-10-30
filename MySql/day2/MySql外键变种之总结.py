"""
一对一

#用户表
create table userinfo1(
    id int auto_increment primary key,
    name char(10),
    gender char(10),
    email varchar(64)
)engine=innodb default charset=utf8;

#登录表
create table admin(
    id int not null auto_increment primary key,
    username varchar(64) not null,
    password varchar(64) not null,
    user_id int not null,
    unique uq_u1(user_id),
    constraint fk_admin_u1 foreign key (user_id) references userinfo1(id) #关联外键
)engine=innodb default charset=utf8;
"""

"""
多对多
create table userinfo2(
    id int auto_increment primary key,
    name char(10),
    gender char(10),
    email varchar(64)
)engine=innodb default charset=utf8;

create table host(
    id int auto_increment primary key,
    hostname char(64)
    
)engine=innodb default charset=utf8;

create table user2host(
    id int auto_increment primary key,
    userid int not null,
    hostid int not null,
    unique uq_user_host(userid,hostid),
    constraint fk_u2h_user foreign key (userid) references userinfo2(id),
    constraint fk_u2h_host foreign key (hostid) references host(id)
)engine=innodb default charset=utf8;
 

"""
