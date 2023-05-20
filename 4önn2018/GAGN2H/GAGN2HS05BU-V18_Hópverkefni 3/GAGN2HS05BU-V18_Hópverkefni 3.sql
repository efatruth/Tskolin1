use 0301865919_THEMEPARK;
SET autocommit = 0;

select * from EMPLOYEE;

#1.query that lists the names and dates of births of all employees born on the 14th day of the month. 
select EMP_LNAME, EMP_FNAME, EMP_DOB
from EMPLOYEE
where day(EMP_DOB) = "14";

#2.query which lists the approximate age of the employees on the company’s tenth anniversary date (11/25/2008).
select avg (round(datediff(curdate(),EMP_DOB)/324)) FROM employee, attraction WHERE DATE;

#3
select concat(substr(EMP_PHONE,1,3), lower(substr(EMP_FNAME,1,2))) as 'user_password' from employee;

#4
select distinct date_format(SALES.SALE_DATE, '%D %M %Y') as 'last_ticket', themepark.PARK_NAME from SALES, themepark;


#5
update employee set EMP_PHONE = concat('354',substr(EMP_PHONE,4)) where EMP_PHONE like '324%';
rollback;

#6
select * from employee where length(EMP_FNAME) >=8;

#7
select * from employee where DAY(EMP_HIRE_DATE) < 7;

#8
select concat(upper(EMP_FNAME),' ',upper(EMP_LNAME)) as 'employee name 'from employee;

#9
select concat(lower(EMP_FNAME),' ',lower(EMP_LNAME)) as 'employee name 'from employee;

#10
select EMP_FNAME, substr(EMP_PHONE,1,3) FROM employee;

#11
select concat(substr(EMP_FNAME,1,1), substr(EMP_LNAME,1,7)) as user_ID FROM employee;

#12
select EMP_NUM,EMP_FNAME, month(EMP_HIRE_DATE) from employee;

#13?
alter table employee add column(EMP_EMAIL varchar(30));

insert into employee(EMP_MAIL) select (concat(substr(EMP_FNAME,1,2), '@tskol.is')) from employee;

#14
select EMP_NUM, EMP_EMAIL from employee;


#15
SELECT EMP_LNAME, LENGTH(EMP_LNAME) AS LengthOfName 
FROM employee 
ORDER BY LengthOfName DESC; 

#16
SELECT MIN(EMP_LNAME), LENGTH(EMP_LNAME) AS MLengthOfLName
FROM employee 
ORDER BY MLengthOfLName; 

#17
SELECT EMP_FNAME 'Name', LENGTH(EMP_FNAME)'LengthOfName'
FROM employee
where EMP_FNAME like 'A%' 
OR EMP_FNAME like 'D%' 
OR EMP_FNAME like'R%'
order by EMP_FNAME;

 
