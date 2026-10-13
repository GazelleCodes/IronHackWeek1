
-- Q. 1 — Create the BritMart Database
CREATE DATABASE IF NOT EXISTS britmart_lab;
USE britmart_lab;
 
SELECT DATABASE()

-- Q. 2 — Create the Customer Table
CREATE TABLE customers (
customer_id INT primary key,
customer_name VARCHAR(100) NOT NULL,
city VARCHAR(50) NOT NULL,
email VARCHAR(120) UNIQUE  NULL,
joined_date DATE NOT NULL,
is_active BOOLEAN NOT NULL
);

INSERT INTO customers (customer_id, customer_name, city, email, joined_date, is_active) VALUES 
(1, "Amelia Clarke", "London", "amelia@example.com", "2026-07-01", True),
(2, "Oliver Bennett", "Manchester", "oliver@example.com", "2026-07-03", True),
(3, "Aisha Khan", "Leeds",  NULL, "2026-07-05", True),
(4, "Harry Thompson", "Bristol", "harry@example.com", "2026-07-07", False);

SELECT * from customers
-- Q. 3 — Create the Orders Table with a Foreign Key

CREATE TABLE orders (
order_id INT primary key,
customer_id INT NOT NULL,
order_date DATE NOT NULL,
amount_gbp DECIMAL(10, 2) NOT NULL,
status VARCHAR(20) NOT NULL,
created_at  DATETIME NOT NULL,
CONSTRAINT chk_order_amount CHECK(amount_gbp >= 0),
CONSTRAINT fk_order_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
-- Q. 4 — MCQ: Foreign Key
-- B. Connect each order to a valid customer row.
-- Q. 5 — Insert Three Order Batches
-- Batch 1
INSERT INTO orders (order_id, customer_id, order_date, amount_gbp, status, created_at) VALUES 
(101, 1, "2026-08-01", 45.50, "complete", "2026-08-01 15:30:00"),
(102, 2, "2026-08-01", 18.00, "cancelled", "2026-08-01 15:30:00"),
(103, 1, "2026-08-01",  62.25, "complete", "2026-08-01 15:30:00");

SELECT COUNT(*) AS order_count FROM orders;
SELECT MAX(amount_gbp) AS max_order_amount, MIN(amount_gbp) AS min_order_amount FROM orders;
SELECT * FROM orders

-- Batch 2
INSERT INTO orders (order_id, customer_id, order_date, amount_gbp, status, created_at) VALUES 
(104, 3, "2026-08-02",  30.00, "complete", "2026-08-02 15:30:00"),
(105, 2, "2026-08-02",  55.50, "complete", "2026-08-02 15:30:00"),
(106, 4, "2026-08-02",  12.00, "pending", "2026-08-02 15:30:00");

SELECT COUNT(*) AS order_count FROM orders;
SELECT MAX(amount_gbp) AS max_order_amount, MIN(amount_gbp) AS min_order_amount FROM orders;
SELECT * FROM orders

-- Batch 3
INSERT INTO orders (order_id, customer_id, order_date, amount_gbp, status, created_at) VALUES 
(107, 3, "2026-08-03",  80.00, "complete", "2026-08-03 15:30:00"),
(108, 1, "2026-08-03",  20.00, "complete", "2026-08-03 15:30:00"),
(109, 2, "2026-08-03",  100.00, "complete", "2026-08-03 15:30:00");

-- Q. 6 — Verify Every Batch
SELECT COUNT(*) AS order_count FROM orders;
SELECT MAX(amount_gbp) AS max_order_amount, MIN(amount_gbp) AS min_order_amount FROM orders;
SELECT * FROM orders;

-- Q. 7 — Select Only Required Columns
SELECT order_id, order_date, amount_gbp, status FROM orders;

-- Q. 8 — MCQ: LIMIT
-- C. Returns the three highest-value orders.
-- Q. 9 — Update One Order Safely

SELECT * FROM orders WHERE order_id = 106;
UPDATE orders SET status = "complete" WHERE order_id = 106;
SELECT * FROM orders WHERE order_id = 106;

-- Q. 10 — Delete One Cancelled Order Safely

SELECT * FROM orders WHERE order_id = 102;
DELETE FROM orders  WHERE order_id = 102;
SELECT * FROM orders WHERE order_id = 102;

SELECT * FROM orders

-- Q. 11 — Practise WHERE, ORDER BY, and LIMIT

SELECT * FROM orders WHERE status = "complete" AND amount_gbp > 50;

SELECT * FROM orders WHERE order_date >= "2026-08-02";

SELECT * FROM orders
ORDER BY amount_gbp DESC
LIMIT 5;

SELECT * FROM orders WHERE status = "complete";

-- Q. 12 — MCQ: Safe UPDATE
-- D. Run the matching SELECT first to confirm which rows will change.

-- Q. 13 — Practise DISTINCT, IN, BETWEEN, and LIKE

SELECT DISTINCT citY FROM customers;

SELECT * FROM customers WHERE citY IN ("London", "Leeds");

SELECT * FROM orders WHERE amount_gbp BETWEEN 30 AND 80;

SELECT * FROM customers WHERE customer_name LIKE "A%";

-- Q. 14 — Find Missing and Present Email Addresses
SELECT * FROM customers WHERE email IS NULL;
SELECT * FROM customers WHERE email IS NOT NULL;

-- Q. 15 — Build a Customer Sales Summary
SELECT COUNT(customer_id) AS customer_id_count FROM orders
WHERE status = "complete";

SELECT COUNT(order_id) AS order_id_count FROM orders
WHERE status = "complete";

SELECT SUM(amount_gbp) AS total_sales_gbp FROM orders
WHERE status = "complete"
GROUP BY customer_id
HAVING SUM(amount_gbp) >= 75;

SELECT AVG(amount_gbp) AS average_order_gbp, MIN(amount_gbp) AS minimum_order_gbp, MAX(amount_gbp) AS maximum_order_gbp  FROM orders
WHERE status = "complete";

SELECT
    customer_id,
    COUNT(*) AS order_count,
    SUM(amount_gbp) AS total_sales_gbp,
    AVG(amount_gbp) AS average_order_gbp,
    MIN(amount_gbp) AS minimum_order_gbp,
    MAX(amount_gbp) AS maximum_order_gbp
FROM orders
WHERE status = 'complete'
GROUP BY customer_id
HAVING SUM(amount_gbp) >= 75
ORDER BY total_sales_gbp DESC;

-- Q. 16 — MCQ: LEFT JOIN
-- A. LEFT JOIN can keep customers even when they have no matching order.
-- Q. 17 — Compare INNER JOIN and LEFT JOIN
-- INNER JOIN
SELECT 
	c.customer_id,
	c.customer_name,
	c.city,
    o.order_id,
    o.amount_gbp,
    o.status
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id;

-- LEFT JOIN
SELECT 
	c.customer_id,
	c.customer_name,
	c.city,
    o.order_id,
    o.amount_gbp,
    o.status
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id;


-- Q. 18 — Find Customers Without Orders

SELECT
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

SELECT COUNT(*) AS customers_without_orders
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Q. 19 — Build a City Report
SELECT
    c.city,
    COUNT(o.order_id) AS completed_order_count,
    SUM(o.amount_gbp) AS completed_revenue_gbp
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
    AND o.status = 'complete'
GROUP BY c.city
ORDER BY completed_revenue_gbp DESC;

-- Q. 20 — Add a New Batch and Recheck the Report
INSERT INTO orders
(order_id, customer_id, order_date, amount_gbp, status, created_at)
VALUES
(110, 4, '2026-08-04', 75.00, 'complete', '2026-08-04 09:00:00'),
(111, 1, '2026-08-04', 40.00, 'complete', '2026-08-04 09:10:00'),
(112, 3, '2026-08-04', 25.00, 'cancelled', '2026-08-04 09:20:00');

SELECT
    customer_id,
    COUNT(*) AS order_count,
    SUM(amount_gbp) AS total_sales_gbp,
    AVG(amount_gbp) AS average_order_gbp,
    MIN(amount_gbp) AS minimum_order_gbp,
    MAX(amount_gbp) AS maximum_order_gbp
FROM orders
WHERE status = 'complete'
GROUP BY customer_id
HAVING SUM(amount_gbp) >= 75
ORDER BY total_sales_gbp DESC;

SELECT
    c.city,
    COUNT(o.order_id) AS completed_order_count,
    SUM(o.amount_gbp) AS completed_revenue_gbp
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
    AND o.status = 'complete'
GROUP BY c.city
ORDER BY completed_revenue_gbp DESC;