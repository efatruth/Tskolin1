CREATE DATABASE 0301865919_BigHit_db

USE 0301865919_BigHit_db;

CREATE TABLE CUSTOMER(
     accountID int,
     firstName varchar(10),
     lastName varchar(10),
     emailAddress varchar(25)
);

create table ShippingAddress(
	 cust_acctID int,
     street varchar(25),
     city varchar(10),
     zipcode int,
     state varchar(10)
);

create table creditCards(
	 acctNo int(10),
	 cust_acctID int(10),
     csvNo int(3),
     expiration int(10),
     ctypeDR_CR varchar(3),
     cardcolour varchar(10)
);

create table sale (
	 Qty int(10),
     saleDate varchar(10),
     charge_card int(10),
     custcredit int(25),
     movieID int(10),
     custAddr varchar(25)
);

create table shopping_cart(
	 custMail varchar(25),
     movieID int(10)
);

create table DvD (
	 MovieID int(10),
     price int(10)
);


create table video_tape (
	 MovieID int(10),
     price int(10)
);

insert into 
CUSTOMER(firstName,accountID)
values
("smith",0201784524);

insert into 
ShippingAddress(city,zipcode)
values
("reykjavik",115),
("selfoss",201);

insert into 
creditCards(csvNo,cardcolour,expiration)
values
(334,"red",12-03-2030),
(231,"blue",10-08-2024);

insert into
sale(Qty,saleDate)
values
(50,30-02-18);

insert into 
Shopping_cart(custMail,movieID)
values
("ebass@gmail.com",111);

insert into 
DvD(MovieID,price)
values
(123,400);

insert into 
video_tape(MovieID,price)
values
(321,500);


select firstName, accountID from CUSTOMER;

select city, zipcode from ShippingAddress;

select csvNo,cardcolour,expiration from creditCards;

select Qty,saleDate from sale;

select custMail,movieID from Shopping_cart;

select MovieID,price from DvD;

select MovieID,price from video_tape;