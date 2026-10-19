# Q. 1 — Perform a Small ETL Flow

import pandas as pd
 
source = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "price_gbp": ["25.50", "invalid", "12.00", "40.00"],
})


new_source = source.copy()

new_source["price_gbp"]= pd.to_numeric(new_source["price_gbp"], errors="coerce")
# print(new_source)

# valid = new_source.dropna(subset=["price_gbp"])
# print (valid)

clean_products = new_source[new_source["price_gbp"].notna()].copy()
 
rejected_products = new_source[new_source["price_gbp"].isna()].copy()
 
# print("Clean rows:")
# print(clean_products)
 
# print("Rejected rows:")
# print(rejected_products)

#Q. 2 — Simulate a Small ELT Flow

source = pd.DataFrame({
    "order_id": [201, 202, 203],
    "amount_gbp": ["45.50", "30.00", "bad"],
})

# print("Raw_orders")
# print(source)

raw_source = source.copy()
new_source = raw_source.copy()

new_source["amount_gbp"]= pd.to_numeric(new_source["amount_gbp"], errors="coerce")

clean_orders = new_source[new_source["amount_gbp"].notna()].copy()

# print("Raw_orders")
# print(raw_source)
# print("Clean_orders")
# print(clean_orders)


# Q. 5 — Process Three Independent Batches

batches = {
    "batch_1": [10, 20, 30],
    "batch_2": [40, 50],
    "batch_3": [60, 70, 80],
}

# for batch_name, values in batches.items():
#     print(batch_name, "rows =", len(values), "sum =", len(values))


# Q. 7 — Preserve Raw Input Before Cleaning
"""
Rules for clean_orders:

city must not be missing;
amount must be positive;
trim spaces from city.
Confirm that raw_orders still has all original rows.
"""

source = pd.DataFrame({
    "order_id": [301, 302, 303],
    "city": [" London ", None, "Leeds"],
    "amount_gbp": [45.50, 20.00, -5.00],
})

raw_orders = source.copy()

cleaned_orders = raw_orders[raw_orders["city"].isna()&(raw_orders["amount_gbp"] > 0)].copy()

cleaned_orders["city"] = (cleaned_orders["city"].str.strip())

# print("Raw rows:", len(raw_orders))
# print("Clean rows:", len(cleaned_orders))
 
# print(raw_orders)
# print(cleaned_orders)

# Q. 10 — Build a Staging Output
source = pd.DataFrame({
    "OrderID": [401, 402, 403],
    "CustomerID": [1, 2, 1],
    "Amount": ["45.50", "30.00", "20.00"],
})

staging = source.rename(columns={"OrderID": "order_id","CustomerID": "customer_id",
"Amount": "amount_gbp",
}).copy()

staging["amount_gbp"] = pd.to_numeric(staging["amount_gbp"], errors="coerce")

# print(staging)


# Q. 11 — Build an Analytics Output

orders = pd.DataFrame({
    "order_id": [501, 502, 503, 504],
    "city": ["London", "Leeds", "London", "Manchester"],
    "amount_gbp": [45.50, 30.00, 62.25, 50.00],
    "status": ["complete", "complete", "complete", "cancelled"],
})
 
completed = orders[orders["status"] == "complete"].copy()
 
report = (completed.groupby("city", as_index=False).agg(completed_revenue_gbp=("amount_gbp", "sum", )))
 
print(report)

# Q. 15 — Plan a Backfill
"""
A sensible plan is:

Confirm the source data exists for all three dates.
Check whether any partial output already exists.
Process 2026-08-05.
Validate counts and totals.
Process 2026-08-06.
Validate counts and totals.
Process 2026-08-07.
Validate counts and totals.
Confirm that rerunning a date will not duplicate data.
"""


#Q. 17 — Build a Complete Independent ETL Script
 
source = pd.DataFrame({
    "order_id": [601, 602, 603, 604],
    "city": ["London", None, "Leeds", "Manchester"],
    "amount_gbp": ["45.50", "30.00", "bad", "50.00"],
    "status": ["complete", "complete", "complete", "cancelled"],
})
 
raw_orders = source.copy()
 
working = raw_orders.copy()
 
working["amount_gbp"] = pd.to_numeric(
    working["amount_gbp"],
    errors="coerce",
)
 
clean_orders = working[
    working["city"].notna()
    & working["amount_gbp"].notna()
].copy()
 
completed = clean_orders[
    clean_orders["status"] == "complete"
].copy()
 
daily_sales = (
    completed
    .groupby("city", as_index=False)
    .agg(
        revenue_gbp=("amount_gbp", "sum")
    )
)
 
print("Raw:")
print(raw_orders)
 
print("Clean:")
print(clean_orders)
 
print("Daily sales:")
print(daily_sales)