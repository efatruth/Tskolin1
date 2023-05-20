#livinus felix bassey

#1
create database 0301865919_company;
use 0301865919_company;

#2
create table dept
(
  dept_no int not null,
  dept_name varchar(100) not null,
  dept_location varchar(100) not null,
  primary key (dept_no)
);

create table employee 
(
  emp_id int not null,
  emp_name varchar(100) not null,
  mgr_emp_id int,
  dept_no int not null,
  salary  double  not null,
  primary key (emp_id),
  key employee_mgr_emp_id (mgr_emp_id),
  foreign key fk_employee_dept_dept_no (dept_no) references dept (dept_no) on delete no action on update no action
);

create table deptsal
(
 dept_no int not null,
 totalsalary int
);

insert into dept values 
(1, 'Dept-1', 'Chicago'), 
(2, 'Dept-2', 'London'),
(3, 'Dept-3', 'Reykjavik'),
(4, 'Dept-4', 'Rabat');


insert into employee values 
(1, 'Clark Mgr', null, 1, 450000),
(2, 'Cameron Emp', 2, 1, 300000),
(3, 'Charlie Emp', 3, 1, 500000),
(4, 'Layton Emp', null, 2, 250000),
(5, 'Linda Emp', null, 2, 370000),
(6, 'Mikel Mor', null, 3, 290000),
(7, 'Mic Coleman', null, 3, 400000),
(8, 'Doud Valantino', null, 3, 300000);


insert into deptsal values
(1,   			0),
(2,   			0),
(3,   			0),
(4,   			0);

select * from employee;
select * from dept;
select * from deptsal;

#3.1
delimiter //
#3.2
create procedure updateSalary(deptnum int)
BEGIN
update deptsal set totalsalary = (select sum(salary) from employee where dept_no = deptnum) where dept_no = deptnum;
end
//
#3.3
delimiter ;
#3.4
call updateSalary(1);
call updateSalary(2);
call updateSalary(3);
call updateSalary(4);
#3.5
select * from deptsal;
#4
show procedure status;
#5
drop procedure updateSalary;
#6
update deptsal set totalSalary = 0;

#7
delimiter //
CREATE PROCEDURE updateAll ()
BEGIN
	DECLARE v INT;
    SET i = 0;
    WHILE i <=4 DO
		UPDATE deptsal set totalsalary = (select sum(salary) from employee where dept_no = i) where dept_no = i;
        SET i = i + 1;
END WHILE;
END;
//
delimiter;
call updateAll();

#9
delimiter //
create procedure raise()
BEGIN
update employee set salary = salary + (salary * 0.1);
end
//
delimiter ;        
call raise();