# QUESTION 1
# Classify Oreder Amounts



amounts = [24.50, 55.00, 120.00, 49.99, 99.50]

for a in amounts:
    if a >= 100:
        print(f"Amount: {a} is High")
    if a >= 50 and a < 100:
        print(f"Amount: {a} is Medium")

    elif a < 50:
        print(f"Amount: {a} is Low")

# QUESTION 2
# Apply two business rules to classify order amounts

amount = 125
is_member = True

if amount >= 100 and is_member:
    print("Discount eligible")
else:
    print("Discount not eligible")

amount = 125
is_member = False

if amount >= 100 and is_member:
    print("Discount eligible")
else:
    print("Discount not eligible")

amount = 65
is_member = True

if amount >= 100 and is_member:
    print("Discount eligible")
else:
    print("Discount not eligible")

# QUESTION 3
# Calculate Completed Revenue

statuses = [
    "complete",
    "cancelled",
    "complete",
    "complete",
]
 
amounts = [
    45.50,
    18.00,
    62.25,
    30.00,
]

completed_revenue = 0

for i in range(len(statuses)):
    if statuses[i] == "complete":
        completed_revenue += amounts[i]
print(f"Completed Revenue: ${completed_revenue:.2f}")

# QUESTION 4
# C. It runs that branch and skips the remaining branches. 

# QUESTION 5
count = 1
limit = 5

while count <= limit:
    print(f"Count: {count}")
    count += 1

count = 1
limit = 3
while count <= limit:
    print(f"Count: {count}")
    count += 1

# QUESTION 6
# Stop When the Order Is Found

order_ids = [301, 302, 303, 304, 305]
target_id = 303

for order_id in order_ids:
    if order_id == target_id:
        print(f"Order {target_id} found.")
        break
# QUESTION 7
# Use continue to skip amounts that are 0 or negative. 
# Print only valid amounts and their total.
amounts = [45.50, -5.00, 18.00, 0, 62.25]
valid_amounts = []

for amount in amounts:
    if amount <= 0 :
        continue
    valid_amounts.append(amount)

total = sum(valid_amounts)
print(f"Valid amounts: {valid_amounts}")
print(f"Total: ${total:.2f}")

# QUESTION 8
# A. When you want to stop the current loop as soon as the required result is found.

# QUESTION 9
# Update a List of Stores
stores = ["London", "Manchester", "Bristol"]

stores.append("Leeds")
stores[2] = "Birmingham"
stores.remove("Manchester")

print(stores)

# QUESTION 10
# Remove Duplicate Store IDs
store_ids = ["LDN-01", "MAN-02", "LDN-01", "BRS-03", "MAN-02"]
new_store_ids = list(set(store_ids))
print(new_store_ids)

original_count = len(store_ids)
unique_count = len(new_store_ids)
unique_values = new_store_ids

print(f"Original count: {original_count}")
print(f"Unique count: {unique_count}")
print(f"Unique values: {unique_values}")

# QUESTION 11

store_location = ("LDN-01", "London", "South")
print(store_location[0])
print(store_location[1])
print(store_location[2])

#store_location[1] = "Leeds"  # This will raise an error because tuples are immutable.

# QUESTION 12
# D. Keep unique values and quickly check membership.

# QUESTION 13
# Create a Customer Dictionary
customer = {
    "customer_id": "C101",
    "name": "Amelia Clarke",
    "city": "London",
    "total_spend": 425.50
}

print(customer["name"])
print(customer["total_spend"])

# QUESTION 14
# Create a Nested Dictionary
stores = {
    "LDN-01": {"city": "London", "revenue": 5000},
    "MAN-02": {"city": "Manchester", "revenue": 4200}
}

print(stores["MAN-02"]["revenue"])

# QUESTION 15
# Create a dictionary where each key is a city and each value is the number of orders for that city.
cities = ["London", "Manchester", "London", "Leeds", "London", "Manchester"]
city_counts = {}

for city in cities:
    if city in city_counts:
        city_counts[city] += 1
    else:
        city_counts[city] = 1

print(city_counts)

# QESTION 17
# Build a Small Order Cleaner
orders = [
    {"order_id": 401, "city": "London", "amount_gbp": 45.50},
    {"order_id": 402, "city": "Manchester", "amount_gbp": -5.00},
    {"order_id": 401, "city": "London", "amount_gbp": 45.50},
    {"order_id": 403, "city": "Leeds", "amount_gbp": 30.00},
]

accepted_orders = []
rejected_orders = []
seen_order_ids = set()

for order in orders:
    order_id = order["order_id"]
    amount = order["amount_gbp"]

    if order_id in seen_order_ids or amount <= 0:
        rejected_orders.append(order)
    else:
        accepted_orders.append(order)
        seen_order_ids.add(order_id)

print("Accepted:", accepted_orders)
print("Rejected:", rejected_orders)
print("Seen IDs:", seen_order_ids)

# QUESTION 18

revenue_by_city = {}

for order in accepted_orders:
    city = order["city"]
    amount = order["amount_gbp"]

    if city in revenue_by_city:
        revenue_by_city[city] += amount
    else:
        revenue_by_city[city] = amount
print(revenue_by_city)

# QUESTION 19
amounts = [10, -5, 20, 0, 30, 40]
valid_amounts = 0

for amount in amounts:
    if amount <= 0:
        continue
    print(amount)
    valid_count += 1
 
    if valid_count == 3:
        break

# QUESTION 20
''' For each case, choose list, tuple, set, or dictionary, and explain why.

1 = List : Lists keep items in order and can be changed.
2 = Set : Sets automatically store only unique values.
3 = Tupel : Tuples are ordered and cannot be changed.
4 = Dictionary : Dictionaries map a key (customer ID) to a value (customer details).

'''

