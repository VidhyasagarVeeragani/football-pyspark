---

## 🎯 Project Goals

- Clean and preprocess raw FIFA player data using PySpark
- Perform transformation and create meaningful features (UDFs, Spark SQL)
- Save optimized data using Parquet
- Convert to Pandas for plotting
- Visualize player stats, trends, and distributions

---

## 🧰 Technologies Used

| Library/Tool     | Use Case |
|------------------|----------|
| **PySpark**      | Distributed data processing, DataFrame operations |
| **Pandas**       | In-memory manipulation, easier plotting |
| **Matplotlib**   | Data visualization (plots, bar charts, etc.) |
| **Seaborn**      | Advanced statistical plots |
| **Parquet**      | Efficient file format for storing large structured data |

---

## 📊 Key Features

### 1. 🧹 Data Cleaning (01_ingest_clean.py)
- Dropped records with missing player names or key metrics
- Replaced null salary/value fields with 0
- Exported cleaned data to `.parquet`

### 2. 🔄 Transformation & Querying (02_transform_query.py)
- Created a UDF to convert currency strings (e.g., "€105M") to numeric
- Derived new fields:
  - `is_top_player`: Boolean for high-rated players (Overall ≥ 85)
  - `age_bucket`: Categorized age groups
- Executed Spark SQL queries to compute player counts per nationality

### 3. 📈 Visual Insights (03_visualize_or_insight.ipynb)
- Converted Spark DataFrame → Pandas for plotting
- Visualized:
  - Top 10 player nationalities
  - Average overall ratings by age bucket
  - Age vs Wage scatter plot
  - Top 10 most valuable players

---

## ✅ Skills Demonstrated

- PySpark DataFrame operations, SQL queries, UDFs
- Parquet-based storage for optimized analytics
- Data visualization using Pandas, Matplotlib, Seaborn
- Working with large datasets in notebooks
- Clean code and modular data pipeline structure

---

## 📎 Dataset Source

- [Kaggle - FIFA 21 Complete Player Dataset](https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset)

---

## 🚀 Future Enhancements

- Add interactive dashboards (Plotly, Streamlit)
- Build a REST API using Flask/FastAPI for real-time queries
- Integrate Spark on cloud (AWS EMR / Databricks)