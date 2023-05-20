select * FROM p;

set autocommit = 0;
update p
	set p_qoh = 10
    where p_code = "11OER/31";
    
    select * from p;
    
    
create table T20(
name varchar(20)
);

insert into t20 values ("Dude");

select * from t20;

start transaction;
update t20
	set name = "livinus"
where name like "jon%"
