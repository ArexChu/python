#create table blog(
#title varchar(50),
#date varchar(15),
#read_num int,
#comment_num int,
#recommend int
#);

#insert into blog values('XGBoost类库使用小结','2019年7月1日',32912,119,14);
#insert into blog values('XGBoost算法小结原理','2019年6月5日',37969,181,18);
#update blog set comment_num=1 where comment_num=119;
#delete from blog where comment_num=1;

#关联查询（多个表查询）left join（左关联）inner join（内关联）right join（右关联）

#create table student(
#name varchar(15),
#sex varchar(15),
#phone int
#);
#
#create table score(
#name varchar(15),
#score int
#);

#insert into student values('alice','f',111);
#insert into student values('bob','m',121);
#insert into score values('alice','98');
#insert into score values('david','99');

select * from student left join score on student.name = score.name;

#select * from student right join score on student.name = score.name;

#select * from student inner join score on student.name = score.name;
