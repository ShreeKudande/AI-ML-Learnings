SELECT @@autocommit;
SET autocommit = 0; -- disabled

CREATE DATABASE prime;
USE prime;

CREATE TABLE accounts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance DECIMAL(10, 2)
);

INSERT INTO accounts (name, balance) VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

SELECT * FROM accounts;
/*
	 id     balance
1	Adam	500.00
2	Bob	    300.00
3	Charlie	1000.00
*/
-- ----------------------------------------------------------------------------------------------
-- transactions

/* WHAT IS IT: 
A Transaction is a single logical unit of work that groups multiple SQL 
operations together.

WHY WE USE IT: 
To ensure Data Integrity. It follows the "All or Nothing" rule: 
either every command in the group succeeds (Commit), or if any single 
command fails, the entire group is cancelled (Rollback) to prevent 
incomplete or corrupt data.

HOW IT PROTECTS DATA (ACID Rules): 
Transactions follow 4 strict properties to ensure data safety:

1. ATOMICITY (All or Nothing): 
   Either every step succeeds, or if one fails, the whole thing is cancelled.

2. CONSISTENCY (Follow Rules): 
   Data must meet all database rules (constraints) before and after the transaction. 
   It never leaves data in a "half-broken" state.

3. ISOLATION (Don't Interfere): 
   If two people make transactions at the same time, they act independently 
   and don't mess up each other's data.

4. DURABILITY (Permanent Save): 
   Once you "COMMIT" (save), the changes are written permanently. 
   Even a system crash or power loss won't erase them.
*/

START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;

/*
	 id     balance
1	Adam	450.00
2	Bob	    350.00
3	Charlie	1000.00
*/
-- ----------------------------------------------------------------------------------------------
-- Rollback
START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
COMMIT;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
ROLLBACK;

/*
	 id     balance
1	Adam	400.00
2	Bob	    350.00
3	Charlie	1000.00
*/
-- ----------------------------------------------------------------------------------------------
-- Savepoints
START TRANSACTION;
UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;
UPDATE accounts SET balance = balance + 10 WHERE id = 1;
ROLLBACK TO after_wallet_topup;
COMMIT;

/*
	 id     balance
1	Adam	1400.00
2	Bob	    350.00
3	Charlie	1000.00
*/
-- ----------------------------------------------------------------------------------------------
/* WHAT ARE JOINS:
Joins are used to combine rows from two or more tables, based on a related 
column between them (like a common ID).

WHY WE USE THEM:
To view a complete picture of data that is split across different tables.
For example, linking a "Customer" to their "Orders" without keeping 
everything in one messy table.

TYPES OF JOINS:
1. INNER JOIN: Returns records that have matching values in BOTH tables.
2. LEFT JOIN: Returns ALL records from the left table, and the matched 
   records from the right table.
3. RIGHT JOIN: Returns ALL records from the right table, and the matched 
   records from the left table.
4. FULL JOIN: Returns ALL records when there is a match in EITHER left 
   or right table.
*/

-- JOINs --> are used to combine rows from two or more tables based on a related column between them.

CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
	orders_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

SELECT * FROM customers;
/*
customer_id  name      city
1	         Alice	   Mumbai
2	         Bob	   Delhi
3	         Charlie   Bangalore
4	         David	   Mumbai
*/

SELECT * FROM orders;
/*
order_id  cutomer_id  amount
101	      1	 		  500
102	      1			  900
103	      2			  300
104	      5			  700
*/
-- ----------------------------------------------------------------------------------------------
-- INNER JOIN
SELECT *
FROM customers  c
INNER JOIN orders  o
ON c.customer_id = o.customer_id;
/* 
customer_id   name    city    | order_id  customer_id  amount
1	          Alice	  Mumbai  |	101	      1	           500
1	          Alice	  Mumbai  |	102	      1	           900
2	          Bob	  Delhi   |	103	      2	           300
*/

SELECT c.customer_id, o.orders_id, c.name
FROM customers  c
INNER JOIN orders  o
ON c.customer_id = o.customer_id;

/* 
customer_id   orders_id  name   
1	          101		 Alice	  
1	          102		 Alice	  
2	          103		 Bob	  
*/
-- ----------------------------------------------------------------------------------------------
-- LEFT JOIN
SELECT *
FROM customers  c
LEFT JOIN orders  o
ON c.customer_id = o.customer_id;

/* 
customer_id   name      city       | order_id  customer_id  amount
1	          Alice	    Mumbai     |	101	      1	           500
1	          Alice	    Mumbai     |	102	      1	           900
2	          Bob	    Delhi      |	103	      2	           300
3 			  Charlie   Bangalore  |    Null     Null          Null
4             David     Mumbai     |    Null     Null          Null
*/
-- ----------------------------------------------------------------------------------------------
-- RIGHT JOIN
SELECT *
FROM customers  c
RIGHT JOIN orders  o
ON c.customer_id = o.customer_id;

/* 
customer_id   name      city       | order_id  customer_id  amount
1	          Alice	    Mumbai     |	101	      1	           500
1	          Alice	    Mumbai     |	102	      1	           900
2	          Bob	    Delhi      |	103	      2	           300
Null 		  Null      Null       |    104       5            700
*/
-- ----------------------------------------------------------------------------------------------
-- OUTER JOIN
SELECT *
FROM customers  c
LEFT JOIN orders  o
ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers  c
RIGHT JOIN orders  o
ON c.customer_id = o.customer_id;

/* 
customer_id   name      city       | order_id  customer_id  amount
1	          Alice	    Mumbai     |	102	      1	           900
1	          Alice	    Mumbai     |	101	      1	           500
2	          Bob	    Delhi      |	103	      2	           300
3 			  Charlie   Bangalore  |    Null     Null          Null
4             David     Mumbai     |    Null     Null          Null
Null 		  Null      Null       |    104       5            700
*/
-- ----------------------------------------------------------------------------------------------
-- CROSS JOIN
SELECT *
FROM customers
CROSS JOIN orders;

/*
customer_id   name      city       | order_id  customer_id  amount
4			  David		Mumbai	   | 101	   1			500
3	          Charlie	Bangalore  | 101	   1	        500
2	          Bob	    Delhi	   | 101	   1	        500
1	          Alice	    Mumbai	   | 101	   1        	500
4	          David	    Mumbai	   | 102	   1	        900
3	          Charlie	Bangalore  | 102	   1	        900
2	          Bob	    Delhi	   | 102	   1	        900
1	          Alice	    Mumbai	   | 102	   1	        900
4	          David	    Mumbai	   | 103	   2	        300
3	          Charlie	Bangalore  | 103	   2	        300
2	          Bob	    Delhi	   | 103	   2	        300
1	          Alice	    Mumbai     | 103	   2  	        300
4	          David	    Mumbai	   | 104	   5	        700
3         	  Charlie	Bangalore  | 104	   5	        700
2	          Bob	    Delhi	   | 104	   5	        700
1	          Alice	    Mumbai	   | 104	   5	        700
*/
-- ----------------------------------------------------------------------------------------------
/* WHAT IS A SELF JOIN:
A Self Join is a regular join where a table is joined with ITSELF.
To do this, we must use aliases (nicknames) to treat the single table 
as two separate instances (e.g., "Employee" vs "Manager").

1. THE TABLE (One single list for everyone)
   -----------------------------------------
   | ID  | Name  | Manager_ID |
   | --- | ----- | ---------- |
   | 10  | KING  | NULL       |  <-- King is the Big Boss (No manager)
   | 20  | SCOTT | 10         |  <-- Scott's manager is ID 10
   | 30  | JAMES | 20         |  <-- James's manager is ID 20
   -----------------------------------------

2. THE PROBLEM
   Look at Scott (Row 2). 
   You see his Manager_ID is "10". 
   But "10" is just a number. You want to know the NAME of his boss.

3. THE SOLUTION (Self Join)
   A Self Join is just "Looking up the number in the SAME list."
   
   * Step 1: Start with Scott. Take his Manager_ID (10).
   * Step 2: Go back to the top of THIS SAME TABLE.
   * Step 3: Find the person with ID 10.
   * Step 4: You found "King".
   
   Result: Scott works for King.
*/

-- SELF JOIN --> It is a regular join but the table is joined with itself.
SELECT *
FROM customers as A
JOIN customers as B
ON A.customer_id = B.customer_id;
/*
customer_id  name      city      | customer_id  name    city
1	         Alice	   Mumbai    | 1            Alice   Mumbai
2	         Bob	   Delhi     | 2            Bob     Delhi
3	         Charlie   Bangalore | 3            Charlie Bangalore
4	         David	   Mumbai    | 4            David   Mumbai
*/
-- ----------------------------------------------------------------------------------------------
-- Exclusive joins
SELECT * FROM customers;
SELECT * FROM orders;

-- Left Exclusive Join
SELECT *
FROM customers A
LEFT JOIN orders B
ON A. customer_id = B.customer_id
WHERE B.customer_id IS NULL;

/*
customer_id  name      city      | customer_id  name    city
3	         Charlie   Bangalore | Null         Null    Null
4	         David	   Mumbai    | Null         Null    Null
*/

-- Right Exclusive Join
SELECT *
FROM customers A
RIGHT JOIN orders B
ON A. customer_id = B.customer_id
WHERE A.customer_id IS NULL;

/*
customer_id  name      city      | customer_id  name    city
Null         Null      Null      | 104          5       700
*/
-- ----------------------------------------------------------------------------------------------
-- Sub-Queries --> A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.
/* Syntax
SELECT columns(s)
FROM table_name
WHERE col_name operator
(subquery);
*/

-- With WHERE
-- We want rows which have order amount greater then average amount of the amount column >
SELECT *
FROM orders
WHERE amount > (
	SELECT AVG(amount)
    FROM orders
);
/*
order_id  cutomer_id  amount
102	      1			  900
104	      5			  700
*/

-- With SELECT
-- We want count of orders per customer >
SELECT name,
	(	
		SELECT COUNT(*)
		FROM orders o
        WHERE o.customer_id = c.customer_id
    ) AS order_count
    FROM customers c;
/*
name    order_count
Alice	2
Bob	    1
Charlie	0
David	0
*/

-- With FROM
-- We want average spending for each customer >
SELECT
	summary.customer_id,
    summary.avg_amount
FROM
	(
		SELECT 
			customer_id,
			AVG(amount) as avg_amount
		FROM orders
		GROUP BY customer_id
	) as summary;

/*
customer_id  avg_amount
1	         700.0000
2	         300.0000
5	         700.0000
*/
-- ----------------------------------------------------------------------------------------------
-- Views in SQL --> A view is a virtual table based on the result-set of an SQL statement.
-- Note : A view always shows up-to-date data. The database engine recreates the view, every time a user queties it.

/* Syntax
CREATE VIEW view1 AS
SELECT col1, col2 FROM table_name;
*/

SELECT * FROM customers;
SELECT * FROM orders;

CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM view1;

/*
customer_id   name
1			  Alice
2			  Bob
3			  Charlie
4			  David
*/
DROP VIEW view1;
/*
1. WHAT IS A VIEW?
   - Think of a View as a "Virtual Table."
   - It doesn't hold data itself; it is simply a saved SQL query that looks 
     and acts like a table.
   - When you query a view, the database runs the saved query behind the 
     scenes to fetch current data.

2. KEY RULES & FEATURES
   A. NO PHYSICAL STORAGE
      - Views do not store data physically on the disk. They are just a 
        window looking at the real tables.
      - (Note: The only exception is a "Materialized View," which saves a 
        snapshot of the data for performance).

   B. COMBINES DATA EASILY
      - A view can include columns from just one table, or it can join 
        multiple tables together into a single, clean virtual table.

   C. WORKS LIKE A TABLE
      - You can use a view anywhere you use a normal table. 
      - It works inside SELECT statements, JOINS, and WHERE clauses.

   D. ENHANCES SECURITY
      - This is a main use case. You can create a view that exposes only 
        "safe" data (like names and emails) while hiding sensitive columns 
        (like passwords or salaries). You give users access to the View, 
        not the raw table.
*/
-- ----------------------------------------------------------------------------------------------
-- Index in SQL --> indexes are special database objects that make data retrieval faster.

CREATE TABLE accounts (
	account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10, 2),
    branch VARCHAR(50)
);

INSERT INTO accounts VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');

SELECT * FROM accounts;

CREATE INDEX idx_branch ON accounts(branch);
SHOW INDEX FROM accounts;

SELECT *
FROM accounts
WHERE branch = "Mumbai";

CREATE INDEX idx2 ON accounts(branch, balance);
SHOW INDEX FROM accounts;

DROP INDEX idx2 ON accounts;
/*
1. SIMPLE DEFINITION
Think of an Index in SQL like the "Index" at the back of a textbook.

* Without an index: To find a specific topic, you have to flip through 
    every single page (this is called a "Full Table Scan").
* With an index: You look up the topic in the back, find the page number, 
    and go directly there.

In technical terms: An Index is a data structure (often a B-Tree) that 
improves the speed of data retrieval operations on a database table.

2. MAIN USES
* Faster Searching: Quickly finding rows where a column matches a specific value 
    (e.g., WHERE user_id = 5).
* Sorting: Speeding up ORDER BY clauses because the index is already sorted.
* Joins: drastically improving performance when linking tables together 
    (e.g., ON table1.id = table2.id).
* Uniqueness: Primary Key and Unique indexes ensure no duplicate data exists 
    in a column.

3. PROS AND CONS
----------------------------------------------------------------------------
| PROS (Advantages)                     | CONS (Disadvantages)             |
|---------------------------------------|----------------------------------|
| Speed: Drastically speeds up          | Storage: Indexes take up extra   |
| SELECT queries (reading data).        | disk space.                      |
|                                       |                                  |
| Efficiency: Reduces the amount of     | Maintenance: Slows down INSERT,  |
| data the database has to scan.        | UPDATE, and DELETE commands.     |
|                                       | (Because every time you change   |
| Sorting: Helps avoid separate         | data, the database must also     |
| sorting steps during query execution. | update the index).               |
----------------------------------------------------------------------------
SUMMARY: 
Use indexes on columns you search often, but avoid putting them on 
columns you rarely search or columns that you update very frequently.
*/
-- ----------------------------------------------------------------------------------------------
-- Stored Procedures --> Predefined set of SQL statements that you can save in the database and execute whenever needed. 
/*
Syntax(Create)
CREATE PROCEDURE procedure_name (parameters)
BEGIN
 -- SQL statements
END;
*/

SELECT * FROM accounts;

-- Input
DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE account_id = acc_id;
END $$
DELIMITER ;

CALL check_balance(1);
CALL check_balance(2);

-- Output
DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL(10,2))
BEGIN
	SELECT balance INTO bal
    FROM accounts
    WHERE account_id = acc_id;
END $$
DELIMITER ;

CALL check_balance(1, @balance);
SELECT @balance;

DROP PROCEDURE IF EXISTS check_balance;

/* SIMPLE DEFINITION:
A Stored Procedure is a pre-written set of SQL code that is saved ("stored") 
in the database so it can be reused. 

Think of it exactly like a "Function" in programming: 
You define it once, and then call it whenever you need it, instead of 
rewriting the code every time.
*/

-- ----------------------------------------------------------------------------------------------
