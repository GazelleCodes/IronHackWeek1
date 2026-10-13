#Q. 1 — Build a Source Inventory
''' Source	         Type of data	    How often it may change	    One check before using it
MySQL orders	     Structured	        Not often	                Right files and date, column counts
Supplier CSV	     Structured	        When needed	                Duplicate values, Missing columns,
                                                                    Headings, Data type

Website JSON	     Semi Structured	Often	                    Right info, filed counts
Excel stock report	 Structured	        When needed	                Missing values, duplicates, columns

'''


'''
Q. 2 — Decide What the Data Engineer Must Do

A -> Data engineering
B -> Data analytics
C -> Data science
D -> Data engineering
E -> Data engineering
'''

#Q. 3 — Inspect Three Small Input Batches

import pandas as pd

batch_1 = pd.DataFrame({"order_id": [101, 102],
                        "city": ["London", "Manchester"],
                        "amount_gbp": [45.50, 18.00]
                        
})

batch_2 = pd.DataFrame({"order_id": [103, 104],
                        "city": ["Bristol", "London"],
                        "amount_gbp": [62.25, 27.40]
                        
})

batch_3 = pd.DataFrame({"order_id": [105, 106],
                        "city": ["Leeds", "Manchester"],
                        "amount_gbp": [34.80, 51.10]
                        
})

'''
Create three DataFrames and print:
'''
 
# row count for each batch;
# print("Row count batch 1:", len(batch_1))
# print("Row count batch 2:", len(batch_2))
# print("Row count batch 3:", len(batch_3))

# total rows after combining them;
merged_orders = pd.concat([batch_1, batch_2,batch_3],ignore_index= True )
# print("Row count merged:", len(merged_orders))


# total sales after combining them.
total_sales = merged_orders["amount_gbp"] .sum()
# print(f"Total Sales:{total_sales:.2f}")

'''
Q. 4 — MCQ: Data Engineering
Which task is most clearly a data-engineering responsibility?
B. Building a reliable process that moves and cleans order data 
'''

'''
Q. 5 — Put the Pipeline Steps in Order

Read new order records
        ↓
Store the received records
        ↓
Clean invalid values
        ↓
Create daily sales summary
        ↓
Make the summary available to analysts
        ↓
Check that the run completed
'''
'''
Q. 6 — Design a Small Pipeline for Daily Orders

Pipeline step	   What happens?	                Simple check
Source	           Supplier sends order file	    File exists
Ingestion	       Read the file	                Expected columns are present
Storage	           Keep received data	            Row count matches input
Processing	       Clean and transform data	        Invalid rows are counted
Serving	           Create useful sales output	    Business totals are checked
Monitoring	       Record whether the run succeeded	Status and counts are available
'''

# Q. 7 — Process Three Batches and Keep the Counts

batch_1["batch_id"]= "batch_1"
batch_2["batch_id"]= "batch_2"
batch_3["batch_id"]= "batch_3"

# Combine the batches and create this summary:
merged_orders = pd.concat([batch_1, batch_2,batch_3],ignore_index= True )

Summary = (merged_orders.groupby("batch_id", as_index= False,) .agg(sales_gbp=( "amount_gbp", "sum",), row_count = ("batch_id", "count",), ))
# print(Summary)

'''
. 8 — MCQ: Ingestion
What does ingestion mean in a data pipeline?

A. Moving data from a source into the data platform
'''

# Q. 9 — Clean a Batch of Orders

orders = pd.DataFrame({
    "order_id": [201, 202, 203, 204],
    "city": [" London ", "Manchester", "Leeds", None],
    "amount_gbp": [45.50, -5.00, 30.00, 20.00],
})

# valid_orders = orders.copy()
# valid_orders["city"]= valid_orders["city"] .fillna("unknown")

# print(valid_orders)

# rejected_orders = orders.dropna(subset = ["amount_gbp" <= 0])
# print(rejected_orders)

invalid_mask = (orders["city"].isna()|(orders["amount_gbp"] <= 0))
 
rejected_orders = orders[invalid_mask].copy()
 
valid_orders = orders[~invalid_mask].copy()
 
valid_orders["city"] = (valid_orders["city"].str.strip())

# print(valid_orders)
# print(rejected_orders)

# Q. 11 — Simulate Three Batch Runs
batches = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80, 90],
]
 
cumulative_total = 0
 
for batch_number, batch in enumerate(
    batches,
    start=1,
):
    batch_total = sum(batch)
    cumulative_total += batch_total
 
    # print(
    #     batch_number,
    #     len(batch),
    #     batch_total,
    #     cumulative_total,
    # )

# Q. 15 — Draw a Small Modern Data Platform


'''
Q. 17 — Design Recovery for a Failed Batch
batch_1 -> received and processed
batch_2 -> received but processing failed
batch_3 -> not started

A sensible approach is:

1. Verify its input and output counts from batch_1
2. Check why batch_2 failed.
3. Confirm whether any output from the failed run was already written.
4. Correct the problem.
5. Rerun batch_2.
6. Verify its input and output counts.
7. Continue with batch_3.
8. Keep the batch status and counts so the team can see what happened.
'''

# Q. 19 — Reconcile Three Batches

expected = [100, 120, 80]
processed = [100, 118, 80]
 
for index in range(len(expected)):
    difference = expected[index] - processed[index]
 
    print(
        f"Batch {index + 1}: "
        f"difference = {difference}"
    )