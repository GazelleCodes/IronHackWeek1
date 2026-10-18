# Q. 1 — Find the Entities
"""
Group the attributes into these entities:

Customer
Order
Product
Order Item

Customer
customer_id
customer_name
customer_city

Order
order_id
order_date
customer_id

Product
product_id
product_name
unit_price_gbp


Order Item
order_id
product_id
quantity

"""

# Q. 3 — Create the Base Tables
"""
CREATE DATABASE IF NOT EXISTS britmart_modelling;
 
USE britmart_modelling;
 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_city VARCHAR(50) NOT NULL
);
 
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    unit_price_gbp DECIMAL(10,2) NOT NULL
);
 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
 
CREATE TABLE order_items (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
"""
# Q. 5 — Fix a 1NF Problem

"""
order_id	customer_id	product_id
101	1	P1
101	1	P2
102	2	P3
"""

#Q. 6 — Find the 2NF Problem

"""
Consider:

order_id
product_id
product_name
quantity

products
---------
product_id
product_name

The order-item table can then keep:

order_id
product_id
quantity
"""

#Q. 7 — Find the 3NF Problem

"""
customer_id
customer_name
postcode
city

city depends on postcode, not directly on the customer.

Many customers can share the same postcode,
so the city value may be repeated many times.

The customer row stores the postcode and the postcode table stores the city.
"""

# Q. 8 — MCQ: Normalisation
"""
What is the main aim of normalisation in an OLTP-style model?
B. Reduce repeated facts and keep relationships clear
"""
#Q. 10 — Rebuild a Denormalised Result with a Join

"""
order_id
order_date
customer_name
customer_city
product_name
quantity
unit_price_gbp
line_total_gbp

SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    c.customer_city,
    p.product_name,
    oi.quantity,
    p.unit_price_gbp,
    oi.quantity * p.unit_price_gbp
        AS line_total_gbp
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id
INNER JOIN order_items oi
    ON o.order_id = oi.order_id
INNER JOIN products p
    ON oi.product_id = p.product_id
ORDER BY o.order_id, p.product_id;
"""
#Q. 13 — Identify the Fact and Dimensions

"""
FactSales
---------
date_key
customer_key
product_key
store_key
quantity
sales_gbp

DimDate
DimCustomer
DimProduct
DimStore
"""

# Q. 20 — Review the Model Before Building It

"""
Before creating tables, write answers to these questions:

1. What does one row represent?
2. Which fields identify the row?
3. Which facts repeat?
4. Which fields describe another entity?
5. Which relationships must remain valid?
6. Is the model mainly for transactions or analytics?

Then explain why answering these questions first can reduce redesign later.



These questions force the team to decide the grain, 
entities, keys, repeated facts, relationships, and 
main workload before creating tables.

That makes the model easier to understand and reduces 
accidental duplication or unclear table responsibilities.
"""













