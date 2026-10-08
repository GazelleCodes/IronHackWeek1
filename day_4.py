import pandas as pd

ages = pd.Series([23,20,25,16])
# print(ages)

ages_new = pd.Series([23,20,25,16], index= ["Alex","Brian", "Jason", "Joy"])
# print(ages_new)

# #Dictionary
data = {
    "name": ["Alex", "Maria", "John", "Sarah"],
    "age": [25, 19, 22, 20],
    "score": [85, 78, 90.34, 78]
}
# #print(data)
df = pd.DataFrame(data)
# print(df)

#Workin with csv

df = pd.read_csv("students.csv")

# Create sample CSV
data = {
    'order_id': [201,202],
    'customer': ['Oliver', 'Amelia'],
    'amount': [500.0, 300.0]
}
df_src = pd.DataFrame(data)
df_src.to_csv('sample_orders.csv', index=False)
 
# Read CSV
df = pd.read_csv('sample_orders.csv')
# print(df)

# print(df)

# print(df.head())
# print(df.head(10))
# print(df.tail())
# print(df.tail(3))

# print(df[["name","age"]])
# print(df[df["age"] >= 20])

# print(df.loc[df["age"] > 20, ["name", "age"]])


# Inspecting Data
 
df = pd.DataFrame({
    'order_id':[1,2,3,4,5],
    'amount':[10, None, 30, 40, 50],
    'city':['Leeds','Leeds','Manchester','Manchester','London']
})
 
# print("head():")
# print(df.head(3))
 
# print("\nshape:")
# print(df.shape)
 
# print("\ninfo():")
# print(df.info())
 
# print("\ndescribe():")
# print(df.describe())

data = {
    "Name": ["Alex", "Riya", "John", "Tony", "Sam"],
    "Department": ["HR", "IT", "IT", "HR", "IT"],
    "Salary": [30000, 50000, 45000, 32000, 52000]
}
df = pd.DataFrame(data)
# print(df)

# # Grouping 
# print(df.groupby("Department"),["Salary"] .mean())

# # Department with highest pay out

df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
# Sort by names
df.groupby(["Department" "Name"])["Salary"] .sum()

# Handling missing values
df = pd.DataFrame({
    'order_id':[1,2,3],
    'amount':[100, None, 200],
    'city':['Leeds', 'Manchester', None]
})

# print("Missing counts:")
# print(df.isnull().sum())

# # Fill missing amount with 0

filled = df.copy()
filled["amount"]= filled["amount"].fillna(0)
# print(filled)

# # Drop rows where city is missing
dropped = df.dropna(subset = ["city"])
print(dropped)
# print(df)


df = pd.DataFrame({'order_id':[1,2], 'amount':[120,80]})
 
df['tax'] = df['amount'] * 0.05
df['total'] = df['amount'] + df['tax']
df['high_value'] = df['amount'] > 100
 
# print(df)

# Merging different DataFrames
 
orders = pd.DataFrame({
    'order_id':[1,2,3],
    'customer_id':[101,102,101],
    'amount':[50,150,200]
})
 
customers = pd.DataFrame({
    'customer_id':[101,102],
    'customer_name':['Anil','Bina'],
    'city':['Leeds','Manchester']
})
 
merged = pd.merge(orders, customers, on='customer_id', how='left')
print(merged)

# Renaming columns
df = pd.DataFrame({'Order ID':[1,2], 'Amount':[10,20]})
print("Before:")
print(df)
 
df_renamed = df.rename(columns={'Order ID':'order_id', 'Amount':'amount'})
print("\nAfter rename:")
print(df_renamed)