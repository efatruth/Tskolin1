/* answer 1**/
select * from customers;

/* answer 2**/
select * from customers;

/* answer 3**/
select id, name, address from shippers;

/* answer 4**/
select * from invoices group by orderid;

/* answer 5**/
select * from orders where order_date = '1-March 2006';

/* answer 6**/
select * from orders where order_date < '1-March 2006';

/* answer 7**/
select * from orders where payment_type is not null and suppliers like 'supplier B' group by employee_id;

/* answer 8**/
select * from products where standard_cost > 10 and listprice < 20 group by productname;

/* answer 9**/
select * from orders where paid_date is null group by customer_id;

/* answer 10**/
select * from customers where city like 'New York' group by job_title, last_name;