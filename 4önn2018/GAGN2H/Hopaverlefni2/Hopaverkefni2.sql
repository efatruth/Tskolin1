create database 0301865919_SaleCo;			
use 0301865919_SaleCo;

CREATE TABLE VERDOR ( 
VEND_CODE 		INTEGER,  
VEND_CONTACT 	VARCHAR(15) NOT NULL, 
VEND_AREACODE 	CHAR(5) NOT NULL, 
VEND_PHONE 	CHAR(8) NOT NULL,
PRIMARY KEY (V_CODE));

CREATE TABLE PRODUCT (
PROD_CODE 	VARCHAR(10) PRIMARY KEY,
PROD_DESCRIPT 	VARCHAR(35) NOT NULL,
PROD_ON_HAND	INTEGER NOT NULL,
PROD_PRICE 	NUMERIC(8,2) NOT NULL,
INDEX		(V_CODE),


CREATE TABLE CUSTOMER (
CUS_CODE	NUMERIC PRIMARY KEY,
CUS_LNAME	VARCHAR(15) NOT NULL,
CUS_FNAME	VARCHAR(15) NOT NULL,
CUS_INITIAL	CHAR(1),
CUS_AREACODE CHAR(4) DEFAULT '0181' NOT NULL CHECK(CUS_AREACODE IN ('0181','0161','1931')),
CUS_PHONE	CHAR(12) NOT NULL,
CUS_BALANCE	NUMERIC(9,2) DEFAULT 0.00,
CONSTRAINT CUS_UI1 UNIQUE(CUS_LNAME,CUS_FNAME));


CREATE TABLE INVOICE (
INV_NUMBER     	NUMERIC PRIMARY KEY,
CUS_CODE	NUMERIC, 
INV_DATE  	DATE NOT NULL,
CONSTRAINT INV_CK1 CHECK (INV_DATE > TO_DATE('01-JAN-2002','DD-MON-YYYY')),
INDEX		(CUS_CODE),
CONSTRAINT FK_INVOICE_CUSTOMER FOREIGN KEY (CUS_CODE) REFERENCES CUSTOMER(CUS_CODE));


CREATE TABLE LINE (
LIN_NUMBER	NUMERIC(2,0) NOT NULL,
LINE_UNITS	NUMERIC(9,2) DEFAULT 0.00 NOT NULL,
LINE_PRICE	NUMERIC(9,2) DEFAULT 0.00 NOT NULL,
PRIMARY KEY (INV_NUMBER,LINE_NUMBER),
INDEX		(INV_NUMBER),
INDEX		 (P_CODE),
CONSTRAINT FK_LINE_INVOICE FOREIGN KEY (INV_NUMBER) REFERENCES INVOICE (INV_NUMBER) ON DELETE CASCADE,
CONSTRAINT FK_LINE_PRODUCT FOREIGN KEY (P_CODE) REFERENCES PRODUCT(P_CODE),
CONSTRAINT LINE_UI1 UNIQUE(INV_NUMBER, P_CODE));

alter table product add column prod_indate varchar(10);
alter table line add column inv_number int not null;
alter table line add column prod_code varchar(0);
alter table product add column vend_code int not null;

alter table customer add constraint primary key(cus_code);
alter table invoice add constraint primary key(inv_number);
alter table line add constraint primary key(line_number);
alter table product add constraint primary key(prod_code);
alter table verdor add constraint primary key(verd_code);

alter table invoice add constraint foreign key(cus_code) references customer(cus_code) on update cascade;
alter table line add constraint foreign key(inv_number) references invoice(inv_number) on delete cascade;
alter table line add constraint foreign key(prod_code) references customer(prod_code) on update set null;
alter table product add constraint foreign key(verd_code) references verdor(verd_code);

alter table customer alter column cus_balance set default 0.00;
alter table customer alter column cus_areacode set default '0181';
alter table line alter column line_units set default 0.00;
alter table line alter column line_price set default 0.00;

create index cus_codex on invoice(cus_code);
create index prod_indatex on product(prod_indate);
create index verdprodx on product(verd_code, prod_code);
create index prod_price on product(prod_price);

drop index prod_price on product;

insert into customer 
values
(10010,'Ramas','Alfred','A','0181','844-2573',0),
(10011,'Dunne','Leona','K','0161','894-1238',0),
(10012,'Smith','Kathy','W','0181','894-2285',345.86);

insert into invoice 
values
(1001,10014,'2008-01-16'),
(1002,10011,'2008-01-16'),
(1003,10012,'2008-01-16');

insert into line
values
(1,1001,1,'13-Q2/P2',1,14.99),
(2,1001,2,'23109-HB',1,9.95),
(3,1002,1,'54778-2T',2,4.99);


insert into product
value
('11QER/31','Power painter, 15 psi., 3-nozzle',2007-11-07,8, 5,109.99,0.00,25595),

('13-Q2/P2','7.25-cm. pwr. saw blade', 2007-12-14, 32, 15, 14.99,0.05,21344),

('14-Q1/L3','9.00-cm. pwr. saw blade', 2007-11-13, 18, 12, 17.49,0.00,21344);


insert into vendor
value
(21225,'Bryson, Inc.','Smithson','0181','223-3234','UK','Y'),
(21226,'SuperLoo, Inc.','Flushing','0113','215-8995','SA','N'),
(21231,'D\&E Supply','Singh','0181','228-3245','UK','Y');


create table Employee(
EMP_NUM INT,
EMP_TITLE CHAR (10),
EMP_LNAME VARCHAR(15),
EMP_FNAME VARCHAR(15),
EMP_INITIAL CHAR(1),
EMP_DOB DATE,
EMP_HIR_DATE DATE,
EMP_AREACODE CHAR(5),
EMP_PHONE CHAR(8)
);


insert into Employee
values
(1, 'mr.','danni','petur','d.p','1987.02.6','2018.08.8','2114','778-923');

alter table Employee add constraint primary key(emp_num);

alter table Customer add column emp_num int not null;
alter table Customer add constraint foreign key (emp_num) references employee(EMP_NUM);

alter table Product add column emp_num int not null;
alter table Product add constraint foreign key emp_num references Employee(EMP_NUM);


