/* salescopy.SQL                                 	*/
/* Introduction to SQL 					*/
/* Script file for MySQL  DBMS				*/
/* This script file creates the following tables:	*/
/* SALES_COPY and loads in the default data rows	*/
/* Acript accompanies Task 7.12 in ORACLE lab guide	*/


DROP TABLE SALES_COPY;

CREATE TABLE SALES_COPY (
TRANSACTION_NO 	NUMERIC(8),
LINE_NO		NUMERIC(2,0),
ITEM_PRICE	NUMERIC(2,0),
LINE_QTY	NUMERIC(4), 
LINE_PRICE	NUMERIC(9,2),
CONSTRAINT	PK_SALES_COPY_LINE PRIMARY KEY (TRANSACTION_NO,LINE_NO));

INSERT INTO SALES_COPY VALUES (10000001,1,10.99,2,21.98);
INSERT INTO SALES_COPY VALUES (10000001,2,15.00,2,30.00);
INSERT INTO SALES_COPY VALUES (10000002,1,10.99,1,10.99);
INSERT INTO SALES_COPY VALUES (10000002,2,20.99,1,20.99);
INSERT INTO SALES_COPY VALUES (10000003,1,20.99,NULL,NULL);
INSERT INTO SALES_COPY VALUES (10000003,2,15.00,NULL,NULL);
INSERT INTO SALES_COPY VALUES (10000004,1,15.00,2,30.00);
INSERT INTO SALES_COPY VALUES (10000004,2,20.99,2,41.98);
