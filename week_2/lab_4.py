
# Q. 1 — Choose the Better Platform
"""
For each requirement, choose data lake, data warehouse, or lakehouse.


Requirement	                                    Choice	        Reason
Large raw mixed data	                        Data lake	    Flexible storage for many data shapes
Controlled SQL-ready business data	            Data warehouse	Structured analytical use
Flexible storage plus managed analytical tables	Lakehouse	    Combines lake-style storage with warehouse-style table capabilities
Raw website events	                            Data lake	    Raw events can be retained before final use is known
"""

#Q. 2 — Place BritMart Data
"""
Place each item where it would most naturally fit in
a data lake, warehouse, or lakehouse design.

MySQL order extract -> lake or lakehouse raw area
supplier CSV -> lake or lakehouse raw area
website JSON -> lake or lakehouse raw area
monthly finance table -> warehouse or governed lakehouse table
daily sales summary -> warehouse or governed lakehouse table
"""
# Q. 3 — Compare the Three Architectures
"""
Area	                    Data Lake	                    Data Warehouse	                Lakehouse
Raw data support	        Strong	                        Usually not the main purpose	Strong
Strong structured reporting	Possible but needs more design	Strong	                        Strong
Flexible data shapes	    Strong	                        More controlled	Strong
Table-style analytics	    Depends on tools and design	    Strong	                        Strong
"""
# Q. 4 — MCQ: Data Warehouse
"""
Which requirement is the strongest fit for a data warehouse?
D. Run controlled business reporting over trusted structured data
"""
# Q. 5 — Schema-on-Read or Schema-on-Write?
"""
A. Data is stored first and interpreted when it is read.
B. Data must match an expected structure before it is accepted into the target.
C. A raw JSON area keeps different optional fields.
D. A controlled reporting table requires known columns and types.

A -> Schema-on-read
B -> Schema-on-write
C -> Schema-on-read
D -> Schema-on-write
"""

# Q. 6 — Design Bronze and Silver Rules

"""
Bronze
Keep the received records close to the source form so the team can inspect or replay them later.

Silver
Apply agreed cleaning rules, for example:

order_id must be present
amount_gbp must be positive
city should be trimmed
duplicate order_id values should be handled


Explain
Bronze preserves received data. Silver creates a more trusted reusable dataset.
"""
# Q. 7 — Process Three Batches from Bronze to Silver
"""
Treat all input rows as Bronze.

Create Silver by:

keeping positive amounts;
trimming city names;
removing duplicate order_id values.
Print Bronze and Silver row counts.

"""
import pandas as pd
 
batch_1 = pd.DataFrame(
    [
        (101, "London", 45.50, "complete"),
        (102, "Manchester", -5.00, "complete"),
    ],
    columns=[
        "order_id",
        "city",
        "amount_gbp",
        "status",
    ],
)
 
batch_2 = pd.DataFrame(
    [
        (103, " Bristol ", 30.00, "complete"),
        (104, "Leeds", 20.00, "cancelled"),
    ],
    columns=[
        "order_id",
        "city",
        "amount_gbp",
        "status",
    ],
)
 
batch_3 = pd.DataFrame(
    [
        (101, "London", 45.50, "complete"),
        (105, "Manchester", 51.00, "complete"),
    ],
    columns=[
        "order_id",
        "city",
        "amount_gbp",
        "status",
    ],
)
 
bronze = pd.concat([batch_1, batch_2, batch_3],ignore_index=True,)
 
silver = bronze[bronze["amount_gbp"] > 0].copy()
 
silver["city"] = (silver["city"].str.strip())
 
silver = silver.drop_duplicates(subset=["order_id"],keep="first",)
 
print("Bronze rows:", len(bronze))
print("Silver rows:", len(silver))
print(silver)

# Q. 8 — MCQ: Silver
"""
Which record belongs most naturally in Silver?
C. A cleaned and deduplicated order row
"""

# Q. 9 — Build a Gold Summary
"""
Using the Silver DataFrame from Q. 7:

keep only completed orders;
calculate revenue by city;
sort highest revenue first.
"""

completed = silver[
    silver["status"] == "complete"
]
 
gold = (
    completed
    .groupby(
        "city",
        as_index=False,
    )
    .agg(
        revenue_gbp=(
            "amount_gbp",
            "sum",
        )
    )
    .sort_values(
        "revenue_gbp",
        ascending=False,
    )
)
 
print(gold)


# Q. 10 — Structured, Semi-Structured, or Unstructured?
"""
MySQL orders table -> Structured
JSON website event -> Semi-structured
CSV supplier file -> Structured
Product photo -> Unstructured
PDF supplier contract -> Unstructured
"""

# Q. 12 — MCQ: Gold
"""
Which output is the strongest Gold example?
A. Daily revenue by city for reporting
"""

# Q. 13 — Compute or Storage?
"""
A. Files kept for later use
B. CPU and memory used to run a transformation
C. Stored analytical table data
D. Processing resources used for a query

A -> Storage
B -> Compute
C -> Storage
D -> Compute
"""
# Q. 14 — Why Separate Compute and Storage?
"""
BritMart stores data all day but runs a large transformation only at night.

Explain why being able to change compute without moving all stored data can be useful.

The stored data can remain available even when large processing resources are not running.

When more processing power is needed, compute can be increased for the workload without redesigning where all data is stored.

This can improve flexibility and cost control.
"""

# Q. 15 — Create a Small Metadata Catalogue
"""
The purpose of metadata here is to help people understand 
what a dataset contains and how it should be used.

ataset	Purpose	Main columns	Source	Owner/team	Last update
bronze_orders	Received order data	order_id, city, amount, status	Source batches	Data Engineering	2026-08-01
silver_orders	Clean reusable orders	order_id, city, amount, status	bronze_orders	Data Engineering	2026-08-01
gold_daily_sales	Reporting summary	city, revenue_gbp	silver_orders	Analytics/Data	2026-08-01

A catalogue helps users find and understand datasets without opening every file or table.
"""

# Q. 16 — MCQ: Metadata
"""
Why is metadata useful?
B. It describes data so people and systems can understand what the data represents.
"""

# Q. 18 — Find a Layering Mistake
"""
A team creates Gold directly from raw Bronze data 
and repeats different cleaning rules in five reports.

Explain two problems with this design.

Possible problems:

different reports may clean the same source differently;
duplicate or invalid data may enter business totals;
cleaning logic is repeated in many places;
fixing a rule requires changing several reports.
A reusable Silver layer gives the reports one trusted cleaned source.
"""
# Q. 20 — Design a Small Platform
"""
Create one architecture using only today's concepts.

It must include:

3 source types
Bronze
Silver
Gold
storage
compute
metadata/catalogue
one reporting consumer

Explain the purpose of each part in one short sentence.


Bronze: keeps received data.
Silver: keeps cleaned reusable data.
Gold: keeps business-ready output.
Storage: keeps the data.
Compute: performs processing.
Metadata/catalogue: describes datasets and helps users find them.
Reporting: uses trusted Gold data.
"""