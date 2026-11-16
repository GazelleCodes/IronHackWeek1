# Databricks notebook source
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/workspace/default/netflix_titles/netflix_titles.csv")


df.printSchema()

#The Netflix dataset is loaded from a CSV file using PySpark.Viewed the schema to see 

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.bronze")

# I wanted to store the data in a table in the bronze schema so i created one

# COMMAND ----------

# I read the dataframe and saved as table in the bronze schema for reuse
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.bronze.netflix_titles")

# COMMAND ----------

# I read the table from bronze schema and imported the count function

df = spark.table("workspace.bronze.netflix_titles")

from pyspark.sql.functions import count
# I grouped the data by type and counted the total number of movies and TV shows, but there were some null values in the type column, so I filtered out the null values and the rows with the value "William Wyler"

df.groupBy("TYPE") \
    .agg(count("*").alias("total")) \
    .show()

from pyspark.sql.functions import col


df.filter(
    col("TYPE").isNull() | (col("TYPE") == "William Wyler")
).show(truncate=False)



# COMMAND ----------

# I read the dataframe again but this time with different options to capture all the quotes and escape characters.

df_new = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("quote", '"') \
    .option("escape", '"') \
    .option("multiLine", True) \
    .csv("/Volumes/workspace/default/netflix_titles/netflix_titles.csv")

# I grouped the data by type and counted the total number of movies and TV shows. I also checked if there were existing null values in the type column.

# Count of Movies vs TV Shows.
df_new.groupBy("type")\
    .agg(count("*").alias("total")) \
    .show()

df_new.count()
df_new.filter(col("TYPE").isNull()).count()

# I changed the data type of the release_year column to integer so I can merge the data with the dataframe from the bronze schema
df_new = df_new.withColumn(
    "release_year",
    col("release_year").cast("int")
)

# I merged the data with the dataframe from the bronze schema with the option overwriteSchema to overwrite the existing schema.
df_new.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.bronze.netflix_titles")

# COMMAND ----------

# 2. Count of null/missing director values.

df_new.filter(col("DIRECTOR").isNull()).count()


# COMMAND ----------

# 3. Count of titles per rating, sorted descending.
df_new.groupBy("rating") \
    .agg(count("*").alias("total")) \
    .orderBy(col("total").desc()) \
    .show()


# COMMAND ----------

#4.Top 10 listed_in genres by title count
df_new.groupBy("listed_in") \
    .agg(count("*").alias("total")) \
    .orderBy(col("total").desc()) \
    .limit(10) \
    .show()


# COMMAND ----------

#5.Top 15 genres by title count
df_new.groupBy("listed_in") \
    .agg(count("*").alias("total")) \
    .orderBy(col("total").desc()) \
    .limit(15) \
    .show()



# COMMAND ----------

#6. Type of available content 
df_new.groupBy("type") \
    .agg(count("*").alias("total")) \
    .show()



# COMMAND ----------

# 7. Quantity of newly added contents by month and year.
df_new.groupBy("date_added") \
    .agg(count("*").alias("total")) \
    .orderBy(col("date_added").desc()) \
    .show()

# COMMAND ----------

# 8. Average duration of Tv Shows in seasons
# spark cannot convert the string to int, so I used regexp_extract to extract the number of seasons from the duration column and cast it to int.
from pyspark.sql.functions import avg, col, regexp_extract

df_new.filter(col("type") == "TV Show") \
    .withColumn(
        "seasons",
        regexp_extract(col("duration"), r"(\d+)", 1).cast("int")
    ) \
    .groupBy("type") \
    .agg(avg("seasons").alias("avg_duration")) \
    .show()

# COMMAND ----------

# 9 .Its Christmas! What movies/Tv shows are you binge watching this weekend? 
# I searched the Netflix dataset for Christmas-related movies and TV shows using the TITLE, DESCRIPTION, and LISTED_IN columns.
#Based on the results, I would recommend some of the Christmas-themed titles for a weekend binge-watching session.
from pyspark.sql.functions import col, lower

christmas_df = df_new.filter(
    lower(col("title")).contains("christmas") |
    lower(col("description")).contains("christmas") |
    lower(col("listed_in")).contains("christmas")
)

christmas_df.select(
    "title",
    "type",
    "release_year",
    "listed_in",
    "description"
).show(5, truncate=False)

# COMMAND ----------

# 10. My friend is a    Ryan Reynold fan , I am thinking of making a movie compilation. What movies should I include ?
# I filtered the Netflix dataset to find movies featuring Ryan Reynolds by searching the CAST column and selecting records where the TYPE is Movie.
ryan_movies = df_new.filter(
    (col("type") == "Movie") &
    (col("cast").contains("Ryan Reynolds"))
)

ryan_movies.select(
    "title",
    "release_year",
    "rating",
    "duration"
).show(5,truncate=False)

# COMMAND ----------

# 11. How many movies or shows were released during COVID season.
# I filtered the Netflix dataset using the RELEASE_YEAR column, considering 2020 and 2021 as the COVID period.

#I then grouped the results by TYPE to calculate the number of Movies and TV Shows released during those years.

covid_df = df_new.filter(
    (col("release_year") >= 2020) &
    (col("release_year") <= 2021)
)
covid_df.groupBy("type") \
    .agg(count("*").alias("total")) \
    .show()

# COMMAND ----------

#12.I am on a short flight of 2 hours, which movies or shows I should download to watch on the flight
# I filtered the Netflix dataset using type and duration columns to find movies with a duration of 120 minutes or less. I then converted the duration column to an integer and selected the relevant columns for the final result.

flight_movies = df_new.filter(
    (col("type") == "Movie") &
    (regexp_extract(col("duration"), r"(\d+)", 1).cast("int") <= 120)
)

flight_movies.select(
    "title",
    "release_year",
    "duration",
    "rating"
).show(10, truncate=False)