SELECT p_descript, p_indate, p_price, v_code
FROM product
WHERE v_code<> 21344;

SELECT p_descript,p_qoh, p_min,p_price
FROM product
WHERE p_price <=10;

select p_code,p_indate,DATE() - 90 AS CUTDATE
FROM product

select 'hello world' as Greetings

SELECT p_descript, v_code FROM product WHERE v_code between 21344 and 24595;

SELECT p_descript, v_code FROM product WHERE v_code in (21344, 24595);

select * from product where v_code != 2134


create table p (select * from product);

