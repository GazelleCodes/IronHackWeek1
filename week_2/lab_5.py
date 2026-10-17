# . 1 — Create a Table for Query Testing

"""
CREATE DATABASE IF NOT EXISTS britmart_performance;
 
USE britmart_performance;
 
CREATE TABLE orders_perf (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    city VARCHAR(50) NOT NULL,
    amount_gbp DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL
);
 
INSERT INTO orders_perf VALUES
(1, 101, '2026-08-01', 'London', 45.50, 'complete'),
(2, 102, '2026-08-01', 'Manchester', 18.00, 'cancelled'),
(3, 101, '2026-08-02', 'London', 62.25, 'complete'),
(4, 103, '2026-08-02', 'Leeds', 30.00, 'complete'),
(5, 104, '2026-08-03', 'Bristol', 55.50, 'complete'),
(6, 102, '2026-08-03', 'Manchester', 12.00, 'pending'),
(7, 101, '2026-08-04', 'London', 80.00, 'complete'),
(8, 105, '2026-08-04', 'Leeds', 20.00, 'complete'),
(9, 106, '2026-08-05', 'Bristol', 100.00, 'complete'),
(10, 102, '2026-08-05', 'Manchester', 40.00, 'complete');
"""

 
# Q. 2 — Inspect a Query Before Adding an Index
"""
EXPLAIN
SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE customer_id = 101;
"""

# Q. 3 — Add an Index and Compare
"""
The exact plan can vary because the table is small.
The useful practice is comparing the plan before and after the index.

CREATE INDEX idx_orders_customer
ON orders_perf(customer_id);

EXPLAIN
SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE customer_id = 101;
"""

# Q. 4 — MCQ: Index
"""
When is an index most likely to help?
B. A query filters a large table using a selective column.
"""


# Q. 5 — Compare SELECT * with Required Columns
"""
Explain why Query B is better when those are the only columns the consumer needs.

SELECT *
FROM orders_perf
WHERE status = 'complete';

SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE status = 'complete';


Query B asks for only the required columns.

This can reduce unnecessary data transfer and makes the query intent clearer.

SELECT * is convenient during exploration,
but it may read or return columns the consumer does not need.
"""

# Q. 6 — Filter Before Returning Data
"""

completed orders
from 2026-08-03 onwards
amount at least £40

Write one query that applies all three filters.

SELECT
    order_id,
    customer_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE status = 'complete'
  AND order_date >= '2026-08-03'
  AND amount_gbp >= 40
ORDER BY order_date, order_id;
"""

# Q. 7 — Choose the Correct Join Key
"""
Join customers to orders using the correct key.

Explain why joining on city would be unsafe.


CREATE TABLE customers_perf (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);
 
INSERT INTO customers_perf VALUES
(101, 'Amelia Clarke', 'London'),
(102, 'Oliver Bennett', 'Manchester'),
(103, 'Aisha Khan', 'Leeds'),
(104, 'Harry Thompson', 'Bristol'),
(105, 'Emily Wilson', 'Leeds'),
(106, 'Noah Davies', 'Bristol');


SELECT
    o.order_id,
    c.customer_name,
    o.amount_gbp,
    o.status
FROM orders_perf o
INNER JOIN customers_perf c
    ON o.customer_id = c.customer_id;


    customer_id identifies the customer relationship.

Joining on city would be unsafe because several customers can 
live in the same city, creating incorrect matches.
"""

#Q. 8 — MCQ: Required Columns
"""
Why should a query select only the columns it needs?

C. It can reduce unnecessary data read or transferred.
"""


# Q. 9 — Choose a Partitioning Column
"""
BritMart stores several years of order data.
Which is the best starting choice for the stated access pattern? Explain why.

Most reports filter by:

order_date is the strongest starting choice because the reports commonly filter by date.

A date-based layout can allow systems to skip data from dates that are not needed.

The exact partition design depends on data volume and query patterns.
"""

# Q. 10 — Design a Date-Based Layout
"""
Create a simple storage layout using the date.

orders/
├── order_date=2026-08-01/
├── order_date=2026-08-02/
└── order_date=2026-08-03/

A query for only 2026-08-02 can potentially avoid reading data 
from the other dates when the processing engine supports partition pruning.
"""

#Q. 11 — Find the Small-Files Problem
"""
Which design is more likely to create excessive file-management and task overhead? 
Explain why.

100 files of about 100 MB each
100,000 files of about 0.1 MB each

Design B is more likely to create a small-files problem.

A very large number of tiny files can increase:

file listing work;
metadata operations;
task setup overhead.
Bigger files are not automatically better in every case, 
but millions of tiny files are usually inefficient for large analytical workloads.
"""
#Q. 12 — MCQ: Compression
"""
What is the main storage benefit of compression?

A. It reduces the amount of storage required for compressible data.
"""

#Q. 13 — Compare the Formats
"""
Format	 Text or binary?	 Row or column oriented?	Common strength
CSV	     Text                Row-oriented	            Simple and widely supported
Parquet	 Binary	             Columnar	                Analytical reads and compression
Avro	 Binary	             Row-oriented               Record exchange with schema
ORC	     Binary	             Columnar	                Analytical storage and compression
"""

# Q. 14 — Choose a Format for Each Requirement
"""
A. A simple file that a business user can open easily.
B. Analytical data where queries often read only a few columns.
C. Record-oriented data exchange where schema travels with the data.
D. Columnar analytical storage used with systems that support ORC well.

A -> CSV
B -> Parquet
C -> Avro
D -> ORC
"""

# Q. 15 — Inspect a CSV and List Its Limitations
"""
order_id,order_date,city,amount_gbp,status
1,2026-08-01,London,45.50,complete
2,2026-08-01,Manchester,18.00,cancelled
3,2026-08-02,Leeds,30.00,complete

Possible observations:

CSV stores column names in the header,
but it does not strongly store full data-type information.
The file is human-readable.
Values are stored as text.
CSV does not provide the same columnar read benefits as Parquet or ORC.
CSV is often larger than compressed binary formats for large analytical datasets.
"""

#Q. 16 — MCQ: Parquet
"""
Why is Parquet commonly used for analytical data?

D. Its columnar layout can help queries read only needed columns.
"""

# Q. 19 — Review a Poor Storage Layout
"""
BritMart stores three years of orders as:

one folder
500,000 tiny CSV files
no date organisation


Most reports filter by date and select only a few columns.

Using only today's concepts, suggest three improvements.

Possible improvements:

Organise data by a useful date partition.
Reduce the excessive number of tiny files.
Use a columnar analytical format such as Parquet or ORC
when supported by the target system.
Use compression to reduce storage where appropriate.
"""

# Q. 20 — Choose the Complete Design

"""
Partitioning:
By a useful date field because reports commonly filter by date.
 
File format:
Parquet or ORC because the workload is analytical and often reads only a few columns.
 
Compression:
Yes, because reducing stored data can reduce storage and I/O.
 
Query habit:
Filter early and select only the required columns.
"""













