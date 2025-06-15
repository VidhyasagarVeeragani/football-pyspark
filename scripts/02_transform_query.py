# 02_transform_query.ipynb

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, regexp_replace, udf
from pyspark.sql.types import FloatType, IntegerType

# 1. Start Spark Session
spark = SparkSession.builder \
    .appName("FIFA Transform and Query") \
    .getOrCreate()

# 2. Load cleaned Parquet file
df = spark.read.parquet("../football-pyspark/Cleaned data/cleaned_fifa.parquet")
df.printSchema()
df.select('short_name', 'Value_EUR').show(1)

# 3. Helper function to convert currency (e.g., "€105M", "€500K") to float

def parse_value(value):
    if value is None:
        return 0.0
    try:
        value = str(value)  # 🛠 convert to string to safely use replace
        value = value.replace('€', '').replace('M', '000000').replace('K', '000')
        return float(value)
    except:
        return 0.0

parse_udf = udf(parse_value, FloatType())

# 4. Apply currency conversion using UDF
df = df.withColumn("Value_EUR1", parse_udf(col("Value_EUR")))
df.select('short_name', 'Value_EUR1', 'Value_EUR').show(10)

df = df.withColumn("Wage_EUR1", parse_udf(col("Wage_EUR")))
df.select('short_name', 'Wage_EUR1', 'Wage_EUR').show(10)

# 5. Create new columns
## Flag top players
df = df.withColumn("is_top_player", when(col("Overall") >= 85, "Yes").otherwise("No"))

df.select('short_name', 'is_top_player').show(10)

## Age Bucket
df = df.withColumn("age_bucket", 
                   when(col("Age") < 20, "Teen")
                   .when((col("Age") >= 20) & (col("Age") < 30), "20s")
                   .when((col("Age") >= 30) & (col("Age") < 40), "30s")
                   .otherwise("40+"))
df.select('short_name', 'age_bucket').show(10)

# 6. Describe and summary stats
df.select("Age", "Overall", "Potential", "Value_EUR", "Wage_EUR").describe().show()

# 7. Group by analysis: Avg rating and value by nationality
df.groupBy("Nationality").agg(
    {"Overall": "avg", "Potential": "avg", "Value_EUR": "avg"}
).orderBy("avg(Overall)", ascending=False).show(10)

# 8. Correlation: Age vs Wage_EUR
corr = df.stat.corr("Age", "Wage_EUR")
print(f"Correlation between Age and Wage: {corr:.2f}")

df.printSchema()

# 9. Save transformed data
df.write.mode("overwrite").parquet("../football-pyspark/Cleaned data/fifa_transformed.parquet")

# Done
print("Transformation and analysis complete.")


# Stop
spark.stop()