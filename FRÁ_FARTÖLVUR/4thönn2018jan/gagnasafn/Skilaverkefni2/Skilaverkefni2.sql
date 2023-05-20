create database 0301865919_skilaverkefni2;
use 0301865919_skilaverkefni2;
SET autocommit = 0;

create table EMPLOYEE(
	EMP_NUM CHAR(3) PRIMARY KEY,
    EMP_LNAME VARCHAR(15),
    EMP_FNAME VARCHAR(15),
    EMP_INITIAL CHAR(1),
    EMP_HIREDATE DATE,
    JOB_CODE CHAR(3),
    EMP_YEARS INT(2),
    foreign key (JOB_CODE) references JOB(JOB_CODE)
);

insert into EMPLOYEE values
('101', 'News', 'John', 'G', '2000.11.08', '502', 4),
('102', 'Senior', 'David', 'H', '1989.07.12', '501', 15),
('103', 'Arbough', 'June', 'E', '1996.12.01', '503', 8),
('104', 'Ramoras', 'Anne', 'K', '1987.11.15', '501', 17),
('105', 'Johnson', 'Alice', 'K', '1993.02.01', '502', 12),
('106', 'Smithfield', 'william', '', '2004.06.22', '500', 0),
('107', 'Alonzo', 'Maria', 'D', '1993.10.10', '500', 11),
('108', 'Washington', 'Ralph', 'B', '1991.08.22', '501', 13),
('109', 'Smith', 'Larry', 'W', '1997.07.18', '501', 7);

select * from EMPLOYEE;


create table PROJECT(
	PROJ_NUM CHAR(3) PRIMARY KEY,
    PROJ_NAME VARCHAR(15),
    PROJ_VALUE INT,
    PROJ_BALANCE INT,
    EMP_NUM CHAR(3),
    foreign key (EMP_NUM) references EMPLOYEE(EMP_NUM)
);

insert into PROJECT values
(15, 'Evergreen', 1453500.00, 1002350.00, '103'),
(18, 'Amber Wave', 3500500.00, 2110346.00, '108'),
(22, 'Rolling Tide', 1453500.00, 500345.20,'102'),
(25, 'Starflight', 1453500.00, 2309880.00, '107');

select * from PROJECT;


#??
create table ASSIGNMENT(
	ASSIGN_NUM CHAR(3),
	ASSIGN_DATE DATE,
    PROJ_NUM CHAR(3),
    EMP_NUM CHAR(3),
    ASSIGN_JOB CHAR(3),
    ASSIGN_CHG_HR DECIMAL(5,2),
    ASSIGN_HOURS DECIMAL(2,2),
    ASSIGN_CHARGE DECIMAL(5,2)
);

#??
insert into ASSIGNMENT values
(1001, '2007.03.22', '18', '103', '503', 84.50, 3.5, 295.75),
(1002, '2007.03.22', '22', '117', '509', 34.55, 4.2, 145.11),
(1003, '2007.03.22', '18', '117', '509', 34.55, 2.0, 69.10),
(1004, '2007.03.22', '18', '103', '503', 84.50, 5.9, 498.55),
(1005, '2007.03.22', '25', '108', '501', 96.75, 2.2, 212.85);

#??
select * from ASSIGNMENT;


create table JOB(
    JOB_CODE CHAR(3) PRIMARY KEY,
    JOB_DESCRIPTION VARCHAR (30),
    JOB_CHG_HOUR DECIMAL(5,2),
    JOB_LAST_UPDATE DATE,
    foreign key (JOB_CODE) references JOB(JOB_CODE)
);

insert into JOB values
('500', 'programmer', 35.75, '2006.11.20'),
('501', 'System Analyst', 96.75, '2006.11.20'),
('502', 'Database Designer', 125.00, '2007.03.24'),
('503', 'Electrical Engineer', 84.50, '2007.11.20');

select * from JOB;

#1
create table EMP_1(
	EMP_NUM CHAR(3),
    EMP_LNAME VARCHAR(15),
    EMP_FNAME VARCHAR(15),
    EMP_INITIAL CHAR(1),
    EMP_HIREDATE DATE,
    JOB_CODE CHAR(3),
    foreign key(JOB_CODE) references JOB(JOB_CODE)
);

#2 ?touching,changes
insert into EMPLOYEE values
('101', 'News', 'John', 'G', '2000.11.08', '502'),
('102', 'Senior','David', 'H', '1989.07.12', '501');

#3
select * from EMP_1 where JOB_CODE like '502';

#4
commit;

#5
select * from EMP_1;
update EMP_1 set JOB_CODE = '501' where EMP_NUM like '107';
rollback;

#6
delete from EMP_1 where EMP_FNAME like 'william' and EMP_LNAME like 'Smithfield' and EMP_HIREDATE like '2004-06-22' and JOB_CODE like '500';

#7
rollback;

#8
create table EMP_2 as select * from EMP_1;
#you can also use this code: select * into EMP_2 from EMP_1;
alter table EMP_2 add column (EMP_PCT DECIMAL(4,2));
alter table EMP_2 add column (PROJ_NUM CHAR(3));

select * from EMP_2;

#9
update EMP_2 set EMP_PCT = 3.85 where EMP_NUM like '103';
update EMP_2 set EMP_PCT = 5.00 where EMP_NUM like '101';
update EMP_2 set EMP_PCT = 8.00 where EMP_NUM like '102';
update EMP_2 set EMP_PCT = 10.00 where EMP_NUM like '104';
update EMP_2 set EMP_PCT = 5.00 where EMP_NUM like '105';
update EMP_2 set EMP_PCT = 6.20 where EMP_NUM like '106';
update EMP_2 set EMP_PCT = 5.15 where EMP_NUM like '107';
update EMP_2 set EMP_PCT = 10.00 where EMP_NUM like '108';
update EMP_2 set EMP_PCT = 2.00 where EMP_NUM like '109';

#10
update EMP_2 set PROJ_NUM = '18' where JOB_CODE like '500';

#11
update EMP_2 set PROJ_NUM = '25' where JOB_CODE >= '502';

#12
update EMP_2 set PROJ_NUM = '14' where EMP_HIREDATE < '1994.01.01' and JOB_CODE > '500';


#13.
#a.
create table TEMP_1 as select EMP_NUM, EMP_PCT from EMP_2;

#b.?? NOT Functioning according to the question
select EMP_NUM, EMP_PCT into TEMP_1 from EMP_2;



#14
drop table TEMP_1;

#15
select * from EMPLOYEE where EMP_LNAME like 'Smith%';

#16 ?not functioning according to question
select EMPLOYEE.EMP_LNAME,EMPLOYEE.EMP_FNAME,EMPLOYEE.EMP_INITIAL,PROJECT.PROJ_NAME,PROJECT.PROJ_VALUE,PROJECT.PROJ_BALANCE,JOB.JOB_CODE,JOB.JOB_DESCRIPTION,JOB.JOB_CHG_HOUR
from ((EMPLOYEE
inner join PROJECT on EMPLOYEE.EMP_NUM=PROJECT.PROJ_NUM)
inner join JOB on EMPLOYEE.JOB_CODE=JOB.JOB_CODE);


#17
create view rep_1 as select PROJECT.PROJ_NAME, PROJECT.PROJ_VALUE, PROJECT.PROJ_BALANCE, EMPLOYEE.EMP_LNAME, EMPLOYEE.EMP_FNAME, EMPLOYEE.EMP_INITIALS, JOB.JOB_CODE, JOB.JOB_DESCRIPTION, JOB.JOB_CHG_HOUR
from PROJECT, EMPLOYEE, JOB;

#18
select avg(EMP_PCT) from EMP_2;

#19
select * from EMP_2 group by EMP_PCT
order by EMP_PCT asc;

#20
select distinct PROJ_NUM 
from EMP_2 ;

#21
#22
#23
#24
#25