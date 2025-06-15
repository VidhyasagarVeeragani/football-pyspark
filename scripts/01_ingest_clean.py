from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Initialize Spark
spark = SparkSession.builder \
    .appName("FIFA Players Data Analysis") \
    .config("spark.sql.warehouse.dir", "./spark-warehouse") \
    .getOrCreate()

# Load CSV
df = spark.read.csv("data", header=True, inferSchema=True)

# Inspect
df.printSchema()

df.show(5)
print("count : " + str(df.count())) # 122841

# Clean nulls
# Drop rows missing important values
df = df.dropna(subset=["long_name", "age", "club_name", "overall", "potential"])

# Fill value/wage with 0 where missing (they're already numeric)
df = df.fillna({"value_eur": 0, "wage_eur": 0})

print("count : " + str(df.count())) # 121272

# Save as Parquet
df.write.mode("overwrite").parquet("../football-pyspark/Cleaned data/cleaned_fifa.parquet")

# # Temp View + SQL
df.createOrReplaceTempView("players")
result = spark.sql("""
    SELECT Nationality, COUNT(*) as total_players
    FROM players
    GROUP BY Nationality
    ORDER BY total_players DESC
""")

result.show(10)


total_players = spark.sql("""SELECT COUNT(*) as total_players FROM players""")
total_players.show()
# result.filter(col("Nationality") == "India").show(10)

# Stop
spark.stop()