import pandas as pd
# Q. 1 — Create a DataFrame

df = pd.DataFrame({"order_id":[101, 102, 103, 104],
                   "city": ["London","Manchester", "London", "Leeds"],
                   "amount_gbp": [45.50, 18.00, 62.25, 30.00],
                   "status": ["complete", "cancelled", "complete", "complete"]

})

# print(df)
# print(df.columns)
# print(df.shape)

# Q. 2 — Create and Read Three CSV Batches

order_1_df = pd.DataFrame({"order_id": [201, 202],
                         "city": ["London", "Manchester"],
                         "amount_gbp": [45.50, 18.00],
                         "status": ["complete", "cancelled"]
                         })
order_1_df.to_csv("order_1.csv", index = False)

df_1 = pd.read_csv("order_1.csv")
# print(df_1)

# Read order 2

order_2_df = pd.DataFrame({"order_id": [203, 204],
                         "city": ["Bristol", "London"],
                         "amount_gbp": [62.25, 27.40],
                         "status": ["complete", "complete"]
                         })
order_2_df.to_csv("order_2.csv", index = False)
df_2 = pd.read_csv("order_2.csv")

# Read order 3

order_3_df = pd.DataFrame({"order_id": [205, 206],
                         "city": ["Leeds", "Manchester"],
                         "amount_gbp": [34.80, 51.10],
                         "status": ["complete", "complete"]
                         })
order_3_df.to_csv("order_3.cvs", index = False)
df_3 = pd.read_csv("order_3.cvs")
# print(len(df_1))
# print(len(df_2))
# print(len(df_3))

# Q. 3 — Combine the CSV Batches
combined = pd.concat([df_1,df_2,df_3], ignore_index= True)

# print(combined)
# print(combined.head(3))
# print(combined.tail(3))

# Q. 4 — MCQ: DataFrame
# A. A two-dimensional labelled table with rows and columns.

# Q. 5 — Write and Read an Excel File
# Write and Read an Excel File

products = pd.DataFrame({
    "product_id": [1, 2, 3],
    "product_name": ["Desk Lamp", "Office Chair", "Notebook Set"],
    "price_gbp": [24.99, 89.50, 8.75],
})

products.to_excel("products.xlsx", index = False)
df = pd.read_excel("products.xlsx")
# print(df)

# Q. 6 — Read a JSON File

customers = [
  {"customer_id": 1, "name": "Amelia Clarke", "city": "London"},
  {"customer_id": 2, "name": "Oliver Bennett", "city": "Manchester"},
  {"customer_id": 3, "name": "Aisha Khan", "city": "Leeds"}
]

df = pd.DataFrame(customers)
df.to_json("customers.json", index = False)
customers_df = pd.read_json("customers.json")

# print(customers_df.head())
# print(customers_df.shape)
# print(customers_df.info())


# Q. 7 — Select Only Required Columns

selected = combined[["order_id", "city", "amount_gbp"]]

# print(selected)

amount_type = combined["amount_gbp"]
# print(type(amount_type))

# Q. 8 — MCQ: Inspecting Data
# A. df.info()

# Q. 9 — Filter Completed Orders

completed = combined[combined["status"] == "complete"]
# print(completed)

revenue = combined["amount_gbp"] .sum()
# print(f"Total Revenue:")
# print(f"{revenue:.2f}")

# Q. 10 — Clean Missing Values

df = pd.DataFrame({
    "order_id": [301, 302, 303, 304],
    "city": ["London", None, "Leeds", "Bristol"],
    "amount_gbp": [45.50, 20.00, None, 30.00],
})

# Print missing Values
# print(f"Missing values:")
# print(df.isnull().sum())

# Replace missing values with unknown
replaced = df.copy()
replaced["city"] = replaced["city"] .fillna("unknown")
# print(replaced)

# Remove missing values(amount)
remove = df.dropna(subset = ["amount_gbp"])
# print(remove)

# Q. 11 — Rename and Create New Columns
df = pd.DataFrame({
    "id": [401, 402, 403],
    "price": [20.00, 50.00, 12.50],
    "qty": [2, 1, 4],
})

renamed_df = df.rename(columns = {"id":"order_id", "price":"unit_price_gbp", "qty":"quantity"})
# print(f"Renamed Column")
# print(renamed_df)

renamed_df["line_total_gbp"]= renamed_df["unit_price_gbp"] * renamed_df["quantity"]

# print(renamed_df.columns.tolist())
# Q. 12 — MCQ: Missing Values
# B. fillna()

# Q. 13 — Sort Sales from Highest to Lowest
sorted_sales = (combined[["order_id", "city", "amount_gbp"]]) .sort_values("amount_gbp", ascending= False)
# print(sorted_sales)

# Q. 14 — Revenue by City
completed = combined[
    combined["status"] == "complete"
]
 
summary = (completed.groupby( "city", as_index=False, ).agg(revenue_gbp=( "amount_gbp", "sum",),
        order_count=("order_id", "count",), ).sort_values("revenue_gbp", ascending=False,))
 
# print(summary)

# Q. 15 — Merge Orders with Store Details
orders = pd.DataFrame({
    "order_id": [501, 502, 503, 504],
    "store_id": ["LDN-01", "MAN-02", "LDN-01", "LDS-04"],
    "amount_gbp": [45.50, 30.00, 62.25, 20.00],
})

stores = pd.DataFrame({
    "store_id": ["LDN-01", "MAN-02", "LDS-04"],
    "city": ["London", "Manchester", "Leeds"],
    "region": ["South", "North", "North"],
})

merged_orders = pd.merge(orders, stores, on="store_id", how="left")
# print(merged_orders)

# Q. 16 — MCQ: Merge
# D. It keeps every order and adds matching store details when available.

#Q. 17 — Build a Three-Batch Cleaning Flow
