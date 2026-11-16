# Databricks notebook source
catalog = "workspace"
schema = "retail_lab"
base = f"/Volumes/{catalog}/{schema}/raw_files"

customers = (spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base}/customers.csv"))

products = (spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base}/products.csv"))

orders = (spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base}/orders.csv"))

display(customers.limit(5))
display(products.limit(5))
display(orders.limit(5))



# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.retail_lab.parquet;
# MAGIC
# MAGIC

# COMMAND ----------


parquet_base = f"/Volumes/{catalog}/{schema}/parquet"

customers.write.mode("overwrite").parquet(f"{parquet_base}/customers")
products.write.mode("overwrite").parquet(f"{parquet_base}/products")
orders.write.mode("overwrite").parquet(f"{parquet_base}/orders")

#Show the schema and row count of each dataset.
# Read the Parquet data back
customers_parquet = spark.read.parquet(f"{parquet_base}/customers")
products_parquet = spark.read.parquet(f"{parquet_base}/products")
orders_parquet = spark.read.parquet(f"{parquet_base}/orders")
# Customers schema
customers_parquet.printSchema()
display(customers_parquet.count())

# Products schema
products_parquet.printSchema()
display(products_parquet.count())

# Orders schema
orders_parquet.printSchema()
display(orders_parquet.count())
# Display the first 10 orders.
display(orders_parquet.limit(10))

# COMMAND ----------

# Find all orders with status Delivered
orders_parquet.filter(orders_parquet.order_status == "Delivered").limit(20).display()


# COMMAND ----------

# Show orders placed in 2025
orders_2025 = (
    orders_parquet
    .filter(
        (orders_parquet.order_date >= "2025-01-01") &
        (orders_parquet.order_date < "2026-01-01")
    )
    .limit(20)
)

display(orders_2025)

# COMMAND ----------

# List all distinct order statuses
orders_parquet.select("order_status").distinct().display()

# COMMAND ----------

# Find orders with a missing shipping_date
missing_date = (orders_parquet.filter(
    orders_parquet.shipping_date.isNull()
)
.limit(20)
)
display(missing_date)

# COMMAND ----------

# I want to do the level2 excersize using SQL so I had to create a temp view so sql can access the data from the parquet files.
customers_parquet = spark.read.parquet(f"{parquet_base}/customers")
products_parquet = spark.read.parquet(f"{parquet_base}/products")
orders_parquet = spark.read.parquet(f"{parquet_base}/orders")

customers_parquet.createOrReplaceTempView("customers")
products_parquet.createOrReplaceTempView("products")
orders_parquet.createOrReplaceTempView("orders")


# COMMAND ----------

#Calculate the total number of orders by status
result = spark.sql("""
    SELECT
        order_status,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY order_status
""")

display(result)

# COMMAND ----------

# Calculate total quantity sold by product.
total_product_qauntity = spark.sql("""
    SELECT
        product_id,
        SUM(quantity) AS total_quantity_sold
    FROM orders
    GROUP BY product_id
    ORDER BY product_id
""")

display(total_product_qauntity)

# COMMAND ----------

#Calculate revenue by payment method. Revenue = quantity × unit_price × (1 − discount_pct). Treat a missing discount as 0.
revenue_by_payment_method = spark.sql("""
   SELECT
    payment_method,
    SUM(
        quantity * unit_price * (1 - COALESCE(discount_pct, 0))
    ) AS total_revenue
FROM orders
GROUP BY payment_method
ORDER BY total_revenue DESC;
""")

display(revenue_by_payment_method)


# COMMAND ----------

# Find monthly revenue for 2025.
revenue_by_month = spark.sql("""
    SELECT  
        EXTRACT(MONTH FROM order_date) AS month,
        SUM(quantity * unit_price * (1 - COALESCE(discount_pct, 0))) AS total_revenue   
        FROM orders
        WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01'
        GROUP BY month
        ORDER BY month;
""")
display(revenue_by_month)


# COMMAND ----------

# Find the top 5 customers by total order value.
total_order_value = spark.sql("""
    SELECT
        customer_id,
        SUM(quantity * unit_price * (1 - COALESCE(discount_pct, 0))) AS total_order_value
    FROM orders
    GROUP BY customer_id
    ORDER BY total_order_value DESC
    LIMIT 5;
""")
display(total_order_value)


# COMMAND ----------

# Calculate average order value by customer segment.
average_order_value = spark.sql("""
    SELECT
    c.customer_segment,
    AVG(
        o.quantity * o.unit_price * (1 - COALESCE(o.discount_pct, 0))
    ) AS average_order_value
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.customer_segment
ORDER BY average_order_value DESC;
""")
display(average_order_value)

# COMMAND ----------

# Join orders to customers and show order ID, customer name, city and region
order_customer_join = spark.sql("""
    SELECT
    o.order_id,
    c.customer_name,
    c.city,
    c.region
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id
    LIMIT 20;
""")
display(order_customer_join)

# COMMAND ----------

# Join orders to products and calculate revenue by product category.
# COALESCE() means to treat missing (NULL) discounts as 0.
revenue_by_product_category = spark.sql("""
    SELECT
    p.category,
    SUM(
        o.quantity * o.unit_price * (1 - COALESCE(o.discount_pct, 0))
    ) AS total_revenue
FROM orders o
INNER JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
""")
display(revenue_by_product_category)

# COMMAND ----------

# Find customers who have never placed an order.
customers_without_orders = spark.sql("""
    SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    c.region
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
""")
display(customers_without_orders)


# COMMAND ----------

# Identify duplicate order IDs.
duplicate_orders = spark.sql("""
    SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
""")
display(duplicate_orders)



# COMMAND ----------

# Replace missing discounts with 0 and verify there are no NULL discounts.

set_discount = spark.sql("""
    SELECT
    order_id,
    quantity,
    unit_price,
    COALESCE(discount_pct, 0) AS discount_pct,
    quantity * unit_price *
        (1 - COALESCE(discount_pct, 0)) AS revenue
FROM orders;
""")
display(set_discount)

missing_discounts = spark.sql("""
    SELECT
    COUNT(*) AS remaining_null_discounts
FROM orders
WHERE discount_pct IS NULL;
""")
display(missing_discounts)



# COMMAND ----------

# Calculate the percentage of orders in each status.
percentage_orders_by_status = spark.sql("""
    SELECT
    order_status,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM orders
GROUP BY order_status
ORDER BY percentage DESC;
""")
display(percentage_orders_by_status)
