
use 0301865919_THEMEPARK;

select * from EMPLOYEE;


select distinct(SALE_DATE) FROM sales;

#1- Using the date specifiers in the table above, display the date in the format ’Fri – 18 – 5 – 07’. 
select distinct(date_format(SALE_DATE, "%a - %m - %y")) as 'date' FROM sales;

#2- write an SQL query that displays the output shown bellow
select distinct(date_format(SALE_DATE, "%d/%m/%Y")) as sale_date from sales;

#3- write an SQL query that displays the output shown bellow
select distinct(date_format(SALE_DATE, "%a - %D of %b %y")) as sale_date from sales;

#query that displays all employees datas. 
SELECT DAYOFMONTH(EMP_DOB) AS “Day”, MONTH(EMP_DOB) AS “Month”, YEAR(EMP_DOB) AS “Year” 
FROM EMPLOYEE; 

#Write a query that displays all employees who were born in November. 
SELECT EMP_DOB from EMPLOYEE WHERE MONTH(EMP_DOB) = 11;


select datediff('2018-12-25','2018-24-24');
 
#DATE_ADD('2015-01-01', INTERVAL 11 MONTH);
select emp_hire_date, date_add( emp_hire_date, interval 12 month) from emplyee; 
select emp_fname, emp_lname, emp_hire_date, date_add( emp_hire_date, interval 12 month) from emplyee; 


select * from sales;


#exercises:
select EMP_LNAME, EMP_FNAME, EMP_DOB
from EMPLOYEE
where EMP_DOB =