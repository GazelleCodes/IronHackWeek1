
# Q. 1 — Build a Small Relational Model
'''
Use:
a primary key on each table;
a foreign key from orders.customer_id to customers.customer_id.
CREATE DATABASE IF NOT EXISTS britmart_db_types;
 
USE britmart_db_types;
 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);
 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    amount_gbp DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
'''

# Q. 2 — Insert and Join the Relational Data
'''
INSERT INTO customers
(customer_id, customer_name, city)
VALUES
(1, 'Amelia Clarke', 'London'),
(2, 'Oliver Bennett', 'Manchester'),
(3, 'Aisha Khan', 'Leeds');
 
INSERT INTO orders
(order_id, customer_id, amount_gbp, status)
VALUES
(101, 1, 45.50, 'complete'),
(102, 2, 18.00, 'cancelled'),
(103, 1, 62.25, 'complete'),
(104, 3, 30.00, 'complete');
 
SELECT
    o.order_id,
    c.customer_name,
    c.city,
    o.amount_gbp,
    o.status
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id
ORDER BY o.order_id;
'''
#Q. 3 — Represent the Same Customer as a Flexible Document
customer_1 = {
    "customer_id": 1,
    "name": "Amelia Clarke",
    "city": "London",
    "email": "amelia@example.com",
    "preferences": {
        "newsletter": True,
        "language": "en",
    },
}
 
customer_2 = {
    "customer_id": 2,
    "name": "Oliver Bennett",
    "city": "Manchester",
    "preferences": {
        "newsletter": False,
        "language": "en",
    },
}
 
# print(customer_1)
# print(customer_2)

# Q. 4 — MCQ: Relational Database
# C. Orders must reference valid customers and transaction consistency is important. 

# Q. 5 — Choose the Better NoSQL Model
'''
A -> Document
B -> Key-value
C -> Column-family
D -> Document
'''

# Q. 6 — Build a Key-Value Example
sessions = {
    "SESSION-1001": {
        "customer_id": 1,
        "cart_count": 3,
    },
    "SESSION-1002": {
        "customer_id": 2,
        "cart_count": 1,
    },
    "SESSION-1003": {
        "customer_id": 3,
        "cart_count": 5,
    },
}
 
# print(sessions["SESSION-1002"])

# Q. 7 — Design Three Product Documents
products = [
    {
        "product_id": "P101",
        "name": "Office Chair",
        "colour": "Black",
        "material": "Mesh",
    },
    {
        "product_id": "P102",
        "name": "Laptop Stand",
        "colour": "Silver",
        "height_adjustable": True,
    },
    {
        "product_id": "P103",
        "name": "Notebook Set",
        "page_count": 200,
        "paper_size": "A5",
    },
]

# Q. 8 — MCQ: Key-Value Database
# Which access pattern is the best fit for a key-value database?
# A. Find a session directly from its session

'''
Q. 10 — Identify the ACID Property
Match each example to Atomicity, Consistency, Isolation, or Durability.

A. An order and its payment should not be half-completed.
B. A successful commit remains stored after a restart.
C. Two transactions should not see unsafe partial work from each other.
D. A transaction must leave the database in a valid state.

A -> Atomicity
B -> Durability
C -> Isolation
D -> Consistency
'''

'''
Q. 11 — ACID or BASE?
Choose the stronger fit.

Requirement          	                        Choice	     Reason
Payment update	                                ACID	     Strong correctness is important
Social activity count	                        BASE	     Temporary inconsistency may be acceptable
Order and stock update	                        ACID	     Related changes must remain consistent
High availability with temporary inconsistency	BASE	     Availability is prioritised
'''


'''
Q. 12 — MCQ: BASE
Which statement best describes a BASE-style design?
B. Temporary inconsistency may be accepted to support availability and scale.
'''

'''
Q. 13 — Fixed or Flexible Schema?
Choose the better starting approach.

Data	            Choice	    Reason
Payment transaction	Fixed	    Required structure and correctness matter
Product catalogue	Flexible	Attributes can differ by product type
Order line	        Fixed	    Required fields and relationships are important
Event payload	    Flexible	Optional fields can vary
'''

'''
Q. 14 — Choose Relational or NoSQL
For each requirement, choose a starting model and explain why.
1. Customer orders with strong foreign-key relationships.
2. Product descriptions with many optional attributes.
3. User session lookup by session ID.
4. Fraud investigation based on many connected entities.

1. Relational
2. Document
3. Key-value
4. Graph
'''

'''
Q. 16 — MCQ: Choosing a Database
BritMart must store orders, customers, and payments with strong relationships 
and transaction correctness. Which is the strongest starting choice?
D. Relational database

'''

'''
Q. 18 — Find Shared Fraud Links
Find the values shared by both C1 and C2.
Do this with Python lists, sets, and loops already covered in Week 1.
Use this data:
'''

relationships = [
    ("C1", "CARD-A"),
    ("C2", "CARD-A"),
    ("C1", "ADDR-X"),
    ("C2", "ADDR-X"),
    ("C3", "CARD-B"),
]

c1_links = set()
c2_links = set()
 
for customer, linked_value in relationships:
    if customer == "C1":
        c1_links.add(linked_value)
 
    if customer == "C2":
        c2_links.add(linked_value)
 
shared = c1_links.intersection(c2_links)
 
# print(shared)

'''
Q. 19 — Database Choice Review
BritMart has these four systems:

System	            Model	    Schema	                Consistency	    Main access
Checkout orders	    Relational	Fixed	                Strong	        Transactions and joins
Product catalogue	Document	Flexible                Depends on use	Read product document
Website sessions	Key-value	Flexible value	        Depends on use	Lookup by session ID
Fraud relationships	Graph	    Relationship-focused	Depends on use	Traverse connections
'''
'''
Q. 20 — Explain the Trade-Off
A team says:

"NoSQL is always faster, so all BritMart data should move to NoSQL."

Write a short response using only today's concepts.

There is no single database model that is best for every workload.

Relational databases are strong when data has clear relationships, required structure, and strong transaction needs.

Different NoSQL models are useful for flexible documents, key-based access, wide distributed data, or relationship-heavy graph problems.

The correct choice depends on the data shape, access pattern, and consistency requirement.
'''