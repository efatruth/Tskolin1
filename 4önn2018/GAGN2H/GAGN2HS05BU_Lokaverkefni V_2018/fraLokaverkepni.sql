create database 0301865919_GagLokaverkefni;
use 0301865919_GagLokaverkefni;

create table membership(
mem_num int not null primary key,
mem_fname varchar(30),
mem_lname varchar(30),
mem_street varchar(30),
mem_state varchar(30),
mem_city varchar(30),
mem_zip varchar(5),
mem_balance int
);

drop table membership;

create table price(
price_code int(1) not null primary key,
price_description varchar(30),
price_rent_fee int(2),
price_daily_late_fee int
);

drop table price;

create table rental(
rent_num int(4) not null,
rent_date date,
price_rent_fee int(3),
mem_num int not null,
foreign key (mem_num) references membership(mem_num)
);

create table movie(
mem_num int(4) not null primary key,
movie_title varchar(30),
movie_year int(4),
movie_cost int(2),
movie_genre varchar(30),
price_code int(1) not null,
foreign key(price_code) references price(price_code)
);

create table video(
vid_num int(5) not null primary key,
vid_indate date,
price_rent_fee int,
movie_num int(4) not null,
foreign key (movie_num) references movie(movie_num)
);

create table detail_rental(
rent_num int(4) not null,
vid_num int(5) not null,
detail_fee int(2),
detail_due_date date,
detail_return_date date,
detail_daily_late_fee int(2),
foreign key (rent_num)references rental(rent_num),
foreign key(vid_num) references video(vid_num)
);

insert into membership values
(102, 'Tami','Dawson','2632 Takli Circle','Norene','TN','37136',11),
(103, 'Curt','Knight','4025 Cornell Court','Flatgap','KY','41219',6),
(104, 'Jamal','Melendez','788 East 145th Avenue','Quebeck','TN','38579',0),
(105, 'Iva','Mcclain','6045 Musket Ball Circle','Summit','KY','42783',15),
(106, 'Miranda','Parks','4469 Maxwell Place','Germantown','TN','38183',0),
(107, 'Rosario','Elliott','7578 Danner Avenue','Columbia','TN','38402',5),
(108, 'Mattie','Guy','4390 Evergreen Street','Lily','KY','40740',0),
(109, 'Clint','Ochoa','1711 Elm Street','Greeneville','TN','37745',10),
(110, 'Lewis','Rosales','4524 Southwind Circle','Counce','TN','38326',0),
(111, 'Stacy','Mann','2789 East Cook Avenue','Murfreesboro','TN','37132',8),
(112, 'Luis','Trujillo','7267 Melvin Avenue','Heiskell','TN','37754',3),
(132, 'Minnie','Gonzales','6430 Vasili Drive','Williston','TN','38076',0);

select * from membership;


insert into price values
(1,'Standard',2,1),
(2,'New Release',3.5,3),
(3,'Discount',1.5,1),
(4,'Weekly Special',1,.5);

select * from price;


insert into rental values
(1001,'2009-03-01',null,103),
(1002,'2009-03-02',null,105),
(1003,'2009-03-02',null,102),
(1004,'2009-03-02',null,110),
(1005,'2009-03-02',null,111),
(1006,'2009-03-02',null,107),
(1007,'2009-03-02',null,104),
(1008,'2009-03-03',null,105),
(1009,'2009-03-03',null,111);

select * from rental;


insert into movie values
(1234,'The Cesar Family Christmas',2007,39.95,'FAMILY',2),
(1235,'Smokey Mountain Wildlife',2004,59.95,'ACTION',1),
(1236,'Richard Goodhope',2008,59.95,'DRAMA',2),
(1237,'Beatnik Fever',2007,29.95,'COMEDY',2),
(1238,'Constant Companion',2008,89.95,'DRAMA',2),
(1239,'Where Hope Dies',2008,25.49,'DRAMA',3),
(1245,'Time to Burn',2005,45.49,'ACTION',1),
(1246,'What He Doesnt Know',2006,58.29,'COMEDY',1);

select * from movie;


insert into video values
(54321,'2008-06-08',null,1234),
(54324,'2008-06-08',null,1234),
(54325,'2008-06-08',null,1235),
(34341,'2007-01-22',null,1235),
(34342,'2007-01-22',null,1236),
(34366,'2009-03-02',null,1236),
(34367,'2009-03-02',null,1236),
(34368,'2009-03-02',null,1236),
(34369,'2009-03-02',null,1237),
(44392,'2008-10-21',null,1237),
(59237,'2009-02-14',null,1237),
(61388,'2007-01-25',null,1239),
(61353,'2006-01-28',null,1245),
(61354,'2006-01-28',null,1246),
(61367,'2008-07-30',null,1246),
(61369,'2008-07-30',null,1246);

select * from video;

insert into detail_rental values
(1001, 34342, 2, '2009-03-04','2009-03-02',1),
(1001, 61353, 2, '2009-03-04','2009-03-03',1),
(1002, 59237, 3.5, '2009-03-04','2009-03-04',3),
(1003, 54325, 3.5, '2009-03-04','2009-03-09',3),
(1003, 61369, 2, '2009-03-06','2009-03-09',1),
(1003, 61388, 0, '2009-03-06','2009-03-09',1),
(1004, 44392, 3.5, '2009-03-05','2009-03-07',3),
(1004, 34367, 3.5, '2009-03-05','2009-03-07',3),
(1004, 34341, 2, '2009-03-07','2009-03-07',1),
(1005, 34342, 2, '2009-03-07','2009-03-05',1),
(1005, 44397, 3.5, '2009-03-05','2009-03-05',3),
(1006, 34366, 3.5, '2009-03-05','2009-03-04',3),
(1006, 61367, 2, '2009-03-07',null,1),
(1007, 34368, 3.5, '2009-03-05',null,3),
(1008, 34369, 3.5, '2009-03-05','2009-03-05',3),
(1009, 54324, 3.5, '2009-03-05',null,3),
(1001, 34366, 3.5, '2009-03-04','2009-03-02',3);


select * from detail_rental;
drop table detail_rental;


SELECT * FROM membership WHERE mem_fname LIKE ‘M’;
                               
#1
select movie_title,movie_year,movie_cost from movie where movie_title like '%hope%'order by movie_title;

#2
select movie_title,movie_year,movie_genre from movie where movie_genre = 'ACTION';

#3
select movie_title,movie_year,movie_cost from movie where movie_COS >;


#3
select movie_title,movie_year,movie_cost from movie where movie_title like '%hope%' order by movie_title asc;

#4
select movie_title,movie_year,movie_genre from movie where movie_genre = 'ACTION';

#5
select movie_title,movie_year,movie_cost from movie where movie_cost > 40 order by movie_title;

#6
select movie_num, movie_title, movie_cost,movie_genre from movie where movie_genre like 'ACTION' and movie_cost < 50 or movie_genre like 'COMEDY' and movie_cost < 50 order by movie_genre asc;

#7
select movie_num, concat(movie_title,'(',movie_year,')',movie_genre) as 'Movie Description' from movie;

#8
select movie_genre, count(movie_title) as 'Number of movies' from movie group by movie_genre;

#9
select avg(movie_cost) as 'Average cost' from movie;

#10
select movie_genre, round(avg(movie_cost),2) as 'Average cost' from movie group by movie_genre;

#11?
select movie.movie_title, movie.movie_genre, price.price_description,price.price_rent_fee 
from movie,price where price.price_code = movie.price_code order by price.price_code;

#12?
select movie.movie_genre, round(avg(price.price_rent_fee),2) from price, movie where price.price_code = movie.price_code group by movie.movie_genre;

#13?
select movie.movie_title,movie.movie_year,round(movie.movie_cost/price.price_rent_fee, 2) as 'Breakeven' from movie, price where price.price_code = movie.price_code;

#14
select movie_title,movie_year from movie where price_code !=0;

#15
select movie_title,movie_year,movie_cost from movie where movie_cost > 44.99 and movie_cost < 49.99 order by movie_title;

#16?
select movie.movie_title,movie.movie_year,price.price_description,price.price_rent_fee, movie_genre 
from movie,price where movie.movie_genre like 'FAMILY' or movie.movie_genre like 'COMEDY' or movie.movie_genre like 'DRAMA'
and movie.price_code = price.price_code group by movie.movie_title;

#17
select min(membership.mem_balance) as 'Minimum', max(membership.mem_balance) as 'Maximum', avg(membership.mem_balance) as 'average' from membership,rental where membership.mem_num = rental.mem_num;

#18
select concat(mem_fname, '',mem_lname) as 'Name', concat(mem_street,' ',mem_city,' ',mem_state,' ',mem_zip) as 'address' from membership;

#19?
select rental.rent_num, rental.rent_date, video.vid_num, movie.movie_title, detail_rental.detail_due_date, detail_rental.detail_return_date from 
rental,video,movie,detail_rental where rental.rent_num = detail_rental.rent_num and detail_rental.vid_num = video.vid_num 
and video.movie_num = movie.movie_num and detail_return_date > detail_due_date order by rental.rent_num, movie.movie_title;

#20?
select rental.rent_num, rental.rent_date, video.vid_num, movie.movie_title, detail_rental.detail_due_date, detail_rental.detail_return_date,datediff(detail_rental.detail_return_date, detail_rental.detail_due_date) as 'Days late'from 
rental,video,movie,detail_rental where rental.rent_num = detail_rental.rent_num and detail_rental.vid_num = video.vid_num 
and video.movie_num = movie.movie_num and detail_return_date > detail_due_date order by rental.rent_num, movie.movie_title;

#21?
select rental.rent_num, rental.rent_date, movie.movie_title, detail_rental.detail_fee from rental,video,movie,detail_rental where rental.rent_num = detail_rental.rent_num and detail_rental.vid_num = video.vid_num 
and video.movie_num = movie.movie_num and detail_return_date <= detail_due_date;

#22?
select membership.mem_num, membership.mem_lname,membership.mem_fname, sum(detail_rental.detail_fee) from membership,detail_rental,rental
where rental.rent_num = detail_rental.rent_num and membership.mem_num = rental.mem_num group by membership.mem_num,membership.mem_lname,membership.mem_fname;

#23
select movie.movie_num, movie.movie_genre,round(avg(movie.movie_cost),2), ((avg(movie.movie_cost) - movie.movie_cost) / avg(movie.movie_cost)* 100) from
movie,video where movie.movie_num = video.movie_num group by movie.movie_num,movie_genre;

select avg(movie.movie_cost),movie.movie_cost, ((avg(movie.movie_cost)-movie.movie_cost)/ avg(movie.movie_cost)*100) from movie group by movie_num, movie_genre;

select movie_num,a.movie_genre, avg(movie_cost) as 'Avg Cost', movie_cost,
((movie_cost - avg(movie_cost)) /avg(movie_cost)*100) as 'percent difference'
from movie a, (select movie_genre,avg(movie_cost) from movie group by movie_genre)s
where a.movie_genre = s.movie_genre;

#24
alter table detail_rental add column detail_dayslate int(3);

#25
alter table video add column vid_status char(4) not null default 'IN';

#26?
update video,detail_rental set video.vid_status = 'IN' where detail_rental.detail_return_date IS NULL;

#27
alter table price add column price_rentdays int(2) not null default 3;

#28?
update price set price_rentdays = 5 where price_code = 1;
update price set price_rentdays = 5 where price_code = 3;
update price set price_rentdays = 7 where price_code = 4;

#29?
delimiter //
#3.2
create procedure pre_new_rental(mem_number int)
BEGIN

alter table rental add row price_rentdays int(2) not null default 3;

update deptsal set totalsalary = (select sum(salary) from employee where dept_no = dept_num) where dept_num = deptnum;
end
//
